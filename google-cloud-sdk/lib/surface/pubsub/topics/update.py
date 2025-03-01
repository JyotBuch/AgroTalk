# -*- coding: utf-8 -*- #
# Copyright 2017 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Cloud Pub/Sub topics update command."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.api_lib.pubsub import topics
from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.kms import resource_args as kms_resource_args
from googlecloudsdk.command_lib.pubsub import flags
from googlecloudsdk.command_lib.pubsub import resource_args
from googlecloudsdk.command_lib.pubsub import util
from googlecloudsdk.command_lib.util.args import labels_util
from googlecloudsdk.core import exceptions as core_exceptions
from googlecloudsdk.core import log

DETAILED_HELP = {'EXAMPLES': """\
          To update existing labels on a Cloud Pub/Sub topic, run:

              $ {command} mytopic --update-labels=KEY1=VAL1,KEY2=VAL2

          To clear all labels on a Cloud Pub/Sub topic, run:

              $ {command} mytopic --clear-labels

          To remove an existing label on a Cloud Pub/Sub topic, run:

              $ {command} mytopic --remove-labels=KEY1,KEY2

          To enable customer-managed encryption for a Cloud Pub/Sub topic by protecting message data with a Cloud KMS CryptoKey, run:

              $ {command} mytopic --topic-encryption-key=projects/PROJECT_ID/locations/KMS_LOCATION/keyRings/KEYRING/cryptoKeys/KEY

          To enable or update retention on a Cloud Pub/Sub topic, run:

              $ {command} mytopic --message-retention-duration=MESSAGE_RETENTION_DURATION

          To disable retention on a Cloud Pub/Sub topic, run:

              $ {command} mytopic --clear-message-retention-duration

          To update a Cloud Pub/Sub topic's message storage policy, run:

              $ {command} mytopic --message-storage-policy-allowed-regions=some-cloud-region1,some-cloud-region2

          To recompute a Cloud Pub/Sub topic's message storage policy based on your organization's "Resource Location Restriction" policy, run:

              $ {command} mytopic --recompute-message-storage-policy

          To enforce both at-rest and in-transit guarantees for messages published to the topic, run:

              $ {command} mytopic --message-storage-policy-allowed-regions=some-cloud-region1,some-cloud-region2 --message-storage-policy-enforce-in-transit
          """}

_KMS_FLAG_OVERRIDES = {
    'kms-key': '--topic-encryption-key',
    'kms-keyring': '--topic-encryption-key-keyring',
    'kms-location': '--topic-encryption-key-location',
    'kms-project': '--topic-encryption-key-project',
}

_KMS_PERMISSION_INFO = """
The specified Cloud KMS key should have purpose set to "ENCRYPT_DECRYPT".
The service account,
"service-${CONSUMER_PROJECT_NUMBER}@gcp-sa-pubsub.iam.gserviceaccount.com"
requires the IAM cryptoKeyEncrypterDecrypter role for the given Cloud KMS key.
CONSUMER_PROJECT_NUMBER is the project number of the project that is the parent
of the topic being updated"""


def _GetKmsKeyNameFromArgs(args):
  """Parses the KMS key resource name from args.

  Args:
    args: an argparse namespace. All the arguments that were provided to this
      command invocation.

  Returns:
    The KMS CryptoKey resource name for the key specified in args, or None.
  """
  kms_ref = args.CONCEPTS.kms_key.Parse()
  if kms_ref:
    return kms_ref.RelativeName()

  # Check whether the user specified any topic-encryption-key flags.
  for keyword in [
      'topic-encryption-key',
      'topic-encryption-key-project',
      'topic-encryption-key-location',
      'topic-encryption-key-keyring',
  ]:
    if args.IsSpecified(keyword.replace('-', '_')):
      raise core_exceptions.Error(
          '--topic-encryption-key was not fully specified.'
      )

  return None


def _Args(
    parser,
):
  """Registers flags for this command."""
  resource_args.AddTopicResourceArg(parser, 'to update.')
  labels_util.AddUpdateLabelsFlags(parser)
  resource_args.AddResourceArgs(
      parser,
      [
          kms_resource_args.GetKmsKeyPresentationSpec(
              'topic',
              flag_overrides=_KMS_FLAG_OVERRIDES,
              permission_info=_KMS_PERMISSION_INFO,
          )
      ],
  )
  flags.AddTopicMessageRetentionFlags(parser, is_update=True)

  flags.AddTopicMessageStoragePolicyFlags(parser, is_update=True)

  flags.AddSchemaSettingsFlags(parser, is_update=True)
  flags.AddIngestionDatasourceFlags(
      parser,
      is_update=True,
  )


