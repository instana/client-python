# SearchFieldResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **str** | Field context | [optional] 
**description** | **str** | Description of the keyword | [optional] 
**fixed_values** | **List[str]** | Fixed value associated to the keyword | [optional] 
**keyword** | **str** | Retrieved keyword | [optional] 
**term_type** | **str** | Term type | [optional] 

## Example

```python
from instana_client.models.search_field_result import SearchFieldResult

# TODO update the JSON string below
json = "{}"
# create an instance of SearchFieldResult from a JSON string
search_field_result_instance = SearchFieldResult.from_json(json)
# print the JSON string representation of the object
print(SearchFieldResult.to_json())

# convert the object into a dict
search_field_result_dict = search_field_result_instance.to_dict()
# create an instance of SearchFieldResult from a dict
search_field_result_from_dict = SearchFieldResult.from_dict(search_field_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


