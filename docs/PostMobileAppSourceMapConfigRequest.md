# PostMobileAppSourceMapConfigRequest

Source map upload configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Name of configuration | [optional] 

## Example

```python
from instana_client.models.post_mobile_app_source_map_config_request import PostMobileAppSourceMapConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostMobileAppSourceMapConfigRequest from a JSON string
post_mobile_app_source_map_config_request_instance = PostMobileAppSourceMapConfigRequest.from_json(json)
# print the JSON string representation of the object
print(PostMobileAppSourceMapConfigRequest.to_json())

# convert the object into a dict
post_mobile_app_source_map_config_request_dict = post_mobile_app_source_map_config_request_instance.to_dict()
# create an instance of PostMobileAppSourceMapConfigRequest from a dict
post_mobile_app_source_map_config_request_from_dict = PostMobileAppSourceMapConfigRequest.from_dict(post_mobile_app_source_map_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


