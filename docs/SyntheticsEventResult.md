# SyntheticsEventResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location_ids** | **List[str]** | IDs of the locations. | [optional] 
**synthetic_test_id** | **str** | ID of the synthetic test. | [optional] 

## Example

```python
from instana_client.models.synthetics_event_result import SyntheticsEventResult

# TODO update the JSON string below
json = "{}"
# create an instance of SyntheticsEventResult from a JSON string
synthetics_event_result_instance = SyntheticsEventResult.from_json(json)
# print the JSON string representation of the object
print(SyntheticsEventResult.to_json())

# convert the object into a dict
synthetics_event_result_dict = synthetics_event_result_instance.to_dict()
# create an instance of SyntheticsEventResult from a dict
synthetics_event_result_from_dict = SyntheticsEventResult.from_dict(synthetics_event_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


