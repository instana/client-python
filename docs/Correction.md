# Correction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_correction_config_ids** | **List[str]** | IDs of correction configs that are active | [optional] 
**correction_windows** | [**List[CorrectionWindow]**](CorrectionWindow.md) | List of Correction Windows | [optional] 
**var_from** | **datetime** | Correction starting timestamp in milliseconds (13-digit) | [optional] 
**in_active_correction_config_ids** | **List[str]** | IDs of correction configs that are inactive | [optional] 
**to** | **datetime** | Correction ending timestamp in milliseconds (13-digit) | [optional] 

## Example

```python
from instana_client.models.correction import Correction

# TODO update the JSON string below
json = "{}"
# create an instance of Correction from a JSON string
correction_instance = Correction.from_json(json)
# print the JSON string representation of the object
print(Correction.to_json())

# convert the object into a dict
correction_dict = correction_instance.to_dict()
# create an instance of Correction from a dict
correction_from_dict = Correction.from_dict(correction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


