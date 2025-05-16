# TagTreeLevel

The name of the tag dataset (tagTree) which can contain one or more tags as its attributes or children. Eg: `Call`. Consider this as the root of the tree where it has tags as attributes or children. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**children** | [**List[TagTreeNode]**](TagTreeNode.md) | Children tags of tagTree | 
**description** | **str** | The description provided, if any. | [optional] 
**icon** | **str** | Each tag has an Icon which can be seen on the drop down list in Unbounded Analytics. If there is an icon, there will be a string associated with it. Eg: For for all &#x60;TAG&#x60; under &#x60;Call&#x60; tagTreeNode, the &#x60;icon&#x60; value is &#x60;lib_application_call&#x60;.  | [optional] 
**label** | **str** | The name of the tagTreeNode. Eg: &#x60;Commonly Used&#x60;, &#x60;Application&#x60;. | 
**queryable** | **bool** |  | [optional] 
**score_boost** | **int** | By default it is &#x60;null&#x60; if it is not set explictily by IBM Instana. The purpose of this parameter is to rank the tagTree. For eg: some set of tags are frequently used. Tags under &#x60;Commonly used&#x60; is frequently used, so it will come up on top of the drop down list of &#x60;Query Builder&#x60; in &#x60;Unbounded Analytics&#x60;. Higher the scoreBoost, higher the ranking.  | [optional] 
**type** | **str** | Type would be either &#x60;LEVEL&#x60; or &#x60;TAG&#x60; depending on whether the tag has any child tags or not respectively. | [optional] 

## Example

```python
from instana_client.models.tag_tree_level import TagTreeLevel

# TODO update the JSON string below
json = "{}"
# create an instance of TagTreeLevel from a JSON string
tag_tree_level_instance = TagTreeLevel.from_json(json)
# print the JSON string representation of the object
print(TagTreeLevel.to_json())

# convert the object into a dict
tag_tree_level_dict = tag_tree_level_instance.to_dict()
# create an instance of TagTreeLevel from a dict
tag_tree_level_from_dict = TagTreeLevel.from_dict(tag_tree_level_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


