# UnifiedBeacon


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accuracy_radius** | **float** |  | [optional] 
**agent_version** | **str** |  | [optional] 
**app_build** | **str** |  | [optional] 
**app_state** | **str** |  | [optional] 
**app_version** | **str** |  | [optional] 
**available_mb** | **int** |  | [optional] 
**backend_trace_id** | **str** |  | [optional] 
**batch_size** | **int** |  | [optional] 
**beacon_clockskew** | **int** |  | [optional] 
**beacon_id** | **str** |  | [optional] 
**beacon_source** | **str** | Source table: LEGACY (all_mobile_app_monitoring_beacons) or ACTION (all_session_replay_mobile_app_metadata) | [optional] 
**beacon_type** | **str** |  | [optional] 
**bundle_identifier** | **str** |  | [optional] 
**bytes_ingested** | **int** |  | [optional] 
**bytes_ingested_metadata** | **int** |  | [optional] 
**carrier** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**clock_skew** | **int** |  | [optional] 
**cold_start_time_ms** | **int** |  | [optional] 
**connection_type** | **str** |  | [optional] 
**continent** | **str** |  | [optional] 
**continent_code** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**current_app_state** | **str** |  | [optional] 
**custom_event_name** | **str** |  | [optional] 
**custom_metric** | **object** |  | [optional] 
**decoded_body_size** | **int** |  | [optional] 
**device_hardware** | **str** |  | [optional] 
**device_manufacturer** | **str** |  | [optional] 
**device_model** | **str** |  | [optional] 
**drop_view** | **str** |  | [optional] 
**duration** | **int** |  | [optional] 
**effective_connection_type** | **str** |  | [optional] 
**encoded_body_size** | **int** |  | [optional] 
**error_count** | **int** |  | [optional] 
**error_id** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 
**error_type** | **str** |  | [optional] 
**event_type** | **str** |  | [optional] 
**frustration_signal** | **str** |  | [optional] 
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
**keyboard_operation** | **str** |  | [optional] 
**latitude** | **float** |  | [optional] 
**longitude** | **float** |  | [optional] 
**max_mb** | **int** |  | [optional] 
**meta** | **Dict[str, str]** |  | [optional] 
**mobile_app_id** | **str** |  | [optional] 
**mobile_app_label** | **str** |  | [optional] 
**orientation_change** | **str** |  | [optional] 
**os_name** | **str** |  | [optional] 
**os_version** | **str** |  | [optional] 
**parent_beacon_id** | **str** |  | [optional] 
**parsed_stack_trace** | **str** |  | [optional] 
**performance_subtype** | **str** |  | [optional] 
**platform** | **str** |  | [optional] 
**rate_limit_beacon_type** | **str** |  | [optional] 
**rate_limit_count** | **int** |  | [optional] 
**rate_limit_custom_metric_val** | **List[object]** |  | [optional] 
**rate_limit_time_max** | **int** |  | [optional] 
**rate_limit_time_min** | **int** |  | [optional] 
**rooted** | **bool** |  | [optional] 
**scroll_direction** | **str** |  | [optional] 
**scroll_duration** | **str** |  | [optional] 
**session_id** | **str** |  | [optional] 
**session_replay_status** | **int** |  | [optional] 
**session_replay_version** | **str** |  | [optional] 
**stack_trace** | **str** |  | [optional] 
**stack_trace_key_checksum** | **str** |  | [optional] 
**stack_trace_key_information** | **str** |  | [optional] 
**stack_trace_line** | **List[object]** |  | [optional] 
**stack_trace_parsing_status** | **int** |  | [optional] 
**subdivision** | **str** |  | [optional] 
**subdivision_code** | **str** |  | [optional] 
**timestamp** | **int** |  | [optional] 
**transfer_size** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**use_features** | **List[str]** |  | [optional] 
**used_mb** | **int** |  | [optional] 
**user_email** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**user_ip** | **str** |  | [optional] 
**user_languages** | **List[str]** |  | [optional] 
**user_name** | **str** |  | [optional] 
**user_session_id** | **str** |  | [optional] 
**view** | **str** |  | [optional] 
**view_component_class_name** | **str** |  | [optional] 
**view_component_id** | **str** |  | [optional] 
**viewport_height** | **int** |  | [optional] 
**viewport_width** | **int** |  | [optional] 
**warm_start_time_ms** | **int** |  | [optional] 

## Example

```python
from instana_client.models.unified_beacon import UnifiedBeacon

# TODO update the JSON string below
json = "{}"
# create an instance of UnifiedBeacon from a JSON string
unified_beacon_instance = UnifiedBeacon.from_json(json)
# print the JSON string representation of the object
print(UnifiedBeacon.to_json())

# convert the object into a dict
unified_beacon_dict = unified_beacon_instance.to_dict()
# create an instance of UnifiedBeacon from a dict
unified_beacon_from_dict = UnifiedBeacon.from_dict(unified_beacon_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


