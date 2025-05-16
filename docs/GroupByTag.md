# GroupByTag

The grouping tags used to group the metric results.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**tag_name** | **str** |  | 

## Example

```python
from instana_client.models.group_by_tag import GroupByTag

# TODO update the JSON string below
json = "{}"
# create an instance of GroupByTag from a JSON string
group_by_tag_instance = GroupByTag.from_json(json)
# print the JSON string representation of the object
print(GroupByTag.to_json())

# convert the object into a dict
group_by_tag_dict = group_by_tag_instance.to_dict()
# create an instance of GroupByTag from a dict
group_by_tag_from_dict = GroupByTag.from_dict(group_by_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


