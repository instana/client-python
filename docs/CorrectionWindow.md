# CorrectionWindow

List of Correction Windows

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correction_configs** | **List[str]** | IDs of the Correction configurations in the Correction Window | [optional] 
**var_from** | **datetime** | Correction Window starting timestamp in milliseconds (13-digit) | [optional] 
**slo_configs** | **List[str]** | IDs of the SLO configurations in the Correction Window | [optional] 
**to** | **datetime** | Correction Window ending timestamp in milliseconds (13-digit) | [optional] 

## Example

```python
from instana_client.models.correction_window import CorrectionWindow

# TODO update the JSON string below
json = "{}"
# create an instance of CorrectionWindow from a JSON string
correction_window_instance = CorrectionWindow.from_json(json)
# print the JSON string representation of the object
print(CorrectionWindow.to_json())

# convert the object into a dict
correction_window_dict = correction_window_instance.to_dict()
# create an instance of CorrectionWindow from a dict
correction_window_from_dict = CorrectionWindow.from_dict(correction_window_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


