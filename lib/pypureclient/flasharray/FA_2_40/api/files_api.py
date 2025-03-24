# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.40
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re

# python 2 and python 3 compatibility library
import six
import uuid
from typing import List, Optional

from .. import models

class FilesApi(object):

    def __init__(self, api_client):
        self.api_client = api_client

    def api240_files_post_with_http_info(
        self,
        source_file=None,  # type: models.FilePost
        authorization=None,  # type: str
        x_request_id=None,  # type: str
        directory_ids=None,  # type: List[str]
        directory_names=None,  # type: List[str]
        paths=None,  # type: List[str]
        overwrite=None,  # type: bool
        async_req=False,  # type: bool
        _return_http_data_only=False,  # type: bool
        _preload_content=True,  # type: bool
        _request_timeout=None,  # type: Optional[int]
    ):
        # type: (...) -> None
        """Create a file copy

        Creates a file copy from one path to another path. The `directory_ids`, `directory_names` or `paths` value must be specified. If the `directory_ids` or `directory_names` value is not specified, the file is copied to the source directory specified in the body params. The `paths` value refers to the path of the target file relative to the target directory. If `paths` value is not specified, the file will be copied to the relative path specified in `source_path` under the target directory. The `source_path` value refers to the path of the source file relative to the source directory. To overwrite an existing file, set the `overwrite` flag to `true`. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api240_files_post_with_http_info(source_file, async_req=True)
        >>> result = thread.get()

        :param FilePost source_file: (required)
        :param str authorization: Access token (in JWT format) required to use any API endpoint (except `/oauth2`, `/login`, and `/logout`) 
        :param str x_request_id: Supplied by client during request or generated by server. 
        :param list[str] directory_ids: Performs the operation on the unique managed directory IDs specified. Enter multiple managed directory IDs in comma-separated format. The `directory_ids` or `directory_names` parameter is required, but they cannot be set together. 
        :param list[str] directory_names: Performs the operation on the managed directory names specified. Enter multiple full managed directory names in comma-separated format. For example, `fs:dir01,fs:dir02`. 
        :param list[str] paths: Target file path relative to the target directory. Enter multiple target file path in a comma-separated format. For example, `/dir1/dir2/file1,/dir3/dir4/file2`. 
        :param bool overwrite: If set to `true`, overwrites an existing object during an object copy operation. If set to `false` or not set at all and the target name is an existing object, the copy operation fails. Required if the `source` body parameter is set and the source overwrites an existing object during the copy operation. 
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
        if paths is not None:
            if not isinstance(paths, list):
                paths = [paths]
        params = {k: v for k, v in six.iteritems(locals()) if v is not None}

        # Convert the filter into a string
        if params.get('filter'):
            params['filter'] = str(params['filter'])
        if params.get('sort'):
            params['sort'] = [str(_x) for _x in params['sort']]
        # Assign a value to X-Request-Id if it is not specified
        if params.get('x_request_id') is None:
            params['x_request_id'] = str(uuid.uuid4())
        # verify the required parameter 'source_file' is set
        if source_file is None:
            raise TypeError("Missing the required parameter `source_file` when calling `api240_files_post`")

        collection_formats = {}
        path_params = {}

        query_params = []
        if 'directory_ids' in params:
            query_params.append(('directory_ids', params['directory_ids']))
            collection_formats['directory_ids'] = 'csv'
        if 'directory_names' in params:
            query_params.append(('directory_names', params['directory_names']))
            collection_formats['directory_names'] = 'csv'
        if 'paths' in params:
            query_params.append(('paths', params['paths']))
            collection_formats['paths'] = 'csv'
        if 'overwrite' in params:
            query_params.append(('overwrite', params['overwrite']))

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']
        if 'x_request_id' in params:
            header_params['X-Request-ID'] = params['x_request_id']

        form_params = []
        local_var_files = {}

        body_params = None
        if 'source_file' in params:
            body_params = params['source_file']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/api/2.40/files', 'POST',
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
