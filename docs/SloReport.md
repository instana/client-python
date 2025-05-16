# SloReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_accumulation_chart** | **Dict[str, int]** | Value of accumulated bad minutes/events of SLO configuration in different timestamps from starting to ending point | [optional] 
**error_budget_remain_chart** | **Dict[str, int]** | Error Budget Remain value of SLO configuration in different timestamps from starting to ending point | [optional] 
**error_budget_remaining** | **int** | Latest Remaining Error Budget value of SLO Configuration | [optional] 
**error_budget_spent** | **int** | Spent Error Budget of SLO Configuration | [optional] 
**error_burn_rate** | **int** | Latest Burn Rate value of SLO Configuration | [optional] 
**error_burn_rate_chart** | **Dict[str, int]** | Budget Rate value of SLO configuration in different timestamps from starting to ending point | [optional] 
**error_chart** | **Dict[str, int]** | Value indicating presence of bad minutes/events of SLO configuration in different timestamps from starting to ending point | [optional] 
**from_timestamp** | **int** | Starting point of the data retrieval, specified as 13 digit Unix Timestamp milliseconds | [optional] 
**sli** | **float** | Latest Status value of SLO Configuration | [optional] 
**slo** | **float** | Target status of SLO Configuration | [optional] 
**to_timestamp** | **int** | Ending point of the data retrieval, specified as 13 digit Unix Timestamp milliseconds | [optional] 
**total_error_budget** | **int** | Latest Available Error Budget value of SLO Configuration | [optional] 
**violation_distribution** | **Dict[str, int]** | Value indicating violation of SLO configuration in different timestamps from starting to ending point | [optional] 

## Example

```python
from instana_client.models.slo_report import SloReport

# TODO update the JSON string below
json = "{}"
# create an instance of SloReport from a JSON string
slo_report_instance = SloReport.from_json(json)
# print the JSON string representation of the object
print(SloReport.to_json())

# convert the object into a dict
slo_report_dict = slo_report_instance.to_dict()
# create an instance of SloReport from a dict
slo_report_from_dict = SloReport.from_dict(slo_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


