# InfraEventResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ibm_mq_file_transfer** | **List[Dict[str, object]]** | IBM MQ file transfer information, if relevant for this entity and event. | [optional] 
**snapshot_id** | **str** | ID of the snapshot. | [optional] 

## Example

```python
from instana_client.models.infra_event_result import InfraEventResult

# TODO update the JSON string below
json = "{}"
# create an instance of InfraEventResult from a JSON string
infra_event_result_instance = InfraEventResult.from_json(json)
# print the JSON string representation of the object
print(InfraEventResult.to_json())

# convert the object into a dict
infra_event_result_dict = infra_event_result_instance.to_dict()
# create an instance of InfraEventResult from a dict
infra_event_result_from_dict = InfraEventResult.from_dict(infra_event_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


