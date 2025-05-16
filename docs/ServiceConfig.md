# ServiceConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | A small description of the service configuration would be present in this field if it was provided during creation of the custom service rule. If it was not provided, this field will remain empty. It is considered as best practice to add a comment to document the reasoning behind creating the rule.  | [optional] 
**enabled** | **bool** | If enabled, calls will be mapped to the rule. | 
**id** | **str** | A unique string for the service configuration. Eg: &#x60;G510hmXYSDysLZ5kuj0BaQ&#x60; | 
**label** | **str** | It contains the tags defined in &#x60;matchSpecification&#x60; concatenated with a dash. Eg: if the &#x60;matchSpecification&#x60; contains keys &#x60;kubernetes.namespace.name&#x60; and &#x60;docker.label&#x60;, &#x60;label&#x60; would be &#x60;kubernetes.namespace.name-docker.label&#x60;.  | 
**match_specification** | [**List[ServiceMatchingRule]**](ServiceMatchingRule.md) | Calls will be matched with the array of key-value tags present in this field. | 
**name** | **str** | The name of the service configuration. Eg: &#x60;Rule ABC&#x60; | 

## Example

```python
from instana_client.models.service_config import ServiceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceConfig from a JSON string
service_config_instance = ServiceConfig.from_json(json)
# print the JSON string representation of the object
print(ServiceConfig.to_json())

# convert the object into a dict
service_config_dict = service_config_instance.to_dict()
# create an instance of ServiceConfig from a dict
service_config_from_dict = ServiceConfig.from_dict(service_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


