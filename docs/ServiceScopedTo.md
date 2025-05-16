# ServiceScopedTo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applications** | [**List[ApplicationScope]**](ApplicationScope.md) |  | 

## Example

```python
from instana_client.models.service_scoped_to import ServiceScopedTo

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceScopedTo from a JSON string
service_scoped_to_instance = ServiceScopedTo.from_json(json)
# print the JSON string representation of the object
print(ServiceScopedTo.to_json())

# convert the object into a dict
service_scoped_to_dict = service_scoped_to_instance.to_dict()
# create an instance of ServiceScopedTo from a dict
service_scoped_to_from_dict = ServiceScopedTo.from_dict(service_scoped_to_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


