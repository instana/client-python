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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from instana_client.models.app_data_metric_configuration import AppDataMetricConfiguration
from instana_client.models.order import Order
from instana_client.models.pagination import Pagination
from instana_client.models.time_frame import TimeFrame
from typing import Optional, Set
from typing_extensions import Self

class GetServices(BaseModel):
    """
    GetServices
    """ # noqa: E501
    application_boundary_scope: Optional[StrictStr] = Field(default=None, description="Use when querying calls of an application:  `INBOUND`: only inbound calls   `ALL`: all the calls to that application (inbound + internal)", alias="applicationBoundaryScope")
    application_id: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=64)]] = Field(default=None, description="An Instana generated unique identifier for an Application. If specified, the list of results will be filtered for the specified Application ID. Eg: `Av62RoIKQv-A3n6DbMQh9g`. One can see the application id from Instana UI by going to an Application Perspective page. In the URL, there will be `appId=Av62RoIKQv-A3n6DbMQh9g`. Alternatively, one can use `Get applications` API endpoint to get the application id in `id` parameter. ", alias="applicationId")
    context_scope: Optional[StrictStr] = Field(default=None, description="separate filtering and group by service id field  - upstream is filtered on destination service and groups on source service  - downstream is filtered on source service and groups on destination service  - none is filtered on destination service and no grouping", alias="contextScope")
    metrics: Annotated[List[AppDataMetricConfiguration], Field(min_length=1, max_length=5)] = Field(description="A list of objects each of which defines a metric and the (statistical) aggregation -- MEAN, SUM, MAX, etc -- that should be used to summarize it for the defined time frame. Eg: `[{ 'metric': 'latency', 'aggregation': 'MEAN'}]`. To know more about supported metrics and its aggregation, See `Get Metric catalog`.")
    name_filter: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=256)]] = Field(default=None, description="filter by name with `contains` semantic. Eg: Let's say there are 2 service names `ecomm-order` and `ecomm-deliver`, you can set `ecomm-` here to include the two Services.", alias="nameFilter")
    order: Optional[Order] = None
    pagination: Optional[Pagination] = None
    service_id: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=64)]] = Field(default=None, description="An Instana generated unique identifier for a Service. If specified, the list of results will be filtered for the specified Service ID. Eg: `3feb3dcd206c166ef2b41c707e0cd38d7cd325aa`. One can see the service id from Instana UI by going to a Service page. In the URL, there will be `serviceId=3feb3dcd206c166ef2b41c707e0cd38d7cd325aa`. Alternatively, one can use `Get services` API endpoint to get the service id in `id` parameter. ", alias="serviceId")
    technologies: Optional[Annotated[List[StrictStr], Field(min_length=0, max_length=20)]] = Field(default=None, description="A list of technologies to be used for filtering data. For example, technologies could include AWS ECS, Cassandra, DB2, JVM, Kafka, etc. A full list of available technologies can be found in X.")
    time_frame: Optional[TimeFrame] = Field(default=None, alias="timeFrame")
    __properties: ClassVar[List[str]] = ["applicationBoundaryScope", "applicationId", "contextScope", "metrics", "nameFilter", "order", "pagination", "serviceId", "technologies", "timeFrame"]

    @field_validator('application_boundary_scope')
    def application_boundary_scope_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['ALL', 'INBOUND']):
            raise ValueError("must be one of enum values ('ALL', 'INBOUND')")
        return value

    @field_validator('context_scope')
    def context_scope_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['NONE', 'UPSTREAM', 'DOWNSTREAM']):
            raise ValueError("must be one of enum values ('NONE', 'UPSTREAM', 'DOWNSTREAM')")
        return value

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
        """Create an instance of GetServices from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in metrics (list)
        _items = []
        if self.metrics:
            for _item_metrics in self.metrics:
                if _item_metrics:
                    _items.append(_item_metrics.to_dict())
            _dict['metrics'] = _items
        # override the default output from pydantic by calling `to_dict()` of order
        if self.order:
            _dict['order'] = self.order.to_dict()
        # override the default output from pydantic by calling `to_dict()` of pagination
        if self.pagination:
            _dict['pagination'] = self.pagination.to_dict()
        # override the default output from pydantic by calling `to_dict()` of time_frame
        if self.time_frame:
            _dict['timeFrame'] = self.time_frame.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetServices from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "applicationBoundaryScope": obj.get("applicationBoundaryScope"),
            "applicationId": obj.get("applicationId"),
            "contextScope": obj.get("contextScope"),
            "metrics": [AppDataMetricConfiguration.from_dict(_item) for _item in obj["metrics"]] if obj.get("metrics") is not None else None,
            "nameFilter": obj.get("nameFilter"),
            "order": Order.from_dict(obj["order"]) if obj.get("order") is not None else None,
            "pagination": Pagination.from_dict(obj["pagination"]) if obj.get("pagination") is not None else None,
            "serviceId": obj.get("serviceId"),
            "technologies": obj.get("technologies"),
            "timeFrame": TimeFrame.from_dict(obj["timeFrame"]) if obj.get("timeFrame") is not None else None
        })
        return _obj


