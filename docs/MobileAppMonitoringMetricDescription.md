# MobileAppMonitoringMetricDescription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregations** | **List[str]** | The types of aggregations that can be applied to a series of values. For example, &#x60;P25&#x60; is 25th percentile. Note that not all aggregations are available for metrics. For example, &#x60;Trace count&#x60; has only &#x60;SUM&#x60; as an aggregation whereas &#x60;Call Count&#x60; has two aggregations, &#x60;SUM&#x60; and &#x60;PER_SECOND&#x60;.  | 
**beacon_types** | **List[str]** |  | 
**default_aggregation** | **str** | The preselected aggregation for a metric. For example, for &#x60;Call latency&#x60; the default aggregation is &#x60;MEAN&#x60;. | [optional] 
**description** | **str** | A description of the metric. For example, for &#x60;Call count&#x60; metric, the description would be something like &#x60;Number of received calls&#x60; | [optional] 
**formatter** | **str** | * &#x60;NUMBER&#x60;: Generic number * &#x60;BYTES&#x60;: Number of bytes * &#x60;KILO_BYTES&#x60;: Number of kilobytes * &#x60;MEGA_BYTES&#x60;: Number of megabytes * &#x60;PERCENTAGE&#x60;: Percentage in scale [0,1] * &#x60;PERCENTAGE_100&#x60;: Percentage in scale [0,100] * &#x60;PERCENTAGE_NO_CAPPING&#x60;: Percentage in scale [0,1] but value could exceed 1 for example when metric is aggregated * &#x60;PERCENTAGE_100_NO_CAPPING&#x60;: Percentage in scale [0,100] but value could exceed 100 for example when metric is aggregated * &#x60;LATENCY&#x60;: Time in milliseconds, with value of 0 should not be considered a a strict 0, but considered as &lt; 1ms * &#x60;NANOS&#x60;: Time in nanoseconds * &#x60;MILLIS&#x60;: Time in milliseconds * &#x60;MICROS&#x60;: Time in microseconds * &#x60;SECONDS&#x60;: Time in seconds * &#x60;RATE&#x60;: Number of occurrences per second * &#x60;BYTE_RATE&#x60;: Number of bytes per second * &#x60;UNDEFINED&#x60;: Metric value unit is not known  | 
**label** | **str** | The name of the metric. For example, &#x60;Call count&#x60;, &#x60;Erroneous calls&#x60;, &#x60;Service count&#x60; etc. | 
**metric_id** | **str** | The unique id of the metric. For example, &#x60;calls&#x60;, &#x60;erroneousCalls&#x60;, &#x60;latency&#x60; etc. | 
**path_to_value_in_beacon** | **List[str]** |  | [optional] 
**secondary_beacon_types** | **List[str]** |  | [optional] 
**tag_name** | **str** |  | [optional] 

## Example

```python
from instana_client.models.mobile_app_monitoring_metric_description import MobileAppMonitoringMetricDescription

# TODO update the JSON string below
json = "{}"
# create an instance of MobileAppMonitoringMetricDescription from a JSON string
mobile_app_monitoring_metric_description_instance = MobileAppMonitoringMetricDescription.from_json(json)
# print the JSON string representation of the object
print(MobileAppMonitoringMetricDescription.to_json())

# convert the object into a dict
mobile_app_monitoring_metric_description_dict = mobile_app_monitoring_metric_description_instance.to_dict()
# create an instance of MobileAppMonitoringMetricDescription from a dict
mobile_app_monitoring_metric_description_from_dict = MobileAppMonitoringMetricDescription.from_dict(mobile_app_monitoring_metric_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


