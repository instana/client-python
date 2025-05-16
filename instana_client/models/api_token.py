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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ApiToken(BaseModel):
    """
    ApiToken
    """ # noqa: E501
    access_granting_token: StrictStr = Field(alias="accessGrantingToken")
    can_configure_agent_run_mode: Optional[StrictBool] = Field(default=None, alias="canConfigureAgentRunMode")
    can_configure_agents: Optional[StrictBool] = Field(default=None, alias="canConfigureAgents")
    can_configure_api_tokens: Optional[StrictBool] = Field(default=None, alias="canConfigureApiTokens")
    can_configure_application_smart_alerts: Optional[StrictBool] = Field(default=None, alias="canConfigureApplicationSmartAlerts")
    can_configure_applications: Optional[StrictBool] = Field(default=None, alias="canConfigureApplications")
    can_configure_authentication_methods: Optional[StrictBool] = Field(default=None, alias="canConfigureAuthenticationMethods")
    can_configure_automation_actions: Optional[StrictBool] = Field(default=None, alias="canConfigureAutomationActions")
    can_configure_automation_policies: Optional[StrictBool] = Field(default=None, alias="canConfigureAutomationPolicies")
    can_configure_bizops: Optional[StrictBool] = Field(default=None, alias="canConfigureBizops")
    can_configure_database_management: Optional[StrictBool] = Field(default=None, alias="canConfigureDatabaseManagement")
    can_configure_eum_applications: Optional[StrictBool] = Field(default=None, alias="canConfigureEumApplications")
    can_configure_events_and_alerts: Optional[StrictBool] = Field(default=None, alias="canConfigureEventsAndAlerts")
    can_configure_global_alert_payload: Optional[StrictBool] = Field(default=None, alias="canConfigureGlobalAlertPayload")
    can_configure_global_application_smart_alerts: Optional[StrictBool] = Field(default=None, alias="canConfigureGlobalApplicationSmartAlerts")
    can_configure_global_infra_smart_alerts: Optional[StrictBool] = Field(default=None, alias="canConfigureGlobalInfraSmartAlerts")
    can_configure_global_log_smart_alerts: Optional[StrictBool] = Field(default=None, alias="canConfigureGlobalLogSmartAlerts")
    can_configure_global_synthetic_smart_alerts: Optional[StrictBool] = Field(default=None, alias="canConfigureGlobalSyntheticSmartAlerts")
    can_configure_integrations: Optional[StrictBool] = Field(default=None, alias="canConfigureIntegrations")
    can_configure_log_management: Optional[StrictBool] = Field(default=None, alias="canConfigureLogManagement")
    can_configure_log_retention_period: Optional[StrictBool] = Field(default=None, alias="canConfigureLogRetentionPeriod")
    can_configure_maintenance_windows: Optional[StrictBool] = Field(default=None, alias="canConfigureMaintenanceWindows")
    can_configure_mobile_app_monitoring: Optional[StrictBool] = Field(default=None, alias="canConfigureMobileAppMonitoring")
    can_configure_mobile_app_smart_alerts: Optional[StrictBool] = Field(default=None, alias="canConfigureMobileAppSmartAlerts")
    can_configure_personal_api_tokens: Optional[StrictBool] = Field(default=None, alias="canConfigurePersonalApiTokens")
    can_configure_releases: Optional[StrictBool] = Field(default=None, alias="canConfigureReleases")
    can_configure_service_level_indicators: Optional[StrictBool] = Field(default=None, alias="canConfigureServiceLevelIndicators")
    can_configure_service_mapping: Optional[StrictBool] = Field(default=None, alias="canConfigureServiceMapping")
    can_configure_session_settings: Optional[StrictBool] = Field(default=None, alias="canConfigureSessionSettings")
    can_configure_subtraces: Optional[StrictBool] = Field(default=None, alias="canConfigureSubtraces")
    can_configure_synthetic_credentials: Optional[StrictBool] = Field(default=None, alias="canConfigureSyntheticCredentials")
    can_configure_synthetic_locations: Optional[StrictBool] = Field(default=None, alias="canConfigureSyntheticLocations")
    can_configure_synthetic_tests: Optional[StrictBool] = Field(default=None, alias="canConfigureSyntheticTests")
    can_configure_teams: Optional[StrictBool] = Field(default=None, alias="canConfigureTeams")
    can_configure_users: Optional[StrictBool] = Field(default=None, alias="canConfigureUsers")
    can_configure_website_smart_alerts: Optional[StrictBool] = Field(default=None, alias="canConfigureWebsiteSmartAlerts")
    can_create_heap_dump: Optional[StrictBool] = Field(default=None, alias="canCreateHeapDump")
    can_create_public_custom_dashboards: Optional[StrictBool] = Field(default=None, alias="canCreatePublicCustomDashboards")
    can_create_thread_dump: Optional[StrictBool] = Field(default=None, alias="canCreateThreadDump")
    can_delete_automation_action_history: Optional[StrictBool] = Field(default=None, alias="canDeleteAutomationActionHistory")
    can_delete_logs: Optional[StrictBool] = Field(default=None, alias="canDeleteLogs")
    can_edit_all_accessible_custom_dashboards: Optional[StrictBool] = Field(default=None, alias="canEditAllAccessibleCustomDashboards")
    can_install_new_agents: Optional[StrictBool] = Field(default=None, alias="canInstallNewAgents")
    can_invoke_alert_channel: Optional[StrictBool] = Field(default=None, alias="canInvokeAlertChannel")
    can_manually_close_issue: Optional[StrictBool] = Field(default=None, alias="canManuallyCloseIssue")
    can_run_automation_actions: Optional[StrictBool] = Field(default=None, alias="canRunAutomationActions")
    can_use_synthetic_credentials: Optional[StrictBool] = Field(default=None, alias="canUseSyntheticCredentials")
    can_view_account_and_billing_information: Optional[StrictBool] = Field(default=None, alias="canViewAccountAndBillingInformation")
    can_view_audit_log: Optional[StrictBool] = Field(default=None, alias="canViewAuditLog")
    can_view_biz_alerts: Optional[StrictBool] = Field(default=None, alias="canViewBizAlerts")
    can_view_business_activities: Optional[StrictBool] = Field(default=None, alias="canViewBusinessActivities")
    can_view_business_process_details: Optional[StrictBool] = Field(default=None, alias="canViewBusinessProcessDetails")
    can_view_business_processes: Optional[StrictBool] = Field(default=None, alias="canViewBusinessProcesses")
    can_view_log_volume: Optional[StrictBool] = Field(default=None, alias="canViewLogVolume")
    can_view_logs: Optional[StrictBool] = Field(default=None, alias="canViewLogs")
    can_view_synthetic_locations: Optional[StrictBool] = Field(default=None, alias="canViewSyntheticLocations")
    can_view_synthetic_test_results: Optional[StrictBool] = Field(default=None, alias="canViewSyntheticTestResults")
    can_view_synthetic_tests: Optional[StrictBool] = Field(default=None, alias="canViewSyntheticTests")
    can_view_trace_details: Optional[StrictBool] = Field(default=None, alias="canViewTraceDetails")
    created_by: Optional[StrictStr] = Field(default=None, alias="createdBy")
    created_on: Optional[StrictInt] = Field(default=None, alias="createdOn")
    expires_on: Optional[StrictInt] = Field(default=None, alias="expiresOn")
    id: Optional[StrictStr] = None
    internal_id: StrictStr = Field(alias="internalId")
    last_used_on: Optional[StrictInt] = Field(default=None, alias="lastUsedOn")
    limited_applications_scope: Optional[StrictBool] = Field(default=None, alias="limitedApplicationsScope")
    limited_automation_scope: Optional[StrictBool] = Field(default=None, alias="limitedAutomationScope")
    limited_biz_ops_scope: Optional[StrictBool] = Field(default=None, alias="limitedBizOpsScope")
    limited_infrastructure_scope: Optional[StrictBool] = Field(default=None, alias="limitedInfrastructureScope")
    limited_kubernetes_scope: Optional[StrictBool] = Field(default=None, alias="limitedKubernetesScope")
    limited_logs_scope: Optional[StrictBool] = Field(default=None, alias="limitedLogsScope")
    limited_mobile_apps_scope: Optional[StrictBool] = Field(default=None, alias="limitedMobileAppsScope")
    limited_nutanix_scope: Optional[StrictBool] = Field(default=None, alias="limitedNutanixScope")
    limited_openstack_scope: Optional[StrictBool] = Field(default=None, alias="limitedOpenstackScope")
    limited_pcf_scope: Optional[StrictBool] = Field(default=None, alias="limitedPcfScope")
    limited_phmc_scope: Optional[StrictBool] = Field(default=None, alias="limitedPhmcScope")
    limited_pvc_scope: Optional[StrictBool] = Field(default=None, alias="limitedPvcScope")
    limited_synthetics_scope: Optional[StrictBool] = Field(default=None, alias="limitedSyntheticsScope")
    limited_vsphere_scope: Optional[StrictBool] = Field(default=None, alias="limitedVsphereScope")
    limited_websites_scope: Optional[StrictBool] = Field(default=None, alias="limitedWebsitesScope")
    limited_zhmc_scope: Optional[StrictBool] = Field(default=None, alias="limitedZhmcScope")
    name: StrictStr
    __properties: ClassVar[List[str]] = ["accessGrantingToken", "canConfigureAgentRunMode", "canConfigureAgents", "canConfigureApiTokens", "canConfigureApplicationSmartAlerts", "canConfigureApplications", "canConfigureAuthenticationMethods", "canConfigureAutomationActions", "canConfigureAutomationPolicies", "canConfigureBizops", "canConfigureDatabaseManagement", "canConfigureEumApplications", "canConfigureEventsAndAlerts", "canConfigureGlobalAlertPayload", "canConfigureGlobalApplicationSmartAlerts", "canConfigureGlobalInfraSmartAlerts", "canConfigureGlobalLogSmartAlerts", "canConfigureGlobalSyntheticSmartAlerts", "canConfigureIntegrations", "canConfigureLogManagement", "canConfigureLogRetentionPeriod", "canConfigureMaintenanceWindows", "canConfigureMobileAppMonitoring", "canConfigureMobileAppSmartAlerts", "canConfigurePersonalApiTokens", "canConfigureReleases", "canConfigureServiceLevelIndicators", "canConfigureServiceMapping", "canConfigureSessionSettings", "canConfigureSubtraces", "canConfigureSyntheticCredentials", "canConfigureSyntheticLocations", "canConfigureSyntheticTests", "canConfigureTeams", "canConfigureUsers", "canConfigureWebsiteSmartAlerts", "canCreateHeapDump", "canCreatePublicCustomDashboards", "canCreateThreadDump", "canDeleteAutomationActionHistory", "canDeleteLogs", "canEditAllAccessibleCustomDashboards", "canInstallNewAgents", "canInvokeAlertChannel", "canManuallyCloseIssue", "canRunAutomationActions", "canUseSyntheticCredentials", "canViewAccountAndBillingInformation", "canViewAuditLog", "canViewBizAlerts", "canViewBusinessActivities", "canViewBusinessProcessDetails", "canViewBusinessProcesses", "canViewLogVolume", "canViewLogs", "canViewSyntheticLocations", "canViewSyntheticTestResults", "canViewSyntheticTests", "canViewTraceDetails", "createdBy", "createdOn", "expiresOn", "id", "internalId", "lastUsedOn", "limitedApplicationsScope", "limitedAutomationScope", "limitedBizOpsScope", "limitedInfrastructureScope", "limitedKubernetesScope", "limitedLogsScope", "limitedMobileAppsScope", "limitedNutanixScope", "limitedOpenstackScope", "limitedPcfScope", "limitedPhmcScope", "limitedPvcScope", "limitedSyntheticsScope", "limitedVsphereScope", "limitedWebsitesScope", "limitedZhmcScope", "name"]

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
        """Create an instance of ApiToken from a JSON string"""
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
        """Create an instance of ApiToken from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accessGrantingToken": obj.get("accessGrantingToken"),
            "canConfigureAgentRunMode": obj.get("canConfigureAgentRunMode"),
            "canConfigureAgents": obj.get("canConfigureAgents"),
            "canConfigureApiTokens": obj.get("canConfigureApiTokens"),
            "canConfigureApplicationSmartAlerts": obj.get("canConfigureApplicationSmartAlerts"),
            "canConfigureApplications": obj.get("canConfigureApplications"),
            "canConfigureAuthenticationMethods": obj.get("canConfigureAuthenticationMethods"),
            "canConfigureAutomationActions": obj.get("canConfigureAutomationActions"),
            "canConfigureAutomationPolicies": obj.get("canConfigureAutomationPolicies"),
            "canConfigureBizops": obj.get("canConfigureBizops"),
            "canConfigureDatabaseManagement": obj.get("canConfigureDatabaseManagement"),
            "canConfigureEumApplications": obj.get("canConfigureEumApplications"),
            "canConfigureEventsAndAlerts": obj.get("canConfigureEventsAndAlerts"),
            "canConfigureGlobalAlertPayload": obj.get("canConfigureGlobalAlertPayload"),
            "canConfigureGlobalApplicationSmartAlerts": obj.get("canConfigureGlobalApplicationSmartAlerts"),
            "canConfigureGlobalInfraSmartAlerts": obj.get("canConfigureGlobalInfraSmartAlerts"),
            "canConfigureGlobalLogSmartAlerts": obj.get("canConfigureGlobalLogSmartAlerts"),
            "canConfigureGlobalSyntheticSmartAlerts": obj.get("canConfigureGlobalSyntheticSmartAlerts"),
            "canConfigureIntegrations": obj.get("canConfigureIntegrations"),
            "canConfigureLogManagement": obj.get("canConfigureLogManagement"),
            "canConfigureLogRetentionPeriod": obj.get("canConfigureLogRetentionPeriod"),
            "canConfigureMaintenanceWindows": obj.get("canConfigureMaintenanceWindows"),
            "canConfigureMobileAppMonitoring": obj.get("canConfigureMobileAppMonitoring"),
            "canConfigureMobileAppSmartAlerts": obj.get("canConfigureMobileAppSmartAlerts"),
            "canConfigurePersonalApiTokens": obj.get("canConfigurePersonalApiTokens"),
            "canConfigureReleases": obj.get("canConfigureReleases"),
            "canConfigureServiceLevelIndicators": obj.get("canConfigureServiceLevelIndicators"),
            "canConfigureServiceMapping": obj.get("canConfigureServiceMapping"),
            "canConfigureSessionSettings": obj.get("canConfigureSessionSettings"),
            "canConfigureSubtraces": obj.get("canConfigureSubtraces"),
            "canConfigureSyntheticCredentials": obj.get("canConfigureSyntheticCredentials"),
            "canConfigureSyntheticLocations": obj.get("canConfigureSyntheticLocations"),
            "canConfigureSyntheticTests": obj.get("canConfigureSyntheticTests"),
            "canConfigureTeams": obj.get("canConfigureTeams"),
            "canConfigureUsers": obj.get("canConfigureUsers"),
            "canConfigureWebsiteSmartAlerts": obj.get("canConfigureWebsiteSmartAlerts"),
            "canCreateHeapDump": obj.get("canCreateHeapDump"),
            "canCreatePublicCustomDashboards": obj.get("canCreatePublicCustomDashboards"),
            "canCreateThreadDump": obj.get("canCreateThreadDump"),
            "canDeleteAutomationActionHistory": obj.get("canDeleteAutomationActionHistory"),
            "canDeleteLogs": obj.get("canDeleteLogs"),
            "canEditAllAccessibleCustomDashboards": obj.get("canEditAllAccessibleCustomDashboards"),
            "canInstallNewAgents": obj.get("canInstallNewAgents"),
            "canInvokeAlertChannel": obj.get("canInvokeAlertChannel"),
            "canManuallyCloseIssue": obj.get("canManuallyCloseIssue"),
            "canRunAutomationActions": obj.get("canRunAutomationActions"),
            "canUseSyntheticCredentials": obj.get("canUseSyntheticCredentials"),
            "canViewAccountAndBillingInformation": obj.get("canViewAccountAndBillingInformation"),
            "canViewAuditLog": obj.get("canViewAuditLog"),
            "canViewBizAlerts": obj.get("canViewBizAlerts"),
            "canViewBusinessActivities": obj.get("canViewBusinessActivities"),
            "canViewBusinessProcessDetails": obj.get("canViewBusinessProcessDetails"),
            "canViewBusinessProcesses": obj.get("canViewBusinessProcesses"),
            "canViewLogVolume": obj.get("canViewLogVolume"),
            "canViewLogs": obj.get("canViewLogs"),
            "canViewSyntheticLocations": obj.get("canViewSyntheticLocations"),
            "canViewSyntheticTestResults": obj.get("canViewSyntheticTestResults"),
            "canViewSyntheticTests": obj.get("canViewSyntheticTests"),
            "canViewTraceDetails": obj.get("canViewTraceDetails"),
            "createdBy": obj.get("createdBy"),
            "createdOn": obj.get("createdOn"),
            "expiresOn": obj.get("expiresOn"),
            "id": obj.get("id"),
            "internalId": obj.get("internalId"),
            "lastUsedOn": obj.get("lastUsedOn"),
            "limitedApplicationsScope": obj.get("limitedApplicationsScope"),
            "limitedAutomationScope": obj.get("limitedAutomationScope"),
            "limitedBizOpsScope": obj.get("limitedBizOpsScope"),
            "limitedInfrastructureScope": obj.get("limitedInfrastructureScope"),
            "limitedKubernetesScope": obj.get("limitedKubernetesScope"),
            "limitedLogsScope": obj.get("limitedLogsScope"),
            "limitedMobileAppsScope": obj.get("limitedMobileAppsScope"),
            "limitedNutanixScope": obj.get("limitedNutanixScope"),
            "limitedOpenstackScope": obj.get("limitedOpenstackScope"),
            "limitedPcfScope": obj.get("limitedPcfScope"),
            "limitedPhmcScope": obj.get("limitedPhmcScope"),
            "limitedPvcScope": obj.get("limitedPvcScope"),
            "limitedSyntheticsScope": obj.get("limitedSyntheticsScope"),
            "limitedVsphereScope": obj.get("limitedVsphereScope"),
            "limitedWebsitesScope": obj.get("limitedWebsitesScope"),
            "limitedZhmcScope": obj.get("limitedZhmcScope"),
            "name": obj.get("name")
        })
        return _obj


