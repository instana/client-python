# SyntheticBulkResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_message** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from instana_client.models.synthetic_bulk_response import SyntheticBulkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SyntheticBulkResponse from a JSON string
synthetic_bulk_response_instance = SyntheticBulkResponse.from_json(json)
# print the JSON string representation of the object
print(SyntheticBulkResponse.to_json())

# convert the object into a dict
synthetic_bulk_response_dict = synthetic_bulk_response_instance.to_dict()
# create an instance of SyntheticBulkResponse from a dict
synthetic_bulk_response_from_dict = SyntheticBulkResponse.from_dict(synthetic_bulk_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


