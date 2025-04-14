# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.32
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re

# python 2 and python 3 compatibility library
import six
import uuid
from typing import List, Optional

from .. import models

class DirectoryExportsApi(object):

    def __init__(self, api_client):
        self.api_client = api_client

    def api232_directory_exports_delete_with_http_info(
        self,
        authorization=None,  # type: str
        x_request_id=None,  # type: str
        directory_ids=None,  # type: List[str]
        directory_names=None,  # type: List[str]
        export_names=None,  # type: List[str]
        policy_ids=None,  # type: List[str]
        policy_names=None,  # type: List[str]
        async_req=False,  # type: bool
        _return_http_data_only=False,  # type: bool
        _preload_content=True,  # type: bool
        _request_timeout=None,  # type: Optional[int]
    ):
        # type: (...) -> None
        """Delete directory exports

        Deletes one or more directory exports. If any of the `export_names` is not unique across the system, `policy_ids` or `policy_names` must be specified to determine the exports.  
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api232_directory_exports_delete_with_http_info(async_req=True)
        >>> result = thread.get()

        :param str authorization: Access token (in JWT format) required to use any API endpoint (except `/oauth2`, `/login`, and `/logout`) 
        :param str x_request_id: Supplied by client during request or generated by server. 
        :param list[str] directory_ids: Performs the operation on the unique managed directory IDs specified. Enter multiple managed directory IDs in comma-separated format. The `directory_ids` or `directory_names` parameter is required, but they cannot be set together. 
        :param list[str] directory_names: Performs the operation on the managed directory names specified. Enter multiple full managed directory names in comma-separated format. For example, `fs:dir01,fs:dir02`. 
        :param list[str] export_names: Performs the operation on the export names specified. Enter multiple names in comma-separated format. For example, `name01,name02`. 
        :param list[str] policy_ids: Performs the operation on the unique policy IDs specified. Enter multiple policy IDs in comma-separated format. The `policy_ids` or `policy_names` parameter is required, but they cannot be set together. 
        :param list[str] policy_names: Performs the operation on the policy names specified. Enter multiple policy names in comma-separated format. For example, `name01,name02`. 
        :param bool async_req: Request runs in separate thread and method returns multiprocessing.pool.ApplyResult.
        :param bool _return_http_data_only: Returns only data field.
        :param bool _preload_content: Response is converted into objects.
        :param int _request_timeout: Total request timeout in seconds.
                 It can also be a tuple of (connection time, read time) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        if directory_ids is not None:
            if not isinstance(directory_ids, list):
                directory_ids = [directory_ids]
        if directory_names is not None:
            if not isinstance(directory_names, list):
                directory_names = [directory_names]
        if export_names is not None:
            if not isinstance(export_names, list):
                export_names = [export_names]
        if policy_ids is not None:
            if not isinstance(policy_ids, list):
                policy_ids = [policy_ids]
        if policy_names is not None:
            if not isinstance(policy_names, list):
                policy_names = [policy_names]
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
        if 'directory_ids' in params:
            query_params.append(('directory_ids', params['directory_ids']))
            collection_formats['directory_ids'] = 'csv'
        if 'directory_names' in params:
            query_params.append(('directory_names', params['directory_names']))
            collection_formats['directory_names'] = 'csv'
        if 'export_names' in params:
            query_params.append(('export_names', params['export_names']))
            collection_formats['export_names'] = 'csv'
        if 'policy_ids' in params:
            query_params.append(('policy_ids', params['policy_ids']))
            collection_formats['policy_ids'] = 'csv'
        if 'policy_names' in params:
            query_params.append(('policy_names', params['policy_names']))
            collection_formats['policy_names'] = 'csv'

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
            '/api/2.32/directory-exports', 'DELETE',
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

    def api232_directory_exports_get_with_http_info(
        self,
        authorization=None,  # type: str
        x_request_id=None,  # type: str
        continuation_token=None,  # type: str
        destroyed=None,  # type: bool
        directory_ids=None,  # type: List[str]
        directory_names=None,  # type: List[str]
        export_names=None,  # type: List[str]
        filter=None,  # type: str
        limit=None,  # type: int
        offset=None,  # type: int
        policy_ids=None,  # type: List[str]
        policy_names=None,  # type: List[str]
        sort=None,  # type: List[str]
        total_item_count=None,  # type: bool
        async_req=False,  # type: bool
        _return_http_data_only=False,  # type: bool
        _preload_content=True,  # type: bool
        _request_timeout=None,  # type: Optional[int]
    ):
        # type: (...) -> models.DirectoryExportGetResponse
        """List directory exports

        Displays a list of directory exports.  
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api232_directory_exports_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param str authorization: Access token (in JWT format) required to use any API endpoint (except `/oauth2`, `/login`, and `/logout`) 
        :param str x_request_id: Supplied by client during request or generated by server. 
        :param str continuation_token: A token used to retrieve the next page of data with some consistency guaranteed. The token is a Base64 encoded value. Set `continuation_token` to the system-generated token taken from the `x-next-token` header field of the response. A query has reached its last page when the response does not include a token. Pagination requires the `limit` and `continuation_token` query parameters. 
        :param bool destroyed: If set to `true`, lists only destroyed objects that are in the eradication pending state. If set to `false`, lists only objects that are not destroyed. For destroyed objects, the time remaining is displayed in milliseconds. 
        :param list[str] directory_ids: Performs the operation on the unique managed directory IDs specified. Enter multiple managed directory IDs in comma-separated format. The `directory_ids` or `directory_names` parameter is required, but they cannot be set together. 
        :param list[str] directory_names: Performs the operation on the managed directory names specified. Enter multiple full managed directory names in comma-separated format. For example, `fs:dir01,fs:dir02`. 
        :param list[str] export_names: Performs the operation on the export names specified. Enter multiple names in comma-separated format. For example, `name01,name02`. 
        :param str filter: Narrows down the results to only the response objects that satisfy the filter criteria. 
        :param int limit: Limits the size of the response to the specified number of objects on each page. To return the total number of resources, set `limit=0`. The total number of resources is returned as a `total_item_count` value. If the page size requested is larger than the system maximum limit, the server returns the maximum limit, disregarding the requested page size. 
        :param int offset: The starting position based on the results of the query in relation to the full set of response objects returned. 
        :param list[str] policy_ids: Performs the operation on the unique policy IDs specified. Enter multiple policy IDs in comma-separated format. The `policy_ids` or `policy_names` parameter is required, but they cannot be set together. 
        :param list[str] policy_names: Performs the operation on the policy names specified. Enter multiple policy names in comma-separated format. For example, `name01,name02`. 
        :param list[str] sort: Returns the response objects in the order specified. Set `sort` to the name in the response by which to sort. Sorting can be performed on any of the names in the response, and the objects can be sorted in ascending or descending order. By default, the response objects are sorted in ascending order. To sort in descending order, append the minus sign (`-`) to the name. A single request can be sorted on multiple objects. For example, you can sort all volumes from largest to smallest volume size, and then sort volumes of the same size in ascending order by volume name. To sort on multiple names, list the names as comma-separated values. 
        :param bool total_item_count: If set to `true`, the `total_item_count` matching the specified query parameters is calculated and returned in the response. If set to `false`, the `total_item_count` is `null` in the response. This may speed up queries where the `total_item_count` is large. If not specified, defaults to `false`. 
        :param bool async_req: Request runs in separate thread and method returns multiprocessing.pool.ApplyResult.
        :param bool _return_http_data_only: Returns only data field.
        :param bool _preload_content: Response is converted into objects.
        :param int _request_timeout: Total request timeout in seconds.
                 It can also be a tuple of (connection time, read time) timeouts.
        :return: DirectoryExportGetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        if directory_ids is not None:
            if not isinstance(directory_ids, list):
                directory_ids = [directory_ids]
        if directory_names is not None:
            if not isinstance(directory_names, list):
                directory_names = [directory_names]
        if export_names is not None:
            if not isinstance(export_names, list):
                export_names = [export_names]
        if policy_ids is not None:
            if not isinstance(policy_ids, list):
                policy_ids = [policy_ids]
        if policy_names is not None:
            if not isinstance(policy_names, list):
                policy_names = [policy_names]
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
            raise ValueError("Invalid value for parameter `limit` when calling `api232_directory_exports_get`, must be a value greater than or equal to `0`")
        if 'offset' in params and params['offset'] < 0:
            raise ValueError("Invalid value for parameter `offset` when calling `api232_directory_exports_get`, must be a value greater than or equal to `0`")
        collection_formats = {}
        path_params = {}

        query_params = []
        if 'continuation_token' in params:
            query_params.append(('continuation_token', params['continuation_token']))
        if 'destroyed' in params:
            query_params.append(('destroyed', params['destroyed']))
        if 'directory_ids' in params:
            query_params.append(('directory_ids', params['directory_ids']))
            collection_formats['directory_ids'] = 'csv'
        if 'directory_names' in params:
            query_params.append(('directory_names', params['directory_names']))
            collection_formats['directory_names'] = 'csv'
        if 'export_names' in params:
            query_params.append(('export_names', params['export_names']))
            collection_formats['export_names'] = 'csv'
        if 'filter' in params:
            query_params.append(('filter', params['filter']))
        if 'limit' in params:
            query_params.append(('limit', params['limit']))
        if 'offset' in params:
            query_params.append(('offset', params['offset']))
        if 'policy_ids' in params:
            query_params.append(('policy_ids', params['policy_ids']))
            collection_formats['policy_ids'] = 'csv'
        if 'policy_names' in params:
            query_params.append(('policy_names', params['policy_names']))
            collection_formats['policy_names'] = 'csv'
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
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/api/2.32/directory-exports', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DirectoryExportGetResponse',
            auth_settings=auth_settings,
            async_req=async_req,
            _return_http_data_only=_return_http_data_only,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            collection_formats=collection_formats,
        )

    def api232_directory_exports_patch_with_http_info(
        self,
        export=None,  # type: models.DirectoryExportPatch
        authorization=None,  # type: str
        x_request_id=None,  # type: str
        directory_ids=None,  # type: List[str]
        directory_names=None,  # type: List[str]
        export_names=None,  # type: List[str]
        policy_ids=None,  # type: List[str]
        policy_names=None,  # type: List[str]
        async_req=False,  # type: bool
        _return_http_data_only=False,  # type: bool
        _preload_content=True,  # type: bool
        _request_timeout=None,  # type: Optional[int]
    ):
        # type: (...) -> models.DirectoryExportResponse
        """Modify directory exports

        Modifies a directory export. Used for manually renaming, enabling, and disabling directory exports. To rename a directory export, set 'export_name' to the new name.  
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api232_directory_exports_patch_with_http_info(export, async_req=True)
        >>> result = thread.get()

        :param DirectoryExportPatch export: (required)
        :param str authorization: Access token (in JWT format) required to use any API endpoint (except `/oauth2`, `/login`, and `/logout`) 
        :param str x_request_id: Supplied by client during request or generated by server. 
        :param list[str] directory_ids: Performs the operation on the unique managed directory IDs specified. Enter multiple managed directory IDs in comma-separated format. The `directory_ids` or `directory_names` parameter is required, but they cannot be set together. 
        :param list[str] directory_names: Performs the operation on the managed directory names specified. Enter multiple full managed directory names in comma-separated format. For example, `fs:dir01,fs:dir02`. 
        :param list[str] export_names: Performs the operation on the export names specified. Enter multiple names in comma-separated format. For example, `name01,name02`. 
        :param list[str] policy_ids: Performs the operation on the unique policy IDs specified. Enter multiple policy IDs in comma-separated format. The `policy_ids` or `policy_names` parameter is required, but they cannot be set together. 
        :param list[str] policy_names: Performs the operation on the policy names specified. Enter multiple policy names in comma-separated format. For example, `name01,name02`. 
        :param bool async_req: Request runs in separate thread and method returns multiprocessing.pool.ApplyResult.
        :param bool _return_http_data_only: Returns only data field.
        :param bool _preload_content: Response is converted into objects.
        :param int _request_timeout: Total request timeout in seconds.
                 It can also be a tuple of (connection time, read time) timeouts.
        :return: DirectoryExportResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        if directory_ids is not None:
            if not isinstance(directory_ids, list):
                directory_ids = [directory_ids]
        if directory_names is not None:
            if not isinstance(directory_names, list):
                directory_names = [directory_names]
        if export_names is not None:
            if not isinstance(export_names, list):
                export_names = [export_names]
        if policy_ids is not None:
            if not isinstance(policy_ids, list):
                policy_ids = [policy_ids]
        if policy_names is not None:
            if not isinstance(policy_names, list):
                policy_names = [policy_names]
        params = {k: v for k, v in six.iteritems(locals()) if v is not None}

        # Convert the filter into a string
        if params.get('filter'):
            params['filter'] = str(params['filter'])
        if params.get('sort'):
            params['sort'] = [str(_x) for _x in params['sort']]
        # Assign a value to X-Request-Id if it is not specified
        if params.get('x_request_id') is None:
            params['x_request_id'] = str(uuid.uuid4())
        # verify the required parameter 'export' is set
        if export is None:
            raise TypeError("Missing the required parameter `export` when calling `api232_directory_exports_patch`")

        collection_formats = {}
        path_params = {}

        query_params = []
        if 'directory_ids' in params:
            query_params.append(('directory_ids', params['directory_ids']))
            collection_formats['directory_ids'] = 'csv'
        if 'directory_names' in params:
            query_params.append(('directory_names', params['directory_names']))
            collection_formats['directory_names'] = 'csv'
        if 'export_names' in params:
            query_params.append(('export_names', params['export_names']))
            collection_formats['export_names'] = 'csv'
        if 'policy_ids' in params:
            query_params.append(('policy_ids', params['policy_ids']))
            collection_formats['policy_ids'] = 'csv'
        if 'policy_names' in params:
            query_params.append(('policy_names', params['policy_names']))
            collection_formats['policy_names'] = 'csv'

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']
        if 'x_request_id' in params:
            header_params['X-Request-ID'] = params['x_request_id']

        form_params = []
        local_var_files = {}

        body_params = None
        if 'export' in params:
            body_params = params['export']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/api/2.32/directory-exports', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DirectoryExportResponse',
            auth_settings=auth_settings,
            async_req=async_req,
            _return_http_data_only=_return_http_data_only,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            collection_formats=collection_formats,
        )

    def api232_directory_exports_post_with_http_info(
        self,
        exports=None,  # type: models.DirectoryExportPost
        authorization=None,  # type: str
        x_request_id=None,  # type: str
        directory_ids=None,  # type: List[str]
        directory_names=None,  # type: List[str]
        policy_ids=None,  # type: List[str]
        policy_names=None,  # type: List[str]
        async_req=False,  # type: bool
        _return_http_data_only=False,  # type: bool
        _preload_content=True,  # type: bool
        _request_timeout=None,  # type: Optional[int]
    ):
        # type: (...) -> models.DirectoryExportResponse
        """Create directory exports

        Creates an export of a managed directory. The `directory_ids` or `directory_names` parameter is required, but cannot be set together. The `policy_ids` or `policy_names` parameter is required, but cannot be set together.  
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api232_directory_exports_post_with_http_info(exports, async_req=True)
        >>> result = thread.get()

        :param DirectoryExportPost exports: (required)
        :param str authorization: Access token (in JWT format) required to use any API endpoint (except `/oauth2`, `/login`, and `/logout`) 
        :param str x_request_id: Supplied by client during request or generated by server. 
        :param list[str] directory_ids: Performs the operation on the unique managed directory IDs specified. Enter multiple managed directory IDs in comma-separated format. The `directory_ids` or `directory_names` parameter is required, but they cannot be set together. 
        :param list[str] directory_names: Performs the operation on the managed directory names specified. Enter multiple full managed directory names in comma-separated format. For example, `fs:dir01,fs:dir02`. 
        :param list[str] policy_ids: Performs the operation on the unique policy IDs specified. Enter multiple policy IDs in comma-separated format. The `policy_ids` or `policy_names` parameter is required, but they cannot be set together. 
        :param list[str] policy_names: Performs the operation on the policy names specified. Enter multiple policy names in comma-separated format. For example, `name01,name02`. 
        :param bool async_req: Request runs in separate thread and method returns multiprocessing.pool.ApplyResult.
        :param bool _return_http_data_only: Returns only data field.
        :param bool _preload_content: Response is converted into objects.
        :param int _request_timeout: Total request timeout in seconds.
                 It can also be a tuple of (connection time, read time) timeouts.
        :return: DirectoryExportResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        if directory_ids is not None:
            if not isinstance(directory_ids, list):
                directory_ids = [directory_ids]
        if directory_names is not None:
            if not isinstance(directory_names, list):
                directory_names = [directory_names]
        if policy_ids is not None:
            if not isinstance(policy_ids, list):
                policy_ids = [policy_ids]
        if policy_names is not None:
            if not isinstance(policy_names, list):
                policy_names = [policy_names]
        params = {k: v for k, v in six.iteritems(locals()) if v is not None}

        # Convert the filter into a string
        if params.get('filter'):
            params['filter'] = str(params['filter'])
        if params.get('sort'):
            params['sort'] = [str(_x) for _x in params['sort']]
        # Assign a value to X-Request-Id if it is not specified
        if params.get('x_request_id') is None:
            params['x_request_id'] = str(uuid.uuid4())
        # verify the required parameter 'exports' is set
        if exports is None:
            raise TypeError("Missing the required parameter `exports` when calling `api232_directory_exports_post`")

        collection_formats = {}
        path_params = {}

        query_params = []
        if 'directory_ids' in params:
            query_params.append(('directory_ids', params['directory_ids']))
            collection_formats['directory_ids'] = 'csv'
        if 'directory_names' in params:
            query_params.append(('directory_names', params['directory_names']))
            collection_formats['directory_names'] = 'csv'
        if 'policy_ids' in params:
            query_params.append(('policy_ids', params['policy_ids']))
            collection_formats['policy_ids'] = 'csv'
        if 'policy_names' in params:
            query_params.append(('policy_names', params['policy_names']))
            collection_formats['policy_names'] = 'csv'

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']
        if 'x_request_id' in params:
            header_params['X-Request-ID'] = params['x_request_id']

        form_params = []
        local_var_files = {}

        body_params = None
        if 'exports' in params:
            body_params = params['exports']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/api/2.32/directory-exports', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DirectoryExportResponse',
            auth_settings=auth_settings,
            async_req=async_req,
            _return_http_data_only=_return_http_data_only,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            collection_formats=collection_formats,
        )
