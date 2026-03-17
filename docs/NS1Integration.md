# NS1Integration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**headers** | **List[str]** |  | [optional] 
**webhook_urls** | **List[str]** |  | 

## Example

```python
from instana_client.models.ns1_integration import NS1Integration

# TODO update the JSON string below
json = "{}"
# create an instance of NS1Integration from a JSON string
ns1_integration_instance = NS1Integration.from_json(json)
# print the JSON string representation of the object
print(NS1Integration.to_json())

# convert the object into a dict
ns1_integration_dict = ns1_integration_instance.to_dict()
# create an instance of NS1Integration from a dict
ns1_integration_from_dict = NS1Integration.from_dict(ns1_integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


