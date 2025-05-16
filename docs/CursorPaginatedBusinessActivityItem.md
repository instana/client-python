# CursorPaginatedBusinessActivityItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_activity** | [**BusinessActivity**](BusinessActivity.md) |  | [optional] 
**cursor** | **object** | Cursor to use between successive queries | 
**metrics** | **Dict[str, List[List[float]]]** |  | [optional] 

## Example

```python
from instana_client.models.cursor_paginated_business_activity_item import CursorPaginatedBusinessActivityItem

# TODO update the JSON string below
json = "{}"
# create an instance of CursorPaginatedBusinessActivityItem from a JSON string
cursor_paginated_business_activity_item_instance = CursorPaginatedBusinessActivityItem.from_json(json)
# print the JSON string representation of the object
print(CursorPaginatedBusinessActivityItem.to_json())

# convert the object into a dict
cursor_paginated_business_activity_item_dict = cursor_paginated_business_activity_item_instance.to_dict()
# create an instance of CursorPaginatedBusinessActivityItem from a dict
cursor_paginated_business_activity_item_from_dict = CursorPaginatedBusinessActivityItem.from_dict(cursor_paginated_business_activity_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


