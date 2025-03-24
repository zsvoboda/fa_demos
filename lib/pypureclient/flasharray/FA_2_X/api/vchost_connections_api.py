# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.X
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re

# python 2 and python 3 compatibility library
import six
import uuid
from typing import List, Optional

from .. import models

class VchostConnectionsApi(object):

    def __init__(self, api_client):
        self.api_client = api_client

    def api2_x_vchost_connections_delete_with_http_info(
        self,
        all_vchosts=None,  # type: bool
        authorization=None,  # type: str
        protocol_endpoint_ids=None,  # type: List[str]
        protocol_endpoint_names=None,  # type: List[str]
        x_request_id=None,  # type: str
        vchost_ids=None,  # type: List[str]
        vchost_names=None,  # type: List[str]
        async_req=False,  # type: bool
        _return_http_data_only=False,  # type: bool
        _preload_content=True,  # type: bool
        _request_timeout=None,  # type: Optional[int]
    ):
        # type: (...) -> None
        """Delete the vchost-connection between a protocol endpoint and its vchost

        Deletes the vchost-connection between a protocol endpoint and its vchost. The storage container represented by the protocol endpoint will no longer be visible to the vCenter represented by the vchost. One of the `protocol_endpoint_names` or `protocol_endpoint_ids` query parameters, and one of the `vchost_names` or `vchost_ids` query parameters are required. But if `all_vchosts` is set to `true`, `vchost_names` and `vchost_ids` should not be specified.  
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api2_x_vchost_connections_delete_with_http_info(async_req=True)
        >>> result = thread.get()

        :param bool all_vchosts: If set to `true`, the storage container represented by the protocol endpoint is accessible to all vchosts. Users should not specify `vchost_ids` or `vchost_names` in the request. If set to `false`, the storage container represented by the protocol endpoint is only accessible to the vchosts that have explicit vchost-connections with the protocol endpoint. Users need to specify `vchost_ids` or `vchost_names` in the request. 
        :param str authorization: Access token (in JWT format) required to use any API endpoint (except `/oauth2`, `/login`, and `/logout`) 
        :param list[str] protocol_endpoint_ids: A comma-separated list of protocol endpoint IDs. Performs the operation on the protocol endpoints specified. For example, `peid01,peid02`. Cannot be used in conjunction with `protocol_endpoint_names`. If the list contains more than one value, then `vchost_ids` or `vchost_names` must have exactly one value. 
        :param list[str] protocol_endpoint_names: A comma-separated list of protocol endpoint names. Performs the operation on the protocol endpoints specified. For example, `pe01,pe02`. Cannot be used in conjunction with `protocol_endpoint_ids`. If the list contains more than one value, then `vchost_ids` or `vchost_names` must have exactly one value. 
        :param str x_request_id: Supplied by client during request or generated by server. 
        :param list[str] vchost_ids: A comma-separated list of vchost IDs. Performs the operation on the vchosts specified. For example, `vchostid01,vchostid02`. Cannot be used in conjunction with `vchost_names`. If the list contains more than one value, then `protocol_endpoint_ids` or `protocol_endpoint_names` must have exactly one value. 
        :param list[str] vchost_names: A comma-separated list of vchost names. Performs the operation on the vchosts specified. For example, `vchost01,vchost02`. Cannot be used in conjunction with `vchost_ids`. If the list contains more than one value, then `protocol_endpoint_ids` or `protocol_endpoint_names` must have exactly one value. 
        :param bool async_req: Request runs in separate thread and method returns multiprocessing.pool.ApplyResult.
        :param bool _return_http_data_only: Returns only data field.
        :param bool _preload_content: Response is converted into objects.
        :param int _request_timeout: Total request timeout in seconds.
                 It can also be a tuple of (connection time, read time) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        if protocol_endpoint_ids is not None:
            if not isinstance(protocol_endpoint_ids, list):
                protocol_endpoint_ids = [protocol_endpoint_ids]
        if protocol_endpoint_names is not None:
            if not isinstance(protocol_endpoint_names, list):
                protocol_endpoint_names = [protocol_endpoint_names]
        if vchost_ids is not None:
            if not isinstance(vchost_ids, list):
                vchost_ids = [vchost_ids]
        if vchost_names is not None:
            if not isinstance(vchost_names, list):
                vchost_names = [vchost_names]
        params = {k: v for k, v in six.iteritems(locals()) if v is not None}

        # Convert the filter into a string
        if params.get('filter'):
            params['filter'] = str(params['filter'])
        if params.get('sort'):
            params['sort'] = [str(_x) for _x in params['sort']]
        # Assign a value to X-Request-Id if it is not specified
        if params.get('x_request_id') is None:
            params['x_request_id'] = str(uuid.uuid4())

        collection_formats = {}
        path_params = {}

        query_params = []
        if 'all_vchosts' in params:
            query_params.append(('all_vchosts', params['all_vchosts']))
        if 'protocol_endpoint_ids' in params:
            query_params.append(('protocol_endpoint_ids', params['protocol_endpoint_ids']))
            collection_formats['protocol_endpoint_ids'] = 'csv'
        if 'protocol_endpoint_names' in params:
            query_params.append(('protocol_endpoint_names', params['protocol_endpoint_names']))
            collection_formats['protocol_endpoint_names'] = 'csv'
        if 'vchost_ids' in params:
            query_params.append(('vchost_ids', params['vchost_ids']))
            collection_formats['vchost_ids'] = 'csv'
        if 'vchost_names' in params:
            query_params.append(('vchost_names', params['vchost_names']))
            collection_formats['vchost_names'] = 'csv'

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']
        if 'x_request_id' in params:
            header_params['X-Request-ID'] = params['x_request_id']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/api/2.X/vchost-connections', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,
            auth_settings=auth_settings,
            async_req=async_req,
            _return_http_data_only=_return_http_data_only,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            collection_formats=collection_formats,
        )

    def api2_x_vchost_connections_get_with_http_info(
        self,
        all_vchosts=None,  # type: bool
        authorization=None,  # type: str
        x_request_id=None,  # type: str
        continuation_token=None,  # type: str
        filter=None,  # type: str
        limit=None,  # type: int
        offset=None,  # type: int
        protocol_endpoint_ids=None,  # type: List[str]
        protocol_endpoint_names=None,  # type: List[str]
        sort=None,  # type: List[str]
        total_item_count=None,  # type: bool
        vchost_ids=None,  # type: List[str]
        vchost_names=None,  # type: List[str]
        async_req=False,  # type: bool
        _return_http_data_only=False,  # type: bool
        _preload_content=True,  # type: bool
        _request_timeout=None,  # type: Optional[int]
    ):
        # type: (...) -> models.VchostConnectionGetResponse
        """List the vchost-connections between protocol endpoint and vchost.

        Displays a list of vchost-connections between the protocol endpoint and vchost.  
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api2_x_vchost_connections_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param bool all_vchosts: If set to `true`, the storage container represented by the protocol endpoint is accessible to all vchosts. Users should not specify `vchost_ids` or `vchost_names` in the request. If set to `false`, the storage container represented by the protocol endpoint is only accessible to the vchosts that have explicit vchost-connections with the protocol endpoint. Users need to specify `vchost_ids` or `vchost_names` in the request. 
        :param str authorization: Access token (in JWT format) required to use any API endpoint (except `/oauth2`, `/login`, and `/logout`) 
        :param str x_request_id: Supplied by client during request or generated by server. 
        :param str continuation_token: A token used to retrieve the next page of data with some consistency guaranteed. The token is a Base64 encoded value. Set `continuation_token` to the system-generated token taken from the `x-next-token` header field of the response. A query has reached its last page when the response does not include a token. Pagination requires the `limit` and `continuation_token` query parameters. 
        :param str filter: Narrows down the results to only the response objects that satisfy the filter criteria. 
        :param int limit: Limits the size of the response to the specified number of objects on each page. To return the total number of resources, set `limit=0`. The total number of resources is returned as a `total_item_count` value. If the page size requested is larger than the system maximum limit, the server returns the maximum limit, disregarding the requested page size. 
        :param int offset: The starting position based on the results of the query in relation to the full set of response objects returned. 
        :param list[str] protocol_endpoint_ids: A comma-separated list of protocol endpoint IDs. Performs the operation on the protocol endpoints specified. For example, `peid01,peid02`. Cannot be used in conjunction with `protocol_endpoint_names`. If the list contains more than one value, then `vchost_ids` or `vchost_names` must have exactly one value. 
        :param list[str] protocol_endpoint_names: A comma-separated list of protocol endpoint names. Performs the operation on the protocol endpoints specified. For example, `pe01,pe02`. Cannot be used in conjunction with `protocol_endpoint_ids`. If the list contains more than one value, then `vchost_ids` or `vchost_names` must have exactly one value. 
        :param list[str] sort: Returns the response objects in the order specified. Set `sort` to the name in the response by which to sort. Sorting can be performed on any of the names in the response, and the objects can be sorted in ascending or descending order. By default, the response objects are sorted in ascending order. To sort in descending order, append the minus sign (`-`) to the name. A single request can be sorted on multiple objects. For example, you can sort all volumes from largest to smallest volume size, and then sort volumes of the same size in ascending order by volume name. To sort on multiple names, list the names as comma-separated values. 
        :param bool total_item_count: If set to `true`, the `total_item_count` matching the specified query parameters is calculated and returned in the response. If set to `false`, the `total_item_count` is `null` in the response. This may speed up queries where the `total_item_count` is large. If not specified, defaults to `false`. 
        :param list[str] vchost_ids: A comma-separated list of vchost IDs. Performs the operation on the vchosts specified. For example, `vchostid01,vchostid02`. Cannot be used in conjunction with `vchost_names`. If the list contains more than one value, then `protocol_endpoint_ids` or `protocol_endpoint_names` must have exactly one value. 
        :param list[str] vchost_names: A comma-separated list of vchost names. Performs the operation on the vchosts specified. For example, `vchost01,vchost02`. Cannot be used in conjunction with `vchost_ids`. If the list contains more than one value, then `protocol_endpoint_ids` or `protocol_endpoint_names` must have exactly one value. 
        :param bool async_req: Request runs in separate thread and method returns multiprocessing.pool.ApplyResult.
        :param bool _return_http_data_only: Returns only data field.
        :param bool _preload_content: Response is converted into objects.
        :param int _request_timeout: Total request timeout in seconds.
                 It can also be a tuple of (connection time, read time) timeouts.
        :return: VchostConnectionGetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        if protocol_endpoint_ids is not None:
            if not isinstance(protocol_endpoint_ids, list):
                protocol_endpoint_ids = [protocol_endpoint_ids]
        if protocol_endpoint_names is not None:
            if not isinstance(protocol_endpoint_names, list):
                protocol_endpoint_names = [protocol_endpoint_names]
        if sort is not None:
            if not isinstance(sort, list):
                sort = [sort]
        if vchost_ids is not None:
            if not isinstance(vchost_ids, list):
                vchost_ids = [vchost_ids]
        if vchost_names is not None:
            if not isinstance(vchost_names, list):
                vchost_names = [vchost_names]
        params = {k: v for k, v in six.iteritems(locals()) if v is not None}

        # Convert the filter into a string
        if params.get('filter'):
            params['filter'] = str(params['filter'])
        if params.get('sort'):
            params['sort'] = [str(_x) for _x in params['sort']]
        # Assign a value to X-Request-Id if it is not specified
        if params.get('x_request_id') is None:
            params['x_request_id'] = str(uuid.uuid4())

        if 'limit' in params and params['limit'] < 0:
            raise ValueError("Invalid value for parameter `limit` when calling `api2_x_vchost_connections_get`, must be a value greater than or equal to `0`")
        if 'offset' in params and params['offset'] < 0:
            raise ValueError("Invalid value for parameter `offset` when calling `api2_x_vchost_connections_get`, must be a value greater than or equal to `0`")
        collection_formats = {}
        path_params = {}

        query_params = []
        if 'all_vchosts' in params:
            query_params.append(('all_vchosts', params['all_vchosts']))
        if 'continuation_token' in params:
            query_params.append(('continuation_token', params['continuation_token']))
        if 'filter' in params:
            query_params.append(('filter', params['filter']))
        if 'limit' in params:
            query_params.append(('limit', params['limit']))
        if 'offset' in params:
            query_params.append(('offset', params['offset']))
        if 'protocol_endpoint_ids' in params:
            query_params.append(('protocol_endpoint_ids', params['protocol_endpoint_ids']))
            collection_formats['protocol_endpoint_ids'] = 'csv'
        if 'protocol_endpoint_names' in params:
            query_params.append(('protocol_endpoint_names', params['protocol_endpoint_names']))
            collection_formats['protocol_endpoint_names'] = 'csv'
        if 'sort' in params:
            query_params.append(('sort', params['sort']))
            collection_formats['sort'] = 'csv'
        if 'total_item_count' in params:
            query_params.append(('total_item_count', params['total_item_count']))
        if 'vchost_ids' in params:
            query_params.append(('vchost_ids', params['vchost_ids']))
            collection_formats['vchost_ids'] = 'csv'
        if 'vchost_names' in params:
            query_params.append(('vchost_names', params['vchost_names']))
            collection_formats['vchost_names'] = 'csv'

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']
        if 'x_request_id' in params:
            header_params['X-Request-ID'] = params['x_request_id']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/api/2.X/vchost-connections', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VchostConnectionGetResponse',
            auth_settings=auth_settings,
            async_req=async_req,
            _return_http_data_only=_return_http_data_only,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            collection_formats=collection_formats,
        )

    def api2_x_vchost_connections_post_with_http_info(
        self,
        all_vchosts=None,  # type: bool
        allow_stretched_multi_vchost=None,  # type: bool
        authorization=None,  # type: str
        protocol_endpoint_names=None,  # type: List[str]
        protocol_endpoint_ids=None,  # type: List[str]
        x_request_id=None,  # type: str
        vchost_ids=None,  # type: List[str]
        vchost_names=None,  # type: List[str]
        async_req=False,  # type: bool
        _return_http_data_only=False,  # type: bool
        _preload_content=True,  # type: bool
        _request_timeout=None,  # type: Optional[int]
    ):
        # type: (...) -> models.VchostConnectionResponse
        """Create a vchost-connection between protocol endpoint and vchost.

        Creates a vchost-connection between protocol endpoint and vchost. Each vchost is associated with a vCenter. Each protocol endpoint is associated with a storage container. A vchost-connection makes the storage container accessible to the vCenter when the vCenter attempts to mount the container. One of `protocol_endpoint_names` or `protocol_endpoint_ids` query parameters and one of `vchost_names` or `vchost_ids` query parameters are required. But if `all_vchosts` is set to `true`, `vchost_names` and `vchost_ids` should not be specified. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api2_x_vchost_connections_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param bool all_vchosts: If set to `true`, the storage container represented by the protocol endpoint is accessible to all vchosts. Users should not specify `vchost_ids` or `vchost_names` in the request. If set to `false`, the storage container represented by the protocol endpoint is only accessible to the vchosts that have explicit vchost-connections with the protocol endpoint. Users need to specify `vchost_ids` or `vchost_names` in the request. 
        :param bool allow_stretched_multi_vchost: If set to `true`, users are allowed to create a new vchost-connection to a stretched container that already has a vchost-connection. In principle, a stretched container can only have one vchost-connection at a time. 
        :param str authorization: Access token (in JWT format) required to use any API endpoint (except `/oauth2`, `/login`, and `/logout`) 
        :param list[str] protocol_endpoint_names: A comma-separated list of protocol endpoint names. Performs the operation on the protocol endpoints specified. For example, `pe01,pe02`. Cannot be used in conjunction with `protocol_endpoint_ids`. If the list contains more than one value, then `vchost_ids` or `vchost_names` must have exactly one value. 
        :param list[str] protocol_endpoint_ids: A comma-separated list of protocol endpoint IDs. Performs the operation on the protocol endpoints specified. For example, `peid01,peid02`. Cannot be used in conjunction with `protocol_endpoint_names`. If the list contains more than one value, then `vchost_ids` or `vchost_names` must have exactly one value. 
        :param str x_request_id: Supplied by client during request or generated by server. 
        :param list[str] vchost_ids: A comma-separated list of vchost IDs. Performs the operation on the vchosts specified. For example, `vchostid01,vchostid02`. Cannot be used in conjunction with `vchost_names`. If the list contains more than one value, then `protocol_endpoint_ids` or `protocol_endpoint_names` must have exactly one value. 
        :param list[str] vchost_names: A comma-separated list of vchost names. Performs the operation on the vchosts specified. For example, `vchost01,vchost02`. Cannot be used in conjunction with `vchost_ids`. If the list contains more than one value, then `protocol_endpoint_ids` or `protocol_endpoint_names` must have exactly one value. 
        :param bool async_req: Request runs in separate thread and method returns multiprocessing.pool.ApplyResult.
        :param bool _return_http_data_only: Returns only data field.
        :param bool _preload_content: Response is converted into objects.
        :param int _request_timeout: Total request timeout in seconds.
                 It can also be a tuple of (connection time, read time) timeouts.
        :return: VchostConnectionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        if protocol_endpoint_names is not None:
            if not isinstance(protocol_endpoint_names, list):
                protocol_endpoint_names = [protocol_endpoint_names]
        if protocol_endpoint_ids is not None:
            if not isinstance(protocol_endpoint_ids, list):
                protocol_endpoint_ids = [protocol_endpoint_ids]
        if vchost_ids is not None:
            if not isinstance(vchost_ids, list):
                vchost_ids = [vchost_ids]
        if vchost_names is not None:
            if not isinstance(vchost_names, list):
                vchost_names = [vchost_names]
        params = {k: v for k, v in six.iteritems(locals()) if v is not None}

        # Convert the filter into a string
        if params.get('filter'):
            params['filter'] = str(params['filter'])
        if params.get('sort'):
            params['sort'] = [str(_x) for _x in params['sort']]
        # Assign a value to X-Request-Id if it is not specified
        if params.get('x_request_id') is None:
            params['x_request_id'] = str(uuid.uuid4())

        collection_formats = {}
        path_params = {}

        query_params = []
        if 'all_vchosts' in params:
            query_params.append(('all_vchosts', params['all_vchosts']))
        if 'allow_stretched_multi_vchost' in params:
            query_params.append(('allow_stretched_multi_vchost', params['allow_stretched_multi_vchost']))
        if 'protocol_endpoint_names' in params:
            query_params.append(('protocol_endpoint_names', params['protocol_endpoint_names']))
            collection_formats['protocol_endpoint_names'] = 'csv'
        if 'protocol_endpoint_ids' in params:
            query_params.append(('protocol_endpoint_ids', params['protocol_endpoint_ids']))
            collection_formats['protocol_endpoint_ids'] = 'csv'
        if 'vchost_ids' in params:
            query_params.append(('vchost_ids', params['vchost_ids']))
            collection_formats['vchost_ids'] = 'csv'
        if 'vchost_names' in params:
            query_params.append(('vchost_names', params['vchost_names']))
            collection_formats['vchost_names'] = 'csv'

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']
        if 'x_request_id' in params:
            header_params['X-Request-ID'] = params['x_request_id']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/api/2.X/vchost-connections', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VchostConnectionResponse',
            auth_settings=auth_settings,
            async_req=async_req,
            _return_http_data_only=_return_http_data_only,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            collection_formats=collection_formats,
        )
