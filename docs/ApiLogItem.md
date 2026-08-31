# ApiLogItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_ecs_container_id** | **str** |  | [optional] 
**aws_ecs_container_name** | **str** |  | [optional] 
**containerd_container_id** | **str** |  | [optional] 
**crio_container_id** | **str** |  | [optional] 
**docker_container_id** | **str** |  | [optional] 
**docker_container_name** | **str** |  | [optional] 
**garden_container_id** | **str** |  | [optional] 
**kubernetes_cluster_name** | **str** |  | [optional] 
**kubernetes_container_name** | **str** |  | [optional] 
**kubernetes_deployment_name** | **str** |  | [optional] 
**kubernetes_namespace_name** | **str** |  | [optional] 
**kubernetes_node_name** | **str** |  | [optional] 
**kubernetes_pod_name** | **str** |  | [optional] 
**log_applications** | **List[str]** |  | [optional] 
**log_custom** | [**List[ApiLogTag]**](ApiLogTag.md) |  | [optional] 
**log_exception_message** | **str** |  | [optional] 
**log_exception_stack_trace** | **str** |  | [optional] 
**log_exception_type** | **str** |  | [optional] 
**log_expiration_ts_seconds** | **str** |  | [optional] 
**log_file_path** | **str** |  | [optional] 
**log_host_id** | **str** |  | [optional] 
**log_host_name** | **str** |  | [optional] 
**log_level** | **str** |  | [optional] 
**log_message** | **str** |  | [optional] 
**log_process_id** | **str** |  | [optional] 
**log_service_id** | **str** |  | [optional] 
**log_service_name** | **str** |  | [optional] 
**log_stream_name** | **str** |  | [optional] 
**log_timestamp** | **int** |  | [optional] 
**log_trace_id** | **str** |  | [optional] 

## Example

```python
from instana_client.models.api_log_item import ApiLogItem

# TODO update the JSON string below
json = "{}"
# create an instance of ApiLogItem from a JSON string
api_log_item_instance = ApiLogItem.from_json(json)
# print the JSON string representation of the object
print(ApiLogItem.to_json())

# convert the object into a dict
api_log_item_dict = api_log_item_instance.to_dict()
# create an instance of ApiLogItem from a dict
api_log_item_from_dict = ApiLogItem.from_dict(api_log_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


