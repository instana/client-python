# WebsiteEventBasedSliEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bad_event_filter_expression** | [**TagFilterExpressionElement**](TagFilterExpressionElement.md) |  | 
**beacon_type** | **str** | Enum value to specify the type of beacons to be monitored | 
**good_event_filter_expression** | [**TagFilterExpressionElement**](TagFilterExpressionElement.md) |  | 
**website_id** | **str** | Specifies the ID of the Website | [optional] 

## Example

```python
from instana_client.models.website_event_based_sli_entity import WebsiteEventBasedSliEntity

# TODO update the JSON string below
json = "{}"
# create an instance of WebsiteEventBasedSliEntity from a JSON string
website_event_based_sli_entity_instance = WebsiteEventBasedSliEntity.from_json(json)
# print the JSON string representation of the object
print(WebsiteEventBasedSliEntity.to_json())

# convert the object into a dict
website_event_based_sli_entity_dict = website_event_based_sli_entity_instance.to_dict()
# create an instance of WebsiteEventBasedSliEntity from a dict
website_event_based_sli_entity_from_dict = WebsiteEventBasedSliEntity.from_dict(website_event_based_sli_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


