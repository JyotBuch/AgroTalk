"""Generated message classes for appconfigmanager version v1alpha.

"""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding
from apitools.base.py import extra_types


package = 'appconfigmanager'


class AppconfigmanagerProjectsLocationsConfigsCreateRequest(_messages.Message):
  r"""A AppconfigmanagerProjectsLocationsConfigsCreateRequest object.

  Fields:
    config: A Config resource to be passed as the request body.
    configId: Required. Id of the requesting object If auto-generating Id
      server-side, remove this field and config_id from the method_signature
      of Create RPC
    parent: Required. Value for parent.
    requestId: Optional. An optional request ID to identify requests. Specify
      a unique request ID so that if you must retry your request, the server
      will know to ignore the request if it has already been completed. The
      server will guarantee that for at least 60 minutes since the first
      request. For example, consider a situation where you make an initial
      request and the request times out. If you make the request again with
      the same request ID, the server can check if original operation with the
      same request ID was received, and if so, will ignore the second request.
      This prevents clients from accidentally creating duplicate commitments.
      The request ID must be a valid UUID with the exception that zero UUID is
      not supported (00000000-0000-0000-0000-000000000000).
  """

  config = _messages.MessageField('Config', 1)
  configId = _messages.StringField(2)
  parent = _messages.StringField(3, required=True)
  requestId = _messages.StringField(4)


class AppconfigmanagerProjectsLocationsConfigsDeleteRequest(_messages.Message):
  r"""A AppconfigmanagerProjectsLocationsConfigsDeleteRequest object.

  Fields:
    name: Required. Name of the resource
    requestId: Optional. An optional request ID to identify requests. Specify
      a unique request ID so that if you must retry your request, the server
      will know to ignore the request if it has already been completed. The
      server will guarantee that for at least 60 minutes after the first
      request. For example, consider a situation where you make an initial
      request and the request times out. If you make the request again with
      the same request ID, the server can check if original operation with the
      same request ID was received, and if so, will ignore the second request.
      This prevents clients from accidentally creating duplicate commitments.
      The request ID must be a valid UUID with the exception that zero UUID is
      not supported (00000000-0000-0000-0000-000000000000).
  """

  name = _messages.StringField(1, required=True)
  requestId = _messages.StringField(2)


class AppconfigmanagerProjectsLocationsConfigsGetRequest(_messages.Message):
  r"""A AppconfigmanagerProjectsLocationsConfigsGetRequest object.

  Fields:
    name: Required. Name of the resource
  """

  name = _messages.StringField(1, required=True)


class AppconfigmanagerProjectsLocationsConfigsListRequest(_messages.Message):
  r"""A AppconfigmanagerProjectsLocationsConfigsListRequest object.

  Fields:
    filter: Optional. Filtering results
    orderBy: Optional. Hint for how to order the results
    pageSize: Optional. Requested page size. Server may return fewer items
      than requested. If unspecified, server will pick an appropriate default.
    pageToken: Optional. A token identifying a page of results the server
      should return.
    parent: Required. Parent value for ListConfigsRequest
  """

  filter = _messages.StringField(1)
  orderBy = _messages.StringField(2)
  pageSize = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(4)
  parent = _messages.StringField(5, required=True)


class AppconfigmanagerProjectsLocationsConfigsPatchRequest(_messages.Message):
  r"""A AppconfigmanagerProjectsLocationsConfigsPatchRequest object.

  Fields:
    config: A Config resource to be passed as the request body.
    name: Identifier. [Output only] The resource name of the Config in the
      format `projects/*locations/*/configs/*`.
    requestId: Optional. An optional request ID to identify requests. Specify
      a unique request ID so that if you must retry your request, the server
      will know to ignore the request if it has already been completed. The
      server will guarantee that for at least 60 minutes since the first
      request. For example, consider a situation where you make an initial
      request and the request times out. If you make the request again with
      the same request ID, the server can check if original operation with the
      same request ID was received, and if so, will ignore the second request.
      This prevents clients from accidentally creating duplicate commitments.
      The request ID must be a valid UUID with the exception that zero UUID is
      not supported (00000000-0000-0000-0000-000000000000).
    updateMask: Optional. Field mask is used to specify the fields to be
      overwritten in the Config resource by the update. The fields specified
      in the update_mask are relative to the resource, not the full request. A
      field will be overwritten if it is in the mask. If the user does not
      provide a mask then all fields will be overwritten. Empty field_mask is
      not allowed.
  """

  config = _messages.MessageField('Config', 1)
  name = _messages.StringField(2, required=True)
  requestId = _messages.StringField(3)
  updateMask = _messages.StringField(4)


