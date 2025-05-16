# HistoricBaseline


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**baseline** | **List[List[float]]** |  | [optional] 
**deviation_factor** | **float** |  | [optional] 
**last_updated** | **int** |  | [optional] 
**seasonality** | **str** |  | 

## Example

```python
from instana_client.models.historic_baseline import HistoricBaseline

# TODO update the JSON string below
json = "{}"
# create an instance of HistoricBaseline from a JSON string
historic_baseline_instance = HistoricBaseline.from_json(json)
# print the JSON string representation of the object
print(HistoricBaseline.to_json())

# convert the object into a dict
historic_baseline_dict = historic_baseline_instance.to_dict()
# create an instance of HistoricBaseline from a dict
historic_baseline_from_dict = HistoricBaseline.from_dict(historic_baseline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


