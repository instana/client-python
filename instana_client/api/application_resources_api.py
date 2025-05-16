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

from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import List, Optional
from typing_extensions import Annotated
from instana_client.models.application_result import ApplicationResult
from instana_client.models.endpoint_result import EndpointResult
from instana_client.models.service_result import ServiceResult

from instana_client.api_client import ApiClient, RequestSerialized
from instana_client.api_response import ApiResponse
from instana_client.rest import RESTResponseType


class ApplicationResourcesApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def get_application_endpoints(
        self,
        name_filter: Annotated[Optional[StrictStr], Field(description="Name of service")] = None,
        types: Annotated[Optional[List[StrictStr]], Field(description="Type of Endpoint")] = None,
        technologies: Annotated[Optional[List[StrictStr]], Field(description="List of technologies")] = None,
        window_size: Annotated[Optional[StrictInt], Field(description="Size of time window in milliseconds")] = None,
        to: Annotated[Optional[StrictInt], Field(description="Timestamp since Unix Epoch in milliseconds of the end of the time window")] = None,
        page: Annotated[Optional[StrictInt], Field(description="Page number from results")] = None,
        page_size: Annotated[Optional[StrictInt], Field(description="Number of items per page")] = None,
        application_boundary_scope: Annotated[Optional[StrictStr], Field(description="Filter for application scope, i.e: INBOUND or ALL")] = None,
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
    ) -> EndpointResult:
        """Get endpoints

        Use this API endpoint if one wants to retrieve a list of Endpoints. A use case could be to view the endpoint id of an Endpoint. 

        :param name_filter: Name of service
        :type name_filter: str
        :param types: Type of Endpoint
        :type types: List[str]
        :param technologies: List of technologies
        :type technologies: List[str]
        :param window_size: Size of time window in milliseconds
        :type window_size: int
        :param to: Timestamp since Unix Epoch in milliseconds of the end of the time window
        :type to: int
        :param page: Page number from results
        :type page: int
        :param page_size: Number of items per page
        :type page_size: int
        :param application_boundary_scope: Filter for application scope, i.e: INBOUND or ALL
        :type application_boundary_scope: str
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

        _param = self._get_application_endpoints_serialize(
            name_filter=name_filter,
            types=types,
            technologies=technologies,
            window_size=window_size,
            to=to,
            page=page,
            page_size=page_size,
            application_boundary_scope=application_boundary_scope,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "EndpointResult",
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
    def get_application_endpoints_with_http_info(
        self,
        name_filter: Annotated[Optional[StrictStr], Field(description="Name of service")] = None,
        types: Annotated[Optional[List[StrictStr]], Field(description="Type of Endpoint")] = None,
        technologies: Annotated[Optional[List[StrictStr]], Field(description="List of technologies")] = None,
        window_size: Annotated[Optional[StrictInt], Field(description="Size of time window in milliseconds")] = None,
        to: Annotated[Optional[StrictInt], Field(description="Timestamp since Unix Epoch in milliseconds of the end of the time window")] = None,
        page: Annotated[Optional[StrictInt], Field(description="Page number from results")] = None,
        page_size: Annotated[Optional[StrictInt], Field(description="Number of items per page")] = None,
        application_boundary_scope: Annotated[Optional[StrictStr], Field(description="Filter for application scope, i.e: INBOUND or ALL")] = None,
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
    ) -> ApiResponse[EndpointResult]:
        """Get endpoints

        Use this API endpoint if one wants to retrieve a list of Endpoints. A use case could be to view the endpoint id of an Endpoint. 

        :param name_filter: Name of service
        :type name_filter: str
        :param types: Type of Endpoint
        :type types: List[str]
        :param technologies: List of technologies
        :type technologies: List[str]
        :param window_size: Size of time window in milliseconds
        :type window_size: int
        :param to: Timestamp since Unix Epoch in milliseconds of the end of the time window
        :type to: int
        :param page: Page number from results
        :type page: int
        :param page_size: Number of items per page
        :type page_size: int
        :param application_boundary_scope: Filter for application scope, i.e: INBOUND or ALL
        :type application_boundary_scope: str
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

        _param = self._get_application_endpoints_serialize(
            name_filter=name_filter,
            types=types,
            technologies=technologies,
            window_size=window_size,
            to=to,
            page=page,
            page_size=page_size,
            application_boundary_scope=application_boundary_scope,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "EndpointResult",
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
    def get_application_endpoints_without_preload_content(
        self,
        name_filter: Annotated[Optional[StrictStr], Field(description="Name of service")] = None,
        types: Annotated[Optional[List[StrictStr]], Field(description="Type of Endpoint")] = None,
        technologies: Annotated[Optional[List[StrictStr]], Field(description="List of technologies")] = None,
        window_size: Annotated[Optional[StrictInt], Field(description="Size of time window in milliseconds")] = None,
        to: Annotated[Optional[StrictInt], Field(description="Timestamp since Unix Epoch in milliseconds of the end of the time window")] = None,
        page: Annotated[Optional[StrictInt], Field(description="Page number from results")] = None,
        page_size: Annotated[Optional[StrictInt], Field(description="Number of items per page")] = None,
        application_boundary_scope: Annotated[Optional[StrictStr], Field(description="Filter for application scope, i.e: INBOUND or ALL")] = None,
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
        """Get endpoints

        Use this API endpoint if one wants to retrieve a list of Endpoints. A use case could be to view the endpoint id of an Endpoint. 

        :param name_filter: Name of service
        :type name_filter: str
        :param types: Type of Endpoint
        :type types: List[str]
        :param technologies: List of technologies
        :type technologies: List[str]
        :param window_size: Size of time window in milliseconds
        :type window_size: int
        :param to: Timestamp since Unix Epoch in milliseconds of the end of the time window
        :type to: int
        :param page: Page number from results
        :type page: int
        :param page_size: Number of items per page
        :type page_size: int
        :param application_boundary_scope: Filter for application scope, i.e: INBOUND or ALL
        :type application_boundary_scope: str
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

        _param = self._get_application_endpoints_serialize(
            name_filter=name_filter,
            types=types,
            technologies=technologies,
            window_size=window_size,
            to=to,
            page=page,
            page_size=page_size,
            application_boundary_scope=application_boundary_scope,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "EndpointResult",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_application_endpoints_serialize(
        self,
        name_filter,
        types,
        technologies,
        window_size,
        to,
        page,
        page_size,
        application_boundary_scope,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'types': 'multi',
            'technologies': 'multi',
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
        if name_filter is not None:
            
            _query_params.append(('nameFilter', name_filter))
            
        if types is not None:
            
            _query_params.append(('types', types))
            
        if technologies is not None:
            
            _query_params.append(('technologies', technologies))
            
        if window_size is not None:
            
            _query_params.append(('windowSize', window_size))
            
        if to is not None:
            
            _query_params.append(('to', to))
            
        if page is not None:
            
            _query_params.append(('page', page))
            
        if page_size is not None:
            
            _query_params.append(('pageSize', page_size))
            
        if application_boundary_scope is not None:
            
            _query_params.append(('applicationBoundaryScope', application_boundary_scope))
            
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
            resource_path='/api/application-monitoring/applications/services/endpoints',
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
    def get_application_services(
        self,
        name_filter: Annotated[Optional[StrictStr], Field(description="Name of application/service")] = None,
        window_size: Annotated[Optional[StrictInt], Field(description="Size of time window in milliseconds")] = None,
        to: Annotated[Optional[StrictInt], Field(description="Timestamp since Unix Epoch in milliseconds of the end of the time window")] = None,
        page: Annotated[Optional[StrictInt], Field(description="Page number from results")] = None,
        page_size: Annotated[Optional[StrictInt], Field(description="Number of items per page")] = None,
        application_boundary_scope: Annotated[Optional[StrictStr], Field(description="Filter for application scope, i.e: INBOUND or ALL")] = None,
        include_snapshot_ids: Annotated[Optional[StrictBool], Field(description="Include snapshot ids in the results")] = None,
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
    ) -> ServiceResult:
        """Get applications/services

        Use this API endpoint if one wants to retrieve a list of services in an Application Perspective. A use case could be to retrieve all service ids present in an Application Perspective. 

        :param name_filter: Name of application/service
        :type name_filter: str
        :param window_size: Size of time window in milliseconds
        :type window_size: int
        :param to: Timestamp since Unix Epoch in milliseconds of the end of the time window
        :type to: int
        :param page: Page number from results
        :type page: int
        :param page_size: Number of items per page
        :type page_size: int
        :param application_boundary_scope: Filter for application scope, i.e: INBOUND or ALL
        :type application_boundary_scope: str
        :param include_snapshot_ids: Include snapshot ids in the results
        :type include_snapshot_ids: bool
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

        _param = self._get_application_services_serialize(
            name_filter=name_filter,
            window_size=window_size,
            to=to,
            page=page,
            page_size=page_size,
            application_boundary_scope=application_boundary_scope,
            include_snapshot_ids=include_snapshot_ids,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ServiceResult",
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
    def get_application_services_with_http_info(
        self,
        name_filter: Annotated[Optional[StrictStr], Field(description="Name of application/service")] = None,
        window_size: Annotated[Optional[StrictInt], Field(description="Size of time window in milliseconds")] = None,
        to: Annotated[Optional[StrictInt], Field(description="Timestamp since Unix Epoch in milliseconds of the end of the time window")] = None,
        page: Annotated[Optional[StrictInt], Field(description="Page number from results")] = None,
        page_size: Annotated[Optional[StrictInt], Field(description="Number of items per page")] = None,
        application_boundary_scope: Annotated[Optional[StrictStr], Field(description="Filter for application scope, i.e: INBOUND or ALL")] = None,
        include_snapshot_ids: Annotated[Optional[StrictBool], Field(description="Include snapshot ids in the results")] = None,
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
    ) -> ApiResponse[ServiceResult]:
        """Get applications/services

        Use this API endpoint if one wants to retrieve a list of services in an Application Perspective. A use case could be to retrieve all service ids present in an Application Perspective. 

        :param name_filter: Name of application/service
        :type name_filter: str
        :param window_size: Size of time window in milliseconds
        :type window_size: int
        :param to: Timestamp since Unix Epoch in milliseconds of the end of the time window
        :type to: int
        :param page: Page number from results
        :type page: int
        :param page_size: Number of items per page
        :type page_size: int
        :param application_boundary_scope: Filter for application scope, i.e: INBOUND or ALL
        :type application_boundary_scope: str
        :param include_snapshot_ids: Include snapshot ids in the results
        :type include_snapshot_ids: bool
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

        _param = self._get_application_services_serialize(
            name_filter=name_filter,
            window_size=window_size,
            to=to,
            page=page,
            page_size=page_size,
            application_boundary_scope=application_boundary_scope,
            include_snapshot_ids=include_snapshot_ids,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ServiceResult",
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
    def get_application_services_without_preload_content(
        self,
        name_filter: Annotated[Optional[StrictStr], Field(description="Name of application/service")] = None,
        window_size: Annotated[Optional[StrictInt], Field(description="Size of time window in milliseconds")] = None,
        to: Annotated[Optional[StrictInt], Field(description="Timestamp since Unix Epoch in milliseconds of the end of the time window")] = None,
        page: Annotated[Optional[StrictInt], Field(description="Page number from results")] = None,
        page_size: Annotated[Optional[StrictInt], Field(description="Number of items per page")] = None,
        application_boundary_scope: Annotated[Optional[StrictStr], Field(description="Filter for application scope, i.e: INBOUND or ALL")] = None,
        include_snapshot_ids: Annotated[Optional[StrictBool], Field(description="Include snapshot ids in the results")] = None,
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
        """Get applications/services

        Use this API endpoint if one wants to retrieve a list of services in an Application Perspective. A use case could be to retrieve all service ids present in an Application Perspective. 

        :param name_filter: Name of application/service
        :type name_filter: str
        :param window_size: Size of time window in milliseconds
        :type window_size: int
        :param to: Timestamp since Unix Epoch in milliseconds of the end of the time window
        :type to: int
        :param page: Page number from results
        :type page: int
        :param page_size: Number of items per page
        :type page_size: int
        :param application_boundary_scope: Filter for application scope, i.e: INBOUND or ALL
        :type application_boundary_scope: str
        :param include_snapshot_ids: Include snapshot ids in the results
        :type include_snapshot_ids: bool
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

        _param = self._get_application_services_serialize(
            name_filter=name_filter,
            window_size=window_size,
            to=to,
            page=page,
            page_size=page_size,
            application_boundary_scope=application_boundary_scope,
            include_snapshot_ids=include_snapshot_ids,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ServiceResult",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_application_services_serialize(
        self,
        name_filter,
        window_size,
        to,
        page,
        page_size,
        application_boundary_scope,
        include_snapshot_ids,
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
        if name_filter is not None:
            
            _query_params.append(('nameFilter', name_filter))
            
        if window_size is not None:
            
            _query_params.append(('windowSize', window_size))
            
        if to is not None:
            
            _query_params.append(('to', to))
            
        if page is not None:
            
            _query_params.append(('page', page))
            
        if page_size is not None:
            
            _query_params.append(('pageSize', page_size))
            
        if application_boundary_scope is not None:
            
            _query_params.append(('applicationBoundaryScope', application_boundary_scope))
            
        if include_snapshot_ids is not None:
            
            _query_params.append(('includeSnapshotIds', include_snapshot_ids))
            
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
            resource_path='/api/application-monitoring/applications/services',
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
    def get_applications(
        self,
        name_filter: Annotated[Optional[StrictStr], Field(description="Name of application")] = None,
        window_size: Annotated[Optional[StrictInt], Field(description="Size of time window in milliseconds")] = None,
        to: Annotated[Optional[StrictInt], Field(description="Timestamp since Unix Epoch in milliseconds of the end of the time window")] = None,
        page: Annotated[Optional[StrictInt], Field(description="Page number from results")] = None,
        page_size: Annotated[Optional[StrictInt], Field(description="Number of items per page")] = None,
        application_boundary_scope: Annotated[Optional[StrictStr], Field(description="Filter for application scope, i.e: INBOUND or ALL")] = None,
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
    ) -> ApplicationResult:
        """Get applications

        Use this API endpoint if one wants to retrieve a list of Application Perspectives. A use case could be to view the application id of an Application Perspective. 

        :param name_filter: Name of application
        :type name_filter: str
        :param window_size: Size of time window in milliseconds
        :type window_size: int
        :param to: Timestamp since Unix Epoch in milliseconds of the end of the time window
        :type to: int
        :param page: Page number from results
        :type page: int
        :param page_size: Number of items per page
        :type page_size: int
        :param application_boundary_scope: Filter for application scope, i.e: INBOUND or ALL
        :type application_boundary_scope: str
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

        _param = self._get_applications_serialize(
            name_filter=name_filter,
            window_size=window_size,
            to=to,
            page=page,
            page_size=page_size,
            application_boundary_scope=application_boundary_scope,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApplicationResult",
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
    def get_applications_with_http_info(
        self,
        name_filter: Annotated[Optional[StrictStr], Field(description="Name of application")] = None,
        window_size: Annotated[Optional[StrictInt], Field(description="Size of time window in milliseconds")] = None,
        to: Annotated[Optional[StrictInt], Field(description="Timestamp since Unix Epoch in milliseconds of the end of the time window")] = None,
        page: Annotated[Optional[StrictInt], Field(description="Page number from results")] = None,
        page_size: Annotated[Optional[StrictInt], Field(description="Number of items per page")] = None,
        application_boundary_scope: Annotated[Optional[StrictStr], Field(description="Filter for application scope, i.e: INBOUND or ALL")] = None,
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
    ) -> ApiResponse[ApplicationResult]:
        """Get applications

        Use this API endpoint if one wants to retrieve a list of Application Perspectives. A use case could be to view the application id of an Application Perspective. 

        :param name_filter: Name of application
        :type name_filter: str
        :param window_size: Size of time window in milliseconds
        :type window_size: int
        :param to: Timestamp since Unix Epoch in milliseconds of the end of the time window
        :type to: int
        :param page: Page number from results
        :type page: int
        :param page_size: Number of items per page
        :type page_size: int
        :param application_boundary_scope: Filter for application scope, i.e: INBOUND or ALL
        :type application_boundary_scope: str
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

        _param = self._get_applications_serialize(
            name_filter=name_filter,
            window_size=window_size,
            to=to,
            page=page,
            page_size=page_size,
            application_boundary_scope=application_boundary_scope,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApplicationResult",
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
    def get_applications_without_preload_content(
        self,
        name_filter: Annotated[Optional[StrictStr], Field(description="Name of application")] = None,
        window_size: Annotated[Optional[StrictInt], Field(description="Size of time window in milliseconds")] = None,
        to: Annotated[Optional[StrictInt], Field(description="Timestamp since Unix Epoch in milliseconds of the end of the time window")] = None,
        page: Annotated[Optional[StrictInt], Field(description="Page number from results")] = None,
        page_size: Annotated[Optional[StrictInt], Field(description="Number of items per page")] = None,
        application_boundary_scope: Annotated[Optional[StrictStr], Field(description="Filter for application scope, i.e: INBOUND or ALL")] = None,
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
        """Get applications

        Use this API endpoint if one wants to retrieve a list of Application Perspectives. A use case could be to view the application id of an Application Perspective. 

        :param name_filter: Name of application
        :type name_filter: str
        :param window_size: Size of time window in milliseconds
        :type window_size: int
        :param to: Timestamp since Unix Epoch in milliseconds of the end of the time window
        :type to: int
        :param page: Page number from results
        :type page: int
        :param page_size: Number of items per page
        :type page_size: int
        :param application_boundary_scope: Filter for application scope, i.e: INBOUND or ALL
        :type application_boundary_scope: str
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

        _param = self._get_applications_serialize(
            name_filter=name_filter,
            window_size=window_size,
            to=to,
            page=page,
            page_size=page_size,
            application_boundary_scope=application_boundary_scope,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ApplicationResult",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_applications_serialize(
        self,
        name_filter,
        window_size,
        to,
        page,
        page_size,
        application_boundary_scope,
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
        if name_filter is not None:
            
            _query_params.append(('nameFilter', name_filter))
            
        if window_size is not None:
            
            _query_params.append(('windowSize', window_size))
            
        if to is not None:
            
            _query_params.append(('to', to))
            
        if page is not None:
            
            _query_params.append(('page', page))
            
        if page_size is not None:
            
            _query_params.append(('pageSize', page_size))
            
        if application_boundary_scope is not None:
            
            _query_params.append(('applicationBoundaryScope', application_boundary_scope))
            
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
            resource_path='/api/application-monitoring/applications',
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
    def get_services(
        self,
        name_filter: Annotated[Optional[StrictStr], Field(description="Name of service")] = None,
        window_size: Annotated[Optional[StrictInt], Field(description="Size of time window in milliseconds")] = None,
        to: Annotated[Optional[StrictInt], Field(description="Timestamp since Unix Epoch in milliseconds of the end of the time window")] = None,
        page: Annotated[Optional[StrictInt], Field(description="Page number from results")] = None,
        page_size: Annotated[Optional[StrictInt], Field(description="Number of items per page")] = None,
        include_snapshot_ids: Annotated[Optional[StrictBool], Field(description="Include snapshot ids in the results")] = None,
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
    ) -> ServiceResult:
        """Get services

        Use this API endpoint if one wants to retrieve a list of Services. A use case could be to view the service id of a Service. 

        :param name_filter: Name of service
        :type name_filter: str
        :param window_size: Size of time window in milliseconds
        :type window_size: int
        :param to: Timestamp since Unix Epoch in milliseconds of the end of the time window
        :type to: int
        :param page: Page number from results
        :type page: int
        :param page_size: Number of items per page
        :type page_size: int
        :param include_snapshot_ids: Include snapshot ids in the results
        :type include_snapshot_ids: bool
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

        _param = self._get_services_serialize(
            name_filter=name_filter,
            window_size=window_size,
            to=to,
            page=page,
            page_size=page_size,
            include_snapshot_ids=include_snapshot_ids,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ServiceResult",
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
    def get_services_with_http_info(
        self,
        name_filter: Annotated[Optional[StrictStr], Field(description="Name of service")] = None,
        window_size: Annotated[Optional[StrictInt], Field(description="Size of time window in milliseconds")] = None,
        to: Annotated[Optional[StrictInt], Field(description="Timestamp since Unix Epoch in milliseconds of the end of the time window")] = None,
        page: Annotated[Optional[StrictInt], Field(description="Page number from results")] = None,
        page_size: Annotated[Optional[StrictInt], Field(description="Number of items per page")] = None,
        include_snapshot_ids: Annotated[Optional[StrictBool], Field(description="Include snapshot ids in the results")] = None,
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
    ) -> ApiResponse[ServiceResult]:
        """Get services

        Use this API endpoint if one wants to retrieve a list of Services. A use case could be to view the service id of a Service. 

        :param name_filter: Name of service
        :type name_filter: str
        :param window_size: Size of time window in milliseconds
        :type window_size: int
        :param to: Timestamp since Unix Epoch in milliseconds of the end of the time window
        :type to: int
        :param page: Page number from results
        :type page: int
        :param page_size: Number of items per page
        :type page_size: int
        :param include_snapshot_ids: Include snapshot ids in the results
        :type include_snapshot_ids: bool
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

        _param = self._get_services_serialize(
            name_filter=name_filter,
            window_size=window_size,
            to=to,
            page=page,
            page_size=page_size,
            include_snapshot_ids=include_snapshot_ids,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ServiceResult",
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
    def get_services_without_preload_content(
        self,
        name_filter: Annotated[Optional[StrictStr], Field(description="Name of service")] = None,
        window_size: Annotated[Optional[StrictInt], Field(description="Size of time window in milliseconds")] = None,
        to: Annotated[Optional[StrictInt], Field(description="Timestamp since Unix Epoch in milliseconds of the end of the time window")] = None,
        page: Annotated[Optional[StrictInt], Field(description="Page number from results")] = None,
        page_size: Annotated[Optional[StrictInt], Field(description="Number of items per page")] = None,
        include_snapshot_ids: Annotated[Optional[StrictBool], Field(description="Include snapshot ids in the results")] = None,
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
        """Get services

        Use this API endpoint if one wants to retrieve a list of Services. A use case could be to view the service id of a Service. 

        :param name_filter: Name of service
        :type name_filter: str
        :param window_size: Size of time window in milliseconds
        :type window_size: int
        :param to: Timestamp since Unix Epoch in milliseconds of the end of the time window
        :type to: int
        :param page: Page number from results
        :type page: int
        :param page_size: Number of items per page
        :type page_size: int
        :param include_snapshot_ids: Include snapshot ids in the results
        :type include_snapshot_ids: bool
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

        _param = self._get_services_serialize(
            name_filter=name_filter,
            window_size=window_size,
            to=to,
            page=page,
            page_size=page_size,
            include_snapshot_ids=include_snapshot_ids,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ServiceResult",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_services_serialize(
        self,
        name_filter,
        window_size,
        to,
        page,
        page_size,
        include_snapshot_ids,
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
        if name_filter is not None:
            
            _query_params.append(('nameFilter', name_filter))
            
        if window_size is not None:
            
            _query_params.append(('windowSize', window_size))
            
        if to is not None:
            
            _query_params.append(('to', to))
            
        if page is not None:
            
            _query_params.append(('page', page))
            
        if page_size is not None:
            
            _query_params.append(('pageSize', page_size))
            
        if include_snapshot_ids is not None:
            
            _query_params.append(('includeSnapshotIds', include_snapshot_ids))
            
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
            resource_path='/api/application-monitoring/services',
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


