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
from instana_client.models.access_rule import AccessRule
from instana_client.models.match_expression_dto import MatchExpressionDTO
from instana_client.models.tag_filter_expression_element import TagFilterExpressionElement
from typing import Optional, Set
from typing_extensions import Self

class ApplicationConfig(BaseModel):
    """
    ApplicationConfig
    """ # noqa: E501
    access_rules: Annotated[List[AccessRule], Field(min_length=1, max_length=64)] = Field(description="Defines permissions and access relationships. ", alias="accessRules")
    boundary_scope: StrictStr = Field(description="**INBOUND**: Inbound calls are calls initiated from outside the application and where the destination service is part of the selected application perspective.  **ALL**: Results and metrics for not only calls at the application perspective boundary, but also those occurring within the application perspective.  **DEFAULT**: Default value, for Application Perspectives created before the introduction of `ALL` and `INBOUND`. At present, whenever new Application Perspectives are created, there are only 2 options to select: `ALL` or `INBOUND`. It is recommended to use either `ALL` or `INBOUND` as `DEFAULT` is deprecated. `DEFAULT` is treated as `INBOUND`. ", alias="boundaryScope")
    id: Annotated[str, Field(min_length=1, strict=True, max_length=128)] = Field(description="Unique ID of the Application Perspective. Eg: `Av62RoIKQv-A3n6DbMQh9g`.")
    label: Annotated[str, Field(min_length=1, strict=True, max_length=128)] = Field(description="Name of the Application Perspective. Eg: `app1`.")
    match_specification: Optional[MatchExpressionDTO] = Field(default=None, alias="matchSpecification")
    scope: StrictStr = Field(description="**INCLUDE_NO_DOWNSTREAM** : Only the selected services from the filters are included (call this the core set). This is useful when you treat the services as opaque. An example would be the services that represent 3rd party APIs.  **INCLUDE_IMMEDIATE_DOWNSTREAM_DATABASE_AND_MESSAGING** : Include the core set of services from the filters and then expand this core set to include the database and messaging services that the core set directly interacts with. This is useful if you are want to monitor a set of services and their direct dependencies. For example, a development team responsible for several micro-services.  **INCLUDE_ALL_DOWNSTREAM** : It effortlessly and automatically includes all the services that form the entire end-to-end dependency chain of the core set of services. This is useful if the AP will be used for troubleshooting. ")
    tag_filter_expression: Optional[TagFilterExpressionElement] = Field(default=None, alias="tagFilterExpression")
    __properties: ClassVar[List[str]] = ["accessRules", "boundaryScope", "id", "label", "matchSpecification", "scope", "tagFilterExpression"]

    @field_validator('boundary_scope')
    def boundary_scope_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['ALL', 'INBOUND', 'DEFAULT']):
            raise ValueError("must be one of enum values ('ALL', 'INBOUND', 'DEFAULT')")
        return value

    @field_validator('scope')
    def scope_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['INCLUDE_NO_DOWNSTREAM', 'INCLUDE_IMMEDIATE_DOWNSTREAM_DATABASE_AND_MESSAGING', 'INCLUDE_ALL_DOWNSTREAM']):
            raise ValueError("must be one of enum values ('INCLUDE_NO_DOWNSTREAM', 'INCLUDE_IMMEDIATE_DOWNSTREAM_DATABASE_AND_MESSAGING', 'INCLUDE_ALL_DOWNSTREAM')")
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
        """Create an instance of ApplicationConfig from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in access_rules (list)
        _items = []
        if self.access_rules:
            for _item_access_rules in self.access_rules:
                if _item_access_rules:
                    _items.append(_item_access_rules.to_dict())
            _dict['accessRules'] = _items
        # override the default output from pydantic by calling `to_dict()` of match_specification
        if self.match_specification:
            _dict['matchSpecification'] = self.match_specification.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tag_filter_expression
        if self.tag_filter_expression:
            _dict['tagFilterExpression'] = self.tag_filter_expression.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApplicationConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accessRules": [AccessRule.from_dict(_item) for _item in obj["accessRules"]] if obj.get("accessRules") is not None else None,
            "boundaryScope": obj.get("boundaryScope"),
            "id": obj.get("id"),
            "label": obj.get("label"),
            "matchSpecification": MatchExpressionDTO.from_dict(obj["matchSpecification"]) if obj.get("matchSpecification") is not None else None,
            "scope": obj.get("scope"),
            "tagFilterExpression": TagFilterExpressionElement.from_dict(obj["tagFilterExpression"]) if obj.get("tagFilterExpression") is not None else None
        })
        return _obj


