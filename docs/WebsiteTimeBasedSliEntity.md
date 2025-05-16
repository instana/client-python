# WebsiteTimeBasedSliEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**beacon_type** | **str** | Enum value to specify the type of beacons to be monitored | 
**filter_expression** | [**TagFilterExpressionElement**](TagFilterExpressionElement.md) |  | [optional] 
**website_id** | **str** | Specifies the ID of the Website | [optional] 

## Example

```python
from instana_client.models.website_time_based_sli_entity import WebsiteTimeBasedSliEntity

# TODO update the JSON string below
json = "{}"
# create an instance of WebsiteTimeBasedSliEntity from a JSON string
website_time_based_sli_entity_instance = WebsiteTimeBasedSliEntity.from_json(json)
# print the JSON string representation of the object
print(WebsiteTimeBasedSliEntity.to_json())

# convert the object into a dict
website_time_based_sli_entity_dict = website_time_based_sli_entity_instance.to_dict()
# create an instance of WebsiteTimeBasedSliEntity from a dict
website_time_based_sli_entity_from_dict = WebsiteTimeBasedSliEntity.from_dict(website_time_based_sli_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