class AppconfigmanagerProjectsLocationsConfigsVersionRendersGetRequest(_messages.Message):
  r"""A AppconfigmanagerProjectsLocationsConfigsVersionRendersGetRequest
  object.

  Enums:
    ViewValueValuesEnum: Optional. View of the ConfigVersionRender. In the
      default FULL view, all metadata & payload associated with the
      ConfigVersionRender will be returned.

  Fields:
    name: Required. Name of the resource
    view: Optional. View of the ConfigVersionRender. In the default FULL view,
      all metadata & payload associated with the ConfigVersionRender will be
      returned.
  """

  class ViewValueValuesEnum(_messages.Enum):
    r"""Optional. View of the ConfigVersionRender. In the default FULL view,
    all metadata & payload associated with the ConfigVersionRender will be
    returned.

    Values:
      VIEW_UNSPECIFIED: The default / unset value. The API will default to the
        BASIC view for LIST calls & FULL for GET calls..
      BASIC: Include only the metadata for the resource. This is the default
        view.
      FULL: Include metadata & other relevant payload data as well. For a
        ConfigVersion this implies that the response will hold the user
        provided payload. For a ConfigVersionRender this implies that the
        response will hold the user provided payload along with the rendered
        payload data.
    """
    VIEW_UNSPECIFIED = 0
    BASIC = 1
    FULL = 2

  name = _messages.StringField(1, required=True)
  view = _messages.EnumField('ViewValueValuesEnum', 2)


class AppconfigmanagerProjectsLocationsConfigsVersionRendersListRequest(_messages.Message):
  r"""A AppconfigmanagerProjectsLocationsConfigsVersionRendersListRequest
  object.

  Enums:
    ViewValueValuesEnum: Optional. View of the ConfigVersionRender. In the
      default BASIC view, only the metadata associated with the
      ConfigVersionRender will be returned.

  Fields:
    filter: Optional. Filtering results
    orderBy: Optional. Hint for how to order the results
    pageSize: Optional. Requested page size. Server may return fewer items
      than requested. If unspecified, server will pick an appropriate default.
    pageToken: Optional. A token identifying a page of results the server
      should return.
    parent: Required. Parent value for ListConfigVersionRendersRequest.
    view: Optional. View of the ConfigVersionRender. In the default BASIC
      view, only the metadata associated with the ConfigVersionRender will be
      returned.
  """

  class ViewValueValuesEnum(_messages.Enum):
    r"""Optional. View of the ConfigVersionRender. In the default BASIC view,
    only the metadata associated with the ConfigVersionRender will be
    returned.

    Values:
      VIEW_UNSPECIFIED: The default / unset value. The API will default to the
        BASIC view for LIST calls & FULL for GET calls..
      BASIC: Include only the metadata for the resource. This is the default
        view.
      FULL: Include metadata & other relevant payload data as well. For a
        ConfigVersion this implies that the response will hold the user
        provided payload. For a ConfigVersionRender this implies that the
        response will hold the user provided payload along with the rendered
        payload data.
    """
    VIEW_UNSPECIFIED = 0
    BASIC = 1
    FULL = 2

  filter = _messages.StringField(1)
  orderBy = _messages.StringField(2)
  pageSize = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(4)
  parent = _messages.StringField(5, required=True)
  view = _messages.EnumField('ViewValueValuesEnum', 6)


