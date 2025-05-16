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
from instana_client.models.stack_trace_line import StackTraceLine
from typing import Optional, Set
from typing_extensions import Self

class MobileAppMonitoringBeacon(BaseModel):
    """
    MobileAppMonitoringBeacon
    """ # noqa: E501
    accuracy_radius: Optional[Annotated[int, Field(strict=True, ge=-1)]] = Field(default=None, alias="accuracyRadius")
    agent_version: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=128)]] = Field(default=None, alias="agentVersion")
    app_build: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=128)]] = Field(default=None, alias="appBuild")
    app_version: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=128)]] = Field(default=None, alias="appVersion")
    app_version_number: Optional[Annotated[int, Field(strict=True, ge=-1)]] = Field(default=None, alias="appVersionNumber")
    available_mb: Optional[Annotated[int, Field(strict=True, ge=-1)]] = Field(default=None, alias="availableMb")
    backend_trace_id: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=128)]] = Field(default=None, alias="backendTraceId")
    batch_size: Optional[Annotated[int, Field(strict=True, ge=1)]] = Field(default=None, alias="batchSize")
    beacon_id: Annotated[str, Field(min_length=0, strict=True, max_length=128)] = Field(alias="beaconId")
    bundle_identifier: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=128)]] = Field(default=None, alias="bundleIdentifier")
    carrier: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=256)]] = None
    city: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=256)]] = None
    clock_skew: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, alias="clockSkew")
    cold_start_time_ms: Optional[Annotated[int, Field(strict=True, ge=-1)]] = Field(default=None, alias="coldStartTimeMs")
    connection_type: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=16)]] = Field(default=None, alias="connectionType")
    continent: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=256)]] = None
    continent_code: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=64)]] = Field(default=None, alias="continentCode")
    country: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=256)]] = None
    country_code: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=64)]] = Field(default=None, alias="countryCode")
    custom_event_name: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=256)]] = Field(default=None, alias="customEventName")
    custom_metric: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="customMetric")
    decoded_body_size: Optional[Annotated[int, Field(strict=True, ge=-1)]] = Field(default=None, alias="decodedBodySize")
    device_hardware: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=128)]] = Field(default=None, alias="deviceHardware")
    device_manufacturer: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=128)]] = Field(default=None, alias="deviceManufacturer")
    device_model: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=128)]] = Field(default=None, alias="deviceModel")
    duration: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    effective_connection_type: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=16)]] = Field(default=None, alias="effectiveConnectionType")
    encoded_body_size: Optional[Annotated[int, Field(strict=True, ge=-1)]] = Field(default=None, alias="encodedBodySize")
    environment: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=256)]] = None
    error_count: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, alias="errorCount")
    error_id: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=128)]] = Field(default=None, alias="errorId")
    error_message: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=16384)]] = Field(default=None, alias="errorMessage")
    error_type: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default=None, alias="errorType")
    google_play_services_missing: Optional[StrictBool] = Field(default=None, alias="googlePlayServicesMissing")
    hot_start_time_ms: Optional[Annotated[int, Field(strict=True, ge=-1)]] = Field(default=None, alias="hotStartTimeMs")
    http_call_headers: Optional[Dict[str, StrictStr]] = Field(default=None, alias="httpCallHeaders")
    http_call_method: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=16)]] = Field(default=None, alias="httpCallMethod")
    http_call_origin: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default=None, alias="httpCallOrigin")
    http_call_path: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=4096)]] = Field(default=None, alias="httpCallPath")
    http_call_status: Optional[Annotated[int, Field(le=599, strict=True, ge=-1)]] = Field(default=None, alias="httpCallStatus")
    http_call_url: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=4096)]] = Field(default=None, alias="httpCallUrl")
    ingestion_time: Optional[Annotated[int, Field(strict=True, ge=1)]] = Field(default=None, alias="ingestionTime")
    internal_meta: Optional[Dict[str, StrictStr]] = Field(default=None, alias="internalMeta")
    latitude: Optional[Union[StrictFloat, StrictInt]] = None
    longitude: Optional[Union[StrictFloat, StrictInt]] = None
    max_mb: Optional[Annotated[int, Field(strict=True, ge=-1)]] = Field(default=None, alias="maxMb")
    meta: Optional[Dict[str, StrictStr]] = None
    mobile_app_id: Annotated[str, Field(min_length=0, strict=True, max_length=64)] = Field(alias="mobileAppId")
    mobile_app_label: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=128)]] = Field(default=None, alias="mobileAppLabel")
    os_name: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=128)]] = Field(default=None, alias="osName")
    os_version: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=128)]] = Field(default=None, alias="osVersion")
    parent_beacon_id: Optional[StrictStr] = Field(default=None, alias="parentBeaconId")
    parsed_stack_trace: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=16384)]] = Field(default=None, alias="parsedStackTrace")
    performance_subtype: Annotated[str, Field(min_length=0, strict=True, max_length=24)] = Field(alias="performanceSubtype")
    platform: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=32)]] = None
    region: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=256)]] = None
    rooted: Optional[StrictBool] = None
    session_id: Annotated[str, Field(min_length=0, strict=True, max_length=128)] = Field(alias="sessionId")
    stack_trace: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=16384)]] = Field(default=None, alias="stackTrace")
    stack_trace_key_checksum: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=128)]] = Field(default=None, alias="stackTraceKeyChecksum")
    stack_trace_key_information: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default=None, alias="stackTraceKeyInformation")
    stack_trace_line: Optional[Annotated[List[StackTraceLine], Field(min_length=0, max_length=128)]] = Field(default=None, alias="stackTraceLine")
    stack_trace_parsing_status: Optional[Annotated[int, Field(strict=True, ge=-1)]] = Field(default=None, alias="stackTraceParsingStatus")
    subdivision: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=256)]] = None
    subdivision_code: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=64)]] = Field(default=None, alias="subdivisionCode")
    tenant: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=256)]] = None
    timestamp: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    transfer_size: Optional[Annotated[int, Field(strict=True, ge=-1)]] = Field(default=None, alias="transferSize")
    type: Annotated[str, Field(min_length=0, strict=True, max_length=24)]
    unit: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=256)]] = None
    use_features: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=15)]] = Field(default=None, alias="useFeatures")
    used_mb: Optional[Annotated[int, Field(strict=True, ge=-1)]] = Field(default=None, alias="usedMb")
    user_email: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=128)]] = Field(default=None, alias="userEmail")
    user_id: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=128)]] = Field(default=None, alias="userId")
    user_ip: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=45)]] = Field(default=None, alias="userIp")
    user_languages: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=5)]] = Field(default=None, alias="userLanguages")
    user_name: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=128)]] = Field(default=None, alias="userName")
    user_session_id: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=128)]] = Field(default=None, alias="userSessionId")
    view: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=256)]] = None
    viewport_height: Optional[Annotated[int, Field(strict=True, ge=-1)]] = Field(default=None, alias="viewportHeight")
    viewport_width: Optional[Annotated[int, Field(strict=True, ge=-1)]] = Field(default=None, alias="viewportWidth")
    warm_start_time_ms: Optional[Annotated[int, Field(strict=True, ge=-1)]] = Field(default=None, alias="warmStartTimeMs")
    __properties: ClassVar[List[str]] = ["accuracyRadius", "agentVersion", "appBuild", "appVersion", "appVersionNumber", "availableMb", "backendTraceId", "batchSize", "beaconId", "bundleIdentifier", "carrier", "city", "clockSkew", "coldStartTimeMs", "connectionType", "continent", "continentCode", "country", "countryCode", "customEventName", "customMetric", "decodedBodySize", "deviceHardware", "deviceManufacturer", "deviceModel", "duration", "effectiveConnectionType", "encodedBodySize", "environment", "errorCount", "errorId", "errorMessage", "errorType", "googlePlayServicesMissing", "hotStartTimeMs", "httpCallHeaders", "httpCallMethod", "httpCallOrigin", "httpCallPath", "httpCallStatus", "httpCallUrl", "ingestionTime", "internalMeta", "latitude", "longitude", "maxMb", "meta", "mobileAppId", "mobileAppLabel", "osName", "osVersion", "parentBeaconId", "parsedStackTrace", "performanceSubtype", "platform", "region", "rooted", "sessionId", "stackTrace", "stackTraceKeyChecksum", "stackTraceKeyInformation", "stackTraceLine", "stackTraceParsingStatus", "subdivision", "subdivisionCode", "tenant", "timestamp", "transferSize", "type", "unit", "useFeatures", "usedMb", "userEmail", "userId", "userIp", "userLanguages", "userName", "userSessionId", "view", "viewportHeight", "viewportWidth", "warmStartTimeMs"]

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
        """Create an instance of MobileAppMonitoringBeacon from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in stack_trace_line (list)
        _items = []
        if self.stack_trace_line:
            for _item_stack_trace_line in self.stack_trace_line:
                if _item_stack_trace_line:
                    _items.append(_item_stack_trace_line.to_dict())
            _dict['stackTraceLine'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MobileAppMonitoringBeacon from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accuracyRadius": obj.get("accuracyRadius"),
            "agentVersion": obj.get("agentVersion"),
            "appBuild": obj.get("appBuild"),
            "appVersion": obj.get("appVersion"),
            "appVersionNumber": obj.get("appVersionNumber"),
            "availableMb": obj.get("availableMb"),
            "backendTraceId": obj.get("backendTraceId"),
            "batchSize": obj.get("batchSize"),
            "beaconId": obj.get("beaconId"),
            "bundleIdentifier": obj.get("bundleIdentifier"),
            "carrier": obj.get("carrier"),
            "city": obj.get("city"),
            "clockSkew": obj.get("clockSkew"),
            "coldStartTimeMs": obj.get("coldStartTimeMs"),
            "connectionType": obj.get("connectionType"),
            "continent": obj.get("continent"),
            "continentCode": obj.get("continentCode"),
            "country": obj.get("country"),
            "countryCode": obj.get("countryCode"),
            "customEventName": obj.get("customEventName"),
            "customMetric": obj.get("customMetric"),
            "decodedBodySize": obj.get("decodedBodySize"),
            "deviceHardware": obj.get("deviceHardware"),
            "deviceManufacturer": obj.get("deviceManufacturer"),
            "deviceModel": obj.get("deviceModel"),
            "duration": obj.get("duration"),
            "effectiveConnectionType": obj.get("effectiveConnectionType"),
            "encodedBodySize": obj.get("encodedBodySize"),
            "environment": obj.get("environment"),
            "errorCount": obj.get("errorCount"),
            "errorId": obj.get("errorId"),
            "errorMessage": obj.get("errorMessage"),
            "errorType": obj.get("errorType"),
            "googlePlayServicesMissing": obj.get("googlePlayServicesMissing"),
            "hotStartTimeMs": obj.get("hotStartTimeMs"),
            "httpCallHeaders": obj.get("httpCallHeaders"),
            "httpCallMethod": obj.get("httpCallMethod"),
            "httpCallOrigin": obj.get("httpCallOrigin"),
            "httpCallPath": obj.get("httpCallPath"),
            "httpCallStatus": obj.get("httpCallStatus"),
            "httpCallUrl": obj.get("httpCallUrl"),
            "ingestionTime": obj.get("ingestionTime"),
            "internalMeta": obj.get("internalMeta"),
            "latitude": obj.get("latitude"),
            "longitude": obj.get("longitude"),
            "maxMb": obj.get("maxMb"),
            "meta": obj.get("meta"),
            "mobileAppId": obj.get("mobileAppId"),
            "mobileAppLabel": obj.get("mobileAppLabel"),
            "osName": obj.get("osName"),
            "osVersion": obj.get("osVersion"),
            "parentBeaconId": obj.get("parentBeaconId"),
            "parsedStackTrace": obj.get("parsedStackTrace"),
            "performanceSubtype": obj.get("performanceSubtype"),
            "platform": obj.get("platform"),
            "region": obj.get("region"),
            "rooted": obj.get("rooted"),
            "sessionId": obj.get("sessionId"),
            "stackTrace": obj.get("stackTrace"),
            "stackTraceKeyChecksum": obj.get("stackTraceKeyChecksum"),
            "stackTraceKeyInformation": obj.get("stackTraceKeyInformation"),
            "stackTraceLine": [StackTraceLine.from_dict(_item) for _item in obj["stackTraceLine"]] if obj.get("stackTraceLine") is not None else None,
            "stackTraceParsingStatus": obj.get("stackTraceParsingStatus"),
            "subdivision": obj.get("subdivision"),
            "subdivisionCode": obj.get("subdivisionCode"),
            "tenant": obj.get("tenant"),
            "timestamp": obj.get("timestamp"),
            "transferSize": obj.get("transferSize"),
            "type": obj.get("type"),
            "unit": obj.get("unit"),
            "useFeatures": obj.get("useFeatures"),
            "usedMb": obj.get("usedMb"),
            "userEmail": obj.get("userEmail"),
            "userId": obj.get("userId"),
            "userIp": obj.get("userIp"),
            "userLanguages": obj.get("userLanguages"),
            "userName": obj.get("userName"),
            "userSessionId": obj.get("userSessionId"),
            "view": obj.get("view"),
            "viewportHeight": obj.get("viewportHeight"),
            "viewportWidth": obj.get("viewportWidth"),
            "warmStartTimeMs": obj.get("warmStartTimeMs")
        })
        return _obj


