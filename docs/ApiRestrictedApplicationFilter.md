# ApiRestrictedApplicationFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**restricting_application_id** | **str** |  | [optional] 
**scope** | **str** |  | [optional] 
**tag_filter_expression** | [**TagFilterExpressionElement**](TagFilterExpressionElement.md) |  | [optional] 

## Example

```python
from instana_client.models.api_restricted_application_filter import ApiRestrictedApplicationFilter

# TODO update the JSON string below
json = "{}"
# create an instance of ApiRestrictedApplicationFilter from a JSON string
api_restricted_application_filter_instance = ApiRestrictedApplicationFilter.from_json(json)
# print the JSON string representation of the object
print(ApiRestrictedApplicationFilter.to_json())

# convert the object into a dict
api_restricted_application_filter_dict = api_restricted_application_filter_instance.to_dict()
# create an instance of ApiRestrictedApplicationFilter from a dict
api_restricted_application_filter_from_dict = ApiRestrictedApplicationFilter.from_dict(api_restricted_application_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


