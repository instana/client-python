# ApiToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_granting_token** | **str** |  | 
**can_configure_agent_run_mode** | **bool** |  | [optional] 
**can_configure_agents** | **bool** |  | [optional] 
**can_configure_ai_agents** | **bool** |  | [optional] 
**can_configure_api_tokens** | **bool** |  | [optional] 
**can_configure_application_smart_alerts** | **bool** |  | [optional] 
**can_configure_applications** | **bool** |  | [optional] 
**can_configure_authentication_methods** | **bool** |  | [optional] 
**can_configure_automation_actions** | **bool** |  | [optional] 
**can_configure_automation_policies** | **bool** |  | [optional] 
**can_configure_bizops** | **bool** |  | [optional] 
**can_configure_database_management** | **bool** |  | [optional] 
**can_configure_eum_applications** | **bool** |  | [optional] 
**can_configure_events_and_alerts** | **bool** |  | [optional] 
**can_configure_global_alert_payload** | **bool** |  | [optional] 
**can_configure_global_application_smart_alerts** | **bool** |  | [optional] 
**can_configure_global_infra_smart_alerts** | **bool** |  | [optional] 
**can_configure_global_log_smart_alerts** | **bool** |  | [optional] 
**can_configure_global_synthetic_smart_alerts** | **bool** |  | [optional] 
**can_configure_integrations** | **bool** |  | [optional] 
**can_configure_llm** | **bool** |  | [optional] 
**can_configure_log_management** | **bool** |  | [optional] 
**can_configure_log_retention_period** | **bool** |  | [optional] 
**can_configure_maintenance_windows** | **bool** |  | [optional] 
**can_configure_mobile_app_monitoring** | **bool** |  | [optional] 
**can_configure_mobile_app_smart_alerts** | **bool** |  | [optional] 
**can_configure_personal_api_tokens** | **bool** |  | [optional] 
**can_configure_releases** | **bool** |  | [optional] 
**can_configure_service_level_indicators** | **bool** |  | [optional] 
**can_configure_service_mapping** | **bool** |  | [optional] 
**can_configure_session_settings** | **bool** |  | [optional] 
**can_configure_subtraces** | **bool** |  | [optional] 
**can_configure_synthetic_credentials** | **bool** |  | [optional] 
**can_configure_synthetic_locations** | **bool** |  | [optional] 
**can_configure_synthetic_tests** | **bool** |  | [optional] 
**can_configure_teams** | **bool** |  | [optional] 
**can_configure_users** | **bool** |  | [optional] 
**can_configure_website_smart_alerts** | **bool** |  | [optional] 
**can_create_heap_dump** | **bool** |  | [optional] 
**can_create_public_custom_dashboards** | **bool** |  | [optional] 
**can_create_thread_dump** | **bool** |  | [optional] 
**can_delete_automation_action_history** | **bool** |  | [optional] 
**can_delete_logs** | **bool** |  | [optional] 
**can_edit_all_accessible_custom_dashboards** | **bool** |  | [optional] 
**can_install_new_agents** | **bool** |  | [optional] 
**can_invoke_alert_channel** | **bool** |  | [optional] 
**can_manually_close_issue** | **bool** |  | [optional] 
**can_run_automation_actions** | **bool** |  | [optional] 
**can_use_synthetic_credentials** | **bool** |  | [optional] 
**can_view_account_and_billing_information** | **bool** |  | [optional] 
**can_view_audit_log** | **bool** |  | [optional] 
**can_view_biz_alerts** | **bool** |  | [optional] 
**can_view_business_activities** | **bool** |  | [optional] 
**can_view_business_process_details** | **bool** |  | [optional] 
**can_view_business_processes** | **bool** |  | [optional] 
**can_view_log_volume** | **bool** |  | [optional] 
**can_view_logs** | **bool** |  | [optional] 
**can_view_synthetic_locations** | **bool** |  | [optional] 
**can_view_synthetic_test_results** | **bool** |  | [optional] 
**can_view_synthetic_tests** | **bool** |  | [optional] 
**can_view_trace_details** | **bool** |  | [optional] 
**created_by** | **str** |  | [optional] 
**created_on** | **int** |  | [optional] 
**expires_on** | **int** |  | [optional] 
**id** | **str** |  | [optional] 
**internal_id** | **str** |  | 
**last_used_on** | **int** |  | [optional] 
**limited_alert_channels_scope** | **bool** |  | [optional] 
**limited_applications_scope** | **bool** |  | [optional] 
**limited_automation_scope** | **bool** |  | [optional] 
**limited_biz_ops_scope** | **bool** |  | [optional] 
**limited_infrastructure_scope** | **bool** |  | [optional] 
**limited_kubernetes_scope** | **bool** |  | [optional] 
**limited_linux_kvm_hypervisor_scope** | **bool** |  | [optional] 
**limited_logs_scope** | **bool** |  | [optional] 
**limited_mobile_apps_scope** | **bool** |  | [optional] 
**limited_nutanix_scope** | **bool** |  | [optional] 
**limited_openstack_scope** | **bool** |  | [optional] 
**limited_pcf_scope** | **bool** |  | [optional] 
**limited_phmc_scope** | **bool** |  | [optional] 
**limited_pvc_scope** | **bool** |  | [optional] 
**limited_synthetics_scope** | **bool** |  | [optional] 
**limited_vsphere_scope** | **bool** |  | [optional] 
**limited_websites_scope** | **bool** |  | [optional] 
**limited_windows_hypervisor_scope** | **bool** |  | [optional] 
**limited_xen_server_scope** | **bool** |  | [optional] 
**limited_zhmc_scope** | **bool** |  | [optional] 
**name** | **str** |  | 

## Example

```python
from instana_client.models.api_token import ApiToken

# TODO update the JSON string below
json = "{}"
# create an instance of ApiToken from a JSON string
api_token_instance = ApiToken.from_json(json)
# print the JSON string representation of the object
print(ApiToken.to_json())

# convert the object into a dict
api_token_dict = api_token_instance.to_dict()
# create an instance of ApiToken from a dict
api_token_from_dict = ApiToken.from_dict(api_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


