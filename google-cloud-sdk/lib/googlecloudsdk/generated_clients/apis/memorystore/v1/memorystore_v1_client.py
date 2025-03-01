"""Generated client library for memorystore version v1."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.generated_clients.apis.memorystore.v1 import memorystore_v1_messages as messages


class MemorystoreV1(base_api.BaseApiClient):
  """Generated client library for service memorystore version v1."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://memorystore.googleapis.com/'
  MTLS_BASE_URL = 'https://memorystore.mtls.googleapis.com/'

  _PACKAGE = 'memorystore'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
  _VERSION = 'v1'
  _CLIENT_ID = 'CLIENT_ID'
  _CLIENT_SECRET = 'CLIENT_SECRET'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'MemorystoreV1'
  _URL_VERSION = 'v1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new memorystore handle."""
    url = url or self.BASE_URL
    super(MemorystoreV1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.projects_locations_instances = self.ProjectsLocationsInstancesService(self)
    self.projects_locations_operations = self.ProjectsLocationsOperationsService(self)
    self.projects_locations = self.ProjectsLocationsService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsLocationsInstancesService(base_api.BaseApiService):
    """Service class for the projects_locations_instances resource."""

    _NAME = 'projects_locations_instances'

    def __init__(self, client):
      super(MemorystoreV1.ProjectsLocationsInstancesService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a new Instance in a given project and location.

      Args:
        request: (MemorystoreProjectsLocationsInstancesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/instances',
        http_method='POST',
        method_id='memorystore.projects.locations.instances.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['instanceId', 'requestId'],
        relative_path='v1/{+parent}/instances',
        request_field='instance',
        request_type_name='MemorystoreProjectsLocationsInstancesCreateRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a single Instance.

      Args:
        request: (MemorystoreProjectsLocationsInstancesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/instances/{instancesId}',
        http_method='DELETE',
        method_id='memorystore.projects.locations.instances.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['requestId'],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='MemorystoreProjectsLocationsInstancesDeleteRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets details of a single Instance.

      Args:
        request: (MemorystoreProjectsLocationsInstancesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Instance) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/instances/{instancesId}',
        http_method='GET',
        method_id='memorystore.projects.locations.instances.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='MemorystoreProjectsLocationsInstancesGetRequest',
        response_type_name='Instance',
        supports_download=False,
    )

    def GetCertificateAuthority(self, request, global_params=None):
      r"""Gets details about the certificate authority for an Instance.

      Args:
        request: (MemorystoreProjectsLocationsInstancesGetCertificateAuthorityRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (CertificateAuthority) The response message.
      """
      config = self.GetMethodConfig('GetCertificateAuthority')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetCertificateAuthority.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/instances/{instancesId}/certificateAuthority',
        http_method='GET',
        method_id='memorystore.projects.locations.instances.getCertificateAuthority',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}/certificateAuthority',
        request_field='',
        request_type_name='MemorystoreProjectsLocationsInstancesGetCertificateAuthorityRequest',
        response_type_name='CertificateAuthority',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists Instances in a given project and location.

      Args:
        request: (MemorystoreProjectsLocationsInstancesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListInstancesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/instances',
        http_method='GET',
        method_id='memorystore.projects.locations.instances.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'orderBy', 'pageSize', 'pageToken'],
        relative_path='v1/{+parent}/instances',
        request_field='',
        request_type_name='MemorystoreProjectsLocationsInstancesListRequest',
        response_type_name='ListInstancesResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates the parameters of a single Instance.

      Args:
        request: (MemorystoreProjectsLocationsInstancesPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/instances/{instancesId}',
        http_method='PATCH',
        method_id='memorystore.projects.locations.instances.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['requestId', 'updateMask'],
        relative_path='v1/{+name}',
        request_field='instance',
        request_type_name='MemorystoreProjectsLocationsInstancesPatchRequest',
        response_type_name='Operation',
        supports_download=False,
    )

  class ProjectsLocationsOperationsService(base_api.BaseApiService):
    """Service class for the projects_locations_operations resource."""

    _NAME = 'projects_locations_operations'

    def __init__(self, client):
      super(MemorystoreV1.ProjectsLocationsOperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Cancel(self, request, global_params=None):
      r"""Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use Operations.GetOperation or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an Operation.error value with a google.rpc.Status.code of `1`, corresponding to `Code.CANCELLED`.

      Args:
        request: (MemorystoreProjectsLocationsOperationsCancelRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Cancel')
      return self._RunMethod(
          config, request, global_params=global_params)

    Cancel.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}:cancel',
        http_method='POST',
        method_id='memorystore.projects.locations.operations.cancel',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}:cancel',
        request_field='',
        request_type_name='MemorystoreProjectsLocationsOperationsCancelRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a long-running operation. This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`.

      Args:
        request: (MemorystoreProjectsLocationsOperationsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}',
        http_method='DELETE',
        method_id='memorystore.projects.locations.operations.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='MemorystoreProjectsLocationsOperationsDeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

      Args:
        request: (MemorystoreProjectsLocationsOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}',
        http_method='GET',
        method_id='memorystore.projects.locations.operations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='MemorystoreProjectsLocationsOperationsGetRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`.

      Args:
        request: (MemorystoreProjectsLocationsOperationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListOperationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/operations',
        http_method='GET',
        method_id='memorystore.projects.locations.operations.list',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1/{+name}/operations',
        request_field='',
        request_type_name='MemorystoreProjectsLocationsOperationsListRequest',
        response_type_name='ListOperationsResponse',
        supports_download=False,
    )

  class ProjectsLocationsService(base_api.BaseApiService):
    """Service class for the projects_locations resource."""

    _NAME = 'projects_locations'

    def __init__(self, client):
      super(MemorystoreV1.ProjectsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets information about a location.

      Args:
        request: (MemorystoreProjectsLocationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Location) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}',
        http_method='GET',
        method_id='memorystore.projects.locations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='MemorystoreProjectsLocationsGetRequest',
        response_type_name='Location',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists information about the supported locations for this service.

      Args:
        request: (MemorystoreProjectsLocationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListLocationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations',
        http_method='GET',
        method_id='memorystore.projects.locations.list',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1/{+name}/locations',
        request_field='',
        request_type_name='MemorystoreProjectsLocationsListRequest',
        response_type_name='ListLocationsResponse',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = 'projects'

    def __init__(self, client):
      super(MemorystoreV1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }
