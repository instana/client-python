# CreateWebsiteRequestInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | Name of team tag | [optional] 
**id** | **str** | ID of team tag | [optional] 

## Example

```python
from instana_client.models.create_website_request_inner import CreateWebsiteRequestInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWebsiteRequestInner from a JSON string
create_website_request_inner_instance = CreateWebsiteRequestInner.from_json(json)
# print the JSON string representation of the object
print(CreateWebsiteRequestInner.to_json())

# convert the object into a dict
create_website_request_inner_dict = create_website_request_inner_instance.to_dict()
# create an instance of CreateWebsiteRequestInner from a dict
create_website_request_inner_from_dict = CreateWebsiteRequestInner.from_dict(create_website_request_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