class AppconfigmanagerProjectsLocationsConfigsVersionsCreateRequest(_messages.Message):
  r"""A AppconfigmanagerProjectsLocationsConfigsVersionsCreateRequest object.

  Fields:
    configVersion: A ConfigVersion resource to be passed as the request body.
    configVersionId: Required. Id of the requesting object If auto-generating
      Id server-side, remove this field and config_version_id from the
      method_signature of Create RPC
    parent: Required. Value for parent.
    requestId: Optional. An optional request ID to identify requests. Specify
      a unique request ID so that if you must retry your request, the server
      will know to ignore the request if it has already been completed. The
      server will guarantee that for at least 60 minutes since the first
      request. For example, consider a situation where you make an initial
      request and the request times out. If you make the request again with
      the same request ID, the server can check if original operation with the
      same request ID was received, and if so, will ignore the second request.
      This prevents clients from accidentally creating duplicate commitments.
      The request ID must be a valid UUID with the exception that zero UUID is
      not supported (00000000-0000-0000-0000-000000000000).
  """

  configVersion = _messages.MessageField('ConfigVersion', 1)
  configVersionId = _messages.StringField(2)
  parent = _messages.StringField(3, required=True)
  requestId = _messages.StringField(4)


class AppconfigmanagerProjectsLocationsConfigsVersionsDeleteRequest(_messages.Message):
  r"""A AppconfigmanagerProjectsLocationsConfigsVersionsDeleteRequest object.

  Fields:
    name: Required. Name of the resource
    requestId: Optional. An optional request ID to identify requests. Specify
      a unique request ID so that if you must retry your request, the server
      will know to ignore the request if it has already been completed. The
      server will guarantee that for at least 60 minutes after the first
      request. For example, consider a situation where you make an initial
      request and the request times out. If you make the request again with
      the same request ID, the server can check if original operation with the
      same request ID was received, and if so, will ignore the second request.
      This prevents clients from accidentally creating duplicate commitments.
      The request ID must be a valid UUID with the exception that zero UUID is
      not supported (00000000-0000-0000-0000-000000000000).
  """

  name = _messages.StringField(1, required=True)
  requestId = _messages.StringField(2)


class AppconfigmanagerProjectsLocationsConfigsVersionsGetRequest(_messages.Message):
  r"""A AppconfigmanagerProjectsLocationsConfigsVersionsGetRequest object.

  Enums:
    ViewValueValuesEnum: Optional. View of the ConfigVersion. In the default
      FULL view, all metadata & payload associated with the ConfigVersion will
      be returned.

  Fields:
    name: Required. Name of the resource
    view: Optional. View of the ConfigVersion. In the default FULL view, all
      metadata & payload associated with the ConfigVersion will be returned.
  """

  class ViewValueValuesEnum(_messages.Enum):
    r"""Optional. View of the ConfigVersion. In the default FULL view, all
    metadata & payload associated with the ConfigVersion will be returned.

    Values:
      VIEW_UNSPECIFIED: The default / unset value. The API will default to the
        BASIC view for LIST calls & FULL for GET calls..
      BASIC: Include only the metadata for the resource. This is the default
        view.
      FULL: Include metadata & other relevant payload data as well. For a
        ConfigVersion this implies that the response will hold the user
        provided payload. For a ConfigVersionRender this implies that the
        response will hold the user provided payload along with the rendered
        payload data.
    """
    VIEW_UNSPECIFIED = 0
    BASIC = 1
    FULL = 2

  name = _messages.StringField(1, required=True)
  view = _messages.EnumField('ViewValueValuesEnum', 2)


