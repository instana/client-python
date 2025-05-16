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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from instana_client.models.api_restricted_application_filter import ApiRestrictedApplicationFilter
from instana_client.models.scope_binding import ScopeBinding
from typing import Optional, Set
from typing_extensions import Self

class ApiPermissionSet(BaseModel):
    """
    ApiPermissionSet
    """ # noqa: E501
    action_filter: Optional[ScopeBinding] = Field(default=None, alias="actionFilter")
    application_ids: Annotated[List[ScopeBinding], Field(min_length=0, max_length=1024)] = Field(alias="applicationIds")
    business_perspective_ids: Annotated[List[ScopeBinding], Field(min_length=0, max_length=1024)] = Field(alias="businessPerspectiveIds")
    infra_dfq_filter: ScopeBinding = Field(alias="infraDfqFilter")
    kubernetes_cluster_uuids: Annotated[List[ScopeBinding], Field(min_length=0, max_length=1024)] = Field(alias="kubernetesClusterUUIDs")
    kubernetes_namespace_uids: Annotated[List[ScopeBinding], Field(min_length=0, max_length=1024)] = Field(alias="kubernetesNamespaceUIDs")
    mobile_app_ids: Annotated[List[ScopeBinding], Field(min_length=0, max_length=1024)] = Field(alias="mobileAppIds")
    permissions: Annotated[List[StrictStr], Field(min_length=0, max_length=1024)]
    restricted_application_filter: Optional[ApiRestrictedApplicationFilter] = Field(default=None, alias="restrictedApplicationFilter")
    synthetic_credential_keys: Annotated[List[ScopeBinding], Field(min_length=0, max_length=1024)] = Field(alias="syntheticCredentialKeys")
    synthetic_test_ids: Annotated[List[ScopeBinding], Field(min_length=0, max_length=1024)] = Field(alias="syntheticTestIds")
    website_ids: Annotated[List[ScopeBinding], Field(min_length=0, max_length=1024)] = Field(alias="websiteIds")
    __properties: ClassVar[List[str]] = ["actionFilter", "applicationIds", "businessPerspectiveIds", "infraDfqFilter", "kubernetesClusterUUIDs", "kubernetesNamespaceUIDs", "mobileAppIds", "permissions", "restrictedApplicationFilter", "syntheticCredentialKeys", "syntheticTestIds", "websiteIds"]

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
        """Create an instance of ApiPermissionSet from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of action_filter
        if self.action_filter:
            _dict['actionFilter'] = self.action_filter.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in application_ids (list)
        _items = []
        if self.application_ids:
            for _item_application_ids in self.application_ids:
                if _item_application_ids:
                    _items.append(_item_application_ids.to_dict())
            _dict['applicationIds'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in business_perspective_ids (list)
        _items = []
        if self.business_perspective_ids:
            for _item_business_perspective_ids in self.business_perspective_ids:
                if _item_business_perspective_ids:
                    _items.append(_item_business_perspective_ids.to_dict())
            _dict['businessPerspectiveIds'] = _items
        # override the default output from pydantic by calling `to_dict()` of infra_dfq_filter
        if self.infra_dfq_filter:
            _dict['infraDfqFilter'] = self.infra_dfq_filter.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in kubernetes_cluster_uuids (list)
        _items = []
        if self.kubernetes_cluster_uuids:
            for _item_kubernetes_cluster_uuids in self.kubernetes_cluster_uuids:
                if _item_kubernetes_cluster_uuids:
                    _items.append(_item_kubernetes_cluster_uuids.to_dict())
            _dict['kubernetesClusterUUIDs'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in kubernetes_namespace_uids (list)
        _items = []
        if self.kubernetes_namespace_uids:
            for _item_kubernetes_namespace_uids in self.kubernetes_namespace_uids:
                if _item_kubernetes_namespace_uids:
                    _items.append(_item_kubernetes_namespace_uids.to_dict())
            _dict['kubernetesNamespaceUIDs'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in mobile_app_ids (list)
        _items = []
        if self.mobile_app_ids:
            for _item_mobile_app_ids in self.mobile_app_ids:
                if _item_mobile_app_ids:
                    _items.append(_item_mobile_app_ids.to_dict())
            _dict['mobileAppIds'] = _items
        # override the default output from pydantic by calling `to_dict()` of restricted_application_filter
        if self.restricted_application_filter:
            _dict['restrictedApplicationFilter'] = self.restricted_application_filter.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in synthetic_credential_keys (list)
        _items = []
        if self.synthetic_credential_keys:
            for _item_synthetic_credential_keys in self.synthetic_credential_keys:
                if _item_synthetic_credential_keys:
                    _items.append(_item_synthetic_credential_keys.to_dict())
            _dict['syntheticCredentialKeys'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in synthetic_test_ids (list)
        _items = []
        if self.synthetic_test_ids:
            for _item_synthetic_test_ids in self.synthetic_test_ids:
                if _item_synthetic_test_ids:
                    _items.append(_item_synthetic_test_ids.to_dict())
            _dict['syntheticTestIds'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in website_ids (list)
        _items = []
        if self.website_ids:
            for _item_website_ids in self.website_ids:
                if _item_website_ids:
                    _items.append(_item_website_ids.to_dict())
            _dict['websiteIds'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApiPermissionSet from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "actionFilter": ScopeBinding.from_dict(obj["actionFilter"]) if obj.get("actionFilter") is not None else None,
            "applicationIds": [ScopeBinding.from_dict(_item) for _item in obj["applicationIds"]] if obj.get("applicationIds") is not None else None,
            "businessPerspectiveIds": [ScopeBinding.from_dict(_item) for _item in obj["businessPerspectiveIds"]] if obj.get("businessPerspectiveIds") is not None else None,
            "infraDfqFilter": ScopeBinding.from_dict(obj["infraDfqFilter"]) if obj.get("infraDfqFilter") is not None else None,
            "kubernetesClusterUUIDs": [ScopeBinding.from_dict(_item) for _item in obj["kubernetesClusterUUIDs"]] if obj.get("kubernetesClusterUUIDs") is not None else None,
            "kubernetesNamespaceUIDs": [ScopeBinding.from_dict(_item) for _item in obj["kubernetesNamespaceUIDs"]] if obj.get("kubernetesNamespaceUIDs") is not None else None,
            "mobileAppIds": [ScopeBinding.from_dict(_item) for _item in obj["mobileAppIds"]] if obj.get("mobileAppIds") is not None else None,
            "permissions": obj.get("permissions"),
            "restrictedApplicationFilter": ApiRestrictedApplicationFilter.from_dict(obj["restrictedApplicationFilter"]) if obj.get("restrictedApplicationFilter") is not None else None,
            "syntheticCredentialKeys": [ScopeBinding.from_dict(_item) for _item in obj["syntheticCredentialKeys"]] if obj.get("syntheticCredentialKeys") is not None else None,
            "syntheticTestIds": [ScopeBinding.from_dict(_item) for _item in obj["syntheticTestIds"]] if obj.get("syntheticTestIds") is not None else None,
            "websiteIds": [ScopeBinding.from_dict(_item) for _item in obj["websiteIds"]] if obj.get("websiteIds") is not None else None
        })
        return _obj