def _Run(args):
  """This is what gets called when the user runs this command.

  Args:
    args: an argparse namespace. All the arguments that were provided to this
      command invocation.

  Returns:
    A serialized object (dict) describing the results of the operation.

  Raises:
    An HttpException if there was a problem calling the
    API topics.Patch command.
  """
  client = topics.TopicsClient()
  topic_ref = args.CONCEPTS.topic.Parse()

  message_retention_duration = getattr(args, 'message_retention_duration', None)
  if message_retention_duration:
    message_retention_duration = util.FormatDuration(message_retention_duration)
  clear_message_retention_duration = getattr(
      args, 'clear_message_retention_duration', None
  )

  labels_update = labels_util.ProcessUpdateArgsLazy(
      args,
      client.messages.Topic.LabelsValue,
      orig_labels_thunk=lambda: client.Get(topic_ref).labels,
  )

  schema = getattr(args, 'schema', None)
  if schema:
    schema = args.CONCEPTS.schema.Parse().RelativeName()
  message_encoding_list = getattr(args, 'message_encoding', None)
  message_encoding = None
  if message_encoding_list:
    message_encoding = message_encoding_list[0]
  first_revision_id = getattr(args, 'first_revision_id', None)
  last_revision_id = getattr(args, 'last_revision_id', None)
  result = None
  clear_schema_settings = getattr(args, 'clear_schema_settings', None)

  message_storage_policy_enforce_in_transit = getattr(
      args, 'message_storage_policy_enforce_in_transit', None
  )

  kinesis_ingestion_stream_arn = getattr(
      args, 'kinesis_ingestion_stream_arn', None
  )
  kinesis_ingestion_consumer_arn = getattr(
      args, 'kinesis_ingestion_consumer_arn', None
  )
  kinesis_ingestion_role_arn = getattr(args, 'kinesis_ingestion_role_arn', None)
  kinesis_ingestion_service_account = getattr(
      args, 'kinesis_ingestion_service_account', None
  )
  cloud_storage_ingestion_bucket = getattr(
      args, 'cloud_storage_ingestion_bucket', None
  )
  cloud_storage_ingestion_input_format_list = getattr(
      args, 'cloud_storage_ingestion_input_format', None
  )
  cloud_storage_ingestion_input_format = None
  if cloud_storage_ingestion_input_format_list:
    cloud_storage_ingestion_input_format = (
        cloud_storage_ingestion_input_format_list[0]
    )
  cloud_storage_ingestion_text_delimiter = getattr(
      args, 'cloud_storage_ingestion_text_delimiter', None
  )
  if cloud_storage_ingestion_text_delimiter:
    # Interprets special characters representations (i.e., "\n") as their
    # expected characters (i.e., newline).
    cloud_storage_ingestion_text_delimiter = (
        cloud_storage_ingestion_text_delimiter.encode('utf-8').decode(
            'unicode-escape'
        )
    )
  cloud_storage_ingestion_minimum_object_create_time = getattr(
      args, 'cloud_storage_ingestion_minimum_object_create_time', None
  )
  cloud_storage_ingestion_match_glob = getattr(
      args, 'cloud_storage_ingestion_match_glob', None
  )
  azure_event_hubs_ingestion_resource_group = getattr(
      args, 'azure_event_hubs_ingestion_resource_group', None
  )
  azure_event_hubs_ingestion_namespace = getattr(
      args, 'azure_event_hubs_ingestion_namespace', None
  )
  azure_event_hubs_ingestion_event_hub = getattr(
      args, 'azure_event_hubs_ingestion_event_hub', None
  )
  azure_event_hubs_ingestion_client_id = getattr(
      args, 'azure_event_hubs_ingestion_client_id', None
  )
  azure_event_hubs_ingestion_tenant_id = getattr(
      args, 'azure_event_hubs_ingestion_tenant_id', None
  )
  azure_event_hubs_ingestion_subscription_id = getattr(
      args, 'azure_event_hubs_ingestion_subscription_id', None
  )
  azure_event_hubs_ingestion_service_account = getattr(
      args, 'azure_event_hubs_ingestion_service_account', None
  )
  aws_msk_ingestion_cluster_arn = getattr(
      args, 'aws_msk_ingestion_cluster_arn', None
  )
  aws_msk_ingestion_topic = getattr(args, 'aws_msk_ingestion_topic', None)
  aws_msk_ingestion_aws_role_arn = getattr(
      args, 'aws_msk_ingestion_aws_role_arn', None
  )
  aws_msk_ingestion_service_account = getattr(
      args, 'aws_msk_ingestion_service_account', None
  )
  confluent_cloud_ingestion_bootstrap_server = getattr(
      args, 'confluent_cloud_ingestion_bootstrap_server', None
  )
  confluent_cloud_ingestion_cluster_id = getattr(
      args, 'confluent_cloud_ingestion_cluster_id', None
  )
  confluent_cloud_ingestion_topic = getattr(
      args, 'confluent_cloud_ingestion_topic', None
  )
  confluent_cloud_ingestion_identity_pool_id = getattr(
      args, 'confluent_cloud_ingestion_identity_pool_id', None
  )
  confluent_cloud_ingestion_service_account = getattr(
      args, 'confluent_cloud_ingestion_service_account', None
  )
  ingestion_log_severity = getattr(args, 'ingestion_log_severity', None)
  clear_ingestion_data_source_settings = getattr(
      args, 'clear_ingestion_data_source_settings', None
  )
  message_transforms_file = getattr(args, 'message_transforms_file', None)
  clear_message_transforms = getattr(args, 'clear_message_transforms', None)

  try:
    result = client.Patch(
        topic_ref,
        labels_update.GetOrNone(),
        _GetKmsKeyNameFromArgs(args),
        message_retention_duration,
        clear_message_retention_duration,
        args.recompute_message_storage_policy,
        args.message_storage_policy_allowed_regions,
        message_storage_policy_enforce_in_transit,
        schema=schema,
        message_encoding=message_encoding,
        first_revision_id=first_revision_id,
        last_revision_id=last_revision_id,
        clear_schema_settings=clear_schema_settings,
        kinesis_ingestion_stream_arn=kinesis_ingestion_stream_arn,
        kinesis_ingestion_consumer_arn=kinesis_ingestion_consumer_arn,
        kinesis_ingestion_role_arn=kinesis_ingestion_role_arn,
        kinesis_ingestion_service_account=kinesis_ingestion_service_account,
        cloud_storage_ingestion_bucket=cloud_storage_ingestion_bucket,
        cloud_storage_ingestion_input_format=cloud_storage_ingestion_input_format,
        cloud_storage_ingestion_text_delimiter=cloud_storage_ingestion_text_delimiter,
        cloud_storage_ingestion_minimum_object_create_time=cloud_storage_ingestion_minimum_object_create_time,
        cloud_storage_ingestion_match_glob=cloud_storage_ingestion_match_glob,
        azure_event_hubs_ingestion_resource_group=azure_event_hubs_ingestion_resource_group,
        azure_event_hubs_ingestion_namespace=azure_event_hubs_ingestion_namespace,
        azure_event_hubs_ingestion_event_hub=azure_event_hubs_ingestion_event_hub,
        azure_event_hubs_ingestion_client_id=azure_event_hubs_ingestion_client_id,
        azure_event_hubs_ingestion_tenant_id=azure_event_hubs_ingestion_tenant_id,
        azure_event_hubs_ingestion_subscription_id=azure_event_hubs_ingestion_subscription_id,
        azure_event_hubs_ingestion_service_account=azure_event_hubs_ingestion_service_account,
        aws_msk_ingestion_cluster_arn=aws_msk_ingestion_cluster_arn,
        aws_msk_ingestion_topic=aws_msk_ingestion_topic,
        aws_msk_ingestion_aws_role_arn=aws_msk_ingestion_aws_role_arn,
        aws_msk_ingestion_service_account=aws_msk_ingestion_service_account,
        confluent_cloud_ingestion_bootstrap_server=confluent_cloud_ingestion_bootstrap_server,
        confluent_cloud_ingestion_cluster_id=confluent_cloud_ingestion_cluster_id,
        confluent_cloud_ingestion_topic=confluent_cloud_ingestion_topic,
        confluent_cloud_ingestion_identity_pool_id=confluent_cloud_ingestion_identity_pool_id,
        confluent_cloud_ingestion_service_account=confluent_cloud_ingestion_service_account,
        clear_ingestion_data_source_settings=clear_ingestion_data_source_settings,
        ingestion_log_severity=ingestion_log_severity,
        message_transforms_file=message_transforms_file,
        clear_message_transforms=clear_message_transforms,
    )
  except topics.NoFieldsSpecifiedError:
    operations = [
        'clear_labels',
        'update_labels',
        'remove_labels',
        'recompute_message_storage_policy',
        'message_storage_policy_allowed_regions',
    ]
    if not any(args.IsSpecified(arg) for arg in operations):
      raise
    log.status.Print('No update to perform.')
  else:
    log.UpdatedResource(topic_ref.RelativeName(), kind='topic')
  return result


@base.UniverseCompatible
@base.ReleaseTracks(base.ReleaseTrack.GA)
class Update(base.UpdateCommand):
  """Updates an existing Cloud Pub/Sub topic."""

  detailed_help = DETAILED_HELP

  @staticmethod
  def Args(parser):
    """Registers flags for this command."""
    _Args(
        parser,
    )

  def Run(self, args):
    return _Run(args)


@base.ReleaseTracks(base.ReleaseTrack.BETA)
class UpdateBeta(Update):
  """Updates an existing Cloud Pub/Sub topic."""

  @staticmethod
  def Args(parser):
    _Args(
        parser,
    )

  def Run(self, args):
    return _Run(args)


@base.ReleaseTracks(base.ReleaseTrack.ALPHA)
class UpdateAlpha(UpdateBeta):
  """Updates an existing Cloud Pub/Sub topic."""

  @staticmethod
  def Args(parser):
    _Args(
        parser,
    )
    flags.AddMessageTransformsFlags(parser, is_update=True)
