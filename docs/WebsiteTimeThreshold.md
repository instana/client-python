# WebsiteTimeThreshold

The type of threshold to define the criteria when the event and alert triggers and resolves.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_window** | **int** |  | [optional] 
**type** | **str** |  | 

## Example

```python
from instana_client.models.website_time_threshold import WebsiteTimeThreshold

# TODO update the JSON string below
json = "{}"
# create an instance of WebsiteTimeThreshold from a JSON string
website_time_threshold_instance = WebsiteTimeThreshold.from_json(json)
# print the JSON string representation of the object
print(WebsiteTimeThreshold.to_json())

# convert the object into a dict
website_time_threshold_dict = website_time_threshold_instance.to_dict()
# create an instance of WebsiteTimeThreshold from a dict
website_time_threshold_from_dict = WebsiteTimeThreshold.from_dict(website_time_threshold_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


