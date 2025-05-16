# LocationStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location_display_label** | **str** |  | [optional] 
**location_id** | **str** |  | 
**success_rate** | **float** |  | [optional] 
**success_runs** | **int** |  | [optional] 
**total_test_runs** | **int** |  | [optional] 

## Example

```python
from instana_client.models.location_status import LocationStatus

# TODO update the JSON string below
json = "{}"
# create an instance of LocationStatus from a JSON string
location_status_instance = LocationStatus.from_json(json)
# print the JSON string representation of the object
print(LocationStatus.to_json())

# convert the object into a dict
location_status_dict = location_status_instance.to_dict()
# create an instance of LocationStatus from a dict
location_status_from_dict = LocationStatus.from_dict(location_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


