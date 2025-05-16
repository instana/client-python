# TagCatalog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag_tree** | [**List[TagTreeLevel]**](TagTreeLevel.md) | The name of the tag dataset (tagTree) which can contain one or more tags as its attributes or children. Eg: &#x60;Call&#x60;. Consider this as the root of the tree where it has tags as attributes or children.  | 
**tags** | [**List[Tag]**](Tag.md) | List of queryable tags available in a tagTree. Eg: &#x60;call.erroneous&#x60;. Consider these tags as attributes of a tagTree. Eg: &#x60;Call&#x60; tagTree has have &#x60;Erroneous&#x60;, &#x60;Call name&#x60;, &#x60;Latency&#x60; etc as attributes.  | 

## Example

```python
from instana_client.models.tag_catalog import TagCatalog

# TODO update the JSON string below
json = "{}"
# create an instance of TagCatalog from a JSON string
tag_catalog_instance = TagCatalog.from_json(json)
# print the JSON string representation of the object
print(TagCatalog.to_json())

# convert the object into a dict
tag_catalog_dict = tag_catalog_instance.to_dict()
# create an instance of TagCatalog from a dict
tag_catalog_from_dict = TagCatalog.from_dict(tag_catalog_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


