# ActionInstanceRequestParameters

Action run input parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the input parameter. | 
**type** | **str** | Type of the input parameter. Valid values are &#x60;static&#x60;, &#x60;dynamic&#x60; or &#x60;vault&#x60;. Default is &#x60;static&#x60;. | [optional] 
**value** | **str** | Value of the input parameter | 

## Example

```python
from instana_client.models.action_instance_request_parameters import ActionInstanceRequestParameters

# TODO update the JSON string below
json = "{}"
# create an instance of ActionInstanceRequestParameters from a JSON string
action_instance_request_parameters_instance = ActionInstanceRequestParameters.from_json(json)
# print the JSON string representation of the object
print(ActionInstanceRequestParameters.to_json())

# convert the object into a dict
action_instance_request_parameters_dict = action_instance_request_parameters_instance.to_dict()
# create an instance of ActionInstanceRequestParameters from a dict
action_instance_request_parameters_from_dict = ActionInstanceRequestParameters.from_dict(action_instance_request_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


