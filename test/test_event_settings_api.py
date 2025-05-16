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

from instana_client.api.event_settings_api import EventSettingsApi


class TestEventSettingsApi(unittest.TestCase):
    """EventSettingsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = EventSettingsApi()

    def tearDown(self) -> None:
        pass

    def test_create_mobile_app_alert_config(self) -> None:
        """Test case for create_mobile_app_alert_config

        Create Mobile Smart Alert Config
        """
        pass

    def test_create_website_alert_config(self) -> None:
        """Test case for create_website_alert_config

        Create Website Smart Alert Config
        """
        pass

    def test_delete_alert(self) -> None:
        """Test case for delete_alert

        Delete Alert Configuration
        """
        pass

    def test_delete_alerting_channel(self) -> None:
        """Test case for delete_alerting_channel

        Delete Alerting Channel
        """
        pass

    def test_delete_built_in_event_specification(self) -> None:
        """Test case for delete_built_in_event_specification

        Delete built-in event specification
        """
        pass

    def test_delete_custom_event_specification(self) -> None:
        """Test case for delete_custom_event_specification

        Delete custom event specification
        """
        pass

    def test_delete_custom_payload_configuration(self) -> None:
        """Test case for delete_custom_payload_configuration

        Delete Custom Payload Configuration
        """
        pass

    def test_delete_mobile_app_alert_config(self) -> None:
        """Test case for delete_mobile_app_alert_config

        Delete Mobile Smart Alert Config
        """
        pass

    def test_delete_website_alert_config(self) -> None:
        """Test case for delete_website_alert_config

        Delete Website Smart Alert Config
        """
        pass

    def test_disable_built_in_event_specification(self) -> None:
        """Test case for disable_built_in_event_specification

        Disable built-in event specification
        """
        pass

    def test_disable_custom_event_specification(self) -> None:
        """Test case for disable_custom_event_specification

        Disable custom event specification
        """
        pass

    def test_disable_mobile_app_alert_config(self) -> None:
        """Test case for disable_mobile_app_alert_config

        Disable Mobile Smart Alert Config
        """
        pass

    def test_disable_website_alert_config(self) -> None:
        """Test case for disable_website_alert_config

        Disable Website Smart Alert Config
        """
        pass

    def test_enable_built_in_event_specification(self) -> None:
        """Test case for enable_built_in_event_specification

        Enable built-in event specification
        """
        pass

    def test_enable_custom_event_specification(self) -> None:
        """Test case for enable_custom_event_specification

        Enable custom event specification
        """
        pass

    def test_enable_mobile_app_alert_config(self) -> None:
        """Test case for enable_mobile_app_alert_config

        Enable Mobile Smart Alert Config
        """
        pass

    def test_enable_website_alert_config(self) -> None:
        """Test case for enable_website_alert_config

        Enable Website Smart Alert Config
        """
        pass

    def test_find_active_mobile_app_alert_configs(self) -> None:
        """Test case for find_active_mobile_app_alert_configs

        Get all Mobile Smart Alert Configs
        """
        pass

    def test_find_active_website_alert_configs(self) -> None:
        """Test case for find_active_website_alert_configs

        Get all Website Smart Alert Configs
        """
        pass

    def test_find_mobile_app_alert_config(self) -> None:
        """Test case for find_mobile_app_alert_config

        Get Mobile Smart Alert Config
        """
        pass

    def test_find_mobile_app_alert_config_versions(self) -> None:
        """Test case for find_mobile_app_alert_config_versions

        Get Mobile Smart Alert Config Versions
        """
        pass

    def test_find_website_alert_config(self) -> None:
        """Test case for find_website_alert_config

        Get Website Smart Alert Config
        """
        pass

    def test_find_website_alert_config_versions(self) -> None:
        """Test case for find_website_alert_config_versions

        Get Website Smart Alert Config Versions. 
        """
        pass

    def test_get_alert(self) -> None:
        """Test case for get_alert

        Get Alert Configuration
        """
        pass

    def test_get_alerting_channel(self) -> None:
        """Test case for get_alerting_channel

        Get Alerting Channel
        """
        pass

    def test_get_alerting_channels(self) -> None:
        """Test case for get_alerting_channels

        Get all Alerting Channels
        """
        pass

    def test_get_alerting_channels_overview(self) -> None:
        """Test case for get_alerting_channels_overview

        Get Overview of Alerting Channels
        """
        pass

    def test_get_alerting_configuration_infos(self) -> None:
        """Test case for get_alerting_configuration_infos

        All alerting configuration info
        """
        pass

    def test_get_alerts(self) -> None:
        """Test case for get_alerts

        Get all Alert Configurations
        """
        pass

    def test_get_built_in_event_specification(self) -> None:
        """Test case for get_built_in_event_specification

        Built-in event specifications
        """
        pass

    def test_get_built_in_event_specifications(self) -> None:
        """Test case for get_built_in_event_specifications

        All built-in event specification
        """
        pass

    def test_get_custom_event_specification(self) -> None:
        """Test case for get_custom_event_specification

        Custom event specification
        """
        pass

    def test_get_custom_event_specifications(self) -> None:
        """Test case for get_custom_event_specifications

        All custom event specifications
        """
        pass

    def test_get_custom_payload_configurations(self) -> None:
        """Test case for get_custom_payload_configurations

        Get All Global Custom Payload Configurations
        """
        pass

    def test_get_custom_payload_tag_catalog(self) -> None:
        """Test case for get_custom_payload_tag_catalog

        Get Tag Catalog for Custom Payload
        """
        pass

    def test_get_event_specification_infos(self) -> None:
        """Test case for get_event_specification_infos

        Summary of all built-in and custom event specifications
        """
        pass

    def test_get_event_specification_infos_by_ids(self) -> None:
        """Test case for get_event_specification_infos_by_ids

        All built-in and custom event specifications
        """
        pass

    def test_get_system_rules(self) -> None:
        """Test case for get_system_rules

        All system rules for custom event specifications
        """
        pass

    def test_manually_close_event(self) -> None:
        """Test case for manually_close_event

        Manually close an event.
        """
        pass

    def test_multi_close_event(self) -> None:
        """Test case for multi_close_event

        Manually closing multiple events
        """
        pass

    def test_post_custom_event_specification(self) -> None:
        """Test case for post_custom_event_specification

        Create new custom event specification
        """
        pass

    def test_put_alert(self) -> None:
        """Test case for put_alert

        Create or update Alert Configuration
        """
        pass

    def test_put_alerting_channel(self) -> None:
        """Test case for put_alerting_channel

        Update Alert Channel
        """
        pass

    def test_put_custom_event_specification(self) -> None:
        """Test case for put_custom_event_specification

        Create or update custom event specification
        """
        pass

    def test_restore_mobile_app_alert_config(self) -> None:
        """Test case for restore_mobile_app_alert_config

        Restore Mobile Smart Alert Config
        """
        pass

    def test_restore_website_alert_config(self) -> None:
        """Test case for restore_website_alert_config

        Restore Website Smart Alert Config
        """
        pass

    def test_send_test_alerting(self) -> None:
        """Test case for send_test_alerting

        Test Alerting Channel
        """
        pass

    def test_send_test_alerting_by_id(self) -> None:
        """Test case for send_test_alerting_by_id

        Notify manually to Alerting Channel
        """
        pass

    def test_update_mobile_app_alert_config(self) -> None:
        """Test case for update_mobile_app_alert_config

        Update Mobile Smart Alert Config
        """
        pass

    def test_update_mobile_app_historic_baseline(self) -> None:
        """Test case for update_mobile_app_historic_baseline

        Recalculate Mobile Smart Alert Config Baseline
        """
        pass

    def test_update_website_alert_config(self) -> None:
        """Test case for update_website_alert_config

        Update Website Smart Alert Config
        """
        pass

    def test_update_website_historic_baseline(self) -> None:
        """Test case for update_website_historic_baseline

        Recalculate Website Smart Alert Config Baseline
        """
        pass

    def test_upsert_custom_payload_configuration(self) -> None:
        """Test case for upsert_custom_payload_configuration

        Create/Update Global Custom Payload Configuration
        """
        pass


if __name__ == '__main__':
    unittest.main()
