# IdpStatusUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] 

## Example

```python
from instana_client.models.idp_status_update import IdpStatusUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of IdpStatusUpdate from a JSON string
idp_status_update_instance = IdpStatusUpdate.from_json(json)
# print the JSON string representation of the object
print(IdpStatusUpdate.to_json())

# convert the object into a dict
idp_status_update_dict = idp_status_update_instance.to_dict()
# create an instance of IdpStatusUpdate from a dict
idp_status_update_from_dict = IdpStatusUpdate.from_dict(idp_status_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


