# coding: utf-8

"""
    Instana REST API documentation

    Searching for answers and best pratices? Check our [IBM Instana Community](https://community.ibm.com/community/user/aiops/communities/community-home?CommunityKey=58f324a3-3104-41be-9510-5b7c413cc48f).  ## Overview The Instana REST API provides programmatic access to the Instana platform. It can be used to retrieve data available through the Instana UI Dashboard -- metrics, events, traces, etc -- and also to automate configuration tasks such as user management.  ### Navigating the API documentation The API endpoints are grouped by product area and functionality. This generally maps to how our UI Dashboard is organized, hopefully making it easier to locate which endpoints you'd use to fetch the data you see visualized in our UI. The [UI sections](https://www.ibm.com/docs/en/instana-observability/current?topic=working-user-interface#navigation-menu) include: - Websites & Mobile Apps - Applications - Infrastructure - Synthetic Monitoring - Events - Automation - Service Levels - Settings - etc  ### Rate Limiting A rate limit is applied to API usage. Up to 5,000 calls per hour can be made. How many remaining calls can be made and when this call limit resets, can inspected via three headers that are part of the responses of the API server.  - **X-RateLimit-Limit:** Shows the maximum number of calls that may be executed per hour. - **X-RateLimit-Remaining:** How many calls may still be executed within the current hour. - **X-RateLimit-Reset:** Time when the remaining calls will be reset to the limit. For compatibility reasons with other rate limited APIs, this date is not the date in milliseconds, but instead in seconds since 1970-01-01T00:00:00+00:00.  ### Further Reading We provide additional documentation for our REST API in our [product documentation](https://www.ibm.com/docs/en/instana-observability/current?topic=apis-web-rest-api). Here you'll also find some common queries for retrieving data and configuring Instana.  ## Getting Started with the REST API  ### API base URL The base URL for an specific instance of Instana can be determined using the tenant and unit information. - `base`: This is the base URL of a tenant unit, e.g. `https://test-example.instana.io`. This is the same URL that is used to access the Instana user interface. - `apiToken`: Requests against the Instana API require valid API tokens. An initial API token can be generated via the Instana user interface. Any additional API tokens can be generated via the API itself.  ### Curl Example Here is an Example to use the REST API with Curl. First lets get all the available metrics with possible aggregations with a GET call.  ```bash curl --request GET \\   --url https://test-instana.instana.io/api/application-monitoring/catalog/metrics \\   --header 'authorization: apiToken xxxxxxxxxxxxxxxx' ```  Next we can get every call grouped by the endpoint name that has an error count greater then zero. As a metric we could get the mean error rate for example.  ```bash curl --request POST \\   --url https://test-instana.instana.io/api/application-monitoring/analyze/call-groups \\   --header 'authorization: apiToken xxxxxxxxxxxxxxxx' \\   --header 'content-type: application/json' \\   --data '{   \"group\":{       \"groupbyTag\":\"endpoint.name\"   },   \"tagFilters\":[    {     \"name\":\"call.error.count\",     \"value\":\"0\",     \"operator\":\"GREATER_THAN\"    }   ],   \"metrics\":[    {     \"metric\":\"errors\",     \"aggregation\":\"MEAN\"    }   ]   }' ```  ### Generating REST API clients  The API is specified using the [OpenAPI v3](https://github.com/OAI/OpenAPI-Specification) (previously known as Swagger) format. You can download the current specification at our [GitHub API documentation](https://instana.github.io/openapi/openapi.yaml).  OpenAPI tries to solve the issue of ever-evolving APIs and clients lagging behind. Please make sure that you always use the latest version of the generator, as a number of improvements are regularly made. To generate a client library for your language, you can use the [OpenAPI client generators](https://github.com/OpenAPITools/openapi-generator).  #### Go For example, to generate a client library for Go to interact with our backend, you can use the following script; mind replacing the values of the `UNIT_NAME` and `TENANT_NAME` environment variables using those for your tenant unit:  ```bash #!/bin/bash  ### This script assumes you have the `java` and `wget` commands on the path  export UNIT_NAME='myunit' # for example: prod export TENANT_NAME='mytenant' # for example: awesomecompany  //Download the generator to your current working directory: wget https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/4.3.1/openapi-generator-cli-4.3.1.jar -O openapi-generator-cli.jar --server-variables \"tenant=${TENANT_NAME},unit=${UNIT_NAME}\"  //generate a client library that you can vendor into your repository java -jar openapi-generator-cli.jar generate -i https://instana.github.io/openapi/openapi.yaml -g go \\     -o pkg/instana/openapi \\     --skip-validate-spec  //(optional) format the Go code according to the Go code standard gofmt -s -w pkg/instana/openapi ```  The generated clients contain comprehensive READMEs, and you can start right away using the client from the example above:  ```go import instana \"./pkg/instana/openapi\"  // readTags will read all available application monitoring tags along with their type and category func readTags() {  configuration := instana.NewConfiguration()  configuration.Host = \"tenant-unit.instana.io\"  configuration.BasePath = \"https://tenant-unit.instana.io\"   client := instana.NewAPIClient(configuration)  auth := context.WithValue(context.Background(), instana.ContextAPIKey, instana.APIKey{   Key:    apiKey,   Prefix: \"apiToken\",  })   tags, _, err := client.ApplicationCatalogApi.GetApplicationTagCatalog(auth)  if err != nil {   fmt.Fatalf(\"Error calling the API, aborting.\")  }   for _, tag := range tags {   fmt.Printf(\"%s (%s): %s\\n\", tag.Category, tag.Type, tag.Name)  } } ```  #### Java Follow the instructions provided in the official documentation from [OpenAPI Tools](https://github.com/OpenAPITools) to download the [openapi-generator-cli.jar](https://github.com/OpenAPITools/openapi-generator?tab=readme-ov-file#13---download-jar).  Depending on your environment, use one of the following java http client implementations which will create a valid client for our OpenAPI specification: ``` //Nativ Java HTTP Client java -jar openapi-generator-cli.jar generate -i https://instana.github.io/openapi/openapi.yaml -g java -o pkg/instana/openapi --skip-validate-spec  -p dateLibrary=java8 --library native  //Spring WebClient java -jar openapi-generator-cli.jar generate -i https://instana.github.io/openapi/openapi.yaml -g java -o pkg/instana/openapi --skip-validate-spec  -p dateLibrary=java8,hideGenerationTimestamp=true --library webclient  //Spring RestTemplate java -jar openapi-generator-cli.jar generate -i https://instana.github.io/openapi/openapi.yaml -g java -o pkg/instana/openapi --skip-validate-spec  -p dateLibrary=java8,hideGenerationTimestamp=true --library resttemplate  ``` 

    The version of the OpenAPI document: 1.291.1002
    Contact: support@instana.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from instana_client.models.api_token import ApiToken

class TestApiToken(unittest.TestCase):
    """ApiToken unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiToken:
        """Test ApiToken
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiToken`
        """
        model = ApiToken()
        if include_optional:
            return ApiToken(
                access_granting_token = '',
                can_configure_agent_run_mode = True,
                can_configure_agents = True,
                can_configure_api_tokens = True,
                can_configure_application_smart_alerts = True,
                can_configure_applications = True,
                can_configure_authentication_methods = True,
                can_configure_automation_actions = True,
                can_configure_automation_policies = True,
                can_configure_bizops = True,
                can_configure_database_management = True,
                can_configure_eum_applications = True,
                can_configure_events_and_alerts = True,
                can_configure_global_alert_payload = True,
                can_configure_global_application_smart_alerts = True,
                can_configure_global_infra_smart_alerts = True,
                can_configure_global_log_smart_alerts = True,
                can_configure_global_synthetic_smart_alerts = True,
                can_configure_integrations = True,
                can_configure_log_management = True,
                can_configure_log_retention_period = True,
                can_configure_maintenance_windows = True,
                can_configure_mobile_app_monitoring = True,
                can_configure_mobile_app_smart_alerts = True,
                can_configure_personal_api_tokens = True,
                can_configure_releases = True,
                can_configure_service_level_indicators = True,
                can_configure_service_mapping = True,
                can_configure_session_settings = True,
                can_configure_subtraces = True,
                can_configure_synthetic_credentials = True,
                can_configure_synthetic_locations = True,
                can_configure_synthetic_tests = True,
                can_configure_teams = True,
                can_configure_users = True,
                can_configure_website_smart_alerts = True,
                can_create_heap_dump = True,
                can_create_public_custom_dashboards = True,
                can_create_thread_dump = True,
                can_delete_automation_action_history = True,
                can_delete_logs = True,
                can_edit_all_accessible_custom_dashboards = True,
                can_install_new_agents = True,
                can_invoke_alert_channel = True,
                can_manually_close_issue = True,
                can_run_automation_actions = True,
                can_use_synthetic_credentials = True,
                can_view_account_and_billing_information = True,
                can_view_audit_log = True,
                can_view_biz_alerts = True,
                can_view_business_activities = True,
                can_view_business_process_details = True,
                can_view_business_processes = True,
                can_view_log_volume = True,
                can_view_logs = True,
                can_view_synthetic_locations = True,
                can_view_synthetic_test_results = True,
                can_view_synthetic_tests = True,
                can_view_trace_details = True,
                created_by = '',
                created_on = 56,
                expires_on = 56,
                id = '',
                internal_id = '',
                last_used_on = 56,
                limited_applications_scope = True,
                limited_automation_scope = True,
                limited_biz_ops_scope = True,
                limited_infrastructure_scope = True,
                limited_kubernetes_scope = True,
                limited_logs_scope = True,
                limited_mobile_apps_scope = True,
                limited_nutanix_scope = True,
                limited_openstack_scope = True,
                limited_pcf_scope = True,
                limited_phmc_scope = True,
                limited_pvc_scope = True,
                limited_synthetics_scope = True,
                limited_vsphere_scope = True,
                limited_websites_scope = True,
                limited_zhmc_scope = True,
                name = ''
            )
        else:
            return ApiToken(
                access_granting_token = '',
                internal_id = '',
                name = '',
        )
        """

    def testApiToken(self):
        """Test ApiToken"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