class AppconfigmanagerProjectsLocationsConfigsVersionsListRequest(_messages.Message):
  r"""A AppconfigmanagerProjectsLocationsConfigsVersionsListRequest object.

  Enums:
    ViewValueValuesEnum: Optional. View of the ConfigVersion. In the default
      BASIC view, only the metadata associated with the ConfigVersion will be
      returned.

  Fields:
    filter: Optional. Filtering results
    orderBy: Optional. Hint for how to order the results
    pageSize: Optional. Requested page size. Server may return fewer items
      than requested. If unspecified, server will pick an appropriate default.
    pageToken: Optional. A token identifying a page of results the server
      should return.
    parent: Required. Parent value for ListConfigVersionsRequest.
    view: Optional. View of the ConfigVersion. In the default BASIC view, only
      the metadata associated with the ConfigVersion will be returned.
  """

  class ViewValueValuesEnum(_messages.Enum):
    r"""Optional. View of the ConfigVersion. In the default BASIC view, only
    the metadata associated with the ConfigVersion will be returned.

    Values:
      VIEW_UNSPECIFIED: The default / unset value. The API will default to the
        BASIC view for LIST calls & FULL for GET calls..
      BASIC: Include only the metadata for the resource. This is the default
        view.
      FULL: Include metadata & other relevant payload data as well. For a
        ConfigVersion this implies that the response will hold the user
        provided payload. For a ConfigVersionRender this implies that the
        response will hold the user provided payload along with the rendered
        payload data.
    """
    VIEW_UNSPECIFIED = 0
    BASIC = 1
    FULL = 2

  filter = _messages.StringField(1)
  orderBy = _messages.StringField(2)
  pageSize = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(4)
  parent = _messages.StringField(5, required=True)
  view = _messages.EnumField('ViewValueValuesEnum', 6)


class AppconfigmanagerProjectsLocationsConfigsVersionsPatchRequest(_messages.Message):
  r"""A AppconfigmanagerProjectsLocationsConfigsVersionsPatchRequest object.

  Fields:
    configVersion: A ConfigVersion resource to be passed as the request body.
    name: Identifier. [Output only] The resource name of the ConfigVersion in
      the format `projects/*/locations/*/configs/*/versions/*`.
    requestId: Optional. An optional request ID to identify requests. Specify
      a unique request ID so that if you must retry your request, the server
      will know to ignore the request if it has already been completed. The
      server will guarantee that for at least 60 minutes since the first
      request. For example, consider a situation where you make an initial
      request and the request times out. If you make the request again with
      the same request ID, the server can check if original operation with the
      same request ID was received, and if so, will ignore the second request.
      This prevents clients from accidentally creating duplicate commitments.
      The request ID must be a valid UUID with the exception that zero UUID is
      not supported (00000000-0000-0000-0000-000000000000).
    updateMask: Optional. Field mask is used to specify the fields to be
      overwritten in the ConfigVersion resource by the update. The fields
      specified in the update_mask are relative to the resource, not the full
      request. A field will be overwritten if it is in the mask. 1. Empty
      field mask is not supported. Specifying an empty field mask will result
      in an INVALID_ARGUMENT error. 2. Wildcard field mask is not supported.
      Specifying a wildcard field mask will result in an INVALID_ARGUMENT
      error. 3. Only a subset of fields are mutable. Mutable fields are: -
      (bool) disabled Specifying an immutable field in the field mask will
      result in an INVALID_ARGUMENT error.
  """

  configVersion = _messages.MessageField('ConfigVersion', 1)
  name = _messages.StringField(2, required=True)
  requestId = _messages.StringField(3)
  updateMask = _messages.StringField(4)


class AppconfigmanagerProjectsLocationsConfigsVersionsRenderRequest(_messages.Message):
  r"""A AppconfigmanagerProjectsLocationsConfigsVersionsRenderRequest object.

  Fields:
    name: Required. Name of the resource
  """

  name = _messages.StringField(1, required=True)


class AppconfigmanagerProjectsLocationsGetRequest(_messages.Message):
  r"""A AppconfigmanagerProjectsLocationsGetRequest object.

  Fields:
    name: Resource name for the location.
  """

  name = _messages.StringField(1, required=True)


