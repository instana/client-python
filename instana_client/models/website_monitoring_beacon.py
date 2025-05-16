# coding: utf-8

"""
    Instana REST API documentation

    Searching for answers and best pratices? Check our [IBM Instana Community](https://community.ibm.com/community/user/aiops/communities/community-home?CommunityKey=58f324a3-3104-41be-9510-5b7c413cc48f).  ## Overview The Instana REST API provides programmatic access to the Instana platform. It can be used to retrieve data available through the Instana UI Dashboard -- metrics, events, traces, etc -- and also to automate configuration tasks such as user management.  ### Navigating the API documentation The API endpoints are grouped by product area and functionality. This generally maps to how our UI Dashboard is organized, hopefully making it easier to locate which endpoints you'd use to fetch the data you see visualized in our UI. The [UI sections](https://www.ibm.com/docs/en/instana-observability/current?topic=working-user-interface#navigation-menu) include: - Websites & Mobile Apps - Applications - Infrastructure - Synthetic Monitoring - Events - Automation - Service Levels - Settings - etc  ### Rate Limiting A rate limit is applied to API usage. Up to 5,000 calls per hour can be made. How many remaining calls can be made and when this call limit resets, can inspected via three headers that are part of the responses of the API server.  - **X-RateLimit-Limit:** Shows the maximum number of calls that may be executed per hour. - **X-RateLimit-Remaining:** How many calls may still be executed within the current hour. - **X-RateLimit-Reset:** Time when the remaining calls will be reset to the limit. For compatibility reasons with other rate limited APIs, this date is not the date in milliseconds, but instead in seconds since 1970-01-01T00:00:00+00:00.  ### Further Reading We provide additional documentation for our REST API in our [product documentation](https://www.ibm.com/docs/en/instana-observability/current?topic=apis-web-rest-api). Here you'll also find some common queries for retrieving data and configuring Instana.  ## Getting Started with the REST API  ### API base URL The base URL for an specific instance of Instana can be determined using the tenant and unit information. - `base`: This is the base URL of a tenant unit, e.g. `https://test-example.instana.io`. This is the same URL that is used to access the Instana user interface. - `apiToken`: Requests against the Instana API require valid API tokens. An initial API token can be generated via the Instana user interface. Any additional API tokens can be generated via the API itself.  ### Curl Example Here is an Example to use the REST API with Curl. First lets get all the available metrics with possible aggregations with a GET call.  ```bash curl --request GET \\   --url https://test-instana.instana.io/api/application-monitoring/catalog/metrics \\   --header 'authorization: apiToken xxxxxxxxxxxxxxxx' ```  Next we can get every call grouped by the endpoint name that has an error count greater then zero. As a metric we could get the mean error rate for example.  ```bash curl --request POST \\   --url https://test-instana.instana.io/api/application-monitoring/analyze/call-groups \\   --header 'authorization: apiToken xxxxxxxxxxxxxxxx' \\   --header 'content-type: application/json' \\   --data '{   \"group\":{       \"groupbyTag\":\"endpoint.name\"   },   \"tagFilters\":[    {     \"name\":\"call.error.count\",     \"value\":\"0\",     \"operator\":\"GREATER_THAN\"    }   ],   \"metrics\":[    {     \"metric\":\"errors\",     \"aggregation\":\"MEAN\"    }   ]   }' ```  ### Generating REST API clients  The API is specified using the [OpenAPI v3](https://github.com/OAI/OpenAPI-Specification) (previously known as Swagger) format. You can download the current specification at our [GitHub API documentation](https://instana.github.io/openapi/openapi.yaml).  OpenAPI tries to solve the issue of ever-evolving APIs and clients lagging behind. Please make sure that you always use the latest version of the generator, as a number of improvements are regularly made. To generate a client library for your language, you can use the [OpenAPI client generators](https://github.com/OpenAPITools/openapi-generator).  #### Go For example, to generate a client library for Go to interact with our backend, you can use the following script; mind replacing the values of the `UNIT_NAME` and `TENANT_NAME` environment variables using those for your tenant unit:  ```bash #!/bin/bash  ### This script assumes you have the `java` and `wget` commands on the path  export UNIT_NAME='myunit' # for example: prod export TENANT_NAME='mytenant' # for example: awesomecompany  //Download the generator to your current working directory: wget https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/4.3.1/openapi-generator-cli-4.3.1.jar -O openapi-generator-cli.jar --server-variables \"tenant=${TENANT_NAME},unit=${UNIT_NAME}\"  //generate a client library that you can vendor into your repository java -jar openapi-generator-cli.jar generate -i https://instana.github.io/openapi/openapi.yaml -g go \\     -o pkg/instana/openapi \\     --skip-validate-spec  //(optional) format the Go code according to the Go code standard gofmt -s -w pkg/instana/openapi ```  The generated clients contain comprehensive READMEs, and you can start right away using the client from the example above:  ```go import instana \"./pkg/instana/openapi\"  // readTags will read all available application monitoring tags along with their type and category func readTags() {  configuration := instana.NewConfiguration()  configuration.Host = \"tenant-unit.instana.io\"  configuration.BasePath = \"https://tenant-unit.instana.io\"   client := instana.NewAPIClient(configuration)  auth := context.WithValue(context.Background(), instana.ContextAPIKey, instana.APIKey{   Key:    apiKey,   Prefix: \"apiToken\",  })   tags, _, err := client.ApplicationCatalogApi.GetApplicationTagCatalog(auth)  if err != nil {   fmt.Fatalf(\"Error calling the API, aborting.\")  }   for _, tag := range tags {   fmt.Printf(\"%s (%s): %s\\n\", tag.Category, tag.Type, tag.Name)  } } ```  #### Java Follow the instructions provided in the official documentation from [OpenAPI Tools](https://github.com/OpenAPITools) to download the [openapi-generator-cli.jar](https://github.com/OpenAPITools/openapi-generator?tab=readme-ov-file#13---download-jar).  Depending on your environment, use one of the following java http client implementations which will create a valid client for our OpenAPI specification: ``` //Nativ Java HTTP Client java -jar openapi-generator-cli.jar generate -i https://instana.github.io/openapi/openapi.yaml -g java -o pkg/instana/openapi --skip-validate-spec  -p dateLibrary=java8 --library native  //Spring WebClient java -jar openapi-generator-cli.jar generate -i https://instana.github.io/openapi/openapi.yaml -g java -o pkg/instana/openapi --skip-validate-spec  -p dateLibrary=java8,hideGenerationTimestamp=true --library webclient  //Spring RestTemplate java -jar openapi-generator-cli.jar generate -i https://instana.github.io/openapi/openapi.yaml -g java -o pkg/instana/openapi --skip-validate-spec  -p dateLibrary=java8,hideGenerationTimestamp=true --library resttemplate  ``` 

    The version of the OpenAPI document: 1.291.1002
    Contact: support@instana.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from instana_client.models.js_stack_trace_line import JsStackTraceLine
from typing import Optional, Set
from typing_extensions import Self

class WebsiteMonitoringBeacon(BaseModel):
    """
    WebsiteMonitoringBeacon
    """ # noqa: E501
    accuracy_radius: Optional[Annotated[int, Field(strict=True, ge=-1)]] = Field(default=None, alias="accuracyRadius")
    accurate_timings_available: Optional[StrictBool] = Field(default=None, alias="accurateTimingsAvailable")
    agent_version: Optional[StrictStr] = Field(default=None, alias="agentVersion")
    app_cache_time: Optional[Annotated[int, Field(strict=True, ge=-1)]] = Field(default=None, alias="appCacheTime")
    backend_time: Optional[Annotated[int, Field(strict=True, ge=-1)]] = Field(default=None, alias="backendTime")
    backend_trace_id: Optional[StrictStr] = Field(default=None, alias="backendTraceId")
    batch_size: Optional[Annotated[int, Field(strict=True, ge=1)]] = Field(default=None, alias="batchSize")
    beacon_id: StrictStr = Field(alias="beaconId")
    browser_name: Optional[StrictStr] = Field(default=None, alias="browserName")
    browser_version: Optional[StrictStr] = Field(default=None, alias="browserVersion")
    cache_interaction: Optional[StrictStr] = Field(default=None, alias="cacheInteraction")
    children_time: Optional[Annotated[int, Field(strict=True, ge=-1)]] = Field(default=None, alias="childrenTime")
    city: Optional[StrictStr] = None
    clock_skew: Optional[Annotated[int, Field(strict=True, ge=-1)]] = Field(default=None, alias="clockSkew")
    component_stack: Optional[StrictStr] = Field(default=None, alias="componentStack")
    connection_type: Optional[StrictStr] = Field(default=None, alias="connectionType")
    continent: Optional[StrictStr] = None
    continent_code: Optional[StrictStr] = Field(default=None, alias="continentCode")
    country: Optional[StrictStr] = None
    country_code: Optional[StrictStr] = Field(default=None, alias="countryCode")
    csp_blocked_uri: Optional[StrictStr] = Field(default=None, alias="cspBlockedUri")
    csp_column_number: Optional[StrictInt] = Field(default=None, alias="cspColumnNumber")
    csp_disposition: Optional[StrictStr] = Field(default=None, alias="cspDisposition")
    csp_effective_directive: Optional[StrictStr] = Field(default=None, alias="cspEffectiveDirective")
    csp_line_number: Optional[StrictInt] = Field(default=None, alias="cspLineNumber")
    csp_original_policy: Optional[StrictStr] = Field(default=None, alias="cspOriginalPolicy")
    csp_sample: Optional[StrictStr] = Field(default=None, alias="cspSample")
    csp_source_file: Optional[StrictStr] = Field(default=None, alias="cspSourceFile")
    cumulative_layout_shift: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="cumulativeLayoutShift")
    custom_event_name: Optional[StrictStr] = Field(default=None, alias="customEventName")
    custom_metric: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="customMetric")
    decoded_body_size: Optional[Annotated[int, Field(strict=True, ge=-1)]] = Field(default=None, alias="decodedBodySize")
    deprecations: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=16)]] = None
    device_type: Optional[StrictStr] = Field(default=None, alias="deviceType")
    dns_time: Optional[Annotated[int, Field(strict=True, ge=-1)]] = Field(default=None, alias="dnsTime")
    dom_time: Optional[Annotated[int, Field(strict=True, ge=-1)]] = Field(default=None, alias="domTime")
    duration: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    encoded_body_size: Optional[Annotated[int, Field(strict=True, ge=-1)]] = Field(default=None, alias="encodedBodySize")
    error_count: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, alias="errorCount")
    error_id: Optional[StrictStr] = Field(default=None, alias="errorId")
    error_message: Optional[StrictStr] = Field(default=None, alias="errorMessage")
    error_type: Optional[StrictStr] = Field(default=None, alias="errorType")
    first_contentful_paint_time: Optional[Annotated[int, Field(strict=True, ge=-1)]] = Field(default=None, alias="firstContentfulPaintTime")
    first_input_delay_time: Optional[Annotated[int, Field(strict=True, ge=-1)]] = Field(default=None, alias="firstInputDelayTime")
    first_paint_time: Optional[Annotated[int, Field(strict=True, ge=-1)]] = Field(default=None, alias="firstPaintTime")
    frontend_time: Optional[Annotated[int, Field(strict=True, ge=-1)]] = Field(default=None, alias="frontendTime")
    graphql_operation_name: Optional[StrictStr] = Field(default=None, alias="graphqlOperationName")
    graphql_operation_type: Optional[StrictStr] = Field(default=None, alias="graphqlOperationType")
    http_call_asynchronous: Optional[StrictBool] = Field(default=None, alias="httpCallAsynchronous")
    http_call_correlation_attempted: Optional[StrictBool] = Field(default=None, alias="httpCallCorrelationAttempted")
    http_call_headers: Optional[Dict[str, StrictStr]] = Field(default=None, alias="httpCallHeaders")
    http_call_method: Optional[StrictStr] = Field(default=None, alias="httpCallMethod")
    http_call_origin: Optional[StrictStr] = Field(default=None, alias="httpCallOrigin")
    http_call_path: Optional[StrictStr] = Field(default=None, alias="httpCallPath")
    http_call_status: Optional[Annotated[int, Field(le=599, strict=True, ge=-1)]] = Field(default=None, alias="httpCallStatus")
    http_call_url: Optional[StrictStr] = Field(default=None, alias="httpCallUrl")
    initiator: Optional[StrictStr] = None
    interaction_next_paint: Optional[StrictInt] = Field(default=None, alias="interactionNextPaint")
    internal_meta: Optional[Dict[str, StrictStr]] = Field(default=None, alias="internalMeta")
    largest_contentful_paint_time: Optional[Annotated[int, Field(strict=True, ge=-1)]] = Field(default=None, alias="largestContentfulPaintTime")
    latitude: Optional[Union[StrictFloat, StrictInt]] = None
    location_origin: StrictStr = Field(alias="locationOrigin")
    location_path: Optional[StrictStr] = Field(default=None, alias="locationPath")
    location_url: StrictStr = Field(alias="locationUrl")
    longitude: Optional[Union[StrictFloat, StrictInt]] = None
    meta: Optional[Dict[str, StrictStr]] = None
    on_load_time: Optional[Annotated[int, Field(strict=True, ge=-1)]] = Field(default=None, alias="onLoadTime")
    os_name: Optional[StrictStr] = Field(default=None, alias="osName")
    os_version: Optional[StrictStr] = Field(default=None, alias="osVersion")
    page: Optional[StrictStr] = None
    page_load_id: StrictStr = Field(alias="pageLoadId")
    parent_beacon_id: Optional[StrictStr] = Field(default=None, alias="parentBeaconId")
    parsed_stack_trace: Optional[Annotated[List[JsStackTraceLine], Field(min_length=0, max_length=64)]] = Field(default=None, alias="parsedStackTrace")
    phase: Optional[StrictStr] = None
    processing_time: Optional[Annotated[int, Field(strict=True, ge=-1)]] = Field(default=None, alias="processingTime")
    redirect_time: Optional[Annotated[int, Field(strict=True, ge=-1)]] = Field(default=None, alias="redirectTime")
    request_time: Optional[Annotated[int, Field(strict=True, ge=-1)]] = Field(default=None, alias="requestTime")
    resource_type: Optional[StrictStr] = Field(default=None, alias="resourceType")
    response_time: Optional[Annotated[int, Field(strict=True, ge=-1)]] = Field(default=None, alias="responseTime")
    session_id: Optional[StrictStr] = Field(default=None, alias="sessionId")
    snippet_version: Optional[StrictStr] = Field(default=None, alias="snippetVersion")
    ssl_time: Optional[Annotated[int, Field(strict=True, ge=-1)]] = Field(default=None, alias="sslTime")
    stack_trace: Optional[StrictStr] = Field(default=None, alias="stackTrace")
    stack_trace_parsing_status: Optional[Annotated[int, Field(strict=True, ge=-1)]] = Field(default=None, alias="stackTraceParsingStatus")
    stack_trace_readability: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, alias="stackTraceReadability")
    subdivision: Optional[StrictStr] = None
    subdivision_code: Optional[StrictStr] = Field(default=None, alias="subdivisionCode")
    tcp_time: Optional[Annotated[int, Field(strict=True, ge=-1)]] = Field(default=None, alias="tcpTime")
    timestamp: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    transfer_size: Optional[Annotated[int, Field(strict=True, ge=-1)]] = Field(default=None, alias="transferSize")
    type: StrictStr
    unload_time: Optional[Annotated[int, Field(strict=True, ge=-1)]] = Field(default=None, alias="unloadTime")
    use_features: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=15)]] = Field(default=None, alias="useFeatures")
    user_email: Optional[StrictStr] = Field(default=None, alias="userEmail")
    user_id: Optional[StrictStr] = Field(default=None, alias="userId")
    user_ip: Optional[StrictStr] = Field(default=None, alias="userIp")
    user_languages: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=5)]] = Field(default=None, alias="userLanguages")
    user_name: Optional[StrictStr] = Field(default=None, alias="userName")
    website_id: StrictStr = Field(alias="websiteId")
    website_label: StrictStr = Field(alias="websiteLabel")
    window_height: Optional[Annotated[int, Field(strict=True, ge=-1)]] = Field(default=None, alias="windowHeight")
    window_hidden: Optional[StrictBool] = Field(default=None, alias="windowHidden")
    window_width: Optional[Annotated[int, Field(strict=True, ge=-1)]] = Field(default=None, alias="windowWidth")
    __properties: ClassVar[List[str]] = ["accuracyRadius", "accurateTimingsAvailable", "agentVersion", "appCacheTime", "backendTime", "backendTraceId", "batchSize", "beaconId", "browserName", "browserVersion", "cacheInteraction", "childrenTime", "city", "clockSkew", "componentStack", "connectionType", "continent", "continentCode", "country", "countryCode", "cspBlockedUri", "cspColumnNumber", "cspDisposition", "cspEffectiveDirective", "cspLineNumber", "cspOriginalPolicy", "cspSample", "cspSourceFile", "cumulativeLayoutShift", "customEventName", "customMetric", "decodedBodySize", "deprecations", "deviceType", "dnsTime", "domTime", "duration", "encodedBodySize", "errorCount", "errorId", "errorMessage", "errorType", "firstContentfulPaintTime", "firstInputDelayTime", "firstPaintTime", "frontendTime", "graphqlOperationName", "graphqlOperationType", "httpCallAsynchronous", "httpCallCorrelationAttempted", "httpCallHeaders", "httpCallMethod", "httpCallOrigin", "httpCallPath", "httpCallStatus", "httpCallUrl", "initiator", "interactionNextPaint", "internalMeta", "largestContentfulPaintTime", "latitude", "locationOrigin", "locationPath", "locationUrl", "longitude", "meta", "onLoadTime", "osName", "osVersion", "page", "pageLoadId", "parentBeaconId", "parsedStackTrace", "phase", "processingTime", "redirectTime", "requestTime", "resourceType", "responseTime", "sessionId", "snippetVersion", "sslTime", "stackTrace", "stackTraceParsingStatus", "stackTraceReadability", "subdivision", "subdivisionCode", "tcpTime", "timestamp", "transferSize", "type", "unloadTime", "useFeatures", "userEmail", "userId", "userIp", "userLanguages", "userName", "websiteId", "websiteLabel", "windowHeight", "windowHidden", "windowWidth"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of WebsiteMonitoringBeacon from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in parsed_stack_trace (list)
        _items = []
        if self.parsed_stack_trace:
            for _item_parsed_stack_trace in self.parsed_stack_trace:
                if _item_parsed_stack_trace:
                    _items.append(_item_parsed_stack_trace.to_dict())
            _dict['parsedStackTrace'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WebsiteMonitoringBeacon from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accuracyRadius": obj.get("accuracyRadius"),
            "accurateTimingsAvailable": obj.get("accurateTimingsAvailable"),
            "agentVersion": obj.get("agentVersion"),
            "appCacheTime": obj.get("appCacheTime"),
            "backendTime": obj.get("backendTime"),
            "backendTraceId": obj.get("backendTraceId"),
            "batchSize": obj.get("batchSize"),
            "beaconId": obj.get("beaconId"),
            "browserName": obj.get("browserName"),
            "browserVersion": obj.get("browserVersion"),
            "cacheInteraction": obj.get("cacheInteraction"),
            "childrenTime": obj.get("childrenTime"),
            "city": obj.get("city"),
            "clockSkew": obj.get("clockSkew"),
            "componentStack": obj.get("componentStack"),
            "connectionType": obj.get("connectionType"),
            "continent": obj.get("continent"),
            "continentCode": obj.get("continentCode"),
            "country": obj.get("country"),
            "countryCode": obj.get("countryCode"),
            "cspBlockedUri": obj.get("cspBlockedUri"),
            "cspColumnNumber": obj.get("cspColumnNumber"),
            "cspDisposition": obj.get("cspDisposition"),
            "cspEffectiveDirective": obj.get("cspEffectiveDirective"),
            "cspLineNumber": obj.get("cspLineNumber"),
            "cspOriginalPolicy": obj.get("cspOriginalPolicy"),
            "cspSample": obj.get("cspSample"),
            "cspSourceFile": obj.get("cspSourceFile"),
            "cumulativeLayoutShift": obj.get("cumulativeLayoutShift"),
            "customEventName": obj.get("customEventName"),
            "customMetric": obj.get("customMetric"),
            "decodedBodySize": obj.get("decodedBodySize"),
            "deprecations": obj.get("deprecations"),
            "deviceType": obj.get("deviceType"),
            "dnsTime": obj.get("dnsTime"),
            "domTime": obj.get("domTime"),
            "duration": obj.get("duration"),
            "encodedBodySize": obj.get("encodedBodySize"),
            "errorCount": obj.get("errorCount"),
            "errorId": obj.get("errorId"),
            "errorMessage": obj.get("errorMessage"),
            "errorType": obj.get("errorType"),
            "firstContentfulPaintTime": obj.get("firstContentfulPaintTime"),
            "firstInputDelayTime": obj.get("firstInputDelayTime"),
            "firstPaintTime": obj.get("firstPaintTime"),
            "frontendTime": obj.get("frontendTime"),
            "graphqlOperationName": obj.get("graphqlOperationName"),
            "graphqlOperationType": obj.get("graphqlOperationType"),
            "httpCallAsynchronous": obj.get("httpCallAsynchronous"),
            "httpCallCorrelationAttempted": obj.get("httpCallCorrelationAttempted"),
            "httpCallHeaders": obj.get("httpCallHeaders"),
            "httpCallMethod": obj.get("httpCallMethod"),
            "httpCallOrigin": obj.get("httpCallOrigin"),
            "httpCallPath": obj.get("httpCallPath"),
            "httpCallStatus": obj.get("httpCallStatus"),
            "httpCallUrl": obj.get("httpCallUrl"),
            "initiator": obj.get("initiator"),
            "interactionNextPaint": obj.get("interactionNextPaint"),
            "internalMeta": obj.get("internalMeta"),
            "largestContentfulPaintTime": obj.get("largestContentfulPaintTime"),
            "latitude": obj.get("latitude"),
            "locationOrigin": obj.get("locationOrigin"),
            "locationPath": obj.get("locationPath"),
            "locationUrl": obj.get("locationUrl"),
            "longitude": obj.get("longitude"),
            "meta": obj.get("meta"),
            "onLoadTime": obj.get("onLoadTime"),
            "osName": obj.get("osName"),
            "osVersion": obj.get("osVersion"),
            "page": obj.get("page"),
            "pageLoadId": obj.get("pageLoadId"),
            "parentBeaconId": obj.get("parentBeaconId"),
            "parsedStackTrace": [JsStackTraceLine.from_dict(_item) for _item in obj["parsedStackTrace"]] if obj.get("parsedStackTrace") is not None else None,
            "phase": obj.get("phase"),
            "processingTime": obj.get("processingTime"),
            "redirectTime": obj.get("redirectTime"),
            "requestTime": obj.get("requestTime"),
            "resourceType": obj.get("resourceType"),
            "responseTime": obj.get("responseTime"),
            "sessionId": obj.get("sessionId"),
            "snippetVersion": obj.get("snippetVersion"),
            "sslTime": obj.get("sslTime"),
            "stackTrace": obj.get("stackTrace"),
            "stackTraceParsingStatus": obj.get("stackTraceParsingStatus"),
            "stackTraceReadability": obj.get("stackTraceReadability"),
            "subdivision": obj.get("subdivision"),
            "subdivisionCode": obj.get("subdivisionCode"),
            "tcpTime": obj.get("tcpTime"),
            "timestamp": obj.get("timestamp"),
            "transferSize": obj.get("transferSize"),
            "type": obj.get("type"),
            "unloadTime": obj.get("unloadTime"),
            "useFeatures": obj.get("useFeatures"),
            "userEmail": obj.get("userEmail"),
            "userId": obj.get("userId"),
            "userIp": obj.get("userIp"),
            "userLanguages": obj.get("userLanguages"),
            "userName": obj.get("userName"),
            "websiteId": obj.get("websiteId"),
            "websiteLabel": obj.get("websiteLabel"),
            "windowHeight": obj.get("windowHeight"),
            "windowHidden": obj.get("windowHidden"),
            "windowWidth": obj.get("windowWidth")
        })
        return _obj


