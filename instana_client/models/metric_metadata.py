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
from typing import Optional, Set
from typing_extensions import Self

class MetricMetadata(BaseModel):
    """
    MetricMetadata
    """ # noqa: E501
    category: Optional[StrictStr] = Field(default=None, description="Category of the metric")
    cross_series_aggregations: Optional[List[StrictStr]] = Field(default=None, description="Possible cross series aggregation the metric supports", alias="crossSeriesAggregations")
    description: Optional[StrictStr] = Field(default=None, description="Description of the metric")
    format: Optional[StrictStr] = Field(default=None, description="| * NUMBER: Generic number * BYTES: Number of bytes * KILO_BYTES: Number of kilobytes * MEGA_BYTES: Number of megabytes * PERCENTAGE: Percentage in scale [0,1] * PERCENTAGE_100: Percentage in scale [0,100] * PERCENTAGE_NO_CAPPING: Percentage in scale [0,1] but value could exceed 1 for example when metric is aggregated * PERCENTAGE_100_NO_CAPPING: Percentage in scale [0,100] but value could exceed 100 for example when metric is aggregated * LATENCY: Time in milliseconds, with value of 0 should not be considered a a strict 0, but considered as < 1ms * NANOS: Time in nanoseconds * MILLIS: Time in milliseconds * MICROS: Time in microseconds * SECONDS: Time in seconds * RATE: Number of occurrences per second * BYTE_RATE: Number of bytes per second * UNDEFINED: Metric value unit is not known ")
    id: StrictStr = Field(description="Identifier for the metric")
    infra_tag_category: StrictStr = Field(description="Category of the entity", alias="infraTagCategory")
    label: StrictStr = Field(description="Label for the metric")
    owner_type: StrictStr = Field(description="Type of the entity associated with the metric", alias="ownerType")
    tags: Optional[List[StrictStr]] = Field(default=None, description="Metric tags")
    __properties: ClassVar[List[str]] = ["category", "crossSeriesAggregations", "description", "format", "id", "infraTagCategory", "label", "ownerType", "tags"]

    @field_validator('cross_series_aggregations')
    def cross_series_aggregations_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['SUM', 'MEAN', 'MAX', 'MIN', 'P25', 'P50', 'P75', 'P90', 'P95', 'P98', 'P99', 'P99_9', 'P99_99', 'DISTINCT_COUNT', 'SUM_POSITIVE', 'PER_SECOND', 'INCREASE']):
                raise ValueError("each list item must be one of ('SUM', 'MEAN', 'MAX', 'MIN', 'P25', 'P50', 'P75', 'P90', 'P95', 'P98', 'P99', 'P99_9', 'P99_99', 'DISTINCT_COUNT', 'SUM_POSITIVE', 'PER_SECOND', 'INCREASE')")
        return value

    @field_validator('format')
    def format_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['NUMBER', 'BYTES', 'KILO_BYTES', 'MEGA_BYTES', 'PERCENTAGE', 'PERCENTAGE_100', 'PERCENTAGE_NO_CAPPING', 'PERCENTAGE_100_NO_CAPPING', 'LATENCY', 'NANOS', 'MILLIS', 'MICROS', 'SECONDS', 'RATE', 'BYTE_RATE', 'UNDEFINED']):
            raise ValueError("must be one of enum values ('NUMBER', 'BYTES', 'KILO_BYTES', 'MEGA_BYTES', 'PERCENTAGE', 'PERCENTAGE_100', 'PERCENTAGE_NO_CAPPING', 'PERCENTAGE_100_NO_CAPPING', 'LATENCY', 'NANOS', 'MILLIS', 'MICROS', 'SECONDS', 'RATE', 'BYTE_RATE', 'UNDEFINED')")
        return value

    @field_validator('infra_tag_category')
    def infra_tag_category_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['ACE', 'ALICLOUD', 'AWS', 'AZURE', 'CASSANDRA', 'CLOUD_FOUNDRY', 'CLR', 'COCKROACH', 'CONSUL', 'CONTAINER', 'COUCHBASE', 'DFQ', 'ELASTICSEARCH', 'GCP', 'HADOOP_YARN', 'HAZELCAST', 'IBM_CLOUD', 'IBM_DATAPOWER', 'IBM_I_SERIES', 'IBM_MQ', 'IBM_MQMFT', 'IBM_OPENSTACK', 'KAFKA_CONNECT', 'KUBERNETES', 'MONGO_DB', 'OTHERS', 'REDIS', 'SAP', 'SELF_MONITORING', 'SOLR', 'SPARK', 'TIBCOBW', 'TUXEDO', 'VSHPERE', 'WEBSPHERE']):
            raise ValueError("must be one of enum values ('ACE', 'ALICLOUD', 'AWS', 'AZURE', 'CASSANDRA', 'CLOUD_FOUNDRY', 'CLR', 'COCKROACH', 'CONSUL', 'CONTAINER', 'COUCHBASE', 'DFQ', 'ELASTICSEARCH', 'GCP', 'HADOOP_YARN', 'HAZELCAST', 'IBM_CLOUD', 'IBM_DATAPOWER', 'IBM_I_SERIES', 'IBM_MQ', 'IBM_MQMFT', 'IBM_OPENSTACK', 'KAFKA_CONNECT', 'KUBERNETES', 'MONGO_DB', 'OTHERS', 'REDIS', 'SAP', 'SELF_MONITORING', 'SOLR', 'SPARK', 'TIBCOBW', 'TUXEDO', 'VSHPERE', 'WEBSPHERE')")
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
        """Create an instance of MetricMetadata from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MetricMetadata from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "category": obj.get("category"),
            "crossSeriesAggregations": obj.get("crossSeriesAggregations"),
            "description": obj.get("description"),
            "format": obj.get("format"),
            "id": obj.get("id"),
            "infraTagCategory": obj.get("infraTagCategory"),
            "label": obj.get("label"),
            "ownerType": obj.get("ownerType"),
            "tags": obj.get("tags")
        })
        return _obj


