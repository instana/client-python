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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from instana_client.models.application_alert_rule import ApplicationAlertRule
from instana_client.models.application_node import ApplicationNode
from instana_client.models.application_time_threshold import ApplicationTimeThreshold
from instana_client.models.custom_payload_field import CustomPayloadField
from instana_client.models.rule_with_threshold_application_alert_rule import RuleWithThresholdApplicationAlertRule
from instana_client.models.tag_filter import TagFilter
from instana_client.models.tag_filter_expression_element import TagFilterExpressionElement
from instana_client.models.threshold import Threshold
from typing import Optional, Set
from typing_extensions import Self

class ApplicationAlertConfigWithMetadata(BaseModel):
    """
    ApplicationAlertConfigWithMetadata
    """ # noqa: E501
    alert_channel_ids: Annotated[List[StrictStr], Field(min_length=0, max_length=1024)] = Field(description="List of IDs of alert channels defined in Instana. Can be left empty.", alias="alertChannelIds")
    alert_channels: Optional[Dict[str, List[StrictStr]]] = Field(default=None, description="Set of alert channel IDs associated with the severity.", alias="alertChannels")
    application_id: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=64)]] = Field(default=None, description="ID of the application that this Smart Alert configuration is applied to.", alias="applicationId")
    applications: Dict[str, ApplicationNode] = Field(description="Selection of applications, services, and endpoints that this Smart Alert configuration is associated with. This selection is connected to the defined `tagFilterExpression` by the logical `AND` operator.")
    boundary_scope: StrictStr = Field(description="Determines the source of the application alert configuration. An `INBOUND` scope refers to consumer-made calls. An `ALL` scope refers to both consumer and internally made calls.", alias="boundaryScope")
    created: Optional[Annotated[int, Field(strict=True, ge=1)]] = Field(default=None, description="Unix timestamp representing the creation time of this revision.")
    custom_payload_fields: Annotated[List[CustomPayloadField], Field(min_length=0, max_length=20)] = Field(description="Custom payload fields to send additional information in the alert notifications. Can be left empty.", alias="customPayloadFields")
    description: Annotated[str, Field(min_length=0, strict=True, max_length=65536)] = Field(description="Description of the application alert configuration. Used as a template for the description of alert/event notifications triggered by this Smart Alert configuration.")
    enabled: Optional[StrictBool] = Field(default=None, description="Flag to indicate whether or not the configuration is enabled.")
    evaluation_type: StrictStr = Field(description="Determines whether calls of the aggregated metrics are grouped by the application, the service, or the endpoint. This also determines whether the resulting events are categorized as an issue on the respective entity of that group.", alias="evaluationType")
    grace_period: Optional[StrictInt] = Field(default=None, description="The duration for which an alert remains open after conditions are no longer violated, with the alert auto-closing once the grace period expires.", alias="gracePeriod")
    granularity: StrictInt = Field(description="The evaluation granularity used for detection of violations of the defined threshold. Defines the size of the tumbling window used.")
    id: Annotated[str, Field(min_length=0, strict=True, max_length=64)] = Field(description="ID of this Application App Alert Config. ")
    include_internal: Optional[StrictBool] = Field(default=None, description="Flag to include Internal Calls. These calls are work done inside a service and correspond to intermediate spans in custom tracing.", alias="includeInternal")
    include_synthetic: Optional[StrictBool] = Field(default=None, description="Flag to include Synthetic Calls. These calls have a synthetic endpoint as their destination, such as calls to health-check endpoints. ", alias="includeSynthetic")
    initial_created: Optional[Annotated[int, Field(strict=True, ge=1)]] = Field(default=None, description="Unix timestamp representing the time of the initial revision.", alias="initialCreated")
    name: Annotated[str, Field(min_length=0, strict=True, max_length=256)] = Field(description="Name of the application alert configuration. Used as a template for the title of alert/event notifications triggered by this Smart Alert configuration.")
    read_only: Optional[StrictBool] = Field(default=None, description="Flag to indicate whether or not the configuration is read-only. Read-only access restricts modification of the config.", alias="readOnly")
    rule: Optional[ApplicationAlertRule] = None
    rules: Optional[Annotated[List[RuleWithThresholdApplicationAlertRule], Field(min_length=1, max_length=1)]] = Field(default=None, description="A list of rules where each rule is associated with multiple thresholds and their corresponding severity levels. This enables more complex alert configurations with validations to ensure consistent and logical threshold-severity combinations.")
    severity: Optional[Annotated[int, Field(le=10, strict=True, ge=5)]] = Field(default=None, description="The severity of the alert when triggered, which is either 5 (Warning), or 10 (Critical).")
    tag_filter_expression: TagFilterExpressionElement = Field(alias="tagFilterExpression")
    tag_filters: Optional[List[TagFilter]] = Field(default=None, alias="tagFilters")
    threshold: Optional[Threshold] = None
    time_threshold: ApplicationTimeThreshold = Field(alias="timeThreshold")
    triggering: Optional[StrictBool] = Field(default=None, description="Optional flag to indicate whether an Incident is also triggered or not.")
    __properties: ClassVar[List[str]] = ["alertChannelIds", "alertChannels", "applicationId", "applications", "boundaryScope", "created", "customPayloadFields", "description", "enabled", "evaluationType", "gracePeriod", "granularity", "id", "includeInternal", "includeSynthetic", "initialCreated", "name", "readOnly", "rule", "rules", "severity", "tagFilterExpression", "tagFilters", "threshold", "timeThreshold", "triggering"]

    @field_validator('boundary_scope')
    def boundary_scope_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['ALL', 'INBOUND']):
            raise ValueError("must be one of enum values ('ALL', 'INBOUND')")
        return value

    @field_validator('evaluation_type')
    def evaluation_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['PER_AP', 'PER_AP_SERVICE', 'PER_AP_ENDPOINT']):
            raise ValueError("must be one of enum values ('PER_AP', 'PER_AP_SERVICE', 'PER_AP_ENDPOINT')")
        return value

    @field_validator('granularity')
    def granularity_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set([60000, 300000, 600000, 900000, 1200000, 1800000]):
            raise ValueError("must be one of enum values (60000, 300000, 600000, 900000, 1200000, 1800000)")
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
        """Create an instance of ApplicationAlertConfigWithMetadata from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each value in applications (dict)
        _field_dict = {}
        if self.applications:
            for _key_applications in self.applications:
                if self.applications[_key_applications]:
                    _field_dict[_key_applications] = self.applications[_key_applications].to_dict()
            _dict['applications'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each item in custom_payload_fields (list)
        _items = []
        if self.custom_payload_fields:
            for _item_custom_payload_fields in self.custom_payload_fields:
                if _item_custom_payload_fields:
                    _items.append(_item_custom_payload_fields.to_dict())
            _dict['customPayloadFields'] = _items
        # override the default output from pydantic by calling `to_dict()` of rule
        if self.rule:
            _dict['rule'] = self.rule.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in rules (list)
        _items = []
        if self.rules:
            for _item_rules in self.rules:
                if _item_rules:
                    _items.append(_item_rules.to_dict())
            _dict['rules'] = _items
        # override the default output from pydantic by calling `to_dict()` of tag_filter_expression
        if self.tag_filter_expression:
            _dict['tagFilterExpression'] = self.tag_filter_expression.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in tag_filters (list)
        _items = []
        if self.tag_filters:
            for _item_tag_filters in self.tag_filters:
                if _item_tag_filters:
                    _items.append(_item_tag_filters.to_dict())
            _dict['tagFilters'] = _items
        # override the default output from pydantic by calling `to_dict()` of threshold
        if self.threshold:
            _dict['threshold'] = self.threshold.to_dict()
        # override the default output from pydantic by calling `to_dict()` of time_threshold
        if self.time_threshold:
            _dict['timeThreshold'] = self.time_threshold.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApplicationAlertConfigWithMetadata from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "alertChannelIds": obj.get("alertChannelIds"),
            "alertChannels": obj.get("alertChannels"),
            "applicationId": obj.get("applicationId"),
            "applications": dict(
                (_k, ApplicationNode.from_dict(_v))
                for _k, _v in obj["applications"].items()
            )
            if obj.get("applications") is not None
            else None,
            "boundaryScope": obj.get("boundaryScope"),
            "created": obj.get("created"),
            "customPayloadFields": [CustomPayloadField.from_dict(_item) for _item in obj["customPayloadFields"]] if obj.get("customPayloadFields") is not None else None,
            "description": obj.get("description"),
            "enabled": obj.get("enabled"),
            "evaluationType": obj.get("evaluationType"),
            "gracePeriod": obj.get("gracePeriod"),
            "granularity": obj.get("granularity") if obj.get("granularity") is not None else 600000,
            "id": obj.get("id"),
            "includeInternal": obj.get("includeInternal"),
            "includeSynthetic": obj.get("includeSynthetic"),
            "initialCreated": obj.get("initialCreated"),
            "name": obj.get("name"),
            "readOnly": obj.get("readOnly"),
            "rule": ApplicationAlertRule.from_dict(obj["rule"]) if obj.get("rule") is not None else None,
            "rules": [RuleWithThresholdApplicationAlertRule.from_dict(_item) for _item in obj["rules"]] if obj.get("rules") is not None else None,
            "severity": obj.get("severity"),
            "tagFilterExpression": TagFilterExpressionElement.from_dict(obj["tagFilterExpression"]) if obj.get("tagFilterExpression") is not None else None,
            "tagFilters": [TagFilter.from_dict(_item) for _item in obj["tagFilters"]] if obj.get("tagFilters") is not None else None,
            "threshold": Threshold.from_dict(obj["threshold"]) if obj.get("threshold") is not None else None,
            "timeThreshold": ApplicationTimeThreshold.from_dict(obj["timeThreshold"]) if obj.get("timeThreshold") is not None else None,
            "triggering": obj.get("triggering")
        })
        return _obj


