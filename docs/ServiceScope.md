# ServiceScope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**scoped_to** | [**ServiceScopedTo**](ServiceScopedTo.md) |  | [optional] 

## Example

```python
from instana_client.models.service_scope import ServiceScope

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceScope from a JSON string
service_scope_instance = ServiceScope.from_json(json)
# print the JSON string representation of the object
print(ServiceScope.to_json())

# convert the object into a dict
service_scope_dict = service_scope_instance.to_dict()
# create an instance of ServiceScope from a dict
service_scope_from_dict = ServiceScope.from_dict(service_scope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


