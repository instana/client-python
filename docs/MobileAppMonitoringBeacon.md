# MobileAppMonitoringBeacon


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accuracy_radius** | **int** |  | [optional] 
**agent_version** | **str** |  | [optional] 
**app_build** | **str** |  | [optional] 
**app_version** | **str** |  | [optional] 
**app_version_number** | **int** |  | [optional] 
**available_mb** | **int** |  | [optional] 
**backend_trace_id** | **str** |  | [optional] 
**batch_size** | **int** |  | [optional] 
**beacon_id** | **str** |  | 
**bundle_identifier** | **str** |  | [optional] 
**carrier** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**clock_skew** | **int** |  | [optional] 
**cold_start_time_ms** | **int** |  | [optional] 
**connection_type** | **str** |  | [optional] 
**continent** | **str** |  | [optional] 
**continent_code** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**custom_event_name** | **str** |  | [optional] 
**custom_metric** | **float** |  | [optional] 
**decoded_body_size** | **int** |  | [optional] 
**device_hardware** | **str** |  | [optional] 
**device_manufacturer** | **str** |  | [optional] 
**device_model** | **str** |  | [optional] 
**duration** | **int** |  | [optional] 
**effective_connection_type** | **str** |  | [optional] 
**encoded_body_size** | **int** |  | [optional] 
**environment** | **str** |  | [optional] 
**error_count** | **int** |  | [optional] 
**error_id** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 
**error_type** | **str** |  | [optional] 
**google_play_services_missing** | **bool** |  | [optional] 
**hot_start_time_ms** | **int** |  | [optional] 
**http_call_headers** | **Dict[str, str]** |  | [optional] 
**http_call_method** | **str** |  | [optional] 
**http_call_origin** | **str** |  | [optional] 
**http_call_path** | **str** |  | [optional] 
**http_call_status** | **int** |  | [optional] 
**http_call_url** | **str** |  | [optional] 
**ingestion_time** | **int** |  | [optional] 
**internal_meta** | **Dict[str, str]** |  | [optional] 
**latitude** | **float** |  | [optional] 
**longitude** | **float** |  | [optional] 
**max_mb** | **int** |  | [optional] 
**meta** | **Dict[str, str]** |  | [optional] 
**mobile_app_id** | **str** |  | 
**mobile_app_label** | **str** |  | [optional] 
**os_name** | **str** |  | [optional] 
**os_version** | **str** |  | [optional] 
**parent_beacon_id** | **str** |  | [optional] 
**parsed_stack_trace** | **str** |  | [optional] 
**performance_subtype** | **str** |  | 
**platform** | **str** |  | [optional] 
**region** | **str** |  | [optional] 
**rooted** | **bool** |  | [optional] 
**session_id** | **str** |  | 
**stack_trace** | **str** |  | [optional] 
**stack_trace_key_checksum** | **str** |  | [optional] 
**stack_trace_key_information** | **str** |  | [optional] 
**stack_trace_line** | [**List[StackTraceLine]**](StackTraceLine.md) |  | [optional] 
**stack_trace_parsing_status** | **int** |  | [optional] 
**subdivision** | **str** |  | [optional] 
**subdivision_code** | **str** |  | [optional] 
**tenant** | **str** |  | [optional] 
**timestamp** | **int** |  | [optional] 
**transfer_size** | **int** |  | [optional] 
**type** | **str** |  | 
**unit** | **str** |  | [optional] 
**use_features** | **List[str]** |  | [optional] 
**used_mb** | **int** |  | [optional] 
**user_email** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**user_ip** | **str** |  | [optional] 
**user_languages** | **List[str]** |  | [optional] 
**user_name** | **str** |  | [optional] 
**user_session_id** | **str** |  | [optional] 
**view** | **str** |  | [optional] 
**viewport_height** | **int** |  | [optional] 
**viewport_width** | **int** |  | [optional] 
**warm_start_time_ms** | **int** |  | [optional] 

## Example

```python
from instana_client.models.mobile_app_monitoring_beacon import MobileAppMonitoringBeacon

# TODO update the JSON string below
json = "{}"
# create an instance of MobileAppMonitoringBeacon from a JSON string
mobile_app_monitoring_beacon_instance = MobileAppMonitoringBeacon.from_json(json)
# print the JSON string representation of the object
print(MobileAppMonitoringBeacon.to_json())

# convert the object into a dict
mobile_app_monitoring_beacon_dict = mobile_app_monitoring_beacon_instance.to_dict()
# create an instance of MobileAppMonitoringBeacon from a dict
mobile_app_monitoring_beacon_from_dict = MobileAppMonitoringBeacon.from_dict(mobile_app_monitoring_beacon_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


