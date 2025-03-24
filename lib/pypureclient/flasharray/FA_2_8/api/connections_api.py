# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re

# python 2 and python 3 compatibility library
import six
import uuid
from typing import List, Optional

from .. import models

class ConnectionsApi(object):

    def __init__(self, api_client):
        self.api_client = api_client

    def api28_connections_delete_with_http_info(
        self,
        authorization=None,  # type: str
        x_request_id=None,  # type: str
        host_group_names=None,  # type: List[str]
        host_names=None,  # type: List[str]
        volume_names=None,  # type: List[str]
        async_req=False,  # type: bool
        _return_http_data_only=False,  # type: bool
        _preload_content=True,  # type: bool
        _request_timeout=None,  # type: Optional[int]
    ):
        # type: (...) -> None
        """Delete a connection between a volume and its host or host group

        Deletes the connection between a volume and its associated host or host group. The `volume_names` and `host_names` or `host_group_names` query parameters are required. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api28_connections_delete_with_http_info(async_req=True)
        >>> result = thread.get()

        :param str authorization: Access token (in JWT format) required to use any API endpoint (except `/oauth2`, `/login`, and `/logout`) 
        :param str x_request_id: Supplied by client during request or generated by server. 
        :param list[str] host_group_names: Performs the operation on the host group specified. Enter multiple names in comma-separated format. A request cannot include a mix of multiple objects with multiple names. For example, a request cannot include a mix of multiple host group names and volume names; instead, at least one of the objects (e.g., `host_group_names`) must be set to only one name (e.g., `hgroup01`). 
        :param list[str] host_names: Performs the operation on the hosts specified. Enter multiple names in comma-separated format. For example, `host01,host02`. A request cannot include a mix of multiple objects with multiple names. For example, a request cannot include a mix of multiple host names and volume names; instead, at least one of the objects (e.g., `host_names`) must be set to only one name (e.g., `host01`). 
        :param list[str] volume_names: Performs the operation on the volume specified. Enter multiple names in comma-separated format. For example, `vol01,vol02`. A request cannot include a mix of multiple objects with multiple names. For example, a request cannot include a mix of multiple volume names and host names; instead, at least one of the objects (e.g., `volume_names`) must be set to only one name (e.g., `vol01`). 
        :param bool async_req: Request runs in separate thread and method returns multiprocessing.pool.ApplyResult.
        :param bool _return_http_data_only: Returns only data field.
        :param bool _preload_content: Response is converted into objects.
        :param int _request_timeout: Total request timeout in seconds.
                 It can also be a tuple of (connection time, read time) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        if host_group_names is not None:
            if not isinstance(host_group_names, list):
                host_group_names = [host_group_names]
        if host_names is not None:
            if not isinstance(host_names, list):
                host_names = [host_names]
        if volume_names is not None:
            if not isinstance(volume_names, list):
                volume_names = [volume_names]
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
        if 'host_group_names' in params:
            query_params.append(('host_group_names', params['host_group_names']))
            collection_formats['host_group_names'] = 'csv'
        if 'host_names' in params:
            query_params.append(('host_names', params['host_names']))
            collection_formats['host_names'] = 'csv'
        if 'volume_names' in params:
            query_params.append(('volume_names', params['volume_names']))
            collection_formats['volume_names'] = 'csv'

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
            '/api/2.8/connections', 'DELETE',
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

    def api28_connections_get_with_http_info(
        self,
        authorization=None,  # type: str
        x_request_id=None,  # type: str
        continuation_token=None,  # type: str
        filter=None,  # type: str
        host_group_names=None,  # type: List[str]
        host_names=None,  # type: List[str]
        limit=None,  # type: int
        offset=None,  # type: int
        protocol_endpoint_names=None,  # type: List[str]
        sort=None,  # type: List[str]
        total_item_count=None,  # type: bool
        volume_names=None,  # type: List[str]
        async_req=False,  # type: bool
        _return_http_data_only=False,  # type: bool
        _preload_content=True,  # type: bool
        _request_timeout=None,  # type: Optional[int]
    ):
        # type: (...) -> models.ConnectionGetResponse
        """List volume connections

        Displays a list of connections between a volume and its hosts and host groups, and the logical unit numbers (LUNs) used by the associated hosts to address these volumes.  
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api28_connections_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param str authorization: Access token (in JWT format) required to use any API endpoint (except `/oauth2`, `/login`, and `/logout`) 
        :param str x_request_id: Supplied by client during request or generated by server. 
        :param str continuation_token: A token used to retrieve the next page of data with some consistency guaranteed. The token is a Base64 encoded value. Set `continuation_token` to the system-generated token taken from the `x-next-token` header field of the response. A query has reached its last page when the response does not include a token. Pagination requires the `limit` and `continuation_token` query parameters. 
        :param str filter: Narrows down the results to only the response objects that satisfy the filter criteria. 
        :param list[str] host_group_names: Performs the operation on the host group specified. Enter multiple names in comma-separated format. A request cannot include a mix of multiple objects with multiple names. For example, a request cannot include a mix of multiple host group names and volume names; instead, at least one of the objects (e.g., `host_group_names`) must be set to only one name (e.g., `hgroup01`). 
        :param list[str] host_names: Performs the operation on the hosts specified. Enter multiple names in comma-separated format. For example, `host01,host02`. A request cannot include a mix of multiple objects with multiple names. For example, a request cannot include a mix of multiple host names and volume names; instead, at least one of the objects (e.g., `host_names`) must be set to only one name (e.g., `host01`). 
        :param int limit: Limits the size of the response to the specified number of objects on each page. To return the total number of resources, set `limit=0`. The total number of resources is returned as a `total_item_count` value. If the page size requested is larger than the system maximum limit, the server returns the maximum limit, disregarding the requested page size. 
        :param int offset: The starting position based on the results of the query in relation to the full set of response objects returned. 
        :param list[str] protocol_endpoint_names: Performs the operation on the protocol endpoints specified. Enter multiple names in comma-separated format. For example, `pe01,pe02`. A request cannot include a mix of multiple objects with multiple names. For example, a request cannot include a mix of multiple protocol endpoint names and host names; instead, at least one of the objects (e.g., `protocol_endpoint_names`) must be set to one name (e.g., `pe01`). 
        :param list[str] sort: Returns the response objects in the order specified. Set `sort` to the name in the response by which to sort. Sorting can be performed on any of the names in the response, and the objects can be sorted in ascending or descending order. By default, the response objects are sorted in ascending order. To sort in descending order, append the minus sign (`-`) to the name. A single request can be sorted on multiple objects. For example, you can sort all volumes from largest to smallest volume size, and then sort volumes of the same size in ascending order by volume name. To sort on multiple names, list the names as comma-separated values. 
        :param bool total_item_count: If set to `true`, the `total_item_count` matching the specified query parameters is calculated and returned in the response. If set to `false`, the `total_item_count` is `null` in the response. This may speed up queries where the `total_item_count` is large. If not specified, defaults to `false`. 
        :param list[str] volume_names: Performs the operation on the volume specified. Enter multiple names in comma-separated format. For example, `vol01,vol02`. A request cannot include a mix of multiple objects with multiple names. For example, a request cannot include a mix of multiple volume names and host names; instead, at least one of the objects (e.g., `volume_names`) must be set to only one name (e.g., `vol01`). 
        :param bool async_req: Request runs in separate thread and method returns multiprocessing.pool.ApplyResult.
        :param bool _return_http_data_only: Returns only data field.
        :param bool _preload_content: Response is converted into objects.
        :param int _request_timeout: Total request timeout in seconds.
                 It can also be a tuple of (connection time, read time) timeouts.
        :return: ConnectionGetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        if host_group_names is not None:
            if not isinstance(host_group_names, list):
                host_group_names = [host_group_names]
        if host_names is not None:
            if not isinstance(host_names, list):
                host_names = [host_names]
        if protocol_endpoint_names is not None:
            if not isinstance(protocol_endpoint_names, list):
                protocol_endpoint_names = [protocol_endpoint_names]
        if sort is not None:
            if not isinstance(sort, list):
                sort = [sort]
        if volume_names is not None:
            if not isinstance(volume_names, list):
                volume_names = [volume_names]
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
            raise ValueError("Invalid value for parameter `limit` when calling `api28_connections_get`, must be a value greater than or equal to `0`")
        if 'offset' in params and params['offset'] < 0:
            raise ValueError("Invalid value for parameter `offset` when calling `api28_connections_get`, must be a value greater than or equal to `0`")
        collection_formats = {}
        path_params = {}

        query_params = []
        if 'continuation_token' in params:
            query_params.append(('continuation_token', params['continuation_token']))
        if 'filter' in params:
            query_params.append(('filter', params['filter']))
        if 'host_group_names' in params:
            query_params.append(('host_group_names', params['host_group_names']))
            collection_formats['host_group_names'] = 'csv'
        if 'host_names' in params:
            query_params.append(('host_names', params['host_names']))
            collection_formats['host_names'] = 'csv'
        if 'limit' in params:
            query_params.append(('limit', params['limit']))
        if 'offset' in params:
            query_params.append(('offset', params['offset']))
        if 'protocol_endpoint_names' in params:
            query_params.append(('protocol_endpoint_names', params['protocol_endpoint_names']))
            collection_formats['protocol_endpoint_names'] = 'csv'
        if 'sort' in params:
            query_params.append(('sort', params['sort']))
            collection_formats['sort'] = 'csv'
        if 'total_item_count' in params:
            query_params.append(('total_item_count', params['total_item_count']))
        if 'volume_names' in params:
            query_params.append(('volume_names', params['volume_names']))
            collection_formats['volume_names'] = 'csv'

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
            '/api/2.8/connections', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ConnectionGetResponse',
            auth_settings=auth_settings,
            async_req=async_req,
            _return_http_data_only=_return_http_data_only,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            collection_formats=collection_formats,
        )

    def api28_connections_post_with_http_info(
        self,
        authorization=None,  # type: str
        x_request_id=None,  # type: str
        host_group_names=None,  # type: List[str]
        host_names=None,  # type: List[str]
        volume_names=None,  # type: List[str]
        connection=None,  # type: models.ConnectionPost
        async_req=False,  # type: bool
        _return_http_data_only=False,  # type: bool
        _preload_content=True,  # type: bool
        _request_timeout=None,  # type: Optional[int]
    ):
        # type: (...) -> models.ConnectionResponse
        """Create a connection between a volume and host or host group

        Creates a connection between a volume and a host or host group. The `volume_names` and `host_names` or `host_group_names` query parameters are required.  
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api28_connections_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param str authorization: Access token (in JWT format) required to use any API endpoint (except `/oauth2`, `/login`, and `/logout`) 
        :param str x_request_id: Supplied by client during request or generated by server. 
        :param list[str] host_group_names: Performs the operation on the host group specified. Enter multiple names in comma-separated format. A request cannot include a mix of multiple objects with multiple names. For example, a request cannot include a mix of multiple host group names and volume names; instead, at least one of the objects (e.g., `host_group_names`) must be set to only one name (e.g., `hgroup01`). 
        :param list[str] host_names: Performs the operation on the hosts specified. Enter multiple names in comma-separated format. For example, `host01,host02`. A request cannot include a mix of multiple objects with multiple names. For example, a request cannot include a mix of multiple host names and volume names; instead, at least one of the objects (e.g., `host_names`) must be set to only one name (e.g., `host01`). 
        :param list[str] volume_names: Performs the operation on the volume specified. Enter multiple names in comma-separated format. For example, `vol01,vol02`. A request cannot include a mix of multiple objects with multiple names. For example, a request cannot include a mix of multiple volume names and host names; instead, at least one of the objects (e.g., `volume_names`) must be set to only one name (e.g., `vol01`). 
        :param ConnectionPost connection:
        :param bool async_req: Request runs in separate thread and method returns multiprocessing.pool.ApplyResult.
        :param bool _return_http_data_only: Returns only data field.
        :param bool _preload_content: Response is converted into objects.
        :param int _request_timeout: Total request timeout in seconds.
                 It can also be a tuple of (connection time, read time) timeouts.
        :return: ConnectionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        if host_group_names is not None:
            if not isinstance(host_group_names, list):
                host_group_names = [host_group_names]
        if host_names is not None:
            if not isinstance(host_names, list):
                host_names = [host_names]
        if volume_names is not None:
            if not isinstance(volume_names, list):
                volume_names = [volume_names]
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
        if 'host_group_names' in params:
            query_params.append(('host_group_names', params['host_group_names']))
            collection_formats['host_group_names'] = 'csv'
        if 'host_names' in params:
            query_params.append(('host_names', params['host_names']))
            collection_formats['host_names'] = 'csv'
        if 'volume_names' in params:
            query_params.append(('volume_names', params['volume_names']))
            collection_formats['volume_names'] = 'csv'

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']
        if 'x_request_id' in params:
            header_params['X-Request-ID'] = params['x_request_id']

        form_params = []
        local_var_files = {}

        body_params = None
        if 'connection' in params:
            body_params = params['connection']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/api/2.8/connections', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ConnectionResponse',
            auth_settings=auth_settings,
            async_req=async_req,
            _return_http_data_only=_return_http_data_only,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            collection_formats=collection_formats,
        )
