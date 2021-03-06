# coding: utf-8
#      Copyright 2020. ThingsBoard
#  #
#      Licensed under the Apache License, Version 2.0 (the "License");
#      you may not use this file except in compliance with the License.
#      You may obtain a copy of the License at
#  #
#          http://www.apache.org/licenses/LICENSE-2.0
#  #
#      Unless required by applicable law or agreed to in writing, software
#      distributed under the License is distributed on an "AS IS" BASIS,
#      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#      See the License for the specific language governing permissions and
#      limitations under the License.
#

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from tb_rest_client.api_client import ApiClient


class AlarmControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.    
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def ack_alarm_using_post(self, alarm_id, **kwargs):  # noqa: E501
        """ackAlarm  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.ack_alarm_using_post(alarm_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str alarm_id: alarmId (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.ack_alarm_using_post_with_http_info(alarm_id, **kwargs)  # noqa: E501
        else:
            (data) = self.ack_alarm_using_post_with_http_info(alarm_id, **kwargs)  # noqa: E501
            return data

    def ack_alarm_using_post_with_http_info(self, alarm_id, **kwargs):  # noqa: E501
        """ackAlarm  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.ack_alarm_using_post_with_http_info(alarm_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str alarm_id: alarmId (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['alarm_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'alarm_id' is set
        if ('alarm_id' not in params or
                params['alarm_id'] is None):
            raise ValueError("Missing the required parameter `alarm_id` when calling `ack_alarm_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'alarm_id' in params:
            path_params['alarmId'] = params['alarm_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/alarm/{alarmId}/ack', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def clear_alarm_using_post(self, alarm_id, **kwargs):  # noqa: E501
        """clearAlarm  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.clear_alarm_using_post(alarm_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str alarm_id: alarmId (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.clear_alarm_using_post_with_http_info(alarm_id, **kwargs)  # noqa: E501
        else:
            (data) = self.clear_alarm_using_post_with_http_info(alarm_id, **kwargs)  # noqa: E501
            return data

    def clear_alarm_using_post_with_http_info(self, alarm_id, **kwargs):  # noqa: E501
        """clearAlarm  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.clear_alarm_using_post_with_http_info(alarm_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str alarm_id: alarmId (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['alarm_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'alarm_id' is set
        if ('alarm_id' not in params or
                params['alarm_id'] is None):
            raise ValueError("Missing the required parameter `alarm_id` when calling `clear_alarm_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'alarm_id' in params:
            path_params['alarmId'] = params['alarm_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/alarm/{alarmId}/clear', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_alarm_using_delete(self, alarm_id, **kwargs):  # noqa: E501
        """deleteAlarm  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.delete_alarm_using_delete(alarm_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str alarm_id: alarmId (required)
        :return: bool
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_alarm_using_delete_with_http_info(alarm_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_alarm_using_delete_with_http_info(alarm_id, **kwargs)  # noqa: E501
            return data

    def delete_alarm_using_delete_with_http_info(self, alarm_id, **kwargs):  # noqa: E501
        """deleteAlarm  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.delete_alarm_using_delete_with_http_info(alarm_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str alarm_id: alarmId (required)
        :return: bool
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['alarm_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'alarm_id' is set
        if ('alarm_id' not in params or
                params['alarm_id'] is None):
            raise ValueError("Missing the required parameter `alarm_id` when calling `delete_alarm_using_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'alarm_id' in params:
            path_params['alarmId'] = params['alarm_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/alarm/{alarmId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='bool',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_alarm_by_id_using_get(self, alarm_id, **kwargs):  # noqa: E501
        """getAlarmById  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.get_alarm_by_id_using_get(alarm_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str alarm_id: alarmId (required)
        :return: Alarm
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_alarm_by_id_using_get_with_http_info(alarm_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_alarm_by_id_using_get_with_http_info(alarm_id, **kwargs)  # noqa: E501
            return data

    def get_alarm_by_id_using_get_with_http_info(self, alarm_id, **kwargs):  # noqa: E501
        """getAlarmById  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.get_alarm_by_id_using_get_with_http_info(alarm_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str alarm_id: alarmId (required)
        :return: Alarm
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['alarm_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'alarm_id' is set
        if ('alarm_id' not in params or
                params['alarm_id'] is None):
            raise ValueError("Missing the required parameter `alarm_id` when calling `get_alarm_by_id_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'alarm_id' in params:
            path_params['alarmId'] = params['alarm_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/alarm/{alarmId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Alarm',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_alarm_info_by_id_using_get(self, alarm_id, **kwargs):  # noqa: E501
        """getAlarmInfoById  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.get_alarm_info_by_id_using_get(alarm_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str alarm_id: alarmId (required)
        :return: AlarmInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_alarm_info_by_id_using_get_with_http_info(alarm_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_alarm_info_by_id_using_get_with_http_info(alarm_id, **kwargs)  # noqa: E501
            return data

    def get_alarm_info_by_id_using_get_with_http_info(self, alarm_id, **kwargs):  # noqa: E501
        """getAlarmInfoById  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.get_alarm_info_by_id_using_get_with_http_info(alarm_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str alarm_id: alarmId (required)
        :return: AlarmInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['alarm_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'alarm_id' is set
        if ('alarm_id' not in params or
                params['alarm_id'] is None):
            raise ValueError("Missing the required parameter `alarm_id` when calling `get_alarm_info_by_id_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'alarm_id' in params:
            path_params['alarmId'] = params['alarm_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/alarm/info/{alarmId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AlarmInfo',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_alarms_using_get(self, entity_type, entity_id, page_size, page, **kwargs):  # noqa: E501
        """getAlarms  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.get_alarms_using_get(entity_type, entity_id, page_size, page, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str entity_type: entityType (required)
        :param str entity_id: entityId (required)
        :param str search_status: searchStatus
        :param str status: status
        :param str page_size: pageSize (required)
        :param str page: page (required)
        :param str text_search: textSearch
        :param str sort_property: sortProperty
        :param str sort_order: sortOrder
        :param int start_time: startTime
        :param int end_time: endTime
        :param bool asc_order: ascOrder
        :param str offset: offset
        :param bool fetch_originator: fetchOriginator
        :return: TimePageDataAlarmInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_alarms_using_get_with_http_info(entity_type, entity_id, page_size, page, **kwargs)  # noqa: E501
        else:
            (data) = self.get_alarms_using_get_with_http_info(entity_type, entity_id, page_size, page, **kwargs)  # noqa: E501
            return data

    def get_alarms_using_get_with_http_info(self, entity_type, entity_id, page_size, page, **kwargs):  # noqa: E501
        """getAlarms  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.get_alarms_using_get_with_http_info(entity_type, entity_id, page_size, page, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str entity_type: entityType (required)
        :param str entity_id: entityId (required)
        :param str search_status: searchStatus
        :param str status: status
        :param str page_size: pageSize (required)
        :param str page: page (required)
        :param str text_search: textSearch
        :param str sort_property: sortProperty
        :param str sort_order: sortOrder
        :param int start_time: startTime
        :param int end_time: endTime
        :param bool asc_order: ascOrder
        :param str offset: offset
        :param bool fetch_originator: fetchOriginator
        :return: TimePageDataAlarmInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['entity_type', 'entity_id', 'search_status', 'status', 'page_size', 'page', 'text_search', 'sort_property', 'sort_order', 'start_time', 'end_time', 'asc_order', 'offset', 'fetch_originator']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'entity_type' is set
        if ('entity_type' not in params or
                params['entity_type'] is None):
            raise ValueError("Missing the required parameter `entity_type` when calling `get_alarms_using_get`")  # noqa: E501
        # verify the required parameter 'entity_id' is set
        if ('entity_id' not in params or
                params['entity_id'] is None):
            raise ValueError("Missing the required parameter `entity_id` when calling `get_alarms_using_get`")  # noqa: E501
        # verify the required parameter 'page_size' is set
        if ('page_size' not in params or
                params['page_size'] is None):
            raise ValueError("Missing the required parameter `page_size` when calling `get_alarms_using_get`")  # noqa: E501
        # verify the required parameter 'page' is set
        if ('page' not in params or
                params['page'] is None):
            raise ValueError("Missing the required parameter `page` when calling `get_alarms_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'entity_type' in params:
            path_params['entityType'] = params['entity_type']  # noqa: E501
        if 'entity_id' in params:
            path_params['entityId'] = params['entity_id']  # noqa: E501

        query_params = []
        if 'search_status' in params:
            query_params.append(('searchStatus', params['search_status']))  # noqa: E501
        if 'status' in params:
            query_params.append(('status', params['status']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'text_search' in params:
            query_params.append(('textSearch', params['text_search']))  # noqa: E501
        if 'sort_property' in params:
            query_params.append(('sortProperty', params['sort_property']))  # noqa: E501
        if 'sort_order' in params:
            query_params.append(('sortOrder', params['sort_order']))  # noqa: E501
        if 'start_time' in params:
            query_params.append(('startTime', params['start_time']))  # noqa: E501
        if 'end_time' in params:
            query_params.append(('endTime', params['end_time']))  # noqa: E501
        if 'asc_order' in params:
            query_params.append(('ascOrder', params['asc_order']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'fetch_originator' in params:
            query_params.append(('fetchOriginator', params['fetch_originator']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/alarm/{entityType}/{entityId}{?searchStatus,status,pageSize,page,textSearch,sortProperty,sortOrder,startTime,endTime,offset,fetchOriginator}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TimePageDataAlarmInfo',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_highest_alarm_severity_using_get(self, entity_type, entity_id, **kwargs):  # noqa: E501
        """getHighestAlarmSeverity  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.get_highest_alarm_severity_using_get(entity_type, entity_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str entity_type: entityType (required)
        :param str entity_id: entityId (required)
        :param str search_status: searchStatus
        :param str status: status
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_highest_alarm_severity_using_get_with_http_info(entity_type, entity_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_highest_alarm_severity_using_get_with_http_info(entity_type, entity_id, **kwargs)  # noqa: E501
            return data

    def get_highest_alarm_severity_using_get_with_http_info(self, entity_type, entity_id, **kwargs):  # noqa: E501
        """getHighestAlarmSeverity  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.get_highest_alarm_severity_using_get_with_http_info(entity_type, entity_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str entity_type: entityType (required)
        :param str entity_id: entityId (required)
        :param str search_status: searchStatus
        :param str status: status
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['entity_type', 'entity_id', 'search_status', 'status']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'entity_type' is set
        if ('entity_type' not in params or
                params['entity_type'] is None):
            raise ValueError("Missing the required parameter `entity_type` when calling `get_highest_alarm_severity_using_get`")  # noqa: E501
        # verify the required parameter 'entity_id' is set
        if ('entity_id' not in params or
                params['entity_id'] is None):
            raise ValueError("Missing the required parameter `entity_id` when calling `get_highest_alarm_severity_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'entity_type' in params:
            path_params['entityType'] = params['entity_type']  # noqa: E501
        if 'entity_id' in params:
            path_params['entityId'] = params['entity_id']  # noqa: E501

        query_params = []
        if 'search_status' in params:
            query_params.append(('searchStatus', params['search_status']))  # noqa: E501
        if 'status' in params:
            query_params.append(('status', params['status']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/alarm/highestSeverity/{entityType}/{entityId}{?searchStatus,status}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def save_alarm_using_post(self, alarm, **kwargs):  # noqa: E501
        """saveAlarm  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.save_alarm_using_post(alarm, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Alarm alarm: alarm (required)
        :return: Alarm
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.save_alarm_using_post_with_http_info(alarm, **kwargs)  # noqa: E501
        else:
            (data) = self.save_alarm_using_post_with_http_info(alarm, **kwargs)  # noqa: E501
            return data

    def save_alarm_using_post_with_http_info(self, alarm, **kwargs):  # noqa: E501
        """saveAlarm  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.save_alarm_using_post_with_http_info(alarm, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Alarm alarm: alarm (required)
        :return: Alarm
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['alarm']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'alarm' is set
        if ('alarm' not in params or
                params['alarm'] is None):
            raise ValueError("Missing the required parameter `alarm` when calling `save_alarm_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'alarm' in params:
            body_params = params['alarm']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/alarm', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Alarm',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
