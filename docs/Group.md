# Group

 Grouping of data under `groupbyTag`, where `groupbyTagEntity` and `groupbyTagSecondLevelKey` are aspects of `groupbyTag`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groupby_tag** | **str** | The name of the group tag (e.g. &#x60;agent.tag&#x60; or &#x60;docker.label&#x60;). | 
**groupby_tag_entity** | **str** | The entity by which the data should be grouped. This field supports three possible values: &#x60;NOT_APPLICABLE&#x60;, &#x60;DESTINATION&#x60;, and &#x60;SOURCE&#x60;. &#x60;SOURCE&#x60;: the tag filter should apply to the source entity. &#x60;DESTINATION&#x60;: the tag filter should apply to the destination entity. &#x60;NOT_APPLICABLE&#x60;: some tags are independent of source or destination, such as tags on the call itself, log tags or trace tags (only destination makes sense because the source is unknown for the root call).  | 
**groupby_tag_second_level_key** | **str** | If present, it&#39;s the 2nd level key part (e.g. &#x60;customKey&#x60; on &#x60;docker.label.customKey&#x60;) | [optional] 

## Example

```python
from instana_client.models.group import Group

# TODO update the JSON string below
json = "{}"
# create an instance of Group from a JSON string
group_instance = Group.from_json(json)
# print the JSON string representation of the object
print(Group.to_json())

# convert the object into a dict
group_dict = group_instance.to_dict()
# create an instance of Group from a dict
group_from_dict = Group.from_dict(group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


