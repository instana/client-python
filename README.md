# openapi-client
Searching for answers and best pratices? Check our [IBM Instana Community](https://community.ibm.com/community/user/aiops/communities/community-home?CommunityKey=58f324a3-3104-41be-9510-5b7c413cc48f).

## Overview
The Instana REST API provides programmatic access to the Instana platform. It can be used to retrieve data available through the Instana UI Dashboard -- metrics, events, traces, etc -- and also to automate configuration tasks such as user management.

### Navigating the API documentation
The API endpoints are grouped by product area and functionality. This generally maps to how our UI Dashboard is organized, hopefully making it easier to locate which endpoints you'd use to fetch the data you see visualized in our UI. The [UI sections](https://www.ibm.com/docs/en/instana-observability/current?topic=working-user-interface#navigation-menu) include:
- Websites & Mobile Apps
- Applications
- Infrastructure
- Synthetic Monitoring
- Events
- Automation
- Service Levels
- Settings
- etc

### Rate Limiting
A rate limit is applied to API usage. Up to 5,000 calls per hour can be made. How many remaining calls can be made and when this call limit resets, can inspected via three headers that are part of the responses of the API server.

- **X-RateLimit-Limit:** Shows the maximum number of calls that may be executed per hour.
- **X-RateLimit-Remaining:** How many calls may still be executed within the current hour.
- **X-RateLimit-Reset:** Time when the remaining calls will be reset to the limit. For compatibility reasons with other rate limited APIs, this date is not the date in milliseconds, but instead in seconds since 1970-01-01T00:00:00+00:00.

### Further Reading
We provide additional documentation for our REST API in our [product documentation](https://www.ibm.com/docs/en/instana-observability/current?topic=apis-web-rest-api). Here you'll also find some common queries for retrieving data and configuring Instana.

## Getting Started with the REST API

### API base URL
The base URL for an specific instance of Instana can be determined using the tenant and unit information.
- `base`: This is the base URL of a tenant unit, e.g. `https://test-example.instana.io`. This is the same URL that is used to access the Instana user interface.
- `apiToken`: Requests against the Instana API require valid API tokens. An initial API token can be generated via the Instana user interface. Any additional API tokens can be generated via the API itself.

### Curl Example
Here is an Example to use the REST API with Curl. First lets get all the available metrics with possible aggregations with a GET call.

```bash
curl --request GET \\
  --url https://test-instana.instana.io/api/application-monitoring/catalog/metrics \\
  --header 'authorization: apiToken xxxxxxxxxxxxxxxx'
```

Next we can get every call grouped by the endpoint name that has an error count greater then zero. As a metric we could get the mean error rate for example.

```bash
curl --request POST \\
  --url https://test-instana.instana.io/api/application-monitoring/analyze/call-groups \\
  --header 'authorization: apiToken xxxxxxxxxxxxxxxx' \\
  --header 'content-type: application/json' \\
  --data '{
  \"group\":{
      \"groupbyTag\":\"endpoint.name\"
  },
  \"tagFilters\":[
   {
    \"name\":\"call.error.count\",
    \"value\":\"0\",
    \"operator\":\"GREATER_THAN\"
   }
  ],
  \"metrics\":[
   {
    \"metric\":\"errors\",
    \"aggregation\":\"MEAN\"
   }
  ]
  }'
```

### Generating REST API clients

The API is specified using the [OpenAPI v3](https://github.com/OAI/OpenAPI-Specification) (previously known as Swagger) format.
You can download the current specification at our [GitHub API documentation](https://instana.github.io/openapi/openapi.yaml).

OpenAPI tries to solve the issue of ever-evolving APIs and clients lagging behind. Please make sure that you always use the latest version of the generator, as a number of improvements are regularly made.
To generate a client library for your language, you can use the [OpenAPI client generators](https://github.com/OpenAPITools/openapi-generator).

#### Go
For example, to generate a client library for Go to interact with our backend, you can use the following script; mind replacing the values of the `UNIT_NAME` and `TENANT_NAME` environment variables using those for your tenant unit:

```bash
#!/bin/bash

### This script assumes you have the `java` and `wget` commands on the path

export UNIT_NAME='myunit' # for example: prod
export TENANT_NAME='mytenant' # for example: awesomecompany

//Download the generator to your current working directory:
wget https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/4.3.1/openapi-generator-cli-4.3.1.jar -O openapi-generator-cli.jar --server-variables \"tenant=${TENANT_NAME},unit=${UNIT_NAME}\"

//generate a client library that you can vendor into your repository
java -jar openapi-generator-cli.jar generate -i https://instana.github.io/openapi/openapi.yaml -g go \\
    -o pkg/instana/openapi \\
    --skip-validate-spec

//(optional) format the Go code according to the Go code standard
gofmt -s -w pkg/instana/openapi
```

The generated clients contain comprehensive READMEs, and you can start right away using the client from the example above:

```go
import instana \"./pkg/instana/openapi\"

// readTags will read all available application monitoring tags along with their type and category
func readTags() {
 configuration := instana.NewConfiguration()
 configuration.Host = \"tenant-unit.instana.io\"
 configuration.BasePath = \"https://tenant-unit.instana.io\"

 client := instana.NewAPIClient(configuration)
 auth := context.WithValue(context.Background(), instana.ContextAPIKey, instana.APIKey{
  Key:    apiKey,
  Prefix: \"apiToken\",
 })

 tags, _, err := client.ApplicationCatalogApi.GetApplicationTagCatalog(auth)
 if err != nil {
  fmt.Fatalf(\"Error calling the API, aborting.\")
 }

 for _, tag := range tags {
  fmt.Printf(\"%s (%s): %s\\n\", tag.Category, tag.Type, tag.Name)
 }
}
```

#### Java
Follow the instructions provided in the official documentation from [OpenAPI Tools](https://github.com/OpenAPITools) to download the [openapi-generator-cli.jar](https://github.com/OpenAPITools/openapi-generator?tab=readme-ov-file#13---download-jar).

Depending on your environment, use one of the following java http client implementations which will create a valid client for our OpenAPI specification:
```
//Nativ Java HTTP Client
java -jar openapi-generator-cli.jar generate -i https://instana.github.io/openapi/openapi.yaml -g java -o pkg/instana/openapi --skip-validate-spec  -p dateLibrary=java8 --library native

//Spring WebClient
java -jar openapi-generator-cli.jar generate -i https://instana.github.io/openapi/openapi.yaml -g java -o pkg/instana/openapi --skip-validate-spec  -p dateLibrary=java8,hideGenerationTimestamp=true --library webclient

//Spring RestTemplate
java -jar openapi-generator-cli.jar generate -i https://instana.github.io/openapi/openapi.yaml -g java -o pkg/instana/openapi --skip-validate-spec  -p dateLibrary=java8,hideGenerationTimestamp=true --library resttemplate

```


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.291.1002
- Package version: 1.0.0
- Generator version: 7.11.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [http://instana.com](http://instana.com)

## Requirements.

Python 3.8+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import instana_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import instana_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import instana_client
from instana_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://unit-tenant.instana.io
# See configuration.py for a list of all supported configuration parameters.
configuration = instana_client.Configuration(
    host = "https://unit-tenant.instana.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'


# Enter a context with an instance of the API client
with instana_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = instana_client.APITokenApi(api_client)
    internal_id = 'internal_id_example' # str | 

    try:
        # Delete API token
        api_instance.delete_api_token(internal_id)
    except ApiException as e:
        print("Exception when calling APITokenApi->delete_api_token: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://unit-tenant.instana.io*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*APITokenApi* | [**delete_api_token**](docs/APITokenApi.md#delete_api_token) | **DELETE** /api/settings/api-tokens/{internalId} | Delete API token
*APITokenApi* | [**get_api_token**](docs/APITokenApi.md#get_api_token) | **GET** /api/settings/api-tokens/{internalId} | Get API token
*APITokenApi* | [**get_api_tokens**](docs/APITokenApi.md#get_api_tokens) | **GET** /api/settings/api-tokens | Get all API Tokens
*APITokenApi* | [**post_api_token**](docs/APITokenApi.md#post_api_token) | **POST** /api/settings/api-tokens | Create an API token
*APITokenApi* | [**put_api_token**](docs/APITokenApi.md#put_api_token) | **PUT** /api/settings/api-tokens/{internalId} | Create or update an API token
*ActionCatalogApi* | [**get_action_by_id**](docs/ActionCatalogApi.md#get_action_by_id) | **GET** /api/automation/actions/{id} | Get an automation action by ID.
*ActionCatalogApi* | [**get_action_matches**](docs/ActionCatalogApi.md#get_action_matches) | **POST** /api/automation/ai/action/match | Get automation actions that match the incidents or issues.
*ActionCatalogApi* | [**get_actions**](docs/ActionCatalogApi.md#get_actions) | **GET** /api/automation/actions | Get all automation actions.
*ActionCatalogApi* | [**get_dynamic_parameters_tag_catalog**](docs/ActionCatalogApi.md#get_dynamic_parameters_tag_catalog) | **GET** /api/automation/parameters/dynamic/catalog | Get tag catalog for dynamic parameters
*ActionCatalogApi* | [**resolve**](docs/ActionCatalogApi.md#resolve) | **PUT** /api/automation/parameters/dynamic | Resolve dynamic parameter values
*ActionHistoryApi* | [**add_action_instance**](docs/ActionHistoryApi.md#add_action_instance) | **POST** /api/automation/actioninstances | Run an automation action.
*ActionHistoryApi* | [**delete_action_instance**](docs/ActionHistoryApi.md#delete_action_instance) | **DELETE** /api/automation/actioninstances/{actionInstanceId} | Deletes an automation action run result from the action run history by ID.
*ActionHistoryApi* | [**delete_action_instances**](docs/ActionHistoryApi.md#delete_action_instances) | **DELETE** /api/automation/actioninstances | Delete automation action run results.
*ActionHistoryApi* | [**get_action_instance**](docs/ActionHistoryApi.md#get_action_instance) | **GET** /api/automation/actioninstances/{actionInstanceId} | Get the details of an automation action run result by ID from action run history.
*ActionHistoryApi* | [**get_action_instances**](docs/ActionHistoryApi.md#get_action_instances) | **GET** /api/automation/actioninstances | Get the details of automation action run results from action run history.
*ApdexReportApi* | [**get_apdex_report**](docs/ApdexReportApi.md#get_apdex_report) | **GET** /api/apdex/report/{apdexId} | Generate Apdex report
*ApdexSettingsApi* | [**create_apdex_configuration**](docs/ApdexSettingsApi.md#create_apdex_configuration) | **POST** /api/settings/apdex | Create Apdex Configuration
*ApdexSettingsApi* | [**delete_apdex_configuration**](docs/ApdexSettingsApi.md#delete_apdex_configuration) | **DELETE** /api/settings/apdex/{id} | Delete Apdex Configuration
*ApdexSettingsApi* | [**get_all_apdex_configurations**](docs/ApdexSettingsApi.md#get_all_apdex_configurations) | **GET** /api/settings/apdex | Get All Apdex Configurations
*ApdexSettingsApi* | [**get_apdex_configuration**](docs/ApdexSettingsApi.md#get_apdex_configuration) | **GET** /api/settings/apdex/{id} | Get Apdex Configuration
*ApdexSettingsApi* | [**get_apdex_configurations_for_entity_type_and_id**](docs/ApdexSettingsApi.md#get_apdex_configurations_for_entity_type_and_id) | **GET** /api/settings/apdex/{entityType}/{entityId} | Get all Apdex configurations for entity type and entity id
*ApplicationAlertConfigurationApi* | [**create_application_alert_config**](docs/ApplicationAlertConfigurationApi.md#create_application_alert_config) | **POST** /api/events/settings/application-alert-configs | Create Smart Alert Config
*ApplicationAlertConfigurationApi* | [**delete_application_alert_config**](docs/ApplicationAlertConfigurationApi.md#delete_application_alert_config) | **DELETE** /api/events/settings/application-alert-configs/{id} | Delete Smart Alert Config
*ApplicationAlertConfigurationApi* | [**disable_application_alert_config**](docs/ApplicationAlertConfigurationApi.md#disable_application_alert_config) | **PUT** /api/events/settings/application-alert-configs/{id}/disable | Disable Smart Alert Config
*ApplicationAlertConfigurationApi* | [**enable_application_alert_config**](docs/ApplicationAlertConfigurationApi.md#enable_application_alert_config) | **PUT** /api/events/settings/application-alert-configs/{id}/enable | Enable Application Alert Config
*ApplicationAlertConfigurationApi* | [**find_active_application_alert_configs**](docs/ApplicationAlertConfigurationApi.md#find_active_application_alert_configs) | **GET** /api/events/settings/application-alert-configs | Get all Smart Alert Configs
*ApplicationAlertConfigurationApi* | [**find_application_alert_config**](docs/ApplicationAlertConfigurationApi.md#find_application_alert_config) | **GET** /api/events/settings/application-alert-configs/{id} | Get Smart Alert Config
*ApplicationAlertConfigurationApi* | [**find_application_alert_config_versions**](docs/ApplicationAlertConfigurationApi.md#find_application_alert_config_versions) | **GET** /api/events/settings/application-alert-configs/{id}/versions | Get Smart Alert Config Versions
*ApplicationAlertConfigurationApi* | [**restore_application_alert_config**](docs/ApplicationAlertConfigurationApi.md#restore_application_alert_config) | **PUT** /api/events/settings/application-alert-configs/{id}/restore/{created} | Restore Smart Alert Config
*ApplicationAlertConfigurationApi* | [**update_application_alert_config**](docs/ApplicationAlertConfigurationApi.md#update_application_alert_config) | **POST** /api/events/settings/application-alert-configs/{id} | Update Smart Alert Config
*ApplicationAlertConfigurationApi* | [**update_application_historic_baseline**](docs/ApplicationAlertConfigurationApi.md#update_application_historic_baseline) | **POST** /api/events/settings/application-alert-configs/{id}/update-baseline | Recalculate Smart Alert Config Baseline
*ApplicationAnalyzeApi* | [**get_call_details**](docs/ApplicationAnalyzeApi.md#get_call_details) | **GET** /api/application-monitoring/v2/analyze/traces/{traceId}/calls/{callId}/details | Get call detail
*ApplicationAnalyzeApi* | [**get_call_group**](docs/ApplicationAnalyzeApi.md#get_call_group) | **POST** /api/application-monitoring/analyze/call-groups | Get grouped call metrics
*ApplicationAnalyzeApi* | [**get_correlated_traces**](docs/ApplicationAnalyzeApi.md#get_correlated_traces) | **GET** /api/application-monitoring/analyze/backend-correlation | Resolve Trace IDs from Monitoring Beacons.
*ApplicationAnalyzeApi* | [**get_trace**](docs/ApplicationAnalyzeApi.md#get_trace) | **GET** /api/application-monitoring/analyze/traces/{id} | Get trace detail
*ApplicationAnalyzeApi* | [**get_trace_download**](docs/ApplicationAnalyzeApi.md#get_trace_download) | **GET** /api/application-monitoring/v2/analyze/traces/{id} | Get trace detail
*ApplicationAnalyzeApi* | [**get_trace_groups**](docs/ApplicationAnalyzeApi.md#get_trace_groups) | **POST** /api/application-monitoring/analyze/trace-groups | Get grouped trace metrics
*ApplicationAnalyzeApi* | [**get_traces**](docs/ApplicationAnalyzeApi.md#get_traces) | **POST** /api/application-monitoring/analyze/traces | Get all traces
*ApplicationCatalogApi* | [**get_application_catalog_metrics**](docs/ApplicationCatalogApi.md#get_application_catalog_metrics) | **GET** /api/application-monitoring/catalog/metrics | Get Metric catalog
*ApplicationCatalogApi* | [**get_application_tag_catalog**](docs/ApplicationCatalogApi.md#get_application_tag_catalog) | **GET** /api/application-monitoring/catalog | Get application tag catalog
*ApplicationCatalogApi* | [**get_application_tags**](docs/ApplicationCatalogApi.md#get_application_tags) | **GET** /api/application-monitoring/catalog/tags | Get application tags
*ApplicationMetricsApi* | [**get_application_data_metrics_v2**](docs/ApplicationMetricsApi.md#get_application_data_metrics_v2) | **POST** /api/application-monitoring/v2/metrics | Get Application Data Metrics
*ApplicationMetricsApi* | [**get_application_metrics**](docs/ApplicationMetricsApi.md#get_application_metrics) | **POST** /api/application-monitoring/metrics/applications | Get Application Metrics
*ApplicationMetricsApi* | [**get_endpoints_metrics**](docs/ApplicationMetricsApi.md#get_endpoints_metrics) | **POST** /api/application-monitoring/metrics/endpoints | Get Endpoint metrics
*ApplicationMetricsApi* | [**get_services_metrics**](docs/ApplicationMetricsApi.md#get_services_metrics) | **POST** /api/application-monitoring/metrics/services | Get Service metrics
*ApplicationResourcesApi* | [**get_application_endpoints**](docs/ApplicationResourcesApi.md#get_application_endpoints) | **GET** /api/application-monitoring/applications/services/endpoints | Get endpoints
*ApplicationResourcesApi* | [**get_application_services**](docs/ApplicationResourcesApi.md#get_application_services) | **GET** /api/application-monitoring/applications/services | Get applications/services
*ApplicationResourcesApi* | [**get_applications**](docs/ApplicationResourcesApi.md#get_applications) | **GET** /api/application-monitoring/applications | Get applications
*ApplicationResourcesApi* | [**get_services**](docs/ApplicationResourcesApi.md#get_services) | **GET** /api/application-monitoring/services | Get services
*ApplicationSettingsApi* | [**add_application_config**](docs/ApplicationSettingsApi.md#add_application_config) | **POST** /api/application-monitoring/settings/application | Add application configuration
*ApplicationSettingsApi* | [**add_manual_service_config**](docs/ApplicationSettingsApi.md#add_manual_service_config) | **POST** /api/application-monitoring/settings/manual-service | Add manual service configuration
*ApplicationSettingsApi* | [**add_service_config**](docs/ApplicationSettingsApi.md#add_service_config) | **POST** /api/application-monitoring/settings/service | Add service configuration
*ApplicationSettingsApi* | [**create_endpoint_config**](docs/ApplicationSettingsApi.md#create_endpoint_config) | **POST** /api/application-monitoring/settings/endpoint | Create endpoint configuration
*ApplicationSettingsApi* | [**create_http_endpoint_config**](docs/ApplicationSettingsApi.md#create_http_endpoint_config) | **POST** /api/application-monitoring/settings/http-endpoint | Create HTTP endpoint configuration
*ApplicationSettingsApi* | [**delete_application_config**](docs/ApplicationSettingsApi.md#delete_application_config) | **DELETE** /api/application-monitoring/settings/application/{id} | Delete application configuration
*ApplicationSettingsApi* | [**delete_endpoint_config**](docs/ApplicationSettingsApi.md#delete_endpoint_config) | **DELETE** /api/application-monitoring/settings/endpoint/{id} | Delete endpoint configuration
*ApplicationSettingsApi* | [**delete_http_endpoint_config**](docs/ApplicationSettingsApi.md#delete_http_endpoint_config) | **DELETE** /api/application-monitoring/settings/http-endpoint/{id} | Delete HTTP endpoint configuration
*ApplicationSettingsApi* | [**delete_manual_service_config**](docs/ApplicationSettingsApi.md#delete_manual_service_config) | **DELETE** /api/application-monitoring/settings/manual-service/{id} | Delete manual service configuration
*ApplicationSettingsApi* | [**delete_service_config**](docs/ApplicationSettingsApi.md#delete_service_config) | **DELETE** /api/application-monitoring/settings/service/{id} | Delete service configuration
*ApplicationSettingsApi* | [**get_all_manual_service_configs**](docs/ApplicationSettingsApi.md#get_all_manual_service_configs) | **GET** /api/application-monitoring/settings/manual-service | All manual service configurations
*ApplicationSettingsApi* | [**get_application_config**](docs/ApplicationSettingsApi.md#get_application_config) | **GET** /api/application-monitoring/settings/application/{id} | Application configuration
*ApplicationSettingsApi* | [**get_application_configs**](docs/ApplicationSettingsApi.md#get_application_configs) | **GET** /api/application-monitoring/settings/application | All Application configurations
*ApplicationSettingsApi* | [**get_endpoint_config**](docs/ApplicationSettingsApi.md#get_endpoint_config) | **GET** /api/application-monitoring/settings/endpoint/{id} | Endpoint configuration
*ApplicationSettingsApi* | [**get_endpoint_configs**](docs/ApplicationSettingsApi.md#get_endpoint_configs) | **GET** /api/application-monitoring/settings/endpoint | All Endpoint configurations
*ApplicationSettingsApi* | [**get_http_endpoint_config**](docs/ApplicationSettingsApi.md#get_http_endpoint_config) | **GET** /api/application-monitoring/settings/http-endpoint/{id} | HTTP Endpoint configuration
*ApplicationSettingsApi* | [**get_http_endpoint_configs**](docs/ApplicationSettingsApi.md#get_http_endpoint_configs) | **GET** /api/application-monitoring/settings/http-endpoint | All HTTP endpoint configurations
*ApplicationSettingsApi* | [**get_service_config**](docs/ApplicationSettingsApi.md#get_service_config) | **GET** /api/application-monitoring/settings/service/{id} | Service configuration
*ApplicationSettingsApi* | [**get_service_configs**](docs/ApplicationSettingsApi.md#get_service_configs) | **GET** /api/application-monitoring/settings/service | All service configurations
*ApplicationSettingsApi* | [**order_service_config**](docs/ApplicationSettingsApi.md#order_service_config) | **PUT** /api/application-monitoring/settings/service/order | Order of service configuration
*ApplicationSettingsApi* | [**put_application_config**](docs/ApplicationSettingsApi.md#put_application_config) | **PUT** /api/application-monitoring/settings/application/{id} | Update application configuration
*ApplicationSettingsApi* | [**put_service_config**](docs/ApplicationSettingsApi.md#put_service_config) | **PUT** /api/application-monitoring/settings/service/{id} | Update service configuration
*ApplicationSettingsApi* | [**replace_all**](docs/ApplicationSettingsApi.md#replace_all) | **PUT** /api/application-monitoring/settings/service | Replace all service configurations
*ApplicationSettingsApi* | [**replace_all_manual_service_configs**](docs/ApplicationSettingsApi.md#replace_all_manual_service_configs) | **PUT** /api/application-monitoring/settings/manual-service | Replace all manual service configurations
*ApplicationSettingsApi* | [**update_endpoint_config**](docs/ApplicationSettingsApi.md#update_endpoint_config) | **PUT** /api/application-monitoring/settings/endpoint/{id} | Update endpoint configuration
*ApplicationSettingsApi* | [**update_http_endpoint_config**](docs/ApplicationSettingsApi.md#update_http_endpoint_config) | **PUT** /api/application-monitoring/settings/http-endpoint/{id} | Update HTTP endpoint configuration
*ApplicationSettingsApi* | [**update_manual_service_config**](docs/ApplicationSettingsApi.md#update_manual_service_config) | **PUT** /api/application-monitoring/settings/manual-service/{id} | Update manual service configuration
*ApplicationTopologyApi* | [**get_services_map**](docs/ApplicationTopologyApi.md#get_services_map) | **GET** /api/application-monitoring/topology/services | Gets the service topology
*AuditLogApi* | [**get_access_logs**](docs/AuditLogApi.md#get_access_logs) | **GET** /api/settings/accesslog | Access log
*AuditLogApi* | [**get_audit_logs**](docs/AuditLogApi.md#get_audit_logs) | **GET** /api/settings/auditlog | Audit log
*AuthenticationApi* | [**delete_google_sso_config**](docs/AuthenticationApi.md#delete_google_sso_config) | **DELETE** /api/settings/authentication/googleSSO | Delete Google SSO configuration
*AuthenticationApi* | [**delete_ldap_config**](docs/AuthenticationApi.md#delete_ldap_config) | **DELETE** /api/settings/authentication/ldap | Delete LDAP configuration
*AuthenticationApi* | [**delete_oidc_config**](docs/AuthenticationApi.md#delete_oidc_config) | **DELETE** /api/settings/authentication/oidc | Delete OIDC configuration
*AuthenticationApi* | [**delete_saml_config**](docs/AuthenticationApi.md#delete_saml_config) | **DELETE** /api/settings/authentication/saml | Delete SAML configuration
*BusinessMonitoringApi* | [**create_business_perspective**](docs/BusinessMonitoringApi.md#create_business_perspective) | **POST** /api/business-monitoring/business-perspectives | Create business perspective
*BusinessMonitoringApi* | [**delete_business_perspective**](docs/BusinessMonitoringApi.md#delete_business_perspective) | **DELETE** /api/business-monitoring/business-perspectives/{id} | Delete business perspective
*BusinessMonitoringApi* | [**get_activities**](docs/BusinessMonitoringApi.md#get_activities) | **POST** /api/business-monitoring/activities | Get Business Activities
*BusinessMonitoringApi* | [**get_activities_csv**](docs/BusinessMonitoringApi.md#get_activities_csv) | **POST** /api/business-monitoring/activities/csv | Download Business Activities
*BusinessMonitoringApi* | [**get_business_perspective**](docs/BusinessMonitoringApi.md#get_business_perspective) | **GET** /api/business-monitoring/business-perspectives/{id} | Get business perspective
*BusinessMonitoringApi* | [**get_business_perspectives**](docs/BusinessMonitoringApi.md#get_business_perspectives) | **GET** /api/business-monitoring/business-perspectives | Get all business perspectives
*BusinessMonitoringApi* | [**get_business_tag_catalog**](docs/BusinessMonitoringApi.md#get_business_tag_catalog) | **GET** /api/business-monitoring/catalog | Get business tag catalog
*BusinessMonitoringApi* | [**update_business_perspective**](docs/BusinessMonitoringApi.md#update_business_perspective) | **PUT** /api/business-monitoring/business-perspectives/{id} | Update business perspective
*CustomDashboardsApi* | [**add_custom_dashboard**](docs/CustomDashboardsApi.md#add_custom_dashboard) | **POST** /api/custom-dashboard | Add custom dashboard
*CustomDashboardsApi* | [**delete_custom_dashboard**](docs/CustomDashboardsApi.md#delete_custom_dashboard) | **DELETE** /api/custom-dashboard/{customDashboardId} | Remove custom dashboard
*CustomDashboardsApi* | [**get_custom_dashboard**](docs/CustomDashboardsApi.md#get_custom_dashboard) | **GET** /api/custom-dashboard/{customDashboardId} | Get custom dashboard
*CustomDashboardsApi* | [**get_custom_dashboards**](docs/CustomDashboardsApi.md#get_custom_dashboards) | **GET** /api/custom-dashboard | Get accessible custom dashboards
*CustomDashboardsApi* | [**get_shareable_api_tokens**](docs/CustomDashboardsApi.md#get_shareable_api_tokens) | **GET** /api/custom-dashboard/shareable-api-tokens | Get all API tokens.
*CustomDashboardsApi* | [**get_shareable_users**](docs/CustomDashboardsApi.md#get_shareable_users) | **GET** /api/custom-dashboard/shareable-users | Get all users (without invitations).
*CustomDashboardsApi* | [**update_custom_dashboard**](docs/CustomDashboardsApi.md#update_custom_dashboard) | **PUT** /api/custom-dashboard/{customDashboardId} | Update custom dashboard
*EventSettingsApi* | [**create_mobile_app_alert_config**](docs/EventSettingsApi.md#create_mobile_app_alert_config) | **POST** /api/events/settings/mobile-app-alert-configs | Create Mobile Smart Alert Config
*EventSettingsApi* | [**create_website_alert_config**](docs/EventSettingsApi.md#create_website_alert_config) | **POST** /api/events/settings/website-alert-configs | Create Website Smart Alert Config
*EventSettingsApi* | [**delete_alert**](docs/EventSettingsApi.md#delete_alert) | **DELETE** /api/events/settings/alerts/{id} | Delete Alert Configuration
*EventSettingsApi* | [**delete_alerting_channel**](docs/EventSettingsApi.md#delete_alerting_channel) | **DELETE** /api/events/settings/alertingChannels/{id} | Delete Alerting Channel
*EventSettingsApi* | [**delete_built_in_event_specification**](docs/EventSettingsApi.md#delete_built_in_event_specification) | **DELETE** /api/events/settings/event-specifications/built-in/{eventSpecificationId} | Delete built-in event specification
*EventSettingsApi* | [**delete_custom_event_specification**](docs/EventSettingsApi.md#delete_custom_event_specification) | **DELETE** /api/events/settings/event-specifications/custom/{eventSpecificationId} | Delete custom event specification
*EventSettingsApi* | [**delete_custom_payload_configuration**](docs/EventSettingsApi.md#delete_custom_payload_configuration) | **DELETE** /api/events/settings/custom-payload-configurations | Delete Custom Payload Configuration
*EventSettingsApi* | [**delete_mobile_app_alert_config**](docs/EventSettingsApi.md#delete_mobile_app_alert_config) | **DELETE** /api/events/settings/mobile-app-alert-configs/{id} | Delete Mobile Smart Alert Config
*EventSettingsApi* | [**delete_website_alert_config**](docs/EventSettingsApi.md#delete_website_alert_config) | **DELETE** /api/events/settings/website-alert-configs/{id} | Delete Website Smart Alert Config
*EventSettingsApi* | [**disable_built_in_event_specification**](docs/EventSettingsApi.md#disable_built_in_event_specification) | **POST** /api/events/settings/event-specifications/built-in/{eventSpecificationId}/disable | Disable built-in event specification
*EventSettingsApi* | [**disable_custom_event_specification**](docs/EventSettingsApi.md#disable_custom_event_specification) | **POST** /api/events/settings/event-specifications/custom/{eventSpecificationId}/disable | Disable custom event specification
*EventSettingsApi* | [**disable_mobile_app_alert_config**](docs/EventSettingsApi.md#disable_mobile_app_alert_config) | **PUT** /api/events/settings/mobile-app-alert-configs/{id}/disable | Disable Mobile Smart Alert Config
*EventSettingsApi* | [**disable_website_alert_config**](docs/EventSettingsApi.md#disable_website_alert_config) | **PUT** /api/events/settings/website-alert-configs/{id}/disable | Disable Website Smart Alert Config
*EventSettingsApi* | [**enable_built_in_event_specification**](docs/EventSettingsApi.md#enable_built_in_event_specification) | **POST** /api/events/settings/event-specifications/built-in/{eventSpecificationId}/enable | Enable built-in event specification
*EventSettingsApi* | [**enable_custom_event_specification**](docs/EventSettingsApi.md#enable_custom_event_specification) | **POST** /api/events/settings/event-specifications/custom/{eventSpecificationId}/enable | Enable custom event specification
*EventSettingsApi* | [**enable_mobile_app_alert_config**](docs/EventSettingsApi.md#enable_mobile_app_alert_config) | **PUT** /api/events/settings/mobile-app-alert-configs/{id}/enable | Enable Mobile Smart Alert Config
*EventSettingsApi* | [**enable_website_alert_config**](docs/EventSettingsApi.md#enable_website_alert_config) | **PUT** /api/events/settings/website-alert-configs/{id}/enable | Enable Website Smart Alert Config
*EventSettingsApi* | [**find_active_mobile_app_alert_configs**](docs/EventSettingsApi.md#find_active_mobile_app_alert_configs) | **GET** /api/events/settings/mobile-app-alert-configs | Get all Mobile Smart Alert Configs
*EventSettingsApi* | [**find_active_website_alert_configs**](docs/EventSettingsApi.md#find_active_website_alert_configs) | **GET** /api/events/settings/website-alert-configs | Get all Website Smart Alert Configs
*EventSettingsApi* | [**find_mobile_app_alert_config**](docs/EventSettingsApi.md#find_mobile_app_alert_config) | **GET** /api/events/settings/mobile-app-alert-configs/{id} | Get Mobile Smart Alert Config
*EventSettingsApi* | [**find_mobile_app_alert_config_versions**](docs/EventSettingsApi.md#find_mobile_app_alert_config_versions) | **GET** /api/events/settings/mobile-app-alert-configs/{id}/versions | Get Mobile Smart Alert Config Versions
*EventSettingsApi* | [**find_website_alert_config**](docs/EventSettingsApi.md#find_website_alert_config) | **GET** /api/events/settings/website-alert-configs/{id} | Get Website Smart Alert Config
*EventSettingsApi* | [**find_website_alert_config_versions**](docs/EventSettingsApi.md#find_website_alert_config_versions) | **GET** /api/events/settings/website-alert-configs/{id}/versions | Get Website Smart Alert Config Versions. 
*EventSettingsApi* | [**get_alert**](docs/EventSettingsApi.md#get_alert) | **GET** /api/events/settings/alerts/{id} | Get Alert Configuration
*EventSettingsApi* | [**get_alerting_channel**](docs/EventSettingsApi.md#get_alerting_channel) | **GET** /api/events/settings/alertingChannels/{id} | Get Alerting Channel
*EventSettingsApi* | [**get_alerting_channels**](docs/EventSettingsApi.md#get_alerting_channels) | **GET** /api/events/settings/alertingChannels | Get all Alerting Channels
*EventSettingsApi* | [**get_alerting_channels_overview**](docs/EventSettingsApi.md#get_alerting_channels_overview) | **GET** /api/events/settings/alertingChannels/infos | Get Overview of Alerting Channels
*EventSettingsApi* | [**get_alerting_configuration_infos**](docs/EventSettingsApi.md#get_alerting_configuration_infos) | **GET** /api/events/settings/alerts/infos | All alerting configuration info
*EventSettingsApi* | [**get_alerts**](docs/EventSettingsApi.md#get_alerts) | **GET** /api/events/settings/alerts | Get all Alert Configurations
*EventSettingsApi* | [**get_built_in_event_specification**](docs/EventSettingsApi.md#get_built_in_event_specification) | **GET** /api/events/settings/event-specifications/built-in/{eventSpecificationId} | Built-in event specifications
*EventSettingsApi* | [**get_built_in_event_specifications**](docs/EventSettingsApi.md#get_built_in_event_specifications) | **GET** /api/events/settings/event-specifications/built-in | All built-in event specification
*EventSettingsApi* | [**get_custom_event_specification**](docs/EventSettingsApi.md#get_custom_event_specification) | **GET** /api/events/settings/event-specifications/custom/{eventSpecificationId} | Custom event specification
*EventSettingsApi* | [**get_custom_event_specifications**](docs/EventSettingsApi.md#get_custom_event_specifications) | **GET** /api/events/settings/event-specifications/custom | All custom event specifications
*EventSettingsApi* | [**get_custom_payload_configurations**](docs/EventSettingsApi.md#get_custom_payload_configurations) | **GET** /api/events/settings/custom-payload-configurations | Get All Global Custom Payload Configurations
*EventSettingsApi* | [**get_custom_payload_tag_catalog**](docs/EventSettingsApi.md#get_custom_payload_tag_catalog) | **GET** /api/events/settings/custom-payload-configurations/catalog | Get Tag Catalog for Custom Payload
*EventSettingsApi* | [**get_event_specification_infos**](docs/EventSettingsApi.md#get_event_specification_infos) | **GET** /api/events/settings/event-specifications/infos | Summary of all built-in and custom event specifications
*EventSettingsApi* | [**get_event_specification_infos_by_ids**](docs/EventSettingsApi.md#get_event_specification_infos_by_ids) | **POST** /api/events/settings/event-specifications/infos | All built-in and custom event specifications
*EventSettingsApi* | [**get_system_rules**](docs/EventSettingsApi.md#get_system_rules) | **GET** /api/events/settings/event-specifications/custom/systemRules | All system rules for custom event specifications
*EventSettingsApi* | [**manually_close_event**](docs/EventSettingsApi.md#manually_close_event) | **POST** /api/events/settings/manual-close/{eventId} | Manually close an event.
*EventSettingsApi* | [**multi_close_event**](docs/EventSettingsApi.md#multi_close_event) | **POST** /api/events/settings/manual-close | Manually closing multiple events
*EventSettingsApi* | [**post_custom_event_specification**](docs/EventSettingsApi.md#post_custom_event_specification) | **POST** /api/events/settings/event-specifications/custom | Create new custom event specification
*EventSettingsApi* | [**put_alert**](docs/EventSettingsApi.md#put_alert) | **PUT** /api/events/settings/alerts/{id} | Create or update Alert Configuration
*EventSettingsApi* | [**put_alerting_channel**](docs/EventSettingsApi.md#put_alerting_channel) | **PUT** /api/events/settings/alertingChannels/{id} | Update Alert Channel
*EventSettingsApi* | [**put_custom_event_specification**](docs/EventSettingsApi.md#put_custom_event_specification) | **PUT** /api/events/settings/event-specifications/custom/{eventSpecificationId} | Create or update custom event specification
*EventSettingsApi* | [**restore_mobile_app_alert_config**](docs/EventSettingsApi.md#restore_mobile_app_alert_config) | **PUT** /api/events/settings/mobile-app-alert-configs/{id}/restore/{created} | Restore Mobile Smart Alert Config
*EventSettingsApi* | [**restore_website_alert_config**](docs/EventSettingsApi.md#restore_website_alert_config) | **PUT** /api/events/settings/website-alert-configs/{id}/restore/{created} | Restore Website Smart Alert Config
*EventSettingsApi* | [**send_test_alerting**](docs/EventSettingsApi.md#send_test_alerting) | **PUT** /api/events/settings/alertingChannels/test | Test Alerting Channel
*EventSettingsApi* | [**send_test_alerting_by_id**](docs/EventSettingsApi.md#send_test_alerting_by_id) | **POST** /api/events/settings/alertingChannels/notify/{id} | Notify manually to Alerting Channel
*EventSettingsApi* | [**update_mobile_app_alert_config**](docs/EventSettingsApi.md#update_mobile_app_alert_config) | **POST** /api/events/settings/mobile-app-alert-configs/{id} | Update Mobile Smart Alert Config
*EventSettingsApi* | [**update_mobile_app_historic_baseline**](docs/EventSettingsApi.md#update_mobile_app_historic_baseline) | **POST** /api/events/settings/mobile-app-alert-configs/{id}/update-baseline | Recalculate Mobile Smart Alert Config Baseline
*EventSettingsApi* | [**update_website_alert_config**](docs/EventSettingsApi.md#update_website_alert_config) | **POST** /api/events/settings/website-alert-configs/{id} | Update Website Smart Alert Config
*EventSettingsApi* | [**update_website_historic_baseline**](docs/EventSettingsApi.md#update_website_historic_baseline) | **POST** /api/events/settings/website-alert-configs/{id}/update-baseline | Recalculate Website Smart Alert Config Baseline
*EventSettingsApi* | [**upsert_custom_payload_configuration**](docs/EventSettingsApi.md#upsert_custom_payload_configuration) | **PUT** /api/events/settings/custom-payload-configurations | Create/Update Global Custom Payload Configuration
*EventsApi* | [**agent_monitoring_events**](docs/EventsApi.md#agent_monitoring_events) | **GET** /api/events/agent-monitoring-events | Get Agent Monitoring Events
*EventsApi* | [**get_event**](docs/EventsApi.md#get_event) | **GET** /api/events/{eventId} | Get Event
*EventsApi* | [**get_events**](docs/EventsApi.md#get_events) | **GET** /api/events | Get all Events
*EventsApi* | [**get_events_by_ids**](docs/EventsApi.md#get_events_by_ids) | **POST** /api/events | Get Events by IDs
*EventsApi* | [**kubernetes_info_events**](docs/EventsApi.md#kubernetes_info_events) | **GET** /api/events/kubernetes-info-events | Get Kubernetes Info Events
*GlobalApplicationAlertConfigurationApi* | [**create_global_application_alert_config**](docs/GlobalApplicationAlertConfigurationApi.md#create_global_application_alert_config) | **POST** /api/events/settings/global-alert-configs/applications | Create Global Smart Alert Config
*GlobalApplicationAlertConfigurationApi* | [**delete_global_application_alert_config**](docs/GlobalApplicationAlertConfigurationApi.md#delete_global_application_alert_config) | **DELETE** /api/events/settings/global-alert-configs/applications/{id} | Delete Global Smart Alert Config
*GlobalApplicationAlertConfigurationApi* | [**disable_global_application_alert_config**](docs/GlobalApplicationAlertConfigurationApi.md#disable_global_application_alert_config) | **PUT** /api/events/settings/global-alert-configs/applications/{id}/disable | Disable Global Smart Alert Config
*GlobalApplicationAlertConfigurationApi* | [**enable_global_application_alert_config**](docs/GlobalApplicationAlertConfigurationApi.md#enable_global_application_alert_config) | **PUT** /api/events/settings/global-alert-configs/applications/{id}/enable | Enable Global Smart Alert Config
*GlobalApplicationAlertConfigurationApi* | [**find_active_global_application_alert_configs**](docs/GlobalApplicationAlertConfigurationApi.md#find_active_global_application_alert_configs) | **GET** /api/events/settings/global-alert-configs/applications | Get all Global Smart Alert Configs
*GlobalApplicationAlertConfigurationApi* | [**find_global_application_alert_config**](docs/GlobalApplicationAlertConfigurationApi.md#find_global_application_alert_config) | **GET** /api/events/settings/global-alert-configs/applications/{id} | Get Global Smart Alert Config
*GlobalApplicationAlertConfigurationApi* | [**find_global_application_alert_config_versions**](docs/GlobalApplicationAlertConfigurationApi.md#find_global_application_alert_config_versions) | **GET** /api/events/settings/global-alert-configs/applications/{id}/versions | Get Global Smart Alert Config Versions
*GlobalApplicationAlertConfigurationApi* | [**restore_global_application_alert_config**](docs/GlobalApplicationAlertConfigurationApi.md#restore_global_application_alert_config) | **PUT** /api/events/settings/global-alert-configs/applications/{id}/restore/{created} | Restore Global Smart Alert Config
*GlobalApplicationAlertConfigurationApi* | [**update_global_application_alert_config**](docs/GlobalApplicationAlertConfigurationApi.md#update_global_application_alert_config) | **POST** /api/events/settings/global-alert-configs/applications/{id} | Update Global Smart Alert Config
*GroupsApi* | [**add_permissions_on_group**](docs/GroupsApi.md#add_permissions_on_group) | **PUT** /api/settings/rbac/groups/{groupId}/permissions | Add permissions to group
*GroupsApi* | [**add_users_to_group**](docs/GroupsApi.md#add_users_to_group) | **PUT** /api/settings/rbac/groups/{groupId}/users | Add users to group
*GroupsApi* | [**create_group**](docs/GroupsApi.md#create_group) | **POST** /api/settings/rbac/groups | Create group
*GroupsApi* | [**create_group_mapping**](docs/GroupsApi.md#create_group_mapping) | **POST** /api/settings/rbac/mappings | Create group mapping
*GroupsApi* | [**delete_group**](docs/GroupsApi.md#delete_group) | **DELETE** /api/settings/rbac/groups/{id} | Delete group
*GroupsApi* | [**delete_group_mapping**](docs/GroupsApi.md#delete_group_mapping) | **DELETE** /api/settings/rbac/mappings/{id} | Delete group mapping
*GroupsApi* | [**get_group**](docs/GroupsApi.md#get_group) | **GET** /api/settings/rbac/groups/{id} | Get group
*GroupsApi* | [**get_group_mappings**](docs/GroupsApi.md#get_group_mappings) | **GET** /api/settings/rbac/mappings | Get all group mappings
*GroupsApi* | [**get_groups**](docs/GroupsApi.md#get_groups) | **GET** /api/settings/rbac/groups | Get groups
*GroupsApi* | [**get_groups_by_user**](docs/GroupsApi.md#get_groups_by_user) | **GET** /api/settings/rbac/groups/user/{email} | Get groups of a single user
*GroupsApi* | [**get_identity_provider_patch**](docs/GroupsApi.md#get_identity_provider_patch) | **GET** /api/settings/rbac/mappings/identityProvider/restrictEmptyIdpGroups | Check user restrictions for empty Idp group mapping
*GroupsApi* | [**remove_user_from_group**](docs/GroupsApi.md#remove_user_from_group) | **DELETE** /api/settings/rbac/groups/{id}/user/{userId} | Remove user from group
*GroupsApi* | [**update_group**](docs/GroupsApi.md#update_group) | **PUT** /api/settings/rbac/groups/{id} | Update group
*GroupsApi* | [**update_group_mapping**](docs/GroupsApi.md#update_group_mapping) | **PUT** /api/settings/rbac/mappings/{id} | Update group mapping
*GroupsApi* | [**update_identity_provider**](docs/GroupsApi.md#update_identity_provider) | **PUT** /api/settings/rbac/mappings/identityProvider/restrictEmptyIdpGroups | Allow/Restrict users with empty Idp group mapping
*HealthApi* | [**get_health_state**](docs/HealthApi.md#get_health_state) | **GET** /api/instana/health | Basic health traffic light
*HealthApi* | [**get_version**](docs/HealthApi.md#get_version) | **GET** /api/instana/version | API version information
*HostAgentApi* | [**get_agent_logs**](docs/HostAgentApi.md#get_agent_logs) | **GET** /api/host-agent/{hostId}/logs | Agent download logs
*HostAgentApi* | [**get_agent_snapshot**](docs/HostAgentApi.md#get_agent_snapshot) | **GET** /api/host-agent/{id} | Get host agent snapshot details
*HostAgentApi* | [**get_agent_support_information**](docs/HostAgentApi.md#get_agent_support_information) | **GET** /api/host-agent/{hostId}/support-info | Agent download support information
*HostAgentApi* | [**search_host_agents**](docs/HostAgentApi.md#search_host_agents) | **GET** /api/host-agent | Query host agent snapshots
*HostAgentApi* | [**update_agent**](docs/HostAgentApi.md#update_agent) | **POST** /api/host-agent/{hostId}/update | Agent update
*HostAgentApi* | [**update_configuration_by_host**](docs/HostAgentApi.md#update_configuration_by_host) | **POST** /api/host-agent/{hostId}/configuration | Update agent configuration by host
*HostAgentApi* | [**update_configuration_by_query**](docs/HostAgentApi.md#update_configuration_by_query) | **POST** /api/host-agent/configuration | Update agent configuration by query
*InfrastructureAlertConfigurationApi* | [**create_infra_alert_config**](docs/InfrastructureAlertConfigurationApi.md#create_infra_alert_config) | **POST** /api/events/settings/infra-alert-configs | Create Infra Alert Config
*InfrastructureAlertConfigurationApi* | [**delete_infra_alert_config**](docs/InfrastructureAlertConfigurationApi.md#delete_infra_alert_config) | **DELETE** /api/events/settings/infra-alert-configs/{id} | Delete Infra Alert Config
*InfrastructureAlertConfigurationApi* | [**disable_infra_alert_config**](docs/InfrastructureAlertConfigurationApi.md#disable_infra_alert_config) | **PUT** /api/events/settings/infra-alert-configs/{id}/disable | Disable Infra Alert Config
*InfrastructureAlertConfigurationApi* | [**enable_infra_alert_config**](docs/InfrastructureAlertConfigurationApi.md#enable_infra_alert_config) | **PUT** /api/events/settings/infra-alert-configs/{id}/enable | Enable Infra Alert Config
*InfrastructureAlertConfigurationApi* | [**find_active_infra_alert_configs**](docs/InfrastructureAlertConfigurationApi.md#find_active_infra_alert_configs) | **GET** /api/events/settings/infra-alert-configs | All Infra Alert Configs
*InfrastructureAlertConfigurationApi* | [**find_infra_alert_config**](docs/InfrastructureAlertConfigurationApi.md#find_infra_alert_config) | **GET** /api/events/settings/infra-alert-configs/{id} | Get Infra Alert Config
*InfrastructureAlertConfigurationApi* | [**find_infra_alert_config_versions**](docs/InfrastructureAlertConfigurationApi.md#find_infra_alert_config_versions) | **GET** /api/events/settings/infra-alert-configs/{id}/versions | Get versions of Infra Alert Config
*InfrastructureAlertConfigurationApi* | [**restore_infra_alert_config**](docs/InfrastructureAlertConfigurationApi.md#restore_infra_alert_config) | **PUT** /api/events/settings/infra-alert-configs/{id}/restore/{created} | Restore Infra Alert Config
*InfrastructureAlertConfigurationApi* | [**update_infra_alert_config**](docs/InfrastructureAlertConfigurationApi.md#update_infra_alert_config) | **POST** /api/events/settings/infra-alert-configs/{id} | Update Infra Alert Config
*InfrastructureAnalyzeApi* | [**get_available_metrics**](docs/InfrastructureAnalyzeApi.md#get_available_metrics) | **POST** /api/infrastructure-monitoring/analyze/metrics | Get available metrics
*InfrastructureAnalyzeApi* | [**get_available_plugins**](docs/InfrastructureAnalyzeApi.md#get_available_plugins) | **POST** /api/infrastructure-monitoring/analyze/entity-types | Get available entity types
*InfrastructureAnalyzeApi* | [**get_entities**](docs/InfrastructureAnalyzeApi.md#get_entities) | **POST** /api/infrastructure-monitoring/analyze/entities | Get infrastructure entities
*InfrastructureAnalyzeApi* | [**get_entity_groups**](docs/InfrastructureAnalyzeApi.md#get_entity_groups) | **POST** /api/infrastructure-monitoring/analyze/entity-groups | Get grouped infrastructure entities with aggregated metrics
*InfrastructureCatalogApi* | [**get_available_payload_keys_by_plugin_id**](docs/InfrastructureCatalogApi.md#get_available_payload_keys_by_plugin_id) | **GET** /api/infrastructure-monitoring/catalog/payloads/{pluginId} | Get payload keys for plugin
*InfrastructureCatalogApi* | [**get_infrastructure_catalog_metrics**](docs/InfrastructureCatalogApi.md#get_infrastructure_catalog_metrics) | **GET** /api/infrastructure-monitoring/catalog/metrics/{plugin} | Get metric catalog
*InfrastructureCatalogApi* | [**get_infrastructure_catalog_plugins**](docs/InfrastructureCatalogApi.md#get_infrastructure_catalog_plugins) | **GET** /api/infrastructure-monitoring/catalog/plugins | Get plugin catalog
*InfrastructureCatalogApi* | [**get_infrastructure_catalog_plugins_with_custom_metrics**](docs/InfrastructureCatalogApi.md#get_infrastructure_catalog_plugins_with_custom_metrics) | **GET** /api/infrastructure-monitoring/catalog/plugins-with-custom-metrics | Get all plugins with custom metrics catalog
*InfrastructureCatalogApi* | [**get_infrastructure_catalog_search_fields**](docs/InfrastructureCatalogApi.md#get_infrastructure_catalog_search_fields) | **GET** /api/infrastructure-monitoring/catalog/search | get search field catalog
*InfrastructureCatalogApi* | [**get_tag_catalog**](docs/InfrastructureCatalogApi.md#get_tag_catalog) | **GET** /api/infrastructure-monitoring/catalog/tags/{plugin} | Get available tags for a particular plugin
*InfrastructureCatalogApi* | [**get_tag_catalog_all**](docs/InfrastructureCatalogApi.md#get_tag_catalog_all) | **GET** /api/infrastructure-monitoring/catalog/tags | Get available tags
*InfrastructureMetricsApi* | [**get_infrastructure_metrics**](docs/InfrastructureMetricsApi.md#get_infrastructure_metrics) | **POST** /api/infrastructure-monitoring/metrics | Get infrastructure metrics
*InfrastructureResourcesApi* | [**get_monitoring_state**](docs/InfrastructureResourcesApi.md#get_monitoring_state) | **GET** /api/infrastructure-monitoring/monitoring-state | Monitored host count
*InfrastructureResourcesApi* | [**get_plugin_payload**](docs/InfrastructureResourcesApi.md#get_plugin_payload) | **GET** /api/infrastructure-monitoring/payloads/{snapshotId}/{payloadKey} | Get a payload for a snapshot
*InfrastructureResourcesApi* | [**get_snapshot**](docs/InfrastructureResourcesApi.md#get_snapshot) | **GET** /api/infrastructure-monitoring/snapshots/{id} | Get snapshot details
*InfrastructureResourcesApi* | [**get_snapshots**](docs/InfrastructureResourcesApi.md#get_snapshots) | **GET** /api/infrastructure-monitoring/snapshots | Search snapshots
*InfrastructureResourcesApi* | [**post_snapshots**](docs/InfrastructureResourcesApi.md#post_snapshots) | **POST** /api/infrastructure-monitoring/snapshots | Get snapshot details for multiple snapshots
*InfrastructureResourcesApi* | [**software_versions**](docs/InfrastructureResourcesApi.md#software_versions) | **GET** /api/infrastructure-monitoring/software/versions | Get installed software
*InfrastructureTopologyApi* | [**get_related_hosts**](docs/InfrastructureTopologyApi.md#get_related_hosts) | **GET** /api/infrastructure-monitoring/graph/related-hosts/{snapshotId} | Related hosts
*InfrastructureTopologyApi* | [**get_topology**](docs/InfrastructureTopologyApi.md#get_topology) | **GET** /api/infrastructure-monitoring/topology | Gets the infrastructure topology
*LogAlertConfigurationApi* | [**create_log_alert_config**](docs/LogAlertConfigurationApi.md#create_log_alert_config) | **POST** /api/events/settings/global-alert-configs/logs | Create Log Alert Config
*LogAlertConfigurationApi* | [**delete_log_alert_config**](docs/LogAlertConfigurationApi.md#delete_log_alert_config) | **DELETE** /api/events/settings/global-alert-configs/logs/{id} | Delete Log Alert Config
*LogAlertConfigurationApi* | [**disable_log_alert_config**](docs/LogAlertConfigurationApi.md#disable_log_alert_config) | **PUT** /api/events/settings/global-alert-configs/logs/{id}/disable | Disable Log Alert Config
*LogAlertConfigurationApi* | [**enable_log_alert_config**](docs/LogAlertConfigurationApi.md#enable_log_alert_config) | **PUT** /api/events/settings/global-alert-configs/logs/{id}/enable | Enable Log Alert Config
*LogAlertConfigurationApi* | [**find_active_log_alert_configs**](docs/LogAlertConfigurationApi.md#find_active_log_alert_configs) | **GET** /api/events/settings/global-alert-configs/logs | All Log Alert Configs
*LogAlertConfigurationApi* | [**find_log_alert_config**](docs/LogAlertConfigurationApi.md#find_log_alert_config) | **GET** /api/events/settings/global-alert-configs/logs/{id} | Get Log Alert Config
*LogAlertConfigurationApi* | [**find_log_alert_config_versions**](docs/LogAlertConfigurationApi.md#find_log_alert_config_versions) | **GET** /api/events/settings/global-alert-configs/logs/{id}/versions | Get versions of Log Alert Config
*LogAlertConfigurationApi* | [**restore_log_alert_config**](docs/LogAlertConfigurationApi.md#restore_log_alert_config) | **PUT** /api/events/settings/global-alert-configs/logs/{id}/restore/{created} | Restore Log Alert Config
*LogAlertConfigurationApi* | [**update_log_alert_config**](docs/LogAlertConfigurationApi.md#update_log_alert_config) | **POST** /api/events/settings/global-alert-configs/logs/{id} | Update Log Alert Config
*MaintenanceConfigurationApi* | [**delete_maintenance_config**](docs/MaintenanceConfigurationApi.md#delete_maintenance_config) | **DELETE** /api/settings/maintenance/{id} | Delete maintenance configuration
*MaintenanceConfigurationApi* | [**delete_maintenance_config_v2**](docs/MaintenanceConfigurationApi.md#delete_maintenance_config_v2) | **DELETE** /api/settings/v2/maintenance/{id} | Delete maintenance configuration
*MaintenanceConfigurationApi* | [**get_maintenance_config**](docs/MaintenanceConfigurationApi.md#get_maintenance_config) | **GET** /api/settings/maintenance/{id} | Maintenance configuration
*MaintenanceConfigurationApi* | [**get_maintenance_config_v2**](docs/MaintenanceConfigurationApi.md#get_maintenance_config_v2) | **GET** /api/settings/v2/maintenance/{id} | Get maintenance configuration
*MaintenanceConfigurationApi* | [**get_maintenance_configs**](docs/MaintenanceConfigurationApi.md#get_maintenance_configs) | **GET** /api/settings/maintenance | All maintenance configurations
*MaintenanceConfigurationApi* | [**get_maintenance_configs_v2**](docs/MaintenanceConfigurationApi.md#get_maintenance_configs_v2) | **GET** /api/settings/v2/maintenance | All maintenance configurations
*MaintenanceConfigurationApi* | [**pause_recurrent_maintenance_configuration**](docs/MaintenanceConfigurationApi.md#pause_recurrent_maintenance_configuration) | **PUT** /api/settings/v2/maintenance/{id}/pause | Pause maintenance configuration
*MaintenanceConfigurationApi* | [**put_maintenance_config**](docs/MaintenanceConfigurationApi.md#put_maintenance_config) | **PUT** /api/settings/maintenance/{id} | Create or update maintenance configuration
*MaintenanceConfigurationApi* | [**put_maintenance_config_v2**](docs/MaintenanceConfigurationApi.md#put_maintenance_config_v2) | **PUT** /api/settings/v2/maintenance/{id} | Create or update maintenance configuration
*MaintenanceConfigurationApi* | [**resume_recurrent_maintenance_configuration**](docs/MaintenanceConfigurationApi.md#resume_recurrent_maintenance_configuration) | **PUT** /api/settings/v2/maintenance/{id}/resume | Resume maintenance configuration
*MobileAppAnalyzeApi* | [**get_mobile_app_beacon_groups**](docs/MobileAppAnalyzeApi.md#get_mobile_app_beacon_groups) | **POST** /api/mobile-app-monitoring/analyze/beacon-groups | Get grouped beacon metrics
*MobileAppAnalyzeApi* | [**get_mobile_app_beacons**](docs/MobileAppAnalyzeApi.md#get_mobile_app_beacons) | **POST** /api/mobile-app-monitoring/analyze/beacons | Get all beacons
*MobileAppCatalogApi* | [**get_all_mobile_app_catalog_tags**](docs/MobileAppCatalogApi.md#get_all_mobile_app_catalog_tags) | **GET** /api/mobile-app-monitoring/catalog/tags | Get all existing mobile app tags
*MobileAppCatalogApi* | [**get_mobile_app_metric_catalog**](docs/MobileAppCatalogApi.md#get_mobile_app_metric_catalog) | **GET** /api/mobile-app-monitoring/catalog/metrics | Metric catalog
*MobileAppCatalogApi* | [**get_mobile_app_tag_catalog**](docs/MobileAppCatalogApi.md#get_mobile_app_tag_catalog) | **GET** /api/mobile-app-monitoring/catalog | Get mobile app tag catalog
*MobileAppConfigurationApi* | [**delete_mobile_app_config**](docs/MobileAppConfigurationApi.md#delete_mobile_app_config) | **DELETE** /api/mobile-app-monitoring/config/{mobileAppId} | Remove mobile app
*MobileAppConfigurationApi* | [**get_mobile_app_config**](docs/MobileAppConfigurationApi.md#get_mobile_app_config) | **GET** /api/mobile-app-monitoring/config | Get configured mobile apps
*MobileAppConfigurationApi* | [**get_mobile_app_geo_location_configuration**](docs/MobileAppConfigurationApi.md#get_mobile_app_geo_location_configuration) | **GET** /api/mobile-app-monitoring/config/{mobileAppId}/geo-location | Get geo location configuration for mobile app
*MobileAppConfigurationApi* | [**get_mobile_app_geo_mapping_rules**](docs/MobileAppConfigurationApi.md#get_mobile_app_geo_mapping_rules) | **GET** /api/mobile-app-monitoring/config/{mobileAppId}/geo-mapping-rules | Get custom geo mapping rules for mobile app
*MobileAppConfigurationApi* | [**get_mobile_app_ip_masking_configuration**](docs/MobileAppConfigurationApi.md#get_mobile_app_ip_masking_configuration) | **GET** /api/mobile-app-monitoring/config/{mobileAppId}/ip-masking | Get IP masking configuration for mobile app
*MobileAppConfigurationApi* | [**post_mobile_app_config**](docs/MobileAppConfigurationApi.md#post_mobile_app_config) | **POST** /api/mobile-app-monitoring/config | Configure new mobile app
*MobileAppConfigurationApi* | [**rename_mobile_app_config**](docs/MobileAppConfigurationApi.md#rename_mobile_app_config) | **PUT** /api/mobile-app-monitoring/config/{mobileAppId} | Rename mobile app
*MobileAppConfigurationApi* | [**set_mobile_app_geo_mapping_rules**](docs/MobileAppConfigurationApi.md#set_mobile_app_geo_mapping_rules) | **PUT** /api/mobile-app-monitoring/config/{mobileAppId}/geo-mapping-rules | Set custom geo mapping rules for mobile app
*MobileAppConfigurationApi* | [**update_mobile_app_geo_location_configuration**](docs/MobileAppConfigurationApi.md#update_mobile_app_geo_location_configuration) | **PUT** /api/mobile-app-monitoring/config/{mobileAppId}/geo-location | Update geo location configuration for mobile app
*MobileAppConfigurationApi* | [**update_mobile_app_ip_masking_configuration**](docs/MobileAppConfigurationApi.md#update_mobile_app_ip_masking_configuration) | **PUT** /api/mobile-app-monitoring/config/{mobileAppId}/ip-masking | Update IP masking configuration for mobile app
*MobileAppMetricsApi* | [**get_mobile_app_beacon_metrics**](docs/MobileAppMetricsApi.md#get_mobile_app_beacon_metrics) | **POST** /api/mobile-app-monitoring/metrics | Get mobile app beacon metrics
*MobileAppMetricsApi* | [**get_mobile_app_beacon_metrics_v2**](docs/MobileAppMetricsApi.md#get_mobile_app_beacon_metrics_v2) | **POST** /api/mobile-app-monitoring/v2/metrics | Get beacon metrics
*MobileAppMetricsApi* | [**get_session**](docs/MobileAppMetricsApi.md#get_session) | **GET** /api/mobile-app-monitoring/session | Get mobile app session
*PoliciesApi* | [**add_policies**](docs/PoliciesApi.md#add_policies) | **POST** /api/automation/policies/bulk | Create automation policies.
*PoliciesApi* | [**add_policy**](docs/PoliciesApi.md#add_policy) | **POST** /api/automation/policies | Create an automation policy.
*PoliciesApi* | [**delete_policy**](docs/PoliciesApi.md#delete_policy) | **DELETE** /api/automation/policies/{id} | Deletes an automation policy by identifier.
*PoliciesApi* | [**get_policies**](docs/PoliciesApi.md#get_policies) | **GET** /api/automation/policies | Get all automation policies.
*PoliciesApi* | [**get_policy_by_id**](docs/PoliciesApi.md#get_policy_by_id) | **GET** /api/automation/policies/{id} | Get an automation policy by ID.
*PoliciesApi* | [**update_policy**](docs/PoliciesApi.md#update_policy) | **PUT** /api/automation/policies/{id} | Updates an automation policy by identifier.
*ReleasesApi* | [**delete_release**](docs/ReleasesApi.md#delete_release) | **DELETE** /api/releases/{releaseId} | Delete release
*ReleasesApi* | [**get_all_releases**](docs/ReleasesApi.md#get_all_releases) | **GET** /api/releases | Get all releases
*ReleasesApi* | [**get_release**](docs/ReleasesApi.md#get_release) | **GET** /api/releases/{releaseId} | Get release
*ReleasesApi* | [**post_release**](docs/ReleasesApi.md#post_release) | **POST** /api/releases | Create release
*ReleasesApi* | [**put_release**](docs/ReleasesApi.md#put_release) | **PUT** /api/releases/{releaseId} | Update release
*SLIReportApi* | [**get_sli**](docs/SLIReportApi.md#get_sli) | **GET** /api/sli/report/{sliId} | Generate SLI report (Limitation: the Classic Edition API report can be available one hour after the SLI configuration created; other editions are around one minute.)
*SLISettingsApi* | [**create_sli_config**](docs/SLISettingsApi.md#create_sli_config) | **POST** /api/settings/sli | Create SLI Config
*SLISettingsApi* | [**create_sli_config_v2**](docs/SLISettingsApi.md#create_sli_config_v2) | **POST** /api/settings/v2/sli | Create SLI Config
*SLISettingsApi* | [**delete_sli_config**](docs/SLISettingsApi.md#delete_sli_config) | **DELETE** /api/settings/sli/{id} | Delete SLI Config
*SLISettingsApi* | [**delete_sli_config_v2**](docs/SLISettingsApi.md#delete_sli_config_v2) | **DELETE** /api/settings/v2/sli/{id} | Delete SLI Config
*SLISettingsApi* | [**get_all_sli_configs**](docs/SLISettingsApi.md#get_all_sli_configs) | **GET** /api/settings/sli | Get All SLI Configs
*SLISettingsApi* | [**get_all_sli_configs_v2**](docs/SLISettingsApi.md#get_all_sli_configs_v2) | **GET** /api/settings/v2/sli | Get All SLI Configs
*SLISettingsApi* | [**get_sli_config**](docs/SLISettingsApi.md#get_sli_config) | **GET** /api/settings/sli/{id} | Get SLI Config
*SLISettingsApi* | [**get_sli_config_v2**](docs/SLISettingsApi.md#get_sli_config_v2) | **GET** /api/settings/v2/sli/{id} | Get SLI Config
*SLISettingsApi* | [**get_sli_configs_for_entity_type_and_id_v2**](docs/SLISettingsApi.md#get_sli_configs_for_entity_type_and_id_v2) | **GET** /api/settings/v2/sli/{entityType}/{entityId} | Get all SLI configs for entity type and entity id
*SLISettingsApi* | [**update_sli_config**](docs/SLISettingsApi.md#update_sli_config) | **PUT** /api/settings/sli/{id} | Update SLI Config
*ServiceLevelsAlertConfigurationApi* | [**create_service_levels_alert_config**](docs/ServiceLevelsAlertConfigurationApi.md#create_service_levels_alert_config) | **POST** /api/events/settings/global-alert-configs/service-levels | Create Service levels Alert Config
*ServiceLevelsAlertConfigurationApi* | [**delete_service_levels_alert_config**](docs/ServiceLevelsAlertConfigurationApi.md#delete_service_levels_alert_config) | **DELETE** /api/events/settings/global-alert-configs/service-levels/{id} | Delete Service levels Alert Config
*ServiceLevelsAlertConfigurationApi* | [**disable_service_levels_alert_config**](docs/ServiceLevelsAlertConfigurationApi.md#disable_service_levels_alert_config) | **PUT** /api/events/settings/global-alert-configs/service-levels/{id}/disable | Disable Service levels Alert Config
*ServiceLevelsAlertConfigurationApi* | [**enable_service_levels_alert_config**](docs/ServiceLevelsAlertConfigurationApi.md#enable_service_levels_alert_config) | **PUT** /api/events/settings/global-alert-configs/service-levels/{id}/enable | Enable Service levels Alert Config
*ServiceLevelsAlertConfigurationApi* | [**find_active_service_levels_alert_configs**](docs/ServiceLevelsAlertConfigurationApi.md#find_active_service_levels_alert_configs) | **GET** /api/events/settings/global-alert-configs/service-levels | All Service levels Alert Configs
*ServiceLevelsAlertConfigurationApi* | [**find_service_levels_alert_config**](docs/ServiceLevelsAlertConfigurationApi.md#find_service_levels_alert_config) | **GET** /api/events/settings/global-alert-configs/service-levels/{id} | Get Service levels Alert Config
*ServiceLevelsAlertConfigurationApi* | [**find_service_levels_alert_config_versions**](docs/ServiceLevelsAlertConfigurationApi.md#find_service_levels_alert_config_versions) | **GET** /api/events/settings/global-alert-configs/service-levels/{id}/versions | Get versions of Service levels Alert Config
*ServiceLevelsAlertConfigurationApi* | [**restore_service_levels_alert_config**](docs/ServiceLevelsAlertConfigurationApi.md#restore_service_levels_alert_config) | **PUT** /api/events/settings/global-alert-configs/service-levels/{id}/restore/{created} | Restore Service levels Alert Config
*ServiceLevelsAlertConfigurationApi* | [**update_service_levels_alert_config**](docs/ServiceLevelsAlertConfigurationApi.md#update_service_levels_alert_config) | **POST** /api/events/settings/global-alert-configs/service-levels/{id} | Update Service levels Alert Config
*ServiceLevelsObjectiveSLOConfigurationsApi* | [**create_slo_config**](docs/ServiceLevelsObjectiveSLOConfigurationsApi.md#create_slo_config) | **POST** /api/settings/slo | Create a new SLO Config
*ServiceLevelsObjectiveSLOConfigurationsApi* | [**delete_slo_config**](docs/ServiceLevelsObjectiveSLOConfigurationsApi.md#delete_slo_config) | **DELETE** /api/settings/slo/{id} | Delete an existing SLO Config
*ServiceLevelsObjectiveSLOConfigurationsApi* | [**get_all_slo_config_tags**](docs/ServiceLevelsObjectiveSLOConfigurationsApi.md#get_all_slo_config_tags) | **GET** /api/settings/slo/tags | Get All SLO Config tags
*ServiceLevelsObjectiveSLOConfigurationsApi* | [**get_all_slo_configs**](docs/ServiceLevelsObjectiveSLOConfigurationsApi.md#get_all_slo_configs) | **GET** /api/settings/slo | Get All SLO Configs
*ServiceLevelsObjectiveSLOConfigurationsApi* | [**get_slo_config_by_id**](docs/ServiceLevelsObjectiveSLOConfigurationsApi.md#get_slo_config_by_id) | **GET** /api/settings/slo/{id} | Get an existing SLO Config
*ServiceLevelsObjectiveSLOConfigurationsApi* | [**update_slo_config**](docs/ServiceLevelsObjectiveSLOConfigurationsApi.md#update_slo_config) | **PUT** /api/settings/slo/{id} | Update an existing SLO Config
*ServiceLevelsObjectiveSLOReportApi* | [**get_slo**](docs/ServiceLevelsObjectiveSLOReportApi.md#get_slo) | **GET** /api/slo/report/{sloId} | Generate Service Levels report
*SessionSettingsApi* | [**delete_session_settings**](docs/SessionSettingsApi.md#delete_session_settings) | **DELETE** /api/settings/session | Delete session settings
*SessionSettingsApi* | [**get_session_settings**](docs/SessionSettingsApi.md#get_session_settings) | **GET** /api/settings/session | Get session settings
*SessionSettingsApi* | [**set_session_settings**](docs/SessionSettingsApi.md#set_session_settings) | **PUT** /api/settings/session | Configure session settings
*SyntheticAlertConfigurationApi* | [**create_synthetic_alert_config**](docs/SyntheticAlertConfigurationApi.md#create_synthetic_alert_config) | **POST** /api/events/settings/global-alert-configs/synthetics | Create Synthetic Smart Alert Config
*SyntheticAlertConfigurationApi* | [**delete_synthetic_alert_config**](docs/SyntheticAlertConfigurationApi.md#delete_synthetic_alert_config) | **DELETE** /api/events/settings/global-alert-configs/synthetics/{id} | Delete Synthetic Smart Alert Config
*SyntheticAlertConfigurationApi* | [**disable_synthetic_alert_config**](docs/SyntheticAlertConfigurationApi.md#disable_synthetic_alert_config) | **PUT** /api/events/settings/global-alert-configs/synthetics/{id}/disable | Disable Synthetic Smart Alert Config
*SyntheticAlertConfigurationApi* | [**enable_synthetic_alert_config**](docs/SyntheticAlertConfigurationApi.md#enable_synthetic_alert_config) | **PUT** /api/events/settings/global-alert-configs/synthetics/{id}/enable | Enable Synthetic Smart Alert Config
*SyntheticAlertConfigurationApi* | [**find_active_synthetic_alert_configs**](docs/SyntheticAlertConfigurationApi.md#find_active_synthetic_alert_configs) | **GET** /api/events/settings/global-alert-configs/synthetics | Get all Synthetic Smart Alert Configs
*SyntheticAlertConfigurationApi* | [**find_synthetic_alert_config**](docs/SyntheticAlertConfigurationApi.md#find_synthetic_alert_config) | **GET** /api/events/settings/global-alert-configs/synthetics/{id} | Get Synthetic Smart Alert Config
*SyntheticAlertConfigurationApi* | [**find_synthetic_alert_config_versions**](docs/SyntheticAlertConfigurationApi.md#find_synthetic_alert_config_versions) | **GET** /api/events/settings/global-alert-configs/synthetics/{id}/versions | Get Synthetic Smart Alert Config Versions
*SyntheticAlertConfigurationApi* | [**restore_synthetic_alert_config**](docs/SyntheticAlertConfigurationApi.md#restore_synthetic_alert_config) | **PUT** /api/events/settings/global-alert-configs/synthetics/{id}/restore/{created} | Restore Synthetic Smart Alert Config
*SyntheticAlertConfigurationApi* | [**update_synthetic_alert_config**](docs/SyntheticAlertConfigurationApi.md#update_synthetic_alert_config) | **POST** /api/events/settings/global-alert-configs/synthetics/{id} | Update Synthetic Smart Alert Config
*SyntheticCallsApi* | [**delete_synthetic_call**](docs/SyntheticCallsApi.md#delete_synthetic_call) | **DELETE** /api/settings/synthetic-calls | Delete synthetic call configurations
*SyntheticCallsApi* | [**get_synthetic_calls**](docs/SyntheticCallsApi.md#get_synthetic_calls) | **GET** /api/settings/synthetic-calls | Synthetic call configurations
*SyntheticCallsApi* | [**update_synthetic_call**](docs/SyntheticCallsApi.md#update_synthetic_call) | **PUT** /api/settings/synthetic-calls | Update synthetic call configurations
*SyntheticCatalogApi* | [**get_synthetic_catalog_metrics**](docs/SyntheticCatalogApi.md#get_synthetic_catalog_metrics) | **GET** /api/synthetics/catalog/metrics | Get Metric catalog
*SyntheticCatalogApi* | [**get_synthetic_tag_catalog**](docs/SyntheticCatalogApi.md#get_synthetic_tag_catalog) | **GET** /api/synthetics/catalog | Get synthetic tag catalog
*SyntheticMetricsApi* | [**get_metrics_result**](docs/SyntheticMetricsApi.md#get_metrics_result) | **POST** /api/synthetics/metrics | Get Synthetic Metrics
*SyntheticSettingsApi* | [**create_synthetic_credential**](docs/SyntheticSettingsApi.md#create_synthetic_credential) | **POST** /api/synthetics/settings/credentials | Create a Synthetic Credential
*SyntheticSettingsApi* | [**create_synthetic_test**](docs/SyntheticSettingsApi.md#create_synthetic_test) | **POST** /api/synthetics/settings/tests | Create a Synthetic test
*SyntheticSettingsApi* | [**delete_synthetic_credential**](docs/SyntheticSettingsApi.md#delete_synthetic_credential) | **DELETE** /api/synthetics/settings/credentials/{name} | Delete Synthetic credential
*SyntheticSettingsApi* | [**delete_synthetic_location**](docs/SyntheticSettingsApi.md#delete_synthetic_location) | **DELETE** /api/synthetics/settings/locations/{id} | Delete Synthetic location
*SyntheticSettingsApi* | [**delete_synthetic_test**](docs/SyntheticSettingsApi.md#delete_synthetic_test) | **DELETE** /api/synthetics/settings/tests/{id} | Delete a Synthetic test
*SyntheticSettingsApi* | [**get_one_synthetic_credential_associations**](docs/SyntheticSettingsApi.md#get_one_synthetic_credential_associations) | **GET** /api/synthetics/settings/credentials/associations/{name} | A Synthetic Credential with Name and Associations
*SyntheticSettingsApi* | [**get_synthetic_credential_associations**](docs/SyntheticSettingsApi.md#get_synthetic_credential_associations) | **GET** /api/synthetics/settings/credentials/associations | All Synthetic Credential Names and Associations
*SyntheticSettingsApi* | [**get_synthetic_credential_names**](docs/SyntheticSettingsApi.md#get_synthetic_credential_names) | **GET** /api/synthetics/settings/credentials | All Synthetic Credential Names
*SyntheticSettingsApi* | [**get_synthetic_datacenter**](docs/SyntheticSettingsApi.md#get_synthetic_datacenter) | **GET** /api/synthetics/settings/datacenters/{datacenterId} | Synthetic datacenter
*SyntheticSettingsApi* | [**get_synthetic_datacenters**](docs/SyntheticSettingsApi.md#get_synthetic_datacenters) | **GET** /api/synthetics/settings/datacenters | All Synthetic datacenters
*SyntheticSettingsApi* | [**get_synthetic_location**](docs/SyntheticSettingsApi.md#get_synthetic_location) | **GET** /api/synthetics/settings/locations/{id} | Synthetic location
*SyntheticSettingsApi* | [**get_synthetic_locations**](docs/SyntheticSettingsApi.md#get_synthetic_locations) | **GET** /api/synthetics/settings/locations | All Synthetic locations
*SyntheticSettingsApi* | [**get_synthetic_test**](docs/SyntheticSettingsApi.md#get_synthetic_test) | **GET** /api/synthetics/settings/tests/{id} | A Synthetic test
*SyntheticSettingsApi* | [**get_synthetic_tests**](docs/SyntheticSettingsApi.md#get_synthetic_tests) | **GET** /api/synthetics/settings/tests | All Synthetic tests
*SyntheticSettingsApi* | [**patch_synthetic_credential**](docs/SyntheticSettingsApi.md#patch_synthetic_credential) | **PATCH** /api/synthetics/settings/credentials/{name} | Patch a Synthetic Credential
*SyntheticSettingsApi* | [**patch_synthetic_test**](docs/SyntheticSettingsApi.md#patch_synthetic_test) | **PATCH** /api/synthetics/settings/tests/{id} | Patch a Synthetic test
*SyntheticSettingsApi* | [**update_synthetic_credential**](docs/SyntheticSettingsApi.md#update_synthetic_credential) | **PUT** /api/synthetics/settings/credentials/{name} | Update a Synthetic Credential
*SyntheticSettingsApi* | [**update_synthetic_test**](docs/SyntheticSettingsApi.md#update_synthetic_test) | **PUT** /api/synthetics/settings/tests/{id} | Update a Synthetic test
*SyntheticTestPlaybackResultsApi* | [**get_location_summary_list**](docs/SyntheticTestPlaybackResultsApi.md#get_location_summary_list) | **POST** /api/synthetics/results/locationsummarylist | Get a list of Synthetic locations with last run test on each location data
*SyntheticTestPlaybackResultsApi* | [**get_synthetic_result**](docs/SyntheticTestPlaybackResultsApi.md#get_synthetic_result) | **POST** /api/synthetics/results | Get Synthetic test playback results
*SyntheticTestPlaybackResultsApi* | [**get_synthetic_result_detail_data**](docs/SyntheticTestPlaybackResultsApi.md#get_synthetic_result_detail_data) | **GET** /api/synthetics/results/{testid}/{testresultid}/detail | Get Synthetic test playback result detail data
*SyntheticTestPlaybackResultsApi* | [**get_synthetic_result_detail_data_file**](docs/SyntheticTestPlaybackResultsApi.md#get_synthetic_result_detail_data_file) | **GET** /api/synthetics/results/{testid}/{testresultid}/file | Download the synthetic test playback result detail data file
*SyntheticTestPlaybackResultsApi* | [**get_synthetic_result_list**](docs/SyntheticTestPlaybackResultsApi.md#get_synthetic_result_list) | **POST** /api/synthetics/results/list | Get a list of Synthetic test playback results
*SyntheticTestPlaybackResultsApi* | [**get_synthetic_result_metadata**](docs/SyntheticTestPlaybackResultsApi.md#get_synthetic_result_metadata) | **GET** /api/synthetics/results/{testid}/{testresultid} | Get Synthetic test playback detail result description(metadata)
*SyntheticTestPlaybackResultsApi* | [**get_test_summary_list**](docs/SyntheticTestPlaybackResultsApi.md#get_test_summary_list) | **POST** /api/synthetics/results/testsummarylist | Get a list of Synthetic tests with success rate and average response time data
*UsageApi* | [**get_all_usage**](docs/UsageApi.md#get_all_usage) | **GET** /api/instana/usage/api | API usage by customer
*UsageApi* | [**get_hosts_per_day**](docs/UsageApi.md#get_hosts_per_day) | **GET** /api/instana/usage/hosts/{day}/{month}/{year} | Host count day / month / year
*UsageApi* | [**get_hosts_per_month**](docs/UsageApi.md#get_hosts_per_month) | **GET** /api/instana/usage/hosts/{month}/{year} | Host count month / year
*UsageApi* | [**get_usage_per_day**](docs/UsageApi.md#get_usage_per_day) | **GET** /api/instana/usage/api/{day}/{month}/{year} | API usage day / month / year
*UsageApi* | [**get_usage_per_month**](docs/UsageApi.md#get_usage_per_month) | **GET** /api/instana/usage/api/{month}/{year} | API usage month / year
*UserApi* | [**get_invitations**](docs/UserApi.md#get_invitations) | **GET** /api/settings/invitations | All pending invitations
*UserApi* | [**get_user_by_id**](docs/UserApi.md#get_user_by_id) | **GET** /api/settings/users/{userId} | Get single user
*UserApi* | [**get_users**](docs/UserApi.md#get_users) | **GET** /api/settings/users | All users (without invitations)
*UserApi* | [**get_users_including_invitations**](docs/UserApi.md#get_users_including_invitations) | **GET** /api/settings/users/overview | All users (incl. invitations)
*UserApi* | [**invite_users**](docs/UserApi.md#invite_users) | **POST** /api/settings/invitations | Send user invitations
*UserApi* | [**remove_user_from_tenant**](docs/UserApi.md#remove_user_from_tenant) | **DELETE** /api/settings/users/{userId} | Remove user from tenant
*UserApi* | [**revoke_pending_invitation**](docs/UserApi.md#revoke_pending_invitation) | **DELETE** /api/settings/invitations | Revoke pending invitation
*UserApi* | [**share_and_invite_users**](docs/UserApi.md#share_and_invite_users) | **POST** /api/settings/invitation/share | Send user invitations
*UserApi* | [**update_user**](docs/UserApi.md#update_user) | **PUT** /api/settings/users/{email} | Change user name of single user
*WebsiteAnalyzeApi* | [**get_beacon_groups**](docs/WebsiteAnalyzeApi.md#get_beacon_groups) | **POST** /api/website-monitoring/analyze/beacon-groups | Get grouped beacon metrics
*WebsiteAnalyzeApi* | [**get_beacons**](docs/WebsiteAnalyzeApi.md#get_beacons) | **POST** /api/website-monitoring/analyze/beacons | Get all beacons
*WebsiteCatalogApi* | [**get_website_catalog_metrics**](docs/WebsiteCatalogApi.md#get_website_catalog_metrics) | **GET** /api/website-monitoring/catalog/metrics | Metric catalog
*WebsiteCatalogApi* | [**get_website_catalog_tags**](docs/WebsiteCatalogApi.md#get_website_catalog_tags) | **GET** /api/website-monitoring/catalog/tags | Get all existing website tags
*WebsiteCatalogApi* | [**get_website_tag_catalog**](docs/WebsiteCatalogApi.md#get_website_tag_catalog) | **GET** /api/website-monitoring/catalog | Get website tag catalog
*WebsiteConfigurationApi* | [**clear_source_map_upload_configuration**](docs/WebsiteConfigurationApi.md#clear_source_map_upload_configuration) | **PUT** /api/website-monitoring/config/{websiteId}/sourcemap-upload/{sourceMapConfigId}/clear | Clear source map files for source map upload configuration
*WebsiteConfigurationApi* | [**create_website**](docs/WebsiteConfigurationApi.md#create_website) | **POST** /api/website-monitoring/config | Configure new website
*WebsiteConfigurationApi* | [**delete_website**](docs/WebsiteConfigurationApi.md#delete_website) | **DELETE** /api/website-monitoring/config/{websiteId} | Remove website
*WebsiteConfigurationApi* | [**get_website**](docs/WebsiteConfigurationApi.md#get_website) | **GET** /api/website-monitoring/config/{websiteId} | Get configured website
*WebsiteConfigurationApi* | [**get_website_geo_location_configuration**](docs/WebsiteConfigurationApi.md#get_website_geo_location_configuration) | **GET** /api/website-monitoring/config/{websiteId}/geo-location | Get geo location configuration for website
*WebsiteConfigurationApi* | [**get_website_geo_mapping_rules**](docs/WebsiteConfigurationApi.md#get_website_geo_mapping_rules) | **GET** /api/website-monitoring/config/{websiteId}/geo-mapping-rules | Get custom geo mapping rules for website
*WebsiteConfigurationApi* | [**get_website_ip_masking_configuration**](docs/WebsiteConfigurationApi.md#get_website_ip_masking_configuration) | **GET** /api/website-monitoring/config/{websiteId}/ip-masking | Get IP masking configuration for website
*WebsiteConfigurationApi* | [**get_websites**](docs/WebsiteConfigurationApi.md#get_websites) | **GET** /api/website-monitoring/config | Get configured websites
*WebsiteConfigurationApi* | [**rename_website**](docs/WebsiteConfigurationApi.md#rename_website) | **PUT** /api/website-monitoring/config/{websiteId} | Rename website
*WebsiteConfigurationApi* | [**set_website_geo_mapping_rules**](docs/WebsiteConfigurationApi.md#set_website_geo_mapping_rules) | **PUT** /api/website-monitoring/config/{websiteId}/geo-mapping-rules | Set custom geo mapping rules for website
*WebsiteConfigurationApi* | [**update_website_geo_location_configuration**](docs/WebsiteConfigurationApi.md#update_website_geo_location_configuration) | **PUT** /api/website-monitoring/config/{websiteId}/geo-location | Update geo location configuration for website
*WebsiteConfigurationApi* | [**update_website_ip_masking_configuration**](docs/WebsiteConfigurationApi.md#update_website_ip_masking_configuration) | **PUT** /api/website-monitoring/config/{websiteId}/ip-masking | Update IP masking configuration for website
*WebsiteConfigurationApi* | [**upload_source_map_file**](docs/WebsiteConfigurationApi.md#upload_source_map_file) | **PUT** /api/website-monitoring/config/{websiteId}/sourcemap-upload/{sourceMapConfigId}/form | Upload source map file for website
*WebsiteMetricsApi* | [**get_beacon_metrics**](docs/WebsiteMetricsApi.md#get_beacon_metrics) | **POST** /api/website-monitoring/metrics | Get beacon metrics
*WebsiteMetricsApi* | [**get_beacon_metrics_v2**](docs/WebsiteMetricsApi.md#get_beacon_metrics_v2) | **POST** /api/website-monitoring/v2/metrics | Get beacon metrics
*WebsiteMetricsApi* | [**get_page_load**](docs/WebsiteMetricsApi.md#get_page_load) | **GET** /api/website-monitoring/page-load | Get page load


## Documentation For Models

 - [AbstractIntegration](docs/AbstractIntegration.md)
 - [AbstractRule](docs/AbstractRule.md)
 - [AccessLogEntry](docs/AccessLogEntry.md)
 - [AccessLogResponse](docs/AccessLogResponse.md)
 - [AccessRule](docs/AccessRule.md)
 - [Action](docs/Action.md)
 - [ActionConfiguration](docs/ActionConfiguration.md)
 - [ActionInstance](docs/ActionInstance.md)
 - [ActionInstanceMetadataEntry](docs/ActionInstanceMetadataEntry.md)
 - [ActionInstanceParameter](docs/ActionInstanceParameter.md)
 - [ActionInstanceRequest](docs/ActionInstanceRequest.md)
 - [ActionInstanceRequestParameters](docs/ActionInstanceRequestParameters.md)
 - [ActionMatch](docs/ActionMatch.md)
 - [ActionSearchSpace](docs/ActionSearchSpace.md)
 - [AdaptiveBaseline](docs/AdaptiveBaseline.md)
 - [AdaptiveThresholdRule](docs/AdaptiveThresholdRule.md)
 - [AdjustedTimeframe](docs/AdjustedTimeframe.md)
 - [AgentConfigurationUpdate](docs/AgentConfigurationUpdate.md)
 - [AlertingConfiguration](docs/AlertingConfiguration.md)
 - [AlertingConfigurationWithLastUpdated](docs/AlertingConfigurationWithLastUpdated.md)
 - [AlertingTimeWindow](docs/AlertingTimeWindow.md)
 - [ApdexConfiguration](docs/ApdexConfiguration.md)
 - [ApdexConfigurationInput](docs/ApdexConfigurationInput.md)
 - [ApdexEntity](docs/ApdexEntity.md)
 - [ApdexReport](docs/ApdexReport.md)
 - [ApiCreateGroup](docs/ApiCreateGroup.md)
 - [ApiGroup](docs/ApiGroup.md)
 - [ApiMember](docs/ApiMember.md)
 - [ApiPermissionSet](docs/ApiPermissionSet.md)
 - [ApiRestrictedApplicationFilter](docs/ApiRestrictedApplicationFilter.md)
 - [ApiToken](docs/ApiToken.md)
 - [AppDataMetricConfiguration](docs/AppDataMetricConfiguration.md)
 - [Application](docs/Application.md)
 - [ApplicationAlertConfig](docs/ApplicationAlertConfig.md)
 - [ApplicationAlertConfigWithMetadata](docs/ApplicationAlertConfigWithMetadata.md)
 - [ApplicationAlertRule](docs/ApplicationAlertRule.md)
 - [ApplicationApdexEntity](docs/ApplicationApdexEntity.md)
 - [ApplicationConfig](docs/ApplicationConfig.md)
 - [ApplicationEventResult](docs/ApplicationEventResult.md)
 - [ApplicationItem](docs/ApplicationItem.md)
 - [ApplicationMetricResult](docs/ApplicationMetricResult.md)
 - [ApplicationNode](docs/ApplicationNode.md)
 - [ApplicationResult](docs/ApplicationResult.md)
 - [ApplicationScope](docs/ApplicationScope.md)
 - [ApplicationScopeWithMetadata](docs/ApplicationScopeWithMetadata.md)
 - [ApplicationSliEntity](docs/ApplicationSliEntity.md)
 - [ApplicationSloEntity](docs/ApplicationSloEntity.md)
 - [ApplicationTimeThreshold](docs/ApplicationTimeThreshold.md)
 - [AuditLogEntry](docs/AuditLogEntry.md)
 - [AuditLogUiResponse](docs/AuditLogUiResponse.md)
 - [Author](docs/Author.md)
 - [AvailabilityBlueprintIndicator](docs/AvailabilityBlueprintIndicator.md)
 - [AvailabilitySliEntity](docs/AvailabilitySliEntity.md)
 - [AvailableMetrics](docs/AvailableMetrics.md)
 - [AvailablePlugins](docs/AvailablePlugins.md)
 - [BackendTraceReference](docs/BackendTraceReference.md)
 - [BinaryOperatorDTO](docs/BinaryOperatorDTO.md)
 - [BrowserScriptConfiguration](docs/BrowserScriptConfiguration.md)
 - [BuiltInEventSpecification](docs/BuiltInEventSpecification.md)
 - [BuiltInEventSpecificationWithLastUpdated](docs/BuiltInEventSpecificationWithLastUpdated.md)
 - [BusinessActivity](docs/BusinessActivity.md)
 - [BusinessPerspectiveConfig](docs/BusinessPerspectiveConfig.md)
 - [CallGroupsItem](docs/CallGroupsItem.md)
 - [CallGroupsResult](docs/CallGroupsResult.md)
 - [CallRelation](docs/CallRelation.md)
 - [ChangeSummary](docs/ChangeSummary.md)
 - [CloudfoundryPhysicalContext](docs/CloudfoundryPhysicalContext.md)
 - [Condition](docs/Condition.md)
 - [ConfigVersion](docs/ConfigVersion.md)
 - [CrashMobileAppAlertRule](docs/CrashMobileAppAlertRule.md)
 - [CursorPaginatedBusinessActivityItem](docs/CursorPaginatedBusinessActivityItem.md)
 - [CursorPagination](docs/CursorPagination.md)
 - [CursorPaginationInfraExploreCursor](docs/CursorPaginationInfraExploreCursor.md)
 - [CustomBlueprintIndicator](docs/CustomBlueprintIndicator.md)
 - [CustomDashboard](docs/CustomDashboard.md)
 - [CustomDashboardPreview](docs/CustomDashboardPreview.md)
 - [CustomEmailSubjectPrefix](docs/CustomEmailSubjectPrefix.md)
 - [CustomEventMobileAppAlertRule](docs/CustomEventMobileAppAlertRule.md)
 - [CustomEventSpecification](docs/CustomEventSpecification.md)
 - [CustomEventSpecificationWithLastUpdated](docs/CustomEventSpecificationWithLastUpdated.md)
 - [CustomEventWebsiteAlertRule](docs/CustomEventWebsiteAlertRule.md)
 - [CustomPayloadConfiguration](docs/CustomPayloadConfiguration.md)
 - [CustomPayloadField](docs/CustomPayloadField.md)
 - [CustomPayloadWithLastUpdated](docs/CustomPayloadWithLastUpdated.md)
 - [DNSActionConfiguration](docs/DNSActionConfiguration.md)
 - [DNSActionFilterQueryTime](docs/DNSActionFilterQueryTime.md)
 - [DNSActionFilterTargetValue](docs/DNSActionFilterTargetValue.md)
 - [DashboardApiToken](docs/DashboardApiToken.md)
 - [DatabaseIntegration](docs/DatabaseIntegration.md)
 - [DeprecatedTagFilter](docs/DeprecatedTagFilter.md)
 - [Duration](docs/Duration.md)
 - [DynamicField](docs/DynamicField.md)
 - [DynamicFieldValue](docs/DynamicFieldValue.md)
 - [DynamicParameter](docs/DynamicParameter.md)
 - [EditUser](docs/EditUser.md)
 - [EmailIntegration](docs/EmailIntegration.md)
 - [EmptyConfiguration](docs/EmptyConfiguration.md)
 - [Endpoint](docs/Endpoint.md)
 - [EndpointConfig](docs/EndpointConfig.md)
 - [EndpointEventResult](docs/EndpointEventResult.md)
 - [EndpointItem](docs/EndpointItem.md)
 - [EndpointMetricResult](docs/EndpointMetricResult.md)
 - [EndpointNode](docs/EndpointNode.md)
 - [EndpointResult](docs/EndpointResult.md)
 - [EndpointSimple](docs/EndpointSimple.md)
 - [EntityCountRule](docs/EntityCountRule.md)
 - [EntityCountVerificationRule](docs/EntityCountVerificationRule.md)
 - [EntityHealthInfo](docs/EntityHealthInfo.md)
 - [EntityId](docs/EntityId.md)
 - [EntityVerificationRule](docs/EntityVerificationRule.md)
 - [ErrorBudgetAlertRule](docs/ErrorBudgetAlertRule.md)
 - [ErrorsApplicationAlertRule](docs/ErrorsApplicationAlertRule.md)
 - [Event](docs/Event.md)
 - [EventFilteringConfiguration](docs/EventFilteringConfiguration.md)
 - [EventResult](docs/EventResult.md)
 - [EventSpecificationInfo](docs/EventSpecificationInfo.md)
 - [ExtendedService](docs/ExtendedService.md)
 - [FailureSyntheticAlertRule](docs/FailureSyntheticAlertRule.md)
 - [FixedHttpPathSegmentMatchingRule](docs/FixedHttpPathSegmentMatchingRule.md)
 - [FixedTimeWindow](docs/FixedTimeWindow.md)
 - [FullTrace](docs/FullTrace.md)
 - [GenericInfraAlertRule](docs/GenericInfraAlertRule.md)
 - [GeoLocationConfiguration](docs/GeoLocationConfiguration.md)
 - [GeoMappingRule](docs/GeoMappingRule.md)
 - [GeoSubdivision](docs/GeoSubdivision.md)
 - [GetActivities](docs/GetActivities.md)
 - [GetApplicationMetrics](docs/GetApplicationMetrics.md)
 - [GetApplications](docs/GetApplications.md)
 - [GetAvailableMetricsQuery](docs/GetAvailableMetricsQuery.md)
 - [GetAvailablePluginsQuery](docs/GetAvailablePluginsQuery.md)
 - [GetCallGroups](docs/GetCallGroups.md)
 - [GetCombinedMetrics](docs/GetCombinedMetrics.md)
 - [GetDynamicParameterValues](docs/GetDynamicParameterValues.md)
 - [GetEndpoints](docs/GetEndpoints.md)
 - [GetInfrastructureGroupsQuery](docs/GetInfrastructureGroupsQuery.md)
 - [GetInfrastructureQuery](docs/GetInfrastructureQuery.md)
 - [GetMetricsResult](docs/GetMetricsResult.md)
 - [GetMobileAppBeaconGroups](docs/GetMobileAppBeaconGroups.md)
 - [GetMobileAppBeacons](docs/GetMobileAppBeacons.md)
 - [GetMobileAppMetrics](docs/GetMobileAppMetrics.md)
 - [GetMobileAppMetricsV2](docs/GetMobileAppMetricsV2.md)
 - [GetPayloadKeysResult](docs/GetPayloadKeysResult.md)
 - [GetServices](docs/GetServices.md)
 - [GetSnapshotsQuery](docs/GetSnapshotsQuery.md)
 - [GetTestResult](docs/GetTestResult.md)
 - [GetTestResultBase](docs/GetTestResultBase.md)
 - [GetTestResultList](docs/GetTestResultList.md)
 - [GetTestSummaryResult](docs/GetTestSummaryResult.md)
 - [GetTraceDownloadResultItem](docs/GetTraceDownloadResultItem.md)
 - [GetTraceGroups](docs/GetTraceGroups.md)
 - [GetTraces](docs/GetTraces.md)
 - [GetWebsiteBeaconGroups](docs/GetWebsiteBeaconGroups.md)
 - [GetWebsiteBeacons](docs/GetWebsiteBeacons.md)
 - [GetWebsiteMetrics](docs/GetWebsiteMetrics.md)
 - [GetWebsiteMetricsV2](docs/GetWebsiteMetricsV2.md)
 - [GlobalApplicationAlertConfigWithMetadata](docs/GlobalApplicationAlertConfigWithMetadata.md)
 - [GlobalApplicationsAlertConfig](docs/GlobalApplicationsAlertConfig.md)
 - [GoogleChatIntegration](docs/GoogleChatIntegration.md)
 - [GraphEdge](docs/GraphEdge.md)
 - [GraphNode](docs/GraphNode.md)
 - [Group](docs/Group.md)
 - [GroupByTag](docs/GroupByTag.md)
 - [GroupMapping](docs/GroupMapping.md)
 - [HealthState](docs/HealthState.md)
 - [HistoricBaseline](docs/HistoricBaseline.md)
 - [HostAvailabilityRule](docs/HostAvailabilityRule.md)
 - [HttpActionConfiguration](docs/HttpActionConfiguration.md)
 - [HttpEndpointConfig](docs/HttpEndpointConfig.md)
 - [HttpEndpointRule](docs/HttpEndpointRule.md)
 - [HttpPathSegmentMatchingRule](docs/HttpPathSegmentMatchingRule.md)
 - [HttpScriptConfiguration](docs/HttpScriptConfiguration.md)
 - [HyperParam](docs/HyperParam.md)
 - [IdentityProviderPatch](docs/IdentityProviderPatch.md)
 - [InfraAlertConfig](docs/InfraAlertConfig.md)
 - [InfraAlertConfigWithMetadata](docs/InfraAlertConfigWithMetadata.md)
 - [InfraAlertRule](docs/InfraAlertRule.md)
 - [InfraEventResult](docs/InfraEventResult.md)
 - [InfraMetricConfiguration](docs/InfraMetricConfiguration.md)
 - [InfraTimeThreshold](docs/InfraTimeThreshold.md)
 - [InfrastructureEntitiesResult](docs/InfrastructureEntitiesResult.md)
 - [InfrastructureGroup](docs/InfrastructureGroup.md)
 - [InfrastructureGroupsResult](docs/InfrastructureGroupsResult.md)
 - [InfrastructureItem](docs/InfrastructureItem.md)
 - [InfrastructureMetricResult](docs/InfrastructureMetricResult.md)
 - [InstanaVersionInfo](docs/InstanaVersionInfo.md)
 - [IntegrationOverview](docs/IntegrationOverview.md)
 - [Invitation](docs/Invitation.md)
 - [InvitationResponse](docs/InvitationResponse.md)
 - [InvitationResult](docs/InvitationResult.md)
 - [IpMaskingConfiguration](docs/IpMaskingConfiguration.md)
 - [JsStackTraceLine](docs/JsStackTraceLine.md)
 - [KubernetesPhysicalContext](docs/KubernetesPhysicalContext.md)
 - [LatencyBlueprintIndicator](docs/LatencyBlueprintIndicator.md)
 - [LocationStatus](docs/LocationStatus.md)
 - [LogAlertConfig](docs/LogAlertConfig.md)
 - [LogAlertConfigWithMetadata](docs/LogAlertConfigWithMetadata.md)
 - [LogAlertRule](docs/LogAlertRule.md)
 - [LogCountAlertRule](docs/LogCountAlertRule.md)
 - [LogEntryActor](docs/LogEntryActor.md)
 - [LogEventResult](docs/LogEventResult.md)
 - [LogTimeThreshold](docs/LogTimeThreshold.md)
 - [LogsApplicationAlertRule](docs/LogsApplicationAlertRule.md)
 - [MaintenanceConfig](docs/MaintenanceConfig.md)
 - [MaintenanceConfigScheduling](docs/MaintenanceConfigScheduling.md)
 - [MaintenanceConfigV2](docs/MaintenanceConfigV2.md)
 - [MaintenanceConfigV2WithStateAndOccurrence](docs/MaintenanceConfigV2WithStateAndOccurrence.md)
 - [MaintenanceConfigWithLastUpdated](docs/MaintenanceConfigWithLastUpdated.md)
 - [MaintenanceWindow](docs/MaintenanceWindow.md)
 - [ManualAlertingChannelConfiguration](docs/ManualAlertingChannelConfiguration.md)
 - [ManualCloseInfo](docs/ManualCloseInfo.md)
 - [ManualServiceConfig](docs/ManualServiceConfig.md)
 - [MatchAllHttpPathSegmentMatchingRule](docs/MatchAllHttpPathSegmentMatchingRule.md)
 - [MatchExpressionDTO](docs/MatchExpressionDTO.md)
 - [MetaData](docs/MetaData.md)
 - [MetricAPIResult](docs/MetricAPIResult.md)
 - [MetricConfig](docs/MetricConfig.md)
 - [MetricConfiguration](docs/MetricConfiguration.md)
 - [MetricDescription](docs/MetricDescription.md)
 - [MetricInstance](docs/MetricInstance.md)
 - [MetricItem](docs/MetricItem.md)
 - [MetricMetadata](docs/MetricMetadata.md)
 - [MetricPattern](docs/MetricPattern.md)
 - [MetricsResult](docs/MetricsResult.md)
 - [MetricsResultItem](docs/MetricsResultItem.md)
 - [MetricsTestResultItem](docs/MetricsTestResultItem.md)
 - [MobileApp](docs/MobileApp.md)
 - [MobileAppAlertConfig](docs/MobileAppAlertConfig.md)
 - [MobileAppAlertRule](docs/MobileAppAlertRule.md)
 - [MobileAppBeaconGroupsItem](docs/MobileAppBeaconGroupsItem.md)
 - [MobileAppBeaconGroupsResult](docs/MobileAppBeaconGroupsResult.md)
 - [MobileAppBeaconResult](docs/MobileAppBeaconResult.md)
 - [MobileAppBeaconTagGroup](docs/MobileAppBeaconTagGroup.md)
 - [MobileAppBeaconsItem](docs/MobileAppBeaconsItem.md)
 - [MobileAppEventResult](docs/MobileAppEventResult.md)
 - [MobileAppMetricResult](docs/MobileAppMetricResult.md)
 - [MobileAppMonitoringBeacon](docs/MobileAppMonitoringBeacon.md)
 - [MobileAppMonitoringMetricDescription](docs/MobileAppMonitoringMetricDescription.md)
 - [MobileAppMonitoringMetricsConfiguration](docs/MobileAppMonitoringMetricsConfiguration.md)
 - [MobileAppTimeThreshold](docs/MobileAppTimeThreshold.md)
 - [ModelField](docs/ModelField.md)
 - [MonitoringState](docs/MonitoringState.md)
 - [MultipleScriptsConfiguration](docs/MultipleScriptsConfiguration.md)
 - [NewApplicationConfig](docs/NewApplicationConfig.md)
 - [NewBusinessPerspectiveConfig](docs/NewBusinessPerspectiveConfig.md)
 - [NewManualServiceConfig](docs/NewManualServiceConfig.md)
 - [Occurrence](docs/Occurrence.md)
 - [Office365Integration](docs/Office365Integration.md)
 - [OneTimeMaintenanceWindow](docs/OneTimeMaintenanceWindow.md)
 - [OpsgenieIntegration](docs/OpsgenieIntegration.md)
 - [Order](docs/Order.md)
 - [PagerdutyIntegration](docs/PagerdutyIntegration.md)
 - [PaginatedResult](docs/PaginatedResult.md)
 - [Pagination](docs/Pagination.md)
 - [Parameter](docs/Parameter.md)
 - [ParameterValue](docs/ParameterValue.md)
 - [PathParameterHttpPathSegmentMatchingRule](docs/PathParameterHttpPathSegmentMatchingRule.md)
 - [PhysicalContext](docs/PhysicalContext.md)
 - [PluginResult](docs/PluginResult.md)
 - [Policy](docs/Policy.md)
 - [PolicyRunnable](docs/PolicyRunnable.md)
 - [PostSnapshotsResult](docs/PostSnapshotsResult.md)
 - [Problem](docs/Problem.md)
 - [PrometheusWebhookIntegration](docs/PrometheusWebhookIntegration.md)
 - [RecurrentMaintenanceWindow](docs/RecurrentMaintenanceWindow.md)
 - [Release](docs/Release.md)
 - [ReleaseScope](docs/ReleaseScope.md)
 - [ReleaseWithMetadata](docs/ReleaseWithMetadata.md)
 - [RollingTimeWindow](docs/RollingTimeWindow.md)
 - [RuleInput](docs/RuleInput.md)
 - [RuleWithThresholdApplicationAlertRule](docs/RuleWithThresholdApplicationAlertRule.md)
 - [RuleWithThresholdInfraAlertRule](docs/RuleWithThresholdInfraAlertRule.md)
 - [RuleWithThresholdLogAlertRule](docs/RuleWithThresholdLogAlertRule.md)
 - [RuleWithThresholdMobileAppAlertRule](docs/RuleWithThresholdMobileAppAlertRule.md)
 - [RuleWithThresholdWebsiteAlertRule](docs/RuleWithThresholdWebsiteAlertRule.md)
 - [RunConfiguration](docs/RunConfiguration.md)
 - [SSLCertificateConfiguration](docs/SSLCertificateConfiguration.md)
 - [SalesforceIntegration](docs/SalesforceIntegration.md)
 - [ScopeBinding](docs/ScopeBinding.md)
 - [SearchFieldResult](docs/SearchFieldResult.md)
 - [Service](docs/Service.md)
 - [ServiceConfig](docs/ServiceConfig.md)
 - [ServiceEventResult](docs/ServiceEventResult.md)
 - [ServiceItem](docs/ServiceItem.md)
 - [ServiceLevelIndicator](docs/ServiceLevelIndicator.md)
 - [ServiceLevelObjectiveAlertRule](docs/ServiceLevelObjectiveAlertRule.md)
 - [ServiceLevelObjectiveConfiguration](docs/ServiceLevelObjectiveConfiguration.md)
 - [ServiceLevelsAlertConfig](docs/ServiceLevelsAlertConfig.md)
 - [ServiceLevelsAlertRule](docs/ServiceLevelsAlertRule.md)
 - [ServiceLevelsBurnRateTimeWindows](docs/ServiceLevelsBurnRateTimeWindows.md)
 - [ServiceLevelsTimeThreshold](docs/ServiceLevelsTimeThreshold.md)
 - [ServiceLevelseAlertConfigWithMetadata](docs/ServiceLevelseAlertConfigWithMetadata.md)
 - [ServiceMap](docs/ServiceMap.md)
 - [ServiceMapConnection](docs/ServiceMapConnection.md)
 - [ServiceMatchingRule](docs/ServiceMatchingRule.md)
 - [ServiceMetricResult](docs/ServiceMetricResult.md)
 - [ServiceNode](docs/ServiceNode.md)
 - [ServiceNowEnhancedIntegration](docs/ServiceNowEnhancedIntegration.md)
 - [ServiceNowIntegration](docs/ServiceNowIntegration.md)
 - [ServiceResult](docs/ServiceResult.md)
 - [ServiceScope](docs/ServiceScope.md)
 - [ServiceScopeWithMetadata](docs/ServiceScopeWithMetadata.md)
 - [ServiceScopedTo](docs/ServiceScopedTo.md)
 - [ServiceScopedToWithMetadata](docs/ServiceScopedToWithMetadata.md)
 - [ServiceSimple](docs/ServiceSimple.md)
 - [SessionSettings](docs/SessionSettings.md)
 - [SlackIntegration](docs/SlackIntegration.md)
 - [SliConfiguration](docs/SliConfiguration.md)
 - [SliConfigurationWithLastUpdated](docs/SliConfigurationWithLastUpdated.md)
 - [SliEntity](docs/SliEntity.md)
 - [SliReport](docs/SliReport.md)
 - [SloEntity](docs/SloEntity.md)
 - [SloReport](docs/SloReport.md)
 - [SlownessApplicationAlertRule](docs/SlownessApplicationAlertRule.md)
 - [SlownessWebsiteAlertRule](docs/SlownessWebsiteAlertRule.md)
 - [SnapshotItem](docs/SnapshotItem.md)
 - [SnapshotPreview](docs/SnapshotPreview.md)
 - [SnapshotResult](docs/SnapshotResult.md)
 - [SoftwareUser](docs/SoftwareUser.md)
 - [SoftwareVersion](docs/SoftwareVersion.md)
 - [SourceMapFileBlob](docs/SourceMapFileBlob.md)
 - [SourceMapFileMeta](docs/SourceMapFileMeta.md)
 - [SourceMapUploadConfig](docs/SourceMapUploadConfig.md)
 - [Span](docs/Span.md)
 - [SpanExcerpt](docs/SpanExcerpt.md)
 - [SpanRelation](docs/SpanRelation.md)
 - [SpecificJsErrorsWebsiteAlertRule](docs/SpecificJsErrorsWebsiteAlertRule.md)
 - [SplunkIntegration](docs/SplunkIntegration.md)
 - [StackTraceItem](docs/StackTraceItem.md)
 - [StackTraceLine](docs/StackTraceLine.md)
 - [StaticBaselineThresholdRule](docs/StaticBaselineThresholdRule.md)
 - [StaticStringField](docs/StaticStringField.md)
 - [StaticThreshold](docs/StaticThreshold.md)
 - [StaticThresholdRule](docs/StaticThresholdRule.md)
 - [StatusCodeApplicationAlertRule](docs/StatusCodeApplicationAlertRule.md)
 - [StatusCodeMobileAppAlertRule](docs/StatusCodeMobileAppAlertRule.md)
 - [StatusCodeWebsiteAlertRule](docs/StatusCodeWebsiteAlertRule.md)
 - [SyntheticAlertConfig](docs/SyntheticAlertConfig.md)
 - [SyntheticAlertConfigWithMetadata](docs/SyntheticAlertConfigWithMetadata.md)
 - [SyntheticAlertRule](docs/SyntheticAlertRule.md)
 - [SyntheticCallConfig](docs/SyntheticCallConfig.md)
 - [SyntheticCallRule](docs/SyntheticCallRule.md)
 - [SyntheticCallWithDefaultsConfig](docs/SyntheticCallWithDefaultsConfig.md)
 - [SyntheticCredential](docs/SyntheticCredential.md)
 - [SyntheticDatacenter](docs/SyntheticDatacenter.md)
 - [SyntheticDatacenterConfiguration](docs/SyntheticDatacenterConfiguration.md)
 - [SyntheticGeoPoint](docs/SyntheticGeoPoint.md)
 - [SyntheticLocation](docs/SyntheticLocation.md)
 - [SyntheticLocationConfiguration](docs/SyntheticLocationConfiguration.md)
 - [SyntheticMetricConfiguration](docs/SyntheticMetricConfiguration.md)
 - [SyntheticMetricTagGroup](docs/SyntheticMetricTagGroup.md)
 - [SyntheticPlaybackCapabilities](docs/SyntheticPlaybackCapabilities.md)
 - [SyntheticSloEntity](docs/SyntheticSloEntity.md)
 - [SyntheticTest](docs/SyntheticTest.md)
 - [SyntheticTimeThreshold](docs/SyntheticTimeThreshold.md)
 - [SyntheticTypeConfiguration](docs/SyntheticTypeConfiguration.md)
 - [SyntheticsEventResult](docs/SyntheticsEventResult.md)
 - [SystemRule](docs/SystemRule.md)
 - [SystemRuleLabel](docs/SystemRuleLabel.md)
 - [Tag](docs/Tag.md)
 - [TagCatalog](docs/TagCatalog.md)
 - [TagFilter](docs/TagFilter.md)
 - [TagFilterExpression](docs/TagFilterExpression.md)
 - [TagFilterExpressionElement](docs/TagFilterExpressionElement.md)
 - [TagMatcherDTO](docs/TagMatcherDTO.md)
 - [TagTreeLevel](docs/TagTreeLevel.md)
 - [TagTreeNode](docs/TagTreeNode.md)
 - [TagTreeTag](docs/TagTreeTag.md)
 - [TestCommonProperties](docs/TestCommonProperties.md)
 - [TestResult](docs/TestResult.md)
 - [TestResultCommonProperties](docs/TestResultCommonProperties.md)
 - [TestResultDetailData](docs/TestResultDetailData.md)
 - [TestResultItem](docs/TestResultItem.md)
 - [TestResultListItem](docs/TestResultListItem.md)
 - [TestResultListResult](docs/TestResultListResult.md)
 - [TestResultMetadata](docs/TestResultMetadata.md)
 - [TestResultSubtransaction](docs/TestResultSubtransaction.md)
 - [Threshold](docs/Threshold.md)
 - [ThresholdConfigRule](docs/ThresholdConfigRule.md)
 - [ThresholdRule](docs/ThresholdRule.md)
 - [ThroughputApplicationAlertRule](docs/ThroughputApplicationAlertRule.md)
 - [ThroughputMobileAppAlertRule](docs/ThroughputMobileAppAlertRule.md)
 - [ThroughputWebsiteAlertRule](docs/ThroughputWebsiteAlertRule.md)
 - [TimeFrame](docs/TimeFrame.md)
 - [TimeWindow](docs/TimeWindow.md)
 - [Topology](docs/Topology.md)
 - [Trace](docs/Trace.md)
 - [TraceActivityTreeNodeDetails](docs/TraceActivityTreeNodeDetails.md)
 - [TraceDownloadResult](docs/TraceDownloadResult.md)
 - [TraceGroupsItem](docs/TraceGroupsItem.md)
 - [TraceGroupsResult](docs/TraceGroupsResult.md)
 - [TraceImpactApplicationTimeThreshold](docs/TraceImpactApplicationTimeThreshold.md)
 - [TraceItem](docs/TraceItem.md)
 - [TraceResult](docs/TraceResult.md)
 - [TrafficBlueprintIndicator](docs/TrafficBlueprintIndicator.md)
 - [Trigger](docs/Trigger.md)
 - [TypeConfiguration](docs/TypeConfiguration.md)
 - [UnsupportedHttpPathSegmentMatchingRule](docs/UnsupportedHttpPathSegmentMatchingRule.md)
 - [UpdatedBusinessPerspectiveConfig](docs/UpdatedBusinessPerspectiveConfig.md)
 - [UsageResult](docs/UsageResult.md)
 - [UsageResultItems](docs/UsageResultItems.md)
 - [UserBasicResult](docs/UserBasicResult.md)
 - [UserImpactMobileAppTimeThreshold](docs/UserImpactMobileAppTimeThreshold.md)
 - [UserImpactWebsiteTimeThreshold](docs/UserImpactWebsiteTimeThreshold.md)
 - [UserResult](docs/UserResult.md)
 - [UsersResult](docs/UsersResult.md)
 - [ValidatedAlertingChannelInputInfo](docs/ValidatedAlertingChannelInputInfo.md)
 - [ValidatedAlertingConfiguration](docs/ValidatedAlertingConfiguration.md)
 - [ValidatedMaintenanceConfigV2WithStateAndOccurrence](docs/ValidatedMaintenanceConfigV2WithStateAndOccurrence.md)
 - [ValidatedMaintenanceConfigWithStatus](docs/ValidatedMaintenanceConfigWithStatus.md)
 - [VictorOpsIntegration](docs/VictorOpsIntegration.md)
 - [ViolationsInPeriodApplicationTimeThreshold](docs/ViolationsInPeriodApplicationTimeThreshold.md)
 - [ViolationsInPeriodMobileAppTimeThreshold](docs/ViolationsInPeriodMobileAppTimeThreshold.md)
 - [ViolationsInPeriodWebsiteTimeThreshold](docs/ViolationsInPeriodWebsiteTimeThreshold.md)
 - [ViolationsInSequenceApplicationTimeThreshold](docs/ViolationsInSequenceApplicationTimeThreshold.md)
 - [ViolationsInSequenceInfraTimeThreshold](docs/ViolationsInSequenceInfraTimeThreshold.md)
 - [ViolationsInSequenceLogTimeThreshold](docs/ViolationsInSequenceLogTimeThreshold.md)
 - [ViolationsInSequenceMobileAppTimeThreshold](docs/ViolationsInSequenceMobileAppTimeThreshold.md)
 - [ViolationsInSequenceSyntheticTimeThreshold](docs/ViolationsInSequenceSyntheticTimeThreshold.md)
 - [ViolationsInSequenceWebsiteTimeThreshold](docs/ViolationsInSequenceWebsiteTimeThreshold.md)
 - [WatsonAIOpsWebhookIntegration](docs/WatsonAIOpsWebhookIntegration.md)
 - [WebexTeamsWebhookIntegration](docs/WebexTeamsWebhookIntegration.md)
 - [WebhookIntegration](docs/WebhookIntegration.md)
 - [WebpageActionConfiguration](docs/WebpageActionConfiguration.md)
 - [WebpageScriptConfiguration](docs/WebpageScriptConfiguration.md)
 - [Website](docs/Website.md)
 - [WebsiteAlertConfig](docs/WebsiteAlertConfig.md)
 - [WebsiteAlertConfigWithMetadata](docs/WebsiteAlertConfigWithMetadata.md)
 - [WebsiteAlertRule](docs/WebsiteAlertRule.md)
 - [WebsiteApdexEntity](docs/WebsiteApdexEntity.md)
 - [WebsiteBeaconGroupsItem](docs/WebsiteBeaconGroupsItem.md)
 - [WebsiteBeaconGroupsResult](docs/WebsiteBeaconGroupsResult.md)
 - [WebsiteBeaconResult](docs/WebsiteBeaconResult.md)
 - [WebsiteBeaconTagGroup](docs/WebsiteBeaconTagGroup.md)
 - [WebsiteBeaconsItem](docs/WebsiteBeaconsItem.md)
 - [WebsiteEventBasedSliEntity](docs/WebsiteEventBasedSliEntity.md)
 - [WebsiteEventResult](docs/WebsiteEventResult.md)
 - [WebsiteMetricResult](docs/WebsiteMetricResult.md)
 - [WebsiteMonitoringBeacon](docs/WebsiteMonitoringBeacon.md)
 - [WebsiteMonitoringMetricDescription](docs/WebsiteMonitoringMetricDescription.md)
 - [WebsiteMonitoringMetricsConfiguration](docs/WebsiteMonitoringMetricsConfiguration.md)
 - [WebsiteSloEntity](docs/WebsiteSloEntity.md)
 - [WebsiteTimeBasedSliEntity](docs/WebsiteTimeBasedSliEntity.md)
 - [WebsiteTimeThreshold](docs/WebsiteTimeThreshold.md)
 - [Widget](docs/Widget.md)
 - [WithMetadata](docs/WithMetadata.md)
 - [WithResolvedName](docs/WithResolvedName.md)
 - [ZChatOpsIntegration](docs/ZChatOpsIntegration.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="ApiKeyAuth"></a>
### ApiKeyAuth

- **Type**: API key
- **API key parameter name**: authorization
- **Location**: HTTP header


## Author

support@instana.com


