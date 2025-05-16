# CustomDashboardPreview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **List[str]** |  | 
**id** | **str** |  | 
**owner_id** | **str** |  | 
**title** | **str** |  | 

## Example

```python
from instana_client.models.custom_dashboard_preview import CustomDashboardPreview

# TODO update the JSON string below
json = "{}"
# create an instance of CustomDashboardPreview from a JSON string
custom_dashboard_preview_instance = CustomDashboardPreview.from_json(json)
# print the JSON string representation of the object
print(CustomDashboardPreview.to_json())

# convert the object into a dict
custom_dashboard_preview_dict = custom_dashboard_preview_instance.to_dict()
# create an instance of CustomDashboardPreview from a dict
custom_dashboard_preview_from_dict = CustomDashboardPreview.from_dict(custom_dashboard_preview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


