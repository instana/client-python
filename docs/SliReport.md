# SliReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_budget_remaining** | **int** | This is the error budget remaining compared to the total error budget | [optional] 
**from_timestamp** | **int** | from timestamp in milliseconds (13-digit) | [optional] 
**sli** | **float** | Service Level Indicator: This indicates the actual performance measure of the service | [optional] 
**slo** | **float** | Service Level Objective: This is the target value that should be met by the SLI | [optional] 
**to_timestamp** | **int** | to timestamp in milliseconds (13-digit) | [optional] 
**total_error_budget** | **int** | This is the total error budget available | [optional] 
**violation_distribution** | **Dict[str, int]** |  | [optional] 

## Example

```python
from instana_client.models.sli_report import SliReport

# TODO update the JSON string below
json = "{}"
# create an instance of SliReport from a JSON string
sli_report_instance = SliReport.from_json(json)
# print the JSON string representation of the object
print(SliReport.to_json())

# convert the object into a dict
sli_report_dict = sli_report_instance.to_dict()
# create an instance of SliReport from a dict
sli_report_from_dict = SliReport.from_dict(sli_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


