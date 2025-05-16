# coding: utf-8

"""
    Instana REST API documentation

    Searching for answers and best pratices? Check our [IBM Instana Community](https://community.ibm.com/community/user/aiops/communities/community-home?CommunityKey=58f324a3-3104-41be-9510-5b7c413cc48f).  ## Overview The Instana REST API provides programmatic access to the Instana platform. It can be used to retrieve data available through the Instana UI Dashboard -- metrics, events, traces, etc -- and also to automate configuration tasks such as user management.  ### Navigating the API documentation The API endpoints are grouped by product area and functionality. This generally maps to how our UI Dashboard is organized, hopefully making it easier to locate which endpoints you'd use to fetch the data you see visualized in our UI. The [UI sections](https://www.ibm.com/docs/en/instana-observability/current?topic=working-user-interface#navigation-menu) include: - Websites & Mobile Apps - Applications - Infrastructure - Synthetic Monitoring - Events - Automation - Service Levels - Settings - etc  ### Rate Limiting A rate limit is applied to API usage. Up to 5,000 calls per hour can be made. How many remaining calls can be made and when this call limit resets, can inspected via three headers that are part of the responses of the API server.  - **X-RateLimit-Limit:** Shows the maximum number of calls that may be executed per hour. - **X-RateLimit-Remaining:** How many calls may still be executed within the current hour. - **X-RateLimit-Reset:** Time when the remaining calls will be reset to the limit. For compatibility reasons with other rate limited APIs, this date is not the date in milliseconds, but instead in seconds since 1970-01-01T00:00:00+00:00.  ### Further Reading We provide additional documentation for our REST API in our [product documentation](https://www.ibm.com/docs/en/instana-observability/current?topic=apis-web-rest-api). Here you'll also find some common queries for retrieving data and configuring Instana.  ## Getting Started with the REST API  ### API base URL The base URL for an specific instance of Instana can be determined using the tenant and unit information. - `base`: This is the base URL of a tenant unit, e.g. `https://test-example.instana.io`. This is the same URL that is used to access the Instana user interface. - `apiToken`: Requests against the Instana API require valid API tokens. An initial API token can be generated via the Instana user interface. Any additional API tokens can be generated via the API itself.  ### Curl Example Here is an Example to use the REST API with Curl. First lets get all the available metrics with possible aggregations with a GET call.  ```bash curl --request GET \\   --url https://test-instana.instana.io/api/application-monitoring/catalog/metrics \\   --header 'authorization: apiToken xxxxxxxxxxxxxxxx' ```  Next we can get every call grouped by the endpoint name that has an error count greater then zero. As a metric we could get the mean error rate for example.  ```bash curl --request POST \\   --url https://test-instana.instana.io/api/application-monitoring/analyze/call-groups \\   --header 'authorization: apiToken xxxxxxxxxxxxxxxx' \\   --header 'content-type: application/json' \\   --data '{   \"group\":{       \"groupbyTag\":\"endpoint.name\"   },   \"tagFilters\":[    {     \"name\":\"call.error.count\",     \"value\":\"0\",     \"operator\":\"GREATER_THAN\"    }   ],   \"metrics\":[    {     \"metric\":\"errors\",     \"aggregation\":\"MEAN\"    }   ]   }' ```  ### Generating REST API clients  The API is specified using the [OpenAPI v3](https://github.com/OAI/OpenAPI-Specification) (previously known as Swagger) format. You can download the current specification at our [GitHub API documentation](https://instana.github.io/openapi/openapi.yaml).  OpenAPI tries to solve the issue of ever-evolving APIs and clients lagging behind. Please make sure that you always use the latest version of the generator, as a number of improvements are regularly made. To generate a client library for your language, you can use the [OpenAPI client generators](https://github.com/OpenAPITools/openapi-generator).  #### Go For example, to generate a client library for Go to interact with our backend, you can use the following script; mind replacing the values of the `UNIT_NAME` and `TENANT_NAME` environment variables using those for your tenant unit:  ```bash #!/bin/bash  ### This script assumes you have the `java` and `wget` commands on the path  export UNIT_NAME='myunit' # for example: prod export TENANT_NAME='mytenant' # for example: awesomecompany  //Download the generator to your current working directory: wget https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/4.3.1/openapi-generator-cli-4.3.1.jar -O openapi-generator-cli.jar --server-variables \"tenant=${TENANT_NAME},unit=${UNIT_NAME}\"  //generate a client library that you can vendor into your repository java -jar openapi-generator-cli.jar generate -i https://instana.github.io/openapi/openapi.yaml -g go \\     -o pkg/instana/openapi \\     --skip-validate-spec  //(optional) format the Go code according to the Go code standard gofmt -s -w pkg/instana/openapi ```  The generated clients contain comprehensive READMEs, and you can start right away using the client from the example above:  ```go import instana \"./pkg/instana/openapi\"  // readTags will read all available application monitoring tags along with their type and category func readTags() {  configuration := instana.NewConfiguration()  configuration.Host = \"tenant-unit.instana.io\"  configuration.BasePath = \"https://tenant-unit.instana.io\"   client := instana.NewAPIClient(configuration)  auth := context.WithValue(context.Background(), instana.ContextAPIKey, instana.APIKey{   Key:    apiKey,   Prefix: \"apiToken\",  })   tags, _, err := client.ApplicationCatalogApi.GetApplicationTagCatalog(auth)  if err != nil {   fmt.Fatalf(\"Error calling the API, aborting.\")  }   for _, tag := range tags {   fmt.Printf(\"%s (%s): %s\\n\", tag.Category, tag.Type, tag.Name)  } } ```  #### Java Follow the instructions provided in the official documentation from [OpenAPI Tools](https://github.com/OpenAPITools) to download the [openapi-generator-cli.jar](https://github.com/OpenAPITools/openapi-generator?tab=readme-ov-file#13---download-jar).  Depending on your environment, use one of the following java http client implementations which will create a valid client for our OpenAPI specification: ``` //Nativ Java HTTP Client java -jar openapi-generator-cli.jar generate -i https://instana.github.io/openapi/openapi.yaml -g java -o pkg/instana/openapi --skip-validate-spec  -p dateLibrary=java8 --library native  //Spring WebClient java -jar openapi-generator-cli.jar generate -i https://instana.github.io/openapi/openapi.yaml -g java -o pkg/instana/openapi --skip-validate-spec  -p dateLibrary=java8,hideGenerationTimestamp=true --library webclient  //Spring RestTemplate java -jar openapi-generator-cli.jar generate -i https://instana.github.io/openapi/openapi.yaml -g java -o pkg/instana/openapi --skip-validate-spec  -p dateLibrary=java8,hideGenerationTimestamp=true --library resttemplate  ``` 

    The version of the OpenAPI document: 1.291.1002
    Contact: support@instana.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, StrictInt, StrictStr
from typing import List, Optional
from typing_extensions import Annotated
from instana_client.models.action_instance import ActionInstance
from instana_client.models.action_instance_request import ActionInstanceRequest
from instana_client.models.paginated_result import PaginatedResult

from instana_client.api_client import ApiClient, RequestSerialized
from instana_client.api_response import ApiResponse
from instana_client.rest import RESTResponseType


class ActionHistoryApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def add_action_instance(
        self,
        action_instance_request: ActionInstanceRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ActionInstance:
        """Run an automation action.

        Submits the automation action for execution on an agent. The automation action to execute and the agent on which to execute the action must be specified as actionId and hostId. For more details on the request payload see the request sample. This call requires `Execution of automation actions`  permission.

        :param action_instance_request: (required)
        :type action_instance_request: ActionInstanceRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._add_action_instance_serialize(
            action_instance_request=action_instance_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ActionInstance",
            '400': None,
            '403': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def add_action_instance_with_http_info(
        self,
        action_instance_request: ActionInstanceRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ActionInstance]:
        """Run an automation action.

        Submits the automation action for execution on an agent. The automation action to execute and the agent on which to execute the action must be specified as actionId and hostId. For more details on the request payload see the request sample. This call requires `Execution of automation actions`  permission.

        :param action_instance_request: (required)
        :type action_instance_request: ActionInstanceRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._add_action_instance_serialize(
            action_instance_request=action_instance_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ActionInstance",
            '400': None,
            '403': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def add_action_instance_without_preload_content(
        self,
        action_instance_request: ActionInstanceRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Run an automation action.

        Submits the automation action for execution on an agent. The automation action to execute and the agent on which to execute the action must be specified as actionId and hostId. For more details on the request payload see the request sample. This call requires `Execution of automation actions`  permission.

        :param action_instance_request: (required)
        :type action_instance_request: ActionInstanceRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._add_action_instance_serialize(
            action_instance_request=action_instance_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ActionInstance",
            '400': None,
            '403': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _add_action_instance_serialize(
        self,
        action_instance_request,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if action_instance_request is not None:
            _body_params = action_instance_request


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'ApiKeyAuth'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/api/automation/actioninstances',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def delete_action_instance(
        self,
        action_instance_id: Annotated[StrictStr, Field(description="Automation action run result ID to delete.")],
        var_from: Annotated[StrictInt, Field(description="From date filter in milliseconds (13-digit) to look up the action run result ID.")],
        to: Annotated[StrictInt, Field(description="To date filter in milliseconds (13-digit) to look up the action run result ID.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Deletes an automation action run result from the action run history by ID.

        Deletes the automation action run result specified in the request path from the action run history. The automation action run result will be deleted only if the action run result was created within the timeframe specified in the `from` and `to` query parameters. To get the automation action run result ID and the created time, you can run `/api/automation/actioninstances` and `/api/automation/actioninstances/<{actionInstanceId}>` REST calls. This call requires `Deletion of automation action history` permission.

        :param action_instance_id: Automation action run result ID to delete. (required)
        :type action_instance_id: str
        :param var_from: From date filter in milliseconds (13-digit) to look up the action run result ID. (required)
        :type var_from: int
        :param to: To date filter in milliseconds (13-digit) to look up the action run result ID. (required)
        :type to: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._delete_action_instance_serialize(
            action_instance_id=action_instance_id,
            var_from=var_from,
            to=to,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': None,
            '500': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def delete_action_instance_with_http_info(
        self,
        action_instance_id: Annotated[StrictStr, Field(description="Automation action run result ID to delete.")],
        var_from: Annotated[StrictInt, Field(description="From date filter in milliseconds (13-digit) to look up the action run result ID.")],
        to: Annotated[StrictInt, Field(description="To date filter in milliseconds (13-digit) to look up the action run result ID.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Deletes an automation action run result from the action run history by ID.

        Deletes the automation action run result specified in the request path from the action run history. The automation action run result will be deleted only if the action run result was created within the timeframe specified in the `from` and `to` query parameters. To get the automation action run result ID and the created time, you can run `/api/automation/actioninstances` and `/api/automation/actioninstances/<{actionInstanceId}>` REST calls. This call requires `Deletion of automation action history` permission.

        :param action_instance_id: Automation action run result ID to delete. (required)
        :type action_instance_id: str
        :param var_from: From date filter in milliseconds (13-digit) to look up the action run result ID. (required)
        :type var_from: int
        :param to: To date filter in milliseconds (13-digit) to look up the action run result ID. (required)
        :type to: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._delete_action_instance_serialize(
            action_instance_id=action_instance_id,
            var_from=var_from,
            to=to,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': None,
            '500': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def delete_action_instance_without_preload_content(
        self,
        action_instance_id: Annotated[StrictStr, Field(description="Automation action run result ID to delete.")],
        var_from: Annotated[StrictInt, Field(description="From date filter in milliseconds (13-digit) to look up the action run result ID.")],
        to: Annotated[StrictInt, Field(description="To date filter in milliseconds (13-digit) to look up the action run result ID.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Deletes an automation action run result from the action run history by ID.

        Deletes the automation action run result specified in the request path from the action run history. The automation action run result will be deleted only if the action run result was created within the timeframe specified in the `from` and `to` query parameters. To get the automation action run result ID and the created time, you can run `/api/automation/actioninstances` and `/api/automation/actioninstances/<{actionInstanceId}>` REST calls. This call requires `Deletion of automation action history` permission.

        :param action_instance_id: Automation action run result ID to delete. (required)
        :type action_instance_id: str
        :param var_from: From date filter in milliseconds (13-digit) to look up the action run result ID. (required)
        :type var_from: int
        :param to: To date filter in milliseconds (13-digit) to look up the action run result ID. (required)
        :type to: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._delete_action_instance_serialize(
            action_instance_id=action_instance_id,
            var_from=var_from,
            to=to,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': None,
            '500': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _delete_action_instance_serialize(
        self,
        action_instance_id,
        var_from,
        to,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if action_instance_id is not None:
            _path_params['actionInstanceId'] = action_instance_id
        # process the query parameters
        if var_from is not None:
            
            _query_params.append(('from', var_from))
            
        if to is not None:
            
            _query_params.append(('to', to))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'ApiKeyAuth'
        ]

        return self.api_client.param_serialize(
            method='DELETE',
            resource_path='/api/automation/actioninstances/{actionInstanceId}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def delete_action_instances(
        self,
        var_from: Annotated[StrictInt, Field(description="From date filter in milliseconds (13-digit) to look up the action run results to delete")],
        to: Annotated[StrictInt, Field(description="To date filter in milliseconds (13-digit) to look up the action run results to delete")],
        target_snapshot_id: Annotated[Optional[StrictStr], Field(description="Target snapshot ID to look up the action run results to delete")] = None,
        event_id: Annotated[Optional[StrictStr], Field(description="Event ID filter to look up the action run results to delete")] = None,
        event_specification_id: Annotated[Optional[StrictStr], Field(description="Event specification ID filter to look up the action run results to delete")] = None,
        search: Annotated[Optional[StrictStr], Field(description="Text in action run result name, description and event name to filter the action run results to delete")] = None,
        types: Annotated[Optional[List[StrictStr]], Field(description="Action type filter to look up the action run results to delete")] = None,
        action_statuses: Annotated[Optional[List[StrictStr]], Field(description="Action status filter to look up the action run results to delete")] = None,
        action_ids: Annotated[Optional[List[StrictStr]], Field(description="List of action IDs  to filter the action run results to delete")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Delete automation action run results.

        Deletes the automation action run results from the action run history. The results to delete is filtered by the filter values given in the query parameters. The automation action run result will be deleted only if the action run result was created within the timeframe specified in the `from` and `to` query parameters. This call requires `Deletion of automation action history` permission and, `from` and `to` query parameters.

        :param var_from: From date filter in milliseconds (13-digit) to look up the action run results to delete (required)
        :type var_from: int
        :param to: To date filter in milliseconds (13-digit) to look up the action run results to delete (required)
        :type to: int
        :param target_snapshot_id: Target snapshot ID to look up the action run results to delete
        :type target_snapshot_id: str
        :param event_id: Event ID filter to look up the action run results to delete
        :type event_id: str
        :param event_specification_id: Event specification ID filter to look up the action run results to delete
        :type event_specification_id: str
        :param search: Text in action run result name, description and event name to filter the action run results to delete
        :type search: str
        :param types: Action type filter to look up the action run results to delete
        :type types: List[str]
        :param action_statuses: Action status filter to look up the action run results to delete
        :type action_statuses: List[str]
        :param action_ids: List of action IDs  to filter the action run results to delete
        :type action_ids: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._delete_action_instances_serialize(
            var_from=var_from,
            to=to,
            target_snapshot_id=target_snapshot_id,
            event_id=event_id,
            event_specification_id=event_specification_id,
            search=search,
            types=types,
            action_statuses=action_statuses,
            action_ids=action_ids,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': None,
            '500': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def delete_action_instances_with_http_info(
        self,
        var_from: Annotated[StrictInt, Field(description="From date filter in milliseconds (13-digit) to look up the action run results to delete")],
        to: Annotated[StrictInt, Field(description="To date filter in milliseconds (13-digit) to look up the action run results to delete")],
        target_snapshot_id: Annotated[Optional[StrictStr], Field(description="Target snapshot ID to look up the action run results to delete")] = None,
        event_id: Annotated[Optional[StrictStr], Field(description="Event ID filter to look up the action run results to delete")] = None,
        event_specification_id: Annotated[Optional[StrictStr], Field(description="Event specification ID filter to look up the action run results to delete")] = None,
        search: Annotated[Optional[StrictStr], Field(description="Text in action run result name, description and event name to filter the action run results to delete")] = None,
        types: Annotated[Optional[List[StrictStr]], Field(description="Action type filter to look up the action run results to delete")] = None,
        action_statuses: Annotated[Optional[List[StrictStr]], Field(description="Action status filter to look up the action run results to delete")] = None,
        action_ids: Annotated[Optional[List[StrictStr]], Field(description="List of action IDs  to filter the action run results to delete")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Delete automation action run results.

        Deletes the automation action run results from the action run history. The results to delete is filtered by the filter values given in the query parameters. The automation action run result will be deleted only if the action run result was created within the timeframe specified in the `from` and `to` query parameters. This call requires `Deletion of automation action history` permission and, `from` and `to` query parameters.

        :param var_from: From date filter in milliseconds (13-digit) to look up the action run results to delete (required)
        :type var_from: int
        :param to: To date filter in milliseconds (13-digit) to look up the action run results to delete (required)
        :type to: int
        :param target_snapshot_id: Target snapshot ID to look up the action run results to delete
        :type target_snapshot_id: str
        :param event_id: Event ID filter to look up the action run results to delete
        :type event_id: str
        :param event_specification_id: Event specification ID filter to look up the action run results to delete
        :type event_specification_id: str
        :param search: Text in action run result name, description and event name to filter the action run results to delete
        :type search: str
        :param types: Action type filter to look up the action run results to delete
        :type types: List[str]
        :param action_statuses: Action status filter to look up the action run results to delete
        :type action_statuses: List[str]
        :param action_ids: List of action IDs  to filter the action run results to delete
        :type action_ids: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._delete_action_instances_serialize(
            var_from=var_from,
            to=to,
            target_snapshot_id=target_snapshot_id,
            event_id=event_id,
            event_specification_id=event_specification_id,
            search=search,
            types=types,
            action_statuses=action_statuses,
            action_ids=action_ids,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': None,
            '500': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def delete_action_instances_without_preload_content(
        self,
        var_from: Annotated[StrictInt, Field(description="From date filter in milliseconds (13-digit) to look up the action run results to delete")],
        to: Annotated[StrictInt, Field(description="To date filter in milliseconds (13-digit) to look up the action run results to delete")],
        target_snapshot_id: Annotated[Optional[StrictStr], Field(description="Target snapshot ID to look up the action run results to delete")] = None,
        event_id: Annotated[Optional[StrictStr], Field(description="Event ID filter to look up the action run results to delete")] = None,
        event_specification_id: Annotated[Optional[StrictStr], Field(description="Event specification ID filter to look up the action run results to delete")] = None,
        search: Annotated[Optional[StrictStr], Field(description="Text in action run result name, description and event name to filter the action run results to delete")] = None,
        types: Annotated[Optional[List[StrictStr]], Field(description="Action type filter to look up the action run results to delete")] = None,
        action_statuses: Annotated[Optional[List[StrictStr]], Field(description="Action status filter to look up the action run results to delete")] = None,
        action_ids: Annotated[Optional[List[StrictStr]], Field(description="List of action IDs  to filter the action run results to delete")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Delete automation action run results.

        Deletes the automation action run results from the action run history. The results to delete is filtered by the filter values given in the query parameters. The automation action run result will be deleted only if the action run result was created within the timeframe specified in the `from` and `to` query parameters. This call requires `Deletion of automation action history` permission and, `from` and `to` query parameters.

        :param var_from: From date filter in milliseconds (13-digit) to look up the action run results to delete (required)
        :type var_from: int
        :param to: To date filter in milliseconds (13-digit) to look up the action run results to delete (required)
        :type to: int
        :param target_snapshot_id: Target snapshot ID to look up the action run results to delete
        :type target_snapshot_id: str
        :param event_id: Event ID filter to look up the action run results to delete
        :type event_id: str
        :param event_specification_id: Event specification ID filter to look up the action run results to delete
        :type event_specification_id: str
        :param search: Text in action run result name, description and event name to filter the action run results to delete
        :type search: str
        :param types: Action type filter to look up the action run results to delete
        :type types: List[str]
        :param action_statuses: Action status filter to look up the action run results to delete
        :type action_statuses: List[str]
        :param action_ids: List of action IDs  to filter the action run results to delete
        :type action_ids: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._delete_action_instances_serialize(
            var_from=var_from,
            to=to,
            target_snapshot_id=target_snapshot_id,
            event_id=event_id,
            event_specification_id=event_specification_id,
            search=search,
            types=types,
            action_statuses=action_statuses,
            action_ids=action_ids,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': None,
            '403': None,
            '500': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _delete_action_instances_serialize(
        self,
        var_from,
        to,
        target_snapshot_id,
        event_id,
        event_specification_id,
        search,
        types,
        action_statuses,
        action_ids,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'types': 'multi',
            'actionStatuses': 'multi',
            'actionIds': 'multi',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if var_from is not None:
            
            _query_params.append(('from', var_from))
            
        if to is not None:
            
            _query_params.append(('to', to))
            
        if target_snapshot_id is not None:
            
            _query_params.append(('targetSnapshotId', target_snapshot_id))
            
        if event_id is not None:
            
            _query_params.append(('eventId', event_id))
            
        if event_specification_id is not None:
            
            _query_params.append(('eventSpecificationId', event_specification_id))
            
        if search is not None:
            
            _query_params.append(('search', search))
            
        if types is not None:
            
            _query_params.append(('types', types))
            
        if action_statuses is not None:
            
            _query_params.append(('actionStatuses', action_statuses))
            
        if action_ids is not None:
            
            _query_params.append(('actionIds', action_ids))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'ApiKeyAuth'
        ]

        return self.api_client.param_serialize(
            method='DELETE',
            resource_path='/api/automation/actioninstances',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def get_action_instance(
        self,
        action_instance_id: Annotated[StrictStr, Field(description="action run result ID to get action run result details")],
        window_size: Annotated[Optional[StrictInt], Field(description="Window size in milliseconds. This value is used compute the from date `(from = to - windowSize)` to get the action run result details. The default `windowSize` is set to 10 minutes if this value is not provided.")] = None,
        to: Annotated[Optional[StrictInt], Field(description="To date filter in milliseconds (13-digit) to get the action run result details. The default `to` date is set to `System.currentTimeMillis()` if this value is not provided.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ActionInstance:
        """Get the details of an automation action run result by ID from action run history.

        Get the details of automation action run result specified in the request path from action run history. The automation action run result will be fetched only if the action run result was created within the timeframe specified by the `windowSize` and `to` query parameters. The `windowSize` parameter is used to compute the from date (`from = to - windowSize`) of the timeframe. The default value for `windowSize` is 10 minutes and the default value for `to` is current system time. To get the automation action run result ID and the created time, you can run `/api/automation/actioninstances` REST calls. When using personal access tokens, the user must have at least `Viewer` access for Automation.

        :param action_instance_id: action run result ID to get action run result details (required)
        :type action_instance_id: str
        :param window_size: Window size in milliseconds. This value is used compute the from date `(from = to - windowSize)` to get the action run result details. The default `windowSize` is set to 10 minutes if this value is not provided.
        :type window_size: int
        :param to: To date filter in milliseconds (13-digit) to get the action run result details. The default `to` date is set to `System.currentTimeMillis()` if this value is not provided.
        :type to: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_action_instance_serialize(
            action_instance_id=action_instance_id,
            window_size=window_size,
            to=to,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ActionInstance",
            '400': None,
            '403': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def get_action_instance_with_http_info(
        self,
        action_instance_id: Annotated[StrictStr, Field(description="action run result ID to get action run result details")],
        window_size: Annotated[Optional[StrictInt], Field(description="Window size in milliseconds. This value is used compute the from date `(from = to - windowSize)` to get the action run result details. The default `windowSize` is set to 10 minutes if this value is not provided.")] = None,
        to: Annotated[Optional[StrictInt], Field(description="To date filter in milliseconds (13-digit) to get the action run result details. The default `to` date is set to `System.currentTimeMillis()` if this value is not provided.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ActionInstance]:
        """Get the details of an automation action run result by ID from action run history.

        Get the details of automation action run result specified in the request path from action run history. The automation action run result will be fetched only if the action run result was created within the timeframe specified by the `windowSize` and `to` query parameters. The `windowSize` parameter is used to compute the from date (`from = to - windowSize`) of the timeframe. The default value for `windowSize` is 10 minutes and the default value for `to` is current system time. To get the automation action run result ID and the created time, you can run `/api/automation/actioninstances` REST calls. When using personal access tokens, the user must have at least `Viewer` access for Automation.

        :param action_instance_id: action run result ID to get action run result details (required)
        :type action_instance_id: str
        :param window_size: Window size in milliseconds. This value is used compute the from date `(from = to - windowSize)` to get the action run result details. The default `windowSize` is set to 10 minutes if this value is not provided.
        :type window_size: int
        :param to: To date filter in milliseconds (13-digit) to get the action run result details. The default `to` date is set to `System.currentTimeMillis()` if this value is not provided.
        :type to: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_action_instance_serialize(
            action_instance_id=action_instance_id,
            window_size=window_size,
            to=to,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ActionInstance",
            '400': None,
            '403': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def get_action_instance_without_preload_content(
        self,
        action_instance_id: Annotated[StrictStr, Field(description="action run result ID to get action run result details")],
        window_size: Annotated[Optional[StrictInt], Field(description="Window size in milliseconds. This value is used compute the from date `(from = to - windowSize)` to get the action run result details. The default `windowSize` is set to 10 minutes if this value is not provided.")] = None,
        to: Annotated[Optional[StrictInt], Field(description="To date filter in milliseconds (13-digit) to get the action run result details. The default `to` date is set to `System.currentTimeMillis()` if this value is not provided.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get the details of an automation action run result by ID from action run history.

        Get the details of automation action run result specified in the request path from action run history. The automation action run result will be fetched only if the action run result was created within the timeframe specified by the `windowSize` and `to` query parameters. The `windowSize` parameter is used to compute the from date (`from = to - windowSize`) of the timeframe. The default value for `windowSize` is 10 minutes and the default value for `to` is current system time. To get the automation action run result ID and the created time, you can run `/api/automation/actioninstances` REST calls. When using personal access tokens, the user must have at least `Viewer` access for Automation.

        :param action_instance_id: action run result ID to get action run result details (required)
        :type action_instance_id: str
        :param window_size: Window size in milliseconds. This value is used compute the from date `(from = to - windowSize)` to get the action run result details. The default `windowSize` is set to 10 minutes if this value is not provided.
        :type window_size: int
        :param to: To date filter in milliseconds (13-digit) to get the action run result details. The default `to` date is set to `System.currentTimeMillis()` if this value is not provided.
        :type to: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_action_instance_serialize(
            action_instance_id=action_instance_id,
            window_size=window_size,
            to=to,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ActionInstance",
            '400': None,
            '403': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_action_instance_serialize(
        self,
        action_instance_id,
        window_size,
        to,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if action_instance_id is not None:
            _path_params['actionInstanceId'] = action_instance_id
        # process the query parameters
        if window_size is not None:
            
            _query_params.append(('windowSize', window_size))
            
        if to is not None:
            
            _query_params.append(('to', to))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'ApiKeyAuth'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/automation/actioninstances/{actionInstanceId}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def get_action_instances(
        self,
        window_size: Annotated[Optional[StrictInt], Field(description="Window size filter in milliseconds (to compute the from date) to get the action run result details")] = None,
        to: Annotated[Optional[StrictInt], Field(description="To date filter in milliseconds (13-digit) to get the action run result details")] = None,
        page: Annotated[Optional[StrictInt], Field(description="Page to fetch -- used for paging the action run result records")] = None,
        page_size: Annotated[Optional[StrictInt], Field(description="Number of records to return in each page -- used for paging the action run result records")] = None,
        target_snapshot_id: Annotated[Optional[StrictStr], Field(description="Target snapshot ID filter to get the action run result details")] = None,
        event_id: Annotated[Optional[StrictStr], Field(description="Event ID filter to get the action run result details")] = None,
        event_specification_id: Annotated[Optional[StrictStr], Field(description="Event specification ID filter to get the action run result details")] = None,
        search: Annotated[Optional[StrictStr], Field(description="Text in action run result name, description and event name filter to get the action run result details")] = None,
        types: Annotated[Optional[List[StrictStr]], Field(description="Action type filter to get the action run result details")] = None,
        action_statuses: Annotated[Optional[List[StrictStr]], Field(description="Action status filter to get the action run result details")] = None,
        order_by: Annotated[Optional[StrictStr], Field(description="Action run result column to order the result set.")] = None,
        order_direction: Annotated[Optional[StrictStr], Field(description="Sort order direction.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> PaginatedResult:
        """Get the details of automation action run results from action run history.

        Get the details of automation action run results from action run history. The results are filtered by the filters in the query parameters. The automation action run result will be fetched only if the action run results were created within the timeframe specified by the `windowSize` and `to` query parameters. The `windowSize` parameter is used to compute the from date (`from = to - windowSize`) of the timeframe. The default value for `windowSize` is 10 minutes and the default value for `to` is current system time. When using personal access tokens, the user must have at least `Viewer` access for Automation and the automation action run results returned are also filtered based on the access set in `Limited access` permission settings. This API returns paginated result as specified in query parameters `page` and `pageSize`. The response contains list of automation action run results whose contents corresponds to the `page` query parameter and whose size corresponds to the `pageSize` query parameter.

        :param window_size: Window size filter in milliseconds (to compute the from date) to get the action run result details
        :type window_size: int
        :param to: To date filter in milliseconds (13-digit) to get the action run result details
        :type to: int
        :param page: Page to fetch -- used for paging the action run result records
        :type page: int
        :param page_size: Number of records to return in each page -- used for paging the action run result records
        :type page_size: int
        :param target_snapshot_id: Target snapshot ID filter to get the action run result details
        :type target_snapshot_id: str
        :param event_id: Event ID filter to get the action run result details
        :type event_id: str
        :param event_specification_id: Event specification ID filter to get the action run result details
        :type event_specification_id: str
        :param search: Text in action run result name, description and event name filter to get the action run result details
        :type search: str
        :param types: Action type filter to get the action run result details
        :type types: List[str]
        :param action_statuses: Action status filter to get the action run result details
        :type action_statuses: List[str]
        :param order_by: Action run result column to order the result set.
        :type order_by: str
        :param order_direction: Sort order direction.
        :type order_direction: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_action_instances_serialize(
            window_size=window_size,
            to=to,
            page=page,
            page_size=page_size,
            target_snapshot_id=target_snapshot_id,
            event_id=event_id,
            event_specification_id=event_specification_id,
            search=search,
            types=types,
            action_statuses=action_statuses,
            order_by=order_by,
            order_direction=order_direction,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PaginatedResult",
            '403': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def get_action_instances_with_http_info(
        self,
        window_size: Annotated[Optional[StrictInt], Field(description="Window size filter in milliseconds (to compute the from date) to get the action run result details")] = None,
        to: Annotated[Optional[StrictInt], Field(description="To date filter in milliseconds (13-digit) to get the action run result details")] = None,
        page: Annotated[Optional[StrictInt], Field(description="Page to fetch -- used for paging the action run result records")] = None,
        page_size: Annotated[Optional[StrictInt], Field(description="Number of records to return in each page -- used for paging the action run result records")] = None,
        target_snapshot_id: Annotated[Optional[StrictStr], Field(description="Target snapshot ID filter to get the action run result details")] = None,
        event_id: Annotated[Optional[StrictStr], Field(description="Event ID filter to get the action run result details")] = None,
        event_specification_id: Annotated[Optional[StrictStr], Field(description="Event specification ID filter to get the action run result details")] = None,
        search: Annotated[Optional[StrictStr], Field(description="Text in action run result name, description and event name filter to get the action run result details")] = None,
        types: Annotated[Optional[List[StrictStr]], Field(description="Action type filter to get the action run result details")] = None,
        action_statuses: Annotated[Optional[List[StrictStr]], Field(description="Action status filter to get the action run result details")] = None,
        order_by: Annotated[Optional[StrictStr], Field(description="Action run result column to order the result set.")] = None,
        order_direction: Annotated[Optional[StrictStr], Field(description="Sort order direction.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[PaginatedResult]:
        """Get the details of automation action run results from action run history.

        Get the details of automation action run results from action run history. The results are filtered by the filters in the query parameters. The automation action run result will be fetched only if the action run results were created within the timeframe specified by the `windowSize` and `to` query parameters. The `windowSize` parameter is used to compute the from date (`from = to - windowSize`) of the timeframe. The default value for `windowSize` is 10 minutes and the default value for `to` is current system time. When using personal access tokens, the user must have at least `Viewer` access for Automation and the automation action run results returned are also filtered based on the access set in `Limited access` permission settings. This API returns paginated result as specified in query parameters `page` and `pageSize`. The response contains list of automation action run results whose contents corresponds to the `page` query parameter and whose size corresponds to the `pageSize` query parameter.

        :param window_size: Window size filter in milliseconds (to compute the from date) to get the action run result details
        :type window_size: int
        :param to: To date filter in milliseconds (13-digit) to get the action run result details
        :type to: int
        :param page: Page to fetch -- used for paging the action run result records
        :type page: int
        :param page_size: Number of records to return in each page -- used for paging the action run result records
        :type page_size: int
        :param target_snapshot_id: Target snapshot ID filter to get the action run result details
        :type target_snapshot_id: str
        :param event_id: Event ID filter to get the action run result details
        :type event_id: str
        :param event_specification_id: Event specification ID filter to get the action run result details
        :type event_specification_id: str
        :param search: Text in action run result name, description and event name filter to get the action run result details
        :type search: str
        :param types: Action type filter to get the action run result details
        :type types: List[str]
        :param action_statuses: Action status filter to get the action run result details
        :type action_statuses: List[str]
        :param order_by: Action run result column to order the result set.
        :type order_by: str
        :param order_direction: Sort order direction.
        :type order_direction: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_action_instances_serialize(
            window_size=window_size,
            to=to,
            page=page,
            page_size=page_size,
            target_snapshot_id=target_snapshot_id,
            event_id=event_id,
            event_specification_id=event_specification_id,
            search=search,
            types=types,
            action_statuses=action_statuses,
            order_by=order_by,
            order_direction=order_direction,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PaginatedResult",
            '403': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def get_action_instances_without_preload_content(
        self,
        window_size: Annotated[Optional[StrictInt], Field(description="Window size filter in milliseconds (to compute the from date) to get the action run result details")] = None,
        to: Annotated[Optional[StrictInt], Field(description="To date filter in milliseconds (13-digit) to get the action run result details")] = None,
        page: Annotated[Optional[StrictInt], Field(description="Page to fetch -- used for paging the action run result records")] = None,
        page_size: Annotated[Optional[StrictInt], Field(description="Number of records to return in each page -- used for paging the action run result records")] = None,
        target_snapshot_id: Annotated[Optional[StrictStr], Field(description="Target snapshot ID filter to get the action run result details")] = None,
        event_id: Annotated[Optional[StrictStr], Field(description="Event ID filter to get the action run result details")] = None,
        event_specification_id: Annotated[Optional[StrictStr], Field(description="Event specification ID filter to get the action run result details")] = None,
        search: Annotated[Optional[StrictStr], Field(description="Text in action run result name, description and event name filter to get the action run result details")] = None,
        types: Annotated[Optional[List[StrictStr]], Field(description="Action type filter to get the action run result details")] = None,
        action_statuses: Annotated[Optional[List[StrictStr]], Field(description="Action status filter to get the action run result details")] = None,
        order_by: Annotated[Optional[StrictStr], Field(description="Action run result column to order the result set.")] = None,
        order_direction: Annotated[Optional[StrictStr], Field(description="Sort order direction.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get the details of automation action run results from action run history.

        Get the details of automation action run results from action run history. The results are filtered by the filters in the query parameters. The automation action run result will be fetched only if the action run results were created within the timeframe specified by the `windowSize` and `to` query parameters. The `windowSize` parameter is used to compute the from date (`from = to - windowSize`) of the timeframe. The default value for `windowSize` is 10 minutes and the default value for `to` is current system time. When using personal access tokens, the user must have at least `Viewer` access for Automation and the automation action run results returned are also filtered based on the access set in `Limited access` permission settings. This API returns paginated result as specified in query parameters `page` and `pageSize`. The response contains list of automation action run results whose contents corresponds to the `page` query parameter and whose size corresponds to the `pageSize` query parameter.

        :param window_size: Window size filter in milliseconds (to compute the from date) to get the action run result details
        :type window_size: int
        :param to: To date filter in milliseconds (13-digit) to get the action run result details
        :type to: int
        :param page: Page to fetch -- used for paging the action run result records
        :type page: int
        :param page_size: Number of records to return in each page -- used for paging the action run result records
        :type page_size: int
        :param target_snapshot_id: Target snapshot ID filter to get the action run result details
        :type target_snapshot_id: str
        :param event_id: Event ID filter to get the action run result details
        :type event_id: str
        :param event_specification_id: Event specification ID filter to get the action run result details
        :type event_specification_id: str
        :param search: Text in action run result name, description and event name filter to get the action run result details
        :type search: str
        :param types: Action type filter to get the action run result details
        :type types: List[str]
        :param action_statuses: Action status filter to get the action run result details
        :type action_statuses: List[str]
        :param order_by: Action run result column to order the result set.
        :type order_by: str
        :param order_direction: Sort order direction.
        :type order_direction: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_action_instances_serialize(
            window_size=window_size,
            to=to,
            page=page,
            page_size=page_size,
            target_snapshot_id=target_snapshot_id,
            event_id=event_id,
            event_specification_id=event_specification_id,
            search=search,
            types=types,
            action_statuses=action_statuses,
            order_by=order_by,
            order_direction=order_direction,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PaginatedResult",
            '403': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_action_instances_serialize(
        self,
        window_size,
        to,
        page,
        page_size,
        target_snapshot_id,
        event_id,
        event_specification_id,
        search,
        types,
        action_statuses,
        order_by,
        order_direction,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'types': 'multi',
            'actionStatuses': 'multi',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if window_size is not None:
            
            _query_params.append(('windowSize', window_size))
            
        if to is not None:
            
            _query_params.append(('to', to))
            
        if page is not None:
            
            _query_params.append(('page', page))
            
        if page_size is not None:
            
            _query_params.append(('pageSize', page_size))
            
        if target_snapshot_id is not None:
            
            _query_params.append(('targetSnapshotId', target_snapshot_id))
            
        if event_id is not None:
            
            _query_params.append(('eventId', event_id))
            
        if event_specification_id is not None:
            
            _query_params.append(('eventSpecificationId', event_specification_id))
            
        if search is not None:
            
            _query_params.append(('search', search))
            
        if types is not None:
            
            _query_params.append(('types', types))
            
        if action_statuses is not None:
            
            _query_params.append(('actionStatuses', action_statuses))
            
        if order_by is not None:
            
            _query_params.append(('orderBy', order_by))
            
        if order_direction is not None:
            
            _query_params.append(('orderDirection', order_direction))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'ApiKeyAuth'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/automation/actioninstances',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


