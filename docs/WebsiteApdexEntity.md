# WebsiteApdexEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**beacon_type** | **str** | Website Beacon Type | 
**entity_id** | **str** | Website ID | 
**threshold** | **int** | Value of the Apdex Threshold | [optional] 

## Example

```python
from instana_client.models.website_apdex_entity import WebsiteApdexEntity

# TODO update the JSON string below
json = "{}"
# create an instance of WebsiteApdexEntity from a JSON string
website_apdex_entity_instance = WebsiteApdexEntity.from_json(json)
# print the JSON string representation of the object
print(WebsiteApdexEntity.to_json())

# convert the object into a dict
website_apdex_entity_dict = website_apdex_entity_instance.to_dict()
# create an instance of WebsiteApdexEntity from a dict
website_apdex_entity_from_dict = WebsiteApdexEntity.from_dict(website_apdex_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