class AppconfigmanagerProjectsLocationsListRequest(_messages.Message):
  r"""A AppconfigmanagerProjectsLocationsListRequest object.

  Fields:
    filter: A filter to narrow down results to a preferred subset. The
      filtering language accepts strings like `"displayName=tokyo"`, and is
      documented in more detail in [AIP-160](https://google.aip.dev/160).
    name: The resource that owns the locations collection, if applicable.
    pageSize: The maximum number of results to return. If not set, the service
      selects a default.
    pageToken: A page token received from the `next_page_token` field in the
      response. Send that page token to receive the subsequent page.
  """

  filter = _messages.StringField(1)
  name = _messages.StringField(2, required=True)
  pageSize = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(4)


class Config(_messages.Message):
  r"""Message describing Config object

  Enums:
    FormatValueValuesEnum: Optional. Specifies the format

  Messages:
    LabelsValue: Optional. Labels as key value pairs

  Fields:
    createTime: Output only. [Output only] Create time stamp
    format: Optional. Specifies the format
    labels: Optional. Labels as key value pairs
    name: Identifier. [Output only] The resource name of the Config in the
      format `projects/*locations/*/configs/*`.
    policyMember: Output only. [Output-only] policy member strings of a Google
      Cloud resource.
    serviceAgentEmail: Output only. Per-resource service agent email
    updateTime: Output only. [Output only] Update time stamp
  """

  class FormatValueValuesEnum(_messages.Enum):
    r"""Optional. Specifies the format

    Values:
      CONFIG_FORMAT_UNSPECIFIED: The default / unset value. The API will
        default to the UNFORMATTED format.
      UNFORMATTED: Unformatted.
      YAML: YAML format.
      JSON: JSON format.
    """
    CONFIG_FORMAT_UNSPECIFIED = 0
    UNFORMATTED = 1
    YAML = 2
    JSON = 3

  @encoding.MapUnrecognizedFields('additionalProperties')
  class LabelsValue(_messages.Message):
    r"""Optional. Labels as key value pairs

    Messages:
      AdditionalProperty: An additional property for a LabelsValue object.

    Fields:
      additionalProperties: Additional properties of type LabelsValue
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a LabelsValue object.

      Fields:
        key: Name of the additional property.
        value: A string attribute.
      """

      key = _messages.StringField(1)
      value = _messages.StringField(2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  createTime = _messages.StringField(1)
  format = _messages.EnumField('FormatValueValuesEnum', 2)
  labels = _messages.MessageField('LabelsValue', 3)
  name = _messages.StringField(4)
  policyMember = _messages.MessageField('ResourcePolicyMember', 5)
  serviceAgentEmail = _messages.StringField(6)
  updateTime = _messages.StringField(7)


class ConfigVersion(_messages.Message):
  r"""Message describing ConfigVersion object

  Messages:
    LabelsValue: Optional. Labels as key value pairs Labels are not supported
      for ConfigVersions. They are only supported at the Configs level.

  Fields:
    configVersionRender: Optional. Resource identifier to the corresponding
      ConfigVersionRender resource associated with the ConfigVersion.
    createTime: Output only. [Output only] Create time stamp
    disabled: Optional. Disabled boolean to determine if a ConfigVersion acts
      as a deleted (but recoverable) resource. Default value is False.
    labels: Optional. Labels as key value pairs Labels are not supported for
      ConfigVersions. They are only supported at the Configs level.
    name: Identifier. [Output only] The resource name of the ConfigVersion in
      the format `projects/*/locations/*/configs/*/versions/*`.
    payload: Required. Immutable. Payload content of a ConfigVersion resource.
      If the parent Config has a RAW ConfigType the payload data must point to
      a RawPayload & if the parent Config has a TEMPLATED ConfigType the
      payload data must point to a TemplateValuesPayload. This is only
      returned when the Get/(List?) request provides the View value of FULL.
    updateTime: Output only. [Output only] Update time stamp
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class LabelsValue(_messages.Message):
    r"""Optional. Labels as key value pairs Labels are not supported for
    ConfigVersions. They are only supported at the Configs level.

    Messages:
      AdditionalProperty: An additional property for a LabelsValue object.

    Fields:
      additionalProperties: Additional properties of type LabelsValue
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a LabelsValue object.

      Fields:
        key: Name of the additional property.
        value: A string attribute.
      """

      key = _messages.StringField(1)
      value = _messages.StringField(2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  configVersionRender = _messages.StringField(1)
  createTime = _messages.StringField(2)
  disabled = _messages.BooleanField(3)
  labels = _messages.MessageField('LabelsValue', 4)
  name = _messages.StringField(5)
  payload = _messages.MessageField('ConfigVersionPayload', 6)
  updateTime = _messages.StringField(7)


class ConfigVersionPayload(_messages.Message):
  r"""Message for storing a ConfigVersion resource's payload data based upon
  its type.

  Fields:
    rawPayload: Optional. REQUIRED for a ConfigType of RAW.
    templateValuesPayload: Optional. REQUIRED for a ConfigType of TEMPLATED.
  """

  rawPayload = _messages.MessageField('RawPayload', 1)
  templateValuesPayload = _messages.MessageField('TemplateValuesPayload', 2)


class ConfigVersionRender(_messages.Message):
  r"""Message describing ConfigVersionRender object

  Messages:
    LabelsValue: Optional. Labels as key value pairs Labels are not supported
      for ConfigVersionRenders. They are only supported at the Configs level.

  Fields:
    configVersion: Output only. Resource identifier to the corresponding
      ConfigVersion resource associated with the ConfigVersionRender.
    createTime: Output only. [Output only] Create time stamp
    disabled: Optional. Disabled boolean to determine if a ConfigVersionRender
      acts as a deleted (but recoverable) resource. Default value is False.
    labels: Optional. Labels as key value pairs Labels are not supported for
      ConfigVersionRenders. They are only supported at the Configs level.
    name: Output only. Identifier. [Output only] The resource name of the
      ConfigVersionRender in the format
      `projects/*/locations/*/configs/*/versionRenders/*`.
    payload: Required. Immutable. Payload content of a ConfigVersion resource.
      If the parent Config has a RAW ConfigType the payload data must point to
      a RawPayload & if the parent Config has a TEMPLATED ConfigType the
      payload data must point to a TemplateValuesPayload. This is only
      returned when the Get/(List?) request provides the View value of FULL.
    renderedPayload: Output only. Server generated rendered version of the
      user provided payload data (ConfigVersionPayload) which has all
      references to a SecretManager version resource substitutions. Any
      TemplateInstances referenced by the ConfigVersions are also processed to
      generate the final templated config output.
    updateTime: Output only. [Output only] Update time stamp
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class LabelsValue(_messages.Message):
    r"""Optional. Labels as key value pairs Labels are not supported for
    ConfigVersionRenders. They are only supported at the Configs level.

    Messages:
      AdditionalProperty: An additional property for a LabelsValue object.

    Fields:
      additionalProperties: Additional properties of type LabelsValue
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a LabelsValue object.

      Fields:
        key: Name of the additional property.
        value: A string attribute.
      """

      key = _messages.StringField(1)
      value = _messages.StringField(2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  configVersion = _messages.StringField(1)
  createTime = _messages.StringField(2)
  disabled = _messages.BooleanField(3)
  labels = _messages.MessageField('LabelsValue', 4)
  name = _messages.StringField(5)
  payload = _messages.MessageField('ConfigVersionPayload', 6)
  renderedPayload = _messages.BytesField(7)
  updateTime = _messages.StringField(8)


class Empty(_messages.Message):
  r"""A generic empty message that you can re-use to avoid defining duplicated
  empty messages in your APIs. A typical example is to use it as the request
  or the response type of an API method. For instance: service Foo { rpc
  Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }
  """



class ListConfigVersionRendersResponse(_messages.Message):
  r"""Message for response to listing ConfigVersionRenders

  Fields:
    configVersionRenders: The list of Config
    nextPageToken: A token identifying a page of results the server should
      return.
    unreachable: Locations that could not be reached.
  """

  configVersionRenders = _messages.MessageField('ConfigVersionRender', 1, repeated=True)
  nextPageToken = _messages.StringField(2)
  unreachable = _messages.StringField(3, repeated=True)


class ListConfigVersionsResponse(_messages.Message):
  r"""Message for response to listing Configs

  Fields:
    configVersions: The list of Config
    nextPageToken: A token identifying a page of results the server should
      return.
    unreachable: Locations that could not be reached.
  """

  configVersions = _messages.MessageField('ConfigVersion', 1, repeated=True)
  nextPageToken = _messages.StringField(2)
  unreachable = _messages.StringField(3, repeated=True)


class ListConfigsResponse(_messages.Message):
  r"""Message for response to listing Configs

  Fields:
    configs: The list of Config
    nextPageToken: A token identifying a page of results the server should
      return.
    unreachable: Locations that could not be reached.
  """

  configs = _messages.MessageField('Config', 1, repeated=True)
  nextPageToken = _messages.StringField(2)
  unreachable = _messages.StringField(3, repeated=True)


class ListLocationsResponse(_messages.Message):
  r"""The response message for Locations.ListLocations.

  Fields:
    locations: A list of locations that matches the specified filter in the
      request.
    nextPageToken: The standard List next-page token.
  """

  locations = _messages.MessageField('Location', 1, repeated=True)
  nextPageToken = _messages.StringField(2)


class Location(_messages.Message):
  r"""A resource that represents a Google Cloud location.

  Messages:
    LabelsValue: Cross-service attributes for the location. For example
      {"cloud.googleapis.com/region": "us-east1"}
    MetadataValue: Service-specific metadata. For example the available
      capacity at the given location.

  Fields:
    displayName: The friendly name for this location, typically a nearby city
      name. For example, "Tokyo".
    labels: Cross-service attributes for the location. For example
      {"cloud.googleapis.com/region": "us-east1"}
    locationId: The canonical id for this location. For example: `"us-east1"`.
    metadata: Service-specific metadata. For example the available capacity at
      the given location.
    name: Resource name for the location, which may vary between
      implementations. For example: `"projects/example-project/locations/us-
      east1"`
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class LabelsValue(_messages.Message):
    r"""Cross-service attributes for the location. For example
    {"cloud.googleapis.com/region": "us-east1"}

    Messages:
      AdditionalProperty: An additional property for a LabelsValue object.

    Fields:
      additionalProperties: Additional properties of type LabelsValue
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a LabelsValue object.

      Fields:
        key: Name of the additional property.
        value: A string attribute.
      """

      key = _messages.StringField(1)
      value = _messages.StringField(2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  @encoding.MapUnrecognizedFields('additionalProperties')
  class MetadataValue(_messages.Message):
    r"""Service-specific metadata. For example the available capacity at the
    given location.

    Messages:
      AdditionalProperty: An additional property for a MetadataValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a MetadataValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  displayName = _messages.StringField(1)
  labels = _messages.MessageField('LabelsValue', 2)
  locationId = _messages.StringField(3)
  metadata = _messages.MessageField('MetadataValue', 4)
  name = _messages.StringField(5)


class RawPayload(_messages.Message):
  r"""Message for storing a ConfigVersion resource payload.

  Fields:
    data: Required. User provided content of a ConfigVersion. It can hold
      references to Secret Manager SecretVersion resources.
  """

  data = _messages.BytesField(1)


class RenderConfigVersionResponse(_messages.Message):
  r"""Message describing RenderConfigVersionResponse object

  Fields:
    configVersion: Output only. Resource identifier to the corresponding
      ConfigVersion resource.
    payload: Payload content of a ConfigVersion resource. If the parent Config
      has a RAW ConfigType the payload data must point to a RawPayload & if
      the parent Config has a TEMPLATED ConfigType the payload data must point
      to a TemplateValuesPayload. This is only returned when the Get/(List?)
      request provides the View value of FULL.
    renderedPayload: Output only. Server generated rendered version of the
      user provided payload data (ConfigVersionPayload) which has all
      references to a SecretManager version resource substitutions.
  """

  configVersion = _messages.StringField(1)
  payload = _messages.MessageField('ConfigVersionPayload', 2)
  renderedPayload = _messages.BytesField(3)


class ResourcePolicyMember(_messages.Message):
  r"""Output-only policy member strings of a Google Cloud resource's built-in
  identity.

  Fields:
    iamPolicyNamePrincipal: Output only. IAM policy binding member referring
      to a Google Cloud resource by user-assigned name
      (https://google.aip.dev/122). If a resource is deleted and recreated
      with the same name, the binding will be applicable to the new resource.
      Example: `principal://parametermanager.googleapis.com/projects/12345/nam
      e/locations/us-central1-a/parameters/my-parameter`
    iamPolicyUidPrincipal: Output only. IAM policy binding member referring to
      a Google Cloud resource by system-assigned unique identifier
      (https://google.aip.dev/148#uid). If a resource is deleted and recreated
      with the same name, the binding will not be applicable to the new
      resource Example: `principal://parametermanager.googleapis.com/projects/
      12345/uid/locations/us-central1-a/parameters/a918fed5`
  """

  iamPolicyNamePrincipal = _messages.StringField(1)
  iamPolicyUidPrincipal = _messages.StringField(2)


class StandardQueryParameters(_messages.Message):
  r"""Query parameters accepted by all methods.

  Enums:
    FXgafvValueValuesEnum: V1 error format.
    AltValueValuesEnum: Data format for response.

  Fields:
    f__xgafv: V1 error format.
    access_token: OAuth access token.
    alt: Data format for response.
    callback: JSONP
    fields: Selector specifying which fields to include in a partial response.
    key: API key. Your API key identifies your project and provides you with
      API access, quota, and reports. Required unless you provide an OAuth 2.0
      token.
    oauth_token: OAuth 2.0 token for the current user.
    prettyPrint: Returns response with indentations and line breaks.
    quotaUser: Available to use for quota purposes for server-side
      applications. Can be any arbitrary string assigned to a user, but should
      not exceed 40 characters.
    trace: A tracing token of the form "token:<tokenid>" to include in api
      requests.
    uploadType: Legacy upload protocol for media (e.g. "media", "multipart").
    upload_protocol: Upload protocol for media (e.g. "raw", "multipart").
  """

  class AltValueValuesEnum(_messages.Enum):
    r"""Data format for response.

    Values:
      json: Responses with Content-Type of application/json
      media: Media download with context-dependent Content-Type
      proto: Responses with Content-Type of application/x-protobuf
    """
    json = 0
    media = 1
    proto = 2

  class FXgafvValueValuesEnum(_messages.Enum):
    r"""V1 error format.

    Values:
      _1: v1 error format
      _2: v2 error format
    """
    _1 = 0
    _2 = 1

  f__xgafv = _messages.EnumField('FXgafvValueValuesEnum', 1)
  access_token = _messages.StringField(2)
  alt = _messages.EnumField('AltValueValuesEnum', 3, default='json')
  callback = _messages.StringField(4)
  fields = _messages.StringField(5)
  key = _messages.StringField(6)
  oauth_token = _messages.StringField(7)
  prettyPrint = _messages.BooleanField(8, default=True)
  quotaUser = _messages.StringField(9)
  trace = _messages.StringField(10)
  uploadType = _messages.StringField(11)
  upload_protocol = _messages.StringField(12)


class TemplateValuesPayload(_messages.Message):
  r"""Message for storing a TEMPLATED ConfigType Config resource.

  Fields:
    data: Required. User provided content of a ConfigVersion in reference to a
      TemplateInstance. It can hold references to Secret Manager SecretVersion
      resources & must hold all template variable definitions required by a
      TemplateInstance to be rendered properly.
  """

  data = _messages.BytesField(1)


encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2')
