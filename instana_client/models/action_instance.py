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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from instana_client.models.action_instance_metadata_entry import ActionInstanceMetadataEntry
from instana_client.models.action_instance_parameter import ActionInstanceParameter
from typing import Optional, Set
from typing_extensions import Self

class ActionInstance(BaseModel):
    """
    ActionInstance
    """ # noqa: E501
    action_description: Optional[StrictStr] = Field(default=None, description="Action description of the action to run.", alias="actionDescription")
    action_id: StrictStr = Field(description="Action identifier of the action to run.", alias="actionId")
    action_instance_id: Optional[StrictStr] = Field(default=None, description="Action run identifier.", alias="actionInstanceId")
    action_name: StrictStr = Field(description="Action name of the action to run.", alias="actionName")
    action_snapshot: Optional[StrictStr] = Field(default=None, description="Snapshot of the action definition.", alias="actionSnapshot")
    actor_id: Optional[StrictStr] = Field(default=None, description="User identifier, API token or the policy identifier that started the action run.", alias="actorId")
    actor_name: Optional[StrictStr] = Field(default=None, description="Name of the user, API token or the policy that started the action run.", alias="actorName")
    actor_type: Optional[StrictStr] = Field(default=None, description="Type of Actor. Valid values are listed in the enum definition.", alias="actorType")
    created_date: Optional[StrictInt] = Field(default=None, description="Action run created timestamp. The timestamp at which the action run got submitted.", alias="createdDate")
    end_date: Optional[StrictInt] = Field(default=None, description="Action run end timestamp. The timestamp at which the action run ended on the agent host.", alias="endDate")
    error_message: Optional[StrictStr] = Field(default=None, description="Error message, if any, of action run on the agent host.", alias="errorMessage")
    event_entity_type: Optional[StrictStr] = Field(default=None, description="Event entity type set in the event that triggered this action run.", alias="eventEntityType")
    event_id: Optional[StrictStr] = Field(default=None, description="Event identifier of the event that triggered this action run.", alias="eventId")
    event_specification_id: Optional[StrictStr] = Field(default=None, description="Event specification identifier of the event that triggered this action run.", alias="eventSpecificationId")
    external_source_type: Optional[StrictStr] = Field(default=None, description="If the action type is external this field contains the name of the external source.", alias="externalSourceType")
    host_snapshot_id: Optional[StrictStr] = Field(default=None, description="Host snapshot identifier of the agent on which the action ran.", alias="hostSnapshotId")
    input_parameters: Optional[List[ActionInstanceParameter]] = Field(default=None, description="List of input parameters to this action run.", alias="inputParameters")
    metadata: Optional[List[ActionInstanceMetadataEntry]] = Field(default=None, description="List of metadata parameters set to this action run by sensors.")
    output: Optional[StrictStr] = Field(default=None, description="Action run output.")
    policy_id: Optional[StrictStr] = Field(default=None, description="Identifier of the policy that triggered this action run.", alias="policyId")
    problem_text: Optional[StrictStr] = Field(default=None, description="Event problem text of the event that triggered this action run.", alias="problemText")
    return_code: Optional[StrictInt] = Field(default=None, description="Return code of action run on the agent host.", alias="returnCode")
    start_date: Optional[StrictInt] = Field(default=None, description="Action run start timestamp. The timestamp at which the action run started on the agent host.", alias="startDate")
    status: Optional[StrictStr] = Field(default=None, description="Action run status. Valid values are listed in the enum definition.")
    target_snapshot_id: Optional[StrictStr] = Field(default=None, description="Action target entity identifier set in the event that triggered this action run. This is the identifier of the entity on which an incident or issue was raised.", alias="targetSnapshotId")
    type: StrictStr = Field(description="Action type. Valid values are listed in the enum definition.")
    __properties: ClassVar[List[str]] = ["actionDescription", "actionId", "actionInstanceId", "actionName", "actionSnapshot", "actorId", "actorName", "actorType", "createdDate", "endDate", "errorMessage", "eventEntityType", "eventId", "eventSpecificationId", "externalSourceType", "hostSnapshotId", "inputParameters", "metadata", "output", "policyId", "problemText", "returnCode", "startDate", "status", "targetSnapshotId", "type"]

    @field_validator('actor_type')
    def actor_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['ACTOR_UNKNOWN', 'USER', 'APITOKEN', 'POLICY']):
            raise ValueError("must be one of enum values ('ACTOR_UNKNOWN', 'USER', 'APITOKEN', 'POLICY')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['STATUS_UNKNOWN', 'SUBMITTED', 'IN_PROGRESS', 'SUCCESS', 'FAILED', 'READY', 'TIMEOUT']):
            raise ValueError("must be one of enum values ('STATUS_UNKNOWN', 'SUBMITTED', 'IN_PROGRESS', 'SUCCESS', 'FAILED', 'READY', 'TIMEOUT')")
        return value

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['SCRIPT', 'HTTP', 'ANSIBLE', 'EXTERNAL', 'GITHUB', 'GITLAB', 'JIRA', 'MANUAL', 'DOC_LINK']):
            raise ValueError("must be one of enum values ('SCRIPT', 'HTTP', 'ANSIBLE', 'EXTERNAL', 'GITHUB', 'GITLAB', 'JIRA', 'MANUAL', 'DOC_LINK')")
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
        """Create an instance of ActionInstance from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "action_instance_id",
            "action_snapshot",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in input_parameters (list)
        _items = []
        if self.input_parameters:
            for _item_input_parameters in self.input_parameters:
                if _item_input_parameters:
                    _items.append(_item_input_parameters.to_dict())
            _dict['inputParameters'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in metadata (list)
        _items = []
        if self.metadata:
            for _item_metadata in self.metadata:
                if _item_metadata:
                    _items.append(_item_metadata.to_dict())
            _dict['metadata'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ActionInstance from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "actionDescription": obj.get("actionDescription"),
            "actionId": obj.get("actionId"),
            "actionInstanceId": obj.get("actionInstanceId"),
            "actionName": obj.get("actionName"),
            "actionSnapshot": obj.get("actionSnapshot"),
            "actorId": obj.get("actorId"),
            "actorName": obj.get("actorName"),
            "actorType": obj.get("actorType"),
            "createdDate": obj.get("createdDate"),
            "endDate": obj.get("endDate"),
            "errorMessage": obj.get("errorMessage"),
            "eventEntityType": obj.get("eventEntityType"),
            "eventId": obj.get("eventId"),
            "eventSpecificationId": obj.get("eventSpecificationId"),
            "externalSourceType": obj.get("externalSourceType"),
            "hostSnapshotId": obj.get("hostSnapshotId"),
            "inputParameters": [ActionInstanceParameter.from_dict(_item) for _item in obj["inputParameters"]] if obj.get("inputParameters") is not None else None,
            "metadata": [ActionInstanceMetadataEntry.from_dict(_item) for _item in obj["metadata"]] if obj.get("metadata") is not None else None,
            "output": obj.get("output"),
            "policyId": obj.get("policyId"),
            "problemText": obj.get("problemText"),
            "returnCode": obj.get("returnCode"),
            "startDate": obj.get("startDate"),
            "status": obj.get("status"),
            "targetSnapshotId": obj.get("targetSnapshotId"),
            "type": obj.get("type")
        })
        return _obj


