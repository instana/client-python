# ApdexReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apdex_id** | **str** | Apdex Configuration ID | [optional] 
**apdex_score** | **List[List[float]]** | Apdex Score in different timestamps from starting to the ending point | [optional] 
**var_from** | **int** | Starting point for the data retrieval, specified as 13 digit Unix Timestamp milliseconds | [optional] 
**to** | **int** | Ending point for the data retrieval, specified as 13 digit Unix Timestamp milliseconds | [optional] 

## Example

```python
from instana_client.models.apdex_report import ApdexReport

# TODO update the JSON string below
json = "{}"
# create an instance of ApdexReport from a JSON string
apdex_report_instance = ApdexReport.from_json(json)
# print the JSON string representation of the object
print(ApdexReport.to_json())

# convert the object into a dict
apdex_report_dict = apdex_report_instance.to_dict()
# create an instance of ApdexReport from a dict
apdex_report_from_dict = ApdexReport.from_dict(apdex_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


