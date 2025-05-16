# TagTreeTag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**hidden** | **bool** | If true, the tag will not be available for query in Unbounded Analytics. | [optional] 
**icon** | **str** |  | [optional] 
**label** | **str** | The name of the tagTreeNode. Eg: &#x60;Call Error Message&#x60;, &#x60;Endpoint Name&#x60;. | 
**queryable** | **bool** | queryable property can have 3 states which will be reflected in the drop down list in &#x60;Query Builder&#x60; of &#x60;Unbounded Analytics&#x60; of Instana UI:    - true: the tag has been seen by IBM Instana and must be shown.    - false: the tag could have been processed, but has not been seen by IBM Instana and could be hidden.    - null: the tag has not been processed and should be shown. The purpose is to make it easier for customers to find the right tags in drop down list  | [optional] 
**score_boost** | **int** | By default it is &#x60;null&#x60; if it is not set explictily by IBM Instana. The purpose of this parameter is to rank the Tag. For eg: tags are frequently used within the tagTree For eg, assume there are 8 tags under &#x60;Commonly Used&#x60;. IBM Instana can set the ranking for each of these tags within &#x60;Commonly Used&#x60;. Higher the scoreBoost, higher the ranking.  | [optional] 
**tag_name** | **str** |  | 

## Example

```python
from instana_client.models.tag_tree_tag import TagTreeTag

# TODO update the JSON string below
json = "{}"
# create an instance of TagTreeTag from a JSON string
tag_tree_tag_instance = TagTreeTag.from_json(json)
# print the JSON string representation of the object
print(TagTreeTag.to_json())

# convert the object into a dict
tag_tree_tag_dict = tag_tree_tag_instance.to_dict()
# create an instance of TagTreeTag from a dict
tag_tree_tag_from_dict = TagTreeTag.from_dict(tag_tree_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


