# WebsiteMonitoringBeacon


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accuracy_radius** | **int** |  | [optional] 
**accurate_timings_available** | **bool** |  | [optional] 
**agent_version** | **str** |  | [optional] 
**app_cache_time** | **int** |  | [optional] 
**backend_time** | **int** |  | [optional] 
**backend_trace_id** | **str** |  | [optional] 
**batch_size** | **int** |  | [optional] 
**beacon_id** | **str** |  | 
**browser_name** | **str** |  | [optional] 
**browser_version** | **str** |  | [optional] 
**cache_interaction** | **str** |  | [optional] 
**children_time** | **int** |  | [optional] 
**city** | **str** |  | [optional] 
**clock_skew** | **int** |  | [optional] 
**component_stack** | **str** |  | [optional] 
**connection_type** | **str** |  | [optional] 
**continent** | **str** |  | [optional] 
**continent_code** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**csp_blocked_uri** | **str** |  | [optional] 
**csp_column_number** | **int** |  | [optional] 
**csp_disposition** | **str** |  | [optional] 
**csp_effective_directive** | **str** |  | [optional] 
**csp_line_number** | **int** |  | [optional] 
**csp_original_policy** | **str** |  | [optional] 
**csp_sample** | **str** |  | [optional] 
**csp_source_file** | **str** |  | [optional] 
**cumulative_layout_shift** | **float** |  | [optional] 
**custom_event_name** | **str** |  | [optional] 
**custom_metric** | **float** |  | [optional] 
**decoded_body_size** | **int** |  | [optional] 
**deprecations** | **List[str]** |  | [optional] 
**device_type** | **str** |  | [optional] 
**dns_time** | **int** |  | [optional] 
**dom_time** | **int** |  | [optional] 
**duration** | **int** |  | [optional] 
**encoded_body_size** | **int** |  | [optional] 
**error_count** | **int** |  | [optional] 
**error_id** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 
**error_type** | **str** |  | [optional] 
**first_contentful_paint_time** | **int** |  | [optional] 
**first_input_delay_time** | **int** |  | [optional] 
**first_paint_time** | **int** |  | [optional] 
**frontend_time** | **int** |  | [optional] 
**graphql_operation_name** | **str** |  | [optional] 
**graphql_operation_type** | **str** |  | [optional] 
**http_call_asynchronous** | **bool** |  | [optional] 
**http_call_correlation_attempted** | **bool** |  | [optional] 
**http_call_headers** | **Dict[str, str]** |  | [optional] 
**http_call_method** | **str** |  | [optional] 
**http_call_origin** | **str** |  | [optional] 
**http_call_path** | **str** |  | [optional] 
**http_call_status** | **int** |  | [optional] 
**http_call_url** | **str** |  | [optional] 
**initiator** | **str** |  | [optional] 
**interaction_next_paint** | **int** |  | [optional] 
**internal_meta** | **Dict[str, str]** |  | [optional] 
**largest_contentful_paint_time** | **int** |  | [optional] 
**latitude** | **float** |  | [optional] 
**location_origin** | **str** |  | 
**location_path** | **str** |  | [optional] 
**location_url** | **str** |  | 
**longitude** | **float** |  | [optional] 
**meta** | **Dict[str, str]** |  | [optional] 
**on_load_time** | **int** |  | [optional] 
**os_name** | **str** |  | [optional] 
**os_version** | **str** |  | [optional] 
**page** | **str** |  | [optional] 
**page_load_id** | **str** |  | 
**parent_beacon_id** | **str** |  | [optional] 
**parsed_stack_trace** | [**List[JsStackTraceLine]**](JsStackTraceLine.md) |  | [optional] 
**phase** | **str** |  | [optional] 
**processing_time** | **int** |  | [optional] 
**redirect_time** | **int** |  | [optional] 
**request_time** | **int** |  | [optional] 
**resource_type** | **str** |  | [optional] 
**response_time** | **int** |  | [optional] 
**session_id** | **str** |  | [optional] 
**snippet_version** | **str** |  | [optional] 
**ssl_time** | **int** |  | [optional] 
**stack_trace** | **str** |  | [optional] 
**stack_trace_parsing_status** | **int** |  | [optional] 
**stack_trace_readability** | **int** |  | [optional] 
**subdivision** | **str** |  | [optional] 
**subdivision_code** | **str** |  | [optional] 
**tcp_time** | **int** |  | [optional] 
**timestamp** | **int** |  | [optional] 
**transfer_size** | **int** |  | [optional] 
**type** | **str** |  | 
**unload_time** | **int** |  | [optional] 
**use_features** | **List[str]** |  | [optional] 
**user_email** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**user_ip** | **str** |  | [optional] 
**user_languages** | **List[str]** |  | [optional] 
**user_name** | **str** |  | [optional] 
**website_id** | **str** |  | 
**website_label** | **str** |  | 
**window_height** | **int** |  | [optional] 
**window_hidden** | **bool** |  | [optional] 
**window_width** | **int** |  | [optional] 

## Example

```python
from instana_client.models.website_monitoring_beacon import WebsiteMonitoringBeacon

# TODO update the JSON string below
json = "{}"
# create an instance of WebsiteMonitoringBeacon from a JSON string
website_monitoring_beacon_instance = WebsiteMonitoringBeacon.from_json(json)
# print the JSON string representation of the object
print(WebsiteMonitoringBeacon.to_json())

# convert the object into a dict
website_monitoring_beacon_dict = website_monitoring_beacon_instance.to_dict()
# create an instance of WebsiteMonitoringBeacon from a dict
website_monitoring_beacon_from_dict = WebsiteMonitoringBeacon.from_dict(website_monitoring_beacon_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


