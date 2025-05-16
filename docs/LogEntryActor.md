# LogEntryActor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**id** | **str** |  | 
**name** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from instana_client.models.log_entry_actor import LogEntryActor

# TODO update the JSON string below
json = "{}"
# create an instance of LogEntryActor from a JSON string
log_entry_actor_instance = LogEntryActor.from_json(json)
# print the JSON string representation of the object
print(LogEntryActor.to_json())

# convert the object into a dict
log_entry_actor_dict = log_entry_actor_instance.to_dict()
# create an instance of LogEntryActor from a dict
log_entry_actor_from_dict = LogEntryActor.from_dict(log_entry_actor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


