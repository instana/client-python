# WebsiteSloEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**beacon_type** | **str** | Type of Website Beacon to be considered for the SLO | 
**website_id** | **str** | The ID of the Website | 

## Example

```python
from instana_client.models.website_slo_entity import WebsiteSloEntity

# TODO update the JSON string below
json = "{}"
# create an instance of WebsiteSloEntity from a JSON string
website_slo_entity_instance = WebsiteSloEntity.from_json(json)
# print the JSON string representation of the object
print(WebsiteSloEntity.to_json())

# convert the object into a dict
website_slo_entity_dict = website_slo_entity_instance.to_dict()
# create an instance of WebsiteSloEntity from a dict
website_slo_entity_from_dict = WebsiteSloEntity.from_dict(website_slo_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


