# Tag

List of queryable tags available in a tagTree. Eg: `call.erroneous`. Consider these tags as attributes of a tagTree. Eg: `Call` tagTree has have `Erroneous`, `Call name`, `Latency` etc as attributes. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aliases** | **List[str]** | List of other names that can refer to this tag  | [optional] 
**availability** | **List[str]** | List of product areas this tag is available in  | [optional] 
**can_apply_to_destination** | **bool** | Whether the tag is available for destination or not. If source and destination is false, it means the tag is independent of source and destination. Eg: of such tag is &#x60;call.http.path&#x60;.  | [optional] 
**can_apply_to_source** | **bool** | Whether the tag is available for source or not. If source and destination is false, it means the tag is independent of source and destination. Eg: of such tag is &#x60;call.http.path&#x60;.  | [optional] 
**description** | **str** | The description of the tag if it is provided. | [optional] 
**id_tag** | **bool** | Whether the Tag is a unique ID or not. Eg: &#x60;idTag&#x60; for &#x60;endpoint.id&#x60; is true but for &#x60;call.rpc.method&#x60; it is false.  | [optional] 
**label** | **str** | The name of the tag which is seen in the UI. Eg: &#x60;Call name&#x60; | [optional] 
**name** | **str** | The name of the tag. Eg: &#x60;call.name&#x60; | 
**type** | **str** | The data type of the tag. Eg: &#x60;call.name&#x60; accepts &#x60;STRING&#x60; value. | 

## Example

```python
from instana_client.models.tag import Tag

# TODO update the JSON string below
json = "{}"
# create an instance of Tag from a JSON string
tag_instance = Tag.from_json(json)
# print the JSON string representation of the object
print(Tag.to_json())

# convert the object into a dict
tag_dict = tag_instance.to_dict()
# create an instance of Tag from a dict
tag_from_dict = Tag.from_dict(tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


