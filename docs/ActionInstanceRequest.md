# ActionInstanceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_id** | **str** | Action identifier of the action to run. | 
**var_async** | **str** | &#x60;\&quot;true\&quot;&#x60; if the action should be run in asynchronous mode &#x60;\&quot;false\&quot;&#x60; otherwise. Default is &#x60;\&quot;true\&quot;&#x60;. | [optional] 
**event_id** | **str** | Event identifier (incident or issue) associated with the policy. | [optional] 
**host_id** | **str** | Agent host identifier on which to run the action. | 
**input_parameters** | [**List[ActionInstanceRequestParameters]**](ActionInstanceRequestParameters.md) | Action run input parameters. | [optional] 
**policy_id** | **str** | Policy identifier that associates the action trigger (incident or issue) to the action to run. | [optional] 
**timeout** | **str** | Action run time out. Default is &#x60;30 seconds&#x60;. | [optional] 

## Example

```python
from instana_client.models.action_instance_request import ActionInstanceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ActionInstanceRequest from a JSON string
action_instance_request_instance = ActionInstanceRequest.from_json(json)
# print the JSON string representation of the object
print(ActionInstanceRequest.to_json())

# convert the object into a dict
action_instance_request_dict = action_instance_request_instance.to_dict()
# create an instance of ActionInstanceRequest from a dict
action_instance_request_from_dict = ActionInstanceRequest.from_dict(action_instance_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


