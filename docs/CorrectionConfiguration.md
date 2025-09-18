# CorrectionConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | If value is true, then the correction window is active | [optional] 
**created_date** | **datetime** | Created date of SLO Correction Window Configuration | [optional] 
**description** | **str** | Description of the SLO Correction Window Configuration | [optional] 
**id** | **str** | SLO Correction Window Configuration ID | [optional] 
**last_updated** | **datetime** | Last updated date of SLO Correction Window Configuration | [optional] 
**name** | **str** | Name of the SLO Correction Window Configuration | 
**scheduling** | [**CorrectionScheduling**](CorrectionScheduling.md) |  | 
**slo_ids** | **List[str]** | This is the list of SLO configurations related to this Correction Window. | 
**tags** | **List[str]** | List of tags associated with SLO Correction Window Configuration | 

## Example

```python
from instana_client.models.correction_configuration import CorrectionConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of CorrectionConfiguration from a JSON string
correction_configuration_instance = CorrectionConfiguration.from_json(json)
# print the JSON string representation of the object
print(CorrectionConfiguration.to_json())

# convert the object into a dict
correction_configuration_dict = correction_configuration_instance.to_dict()
# create an instance of CorrectionConfiguration from a dict
correction_configuration_from_dict = CorrectionConfiguration.from_dict(correction_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


