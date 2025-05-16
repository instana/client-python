# Application

Returns a list of Application Perspectives.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**boundary_scope** | **str** | Here, &#x60;ALL&#x60; Application Boundary Scope is considered. | 
**entity_type** | **str** | Since, this is an Application Perspective, it will be of type &#x60;APPLICATION&#x60;. | [optional] 
**id** | **str** | Unique ID of the Application Perspective. Eg: &#x60;Av62RoIKQv-A3n6DbMQh9g&#x60;. | 
**label** | **str** | Name of the Application Perspective. Eg: &#x60;app1&#x60;. | 

## Example

```python
from instana_client.models.application import Application

# TODO update the JSON string below
json = "{}"
# create an instance of Application from a JSON string
application_instance = Application.from_json(json)
# print the JSON string representation of the object
print(Application.to_json())

# convert the object into a dict
application_dict = application_instance.to_dict()
# create an instance of Application from a dict
application_from_dict = Application.from_dict(application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


