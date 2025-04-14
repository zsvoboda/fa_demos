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

class RemotePodsApi(object):

    def __init__(self, api_client):
        self.api_client = api_client

    def api2_x_remote_pods_get_with_http_info(
        self,
        authorization=None,  # type: str
        x_request_id=None,  # type: str
        allow_errors=None,  # type: bool
        context_names=None,  # type: List[str]
        continuation_token=None,  # type: str
        filter=None,  # type: str
        ids=None,  # type: List[str]
        limit=None,  # type: int
        names=None,  # type: List[str]
        offset=None,  # type: int
        on=None,  # type: List[str]
        sort=None,  # type: List[str]
        total_item_count=None,  # type: bool
        async_req=False,  # type: bool
        _return_http_data_only=False,  # type: bool
        _preload_content=True,  # type: bool
        _request_timeout=None,  # type: Optional[int]
    ):
        # type: (...) -> models.RemotePodsResponse
        """List remote pods

        Displays a list of pods that that are on connected arrays or realms but not stretched to this array or realm. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api2_x_remote_pods_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param str authorization: Access token (in JWT format) required to use any API endpoint (except `/oauth2`, `/login`, and `/logout`) 
        :param str x_request_id: Supplied by client during request or generated by server. 
        :param bool allow_errors: If set to `true`, the API will allow the operation to continue even if there are errors. Any errors will be returned in the `errors` field of the response. If set to `false`, the operation will fail if there are any errors. 
        :param list[str] context_names: Performs the operation on the unique contexts specified. If specified, each context name must be the name of an array in the same fleet. If not specified, the context will default to the array that received this request.  Other parameters provided with the request, such as names of volumes or snapshots, are resolved relative to the provided `context`.  Enter multiple names in comma-separated format. For example, `name01,name02`. 
        :param str continuation_token: A token used to retrieve the next page of data with some consistency guaranteed. The token is a Base64 encoded value. Set `continuation_token` to the system-generated token taken from the `x-next-token` header field of the response. A query has reached its last page when the response does not include a token. Pagination requires the `limit` and `continuation_token` query parameters. 
        :param str filter: Narrows down the results to only the response objects that satisfy the filter criteria. 
        :param list[str] ids: Performs the operation on the unique resource IDs specified. Enter multiple resource IDs in comma-separated format. The `ids` or `names` parameter is required, but they cannot be set together. 
        :param int limit: Limits the size of the response to the specified number of objects on each page. To return the total number of resources, set `limit=0`. The total number of resources is returned as a `total_item_count` value. If the page size requested is larger than the system maximum limit, the server returns the maximum limit, disregarding the requested page size. 
        :param list[str] names: Performs the operation on the unique name specified. Enter multiple names in comma-separated format. For example, `name01,name02`. 
        :param int offset: The starting position based on the results of the query in relation to the full set of response objects returned. 
        :param list[str] on: Performs the operation on the target name specified. Enter multiple target names in comma-separated format. For example, `targetName01,targetName02`. 
        :param list[str] sort: Returns the response objects in the order specified. Set `sort` to the name in the response by which to sort. Sorting can be performed on any of the names in the response, and the objects can be sorted in ascending or descending order. By default, the response objects are sorted in ascending order. To sort in descending order, append the minus sign (`-`) to the name. A single request can be sorted on multiple objects. For example, you can sort all volumes from largest to smallest volume size, and then sort volumes of the same size in ascending order by volume name. To sort on multiple names, list the names as comma-separated values. 
        :param bool total_item_count: If set to `true`, the `total_item_count` matching the specified query parameters is calculated and returned in the response. If set to `false`, the `total_item_count` is `null` in the response. This may speed up queries where the `total_item_count` is large. If not specified, defaults to `false`. 
        :param bool async_req: Request runs in separate thread and method returns multiprocessing.pool.ApplyResult.
        :param bool _return_http_data_only: Returns only data field.
        :param bool _preload_content: Response is converted into objects.
        :param int _request_timeout: Total request timeout in seconds.
                 It can also be a tuple of (connection time, read time) timeouts.
        :return: RemotePodsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        if context_names is not None:
            if not isinstance(context_names, list):
                context_names = [context_names]
        if ids is not None:
            if not isinstance(ids, list):
                ids = [ids]
        if names is not None:
            if not isinstance(names, list):
                names = [names]
        if on is not None:
            if not isinstance(on, list):
                on = [on]
        if sort is not None:
            if not isinstance(sort, list):
                sort = [sort]
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
            raise ValueError("Invalid value for parameter `limit` when calling `api2_x_remote_pods_get`, must be a value greater than or equal to `0`")
        if 'offset' in params and params['offset'] < 0:
            raise ValueError("Invalid value for parameter `offset` when calling `api2_x_remote_pods_get`, must be a value greater than or equal to `0`")
        collection_formats = {}
        path_params = {}

        query_params = []
        if 'allow_errors' in params:
            query_params.append(('allow_errors', params['allow_errors']))
        if 'context_names' in params:
            query_params.append(('context_names', params['context_names']))
            collection_formats['context_names'] = 'csv'
        if 'continuation_token' in params:
            query_params.append(('continuation_token', params['continuation_token']))
        if 'filter' in params:
            query_params.append(('filter', params['filter']))
        if 'ids' in params:
            query_params.append(('ids', params['ids']))
            collection_formats['ids'] = 'csv'
        if 'limit' in params:
            query_params.append(('limit', params['limit']))
        if 'names' in params:
            query_params.append(('names', params['names']))
            collection_formats['names'] = 'csv'
        if 'offset' in params:
            query_params.append(('offset', params['offset']))
        if 'on' in params:
            query_params.append(('on', params['on']))
            collection_formats['on'] = 'csv'
        if 'sort' in params:
            query_params.append(('sort', params['sort']))
            collection_formats['sort'] = 'csv'
        if 'total_item_count' in params:
            query_params.append(('total_item_count', params['total_item_count']))

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
            ['application/json', 'application/octet-stream', 'text/plain'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/x-www-form-urlencoded', 'application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/api/2.X/remote-pods', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RemotePodsResponse',
            auth_settings=auth_settings,
            async_req=async_req,
            _return_http_data_only=_return_http_data_only,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            collection_formats=collection_formats,
        )

    def api2_x_remote_pods_tags_get_with_http_info(
        self,
        authorization=None,  # type: str
        x_request_id=None,  # type: str
        allow_errors=None,  # type: bool
        context_names=None,  # type: List[str]
        continuation_token=None,  # type: str
        filter=None,  # type: str
        limit=None,  # type: int
        namespaces=None,  # type: List[str]
        offset=None,  # type: int
        resource_ids=None,  # type: List[str]
        resource_names=None,  # type: List[str]
        sort=None,  # type: List[str]
        total_item_count=None,  # type: bool
        async_req=False,  # type: bool
        _return_http_data_only=False,  # type: bool
        _preload_content=True,  # type: bool
        _request_timeout=None,  # type: Optional[int]
    ):
        # type: (...) -> models.TagGetResponse
        """List tags

        Displays the list of tags.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api2_x_remote_pods_tags_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param str authorization: Access token (in JWT format) required to use any API endpoint (except `/oauth2`, `/login`, and `/logout`) 
        :param str x_request_id: Supplied by client during request or generated by server. 
        :param bool allow_errors: If set to `true`, the API will allow the operation to continue even if there are errors. Any errors will be returned in the `errors` field of the response. If set to `false`, the operation will fail if there are any errors. 
        :param list[str] context_names: Performs the operation on the unique contexts specified. If specified, each context name must be the name of an array in the same fleet. If not specified, the context will default to the array that received this request.  Other parameters provided with the request, such as names of volumes or snapshots, are resolved relative to the provided `context`.  Enter multiple names in comma-separated format. For example, `name01,name02`. 
        :param str continuation_token: A token used to retrieve the next page of data with some consistency guaranteed. The token is a Base64 encoded value. Set `continuation_token` to the system-generated token taken from the `x-next-token` header field of the response. A query has reached its last page when the response does not include a token. Pagination requires the `limit` and `continuation_token` query parameters. 
        :param str filter: Narrows down the results to only the response objects that satisfy the filter criteria. 
        :param int limit: Limits the size of the response to the specified number of objects on each page. To return the total number of resources, set `limit=0`. The total number of resources is returned as a `total_item_count` value. If the page size requested is larger than the system maximum limit, the server returns the maximum limit, disregarding the requested page size. 
        :param list[str] namespaces: A comma-separated list of namespaces. 
        :param int offset: The starting position based on the results of the query in relation to the full set of response objects returned. 
        :param list[str] resource_ids: A comma-separated list of resource IDs. The `resource_ids` or `resource_names` parameter is required, but they cannot be set together. 
        :param list[str] resource_names: A comma-separated list of resource names. The `resource_ids` or `resource_names` parameter is required, but they cannot be set together. 
        :param list[str] sort: Returns the response objects in the order specified. Set `sort` to the name in the response by which to sort. Sorting can be performed on any of the names in the response, and the objects can be sorted in ascending or descending order. By default, the response objects are sorted in ascending order. To sort in descending order, append the minus sign (`-`) to the name. A single request can be sorted on multiple objects. For example, you can sort all volumes from largest to smallest volume size, and then sort volumes of the same size in ascending order by volume name. To sort on multiple names, list the names as comma-separated values. 
        :param bool total_item_count: If set to `true`, the `total_item_count` matching the specified query parameters is calculated and returned in the response. If set to `false`, the `total_item_count` is `null` in the response. This may speed up queries where the `total_item_count` is large. If not specified, defaults to `false`. 
        :param bool async_req: Request runs in separate thread and method returns multiprocessing.pool.ApplyResult.
        :param bool _return_http_data_only: Returns only data field.
        :param bool _preload_content: Response is converted into objects.
        :param int _request_timeout: Total request timeout in seconds.
                 It can also be a tuple of (connection time, read time) timeouts.
        :return: TagGetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        if context_names is not None:
            if not isinstance(context_names, list):
                context_names = [context_names]
        if namespaces is not None:
            if not isinstance(namespaces, list):
                namespaces = [namespaces]
        if resource_ids is not None:
            if not isinstance(resource_ids, list):
                resource_ids = [resource_ids]
        if resource_names is not None:
            if not isinstance(resource_names, list):
                resource_names = [resource_names]
        if sort is not None:
            if not isinstance(sort, list):
                sort = [sort]
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
            raise ValueError("Invalid value for parameter `limit` when calling `api2_x_remote_pods_tags_get`, must be a value greater than or equal to `0`")
        if 'offset' in params and params['offset'] < 0:
            raise ValueError("Invalid value for parameter `offset` when calling `api2_x_remote_pods_tags_get`, must be a value greater than or equal to `0`")
        collection_formats = {}
        path_params = {}

        query_params = []
        if 'allow_errors' in params:
            query_params.append(('allow_errors', params['allow_errors']))
        if 'context_names' in params:
            query_params.append(('context_names', params['context_names']))
            collection_formats['context_names'] = 'csv'
        if 'continuation_token' in params:
            query_params.append(('continuation_token', params['continuation_token']))
        if 'filter' in params:
            query_params.append(('filter', params['filter']))
        if 'limit' in params:
            query_params.append(('limit', params['limit']))
        if 'namespaces' in params:
            query_params.append(('namespaces', params['namespaces']))
            collection_formats['namespaces'] = 'csv'
        if 'offset' in params:
            query_params.append(('offset', params['offset']))
        if 'resource_ids' in params:
            query_params.append(('resource_ids', params['resource_ids']))
            collection_formats['resource_ids'] = 'csv'
        if 'resource_names' in params:
            query_params.append(('resource_names', params['resource_names']))
            collection_formats['resource_names'] = 'csv'
        if 'sort' in params:
            query_params.append(('sort', params['sort']))
            collection_formats['sort'] = 'csv'
        if 'total_item_count' in params:
            query_params.append(('total_item_count', params['total_item_count']))

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
            ['application/json', 'application/octet-stream', 'text/plain'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/x-www-form-urlencoded', 'application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/api/2.X/remote-pods/tags', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TagGetResponse',
            auth_settings=auth_settings,
            async_req=async_req,
            _return_http_data_only=_return_http_data_only,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            collection_formats=collection_formats,
        )
