# ApplicationBatchBusinessCriticalityUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_criticality** | **int** |  | 
**ids** | **List[str]** |  | 
**ids_unique** | **bool** |  | [optional] 

## Example

```python
from instana_client.models.application_batch_business_criticality_update import ApplicationBatchBusinessCriticalityUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationBatchBusinessCriticalityUpdate from a JSON string
application_batch_business_criticality_update_instance = ApplicationBatchBusinessCriticalityUpdate.from_json(json)
# print the JSON string representation of the object
print(ApplicationBatchBusinessCriticalityUpdate.to_json())

# convert the object into a dict
application_batch_business_criticality_update_dict = application_batch_business_criticality_update_instance.to_dict()
# create an instance of ApplicationBatchBusinessCriticalityUpdate from a dict
application_batch_business_criticality_update_from_dict = ApplicationBatchBusinessCriticalityUpdate.from_dict(application_batch_business_criticality_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


