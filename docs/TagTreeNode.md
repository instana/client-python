# TagTreeNode

Children tags of tagTree

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**icon** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**type** | **str** | Type would be either &#x60;LEVEL&#x60; or &#x60;TAG&#x60; depending on whether the tag has any child tags or not respectively. | [optional] 

## Example

```python
from instana_client.models.tag_tree_node import TagTreeNode

# TODO update the JSON string below
json = "{}"
# create an instance of TagTreeNode from a JSON string
tag_tree_node_instance = TagTreeNode.from_json(json)
# print the JSON string representation of the object
print(TagTreeNode.to_json())

# convert the object into a dict
tag_tree_node_dict = tag_tree_node_instance.to_dict()
# create an instance of TagTreeNode from a dict
tag_tree_node_from_dict = TagTreeNode.from_dict(tag_tree_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


