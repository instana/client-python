# WebsiteEventResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**probable_root_cause** | **Dict[str, object]** |  | [optional] 
**website_id** | **str** |  | [optional] 

## Example

```python
from instana_client.models.website_event_result import WebsiteEventResult

# TODO update the JSON string below
json = "{}"
# create an instance of WebsiteEventResult from a JSON string
website_event_result_instance = WebsiteEventResult.from_json(json)
# print the JSON string representation of the object
print(WebsiteEventResult.to_json())

# convert the object into a dict
website_event_result_dict = website_event_result_instance.to_dict()
# create an instance of WebsiteEventResult from a dict
website_event_result_from_dict = WebsiteEventResult.from_dict(website_event_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


