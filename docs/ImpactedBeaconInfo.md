# ImpactedBeaconInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**subdivision** | **str** |  | [optional] 
**user_email** | **str** |  | [optional] 
**user_name** | **str** |  | [optional] 

## Example

```python
from instana_client.models.impacted_beacon_info import ImpactedBeaconInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ImpactedBeaconInfo from a JSON string
impacted_beacon_info_instance = ImpactedBeaconInfo.from_json(json)
# print the JSON string representation of the object
print(ImpactedBeaconInfo.to_json())

# convert the object into a dict
impacted_beacon_info_dict = impacted_beacon_info_instance.to_dict()
# create an instance of ImpactedBeaconInfo from a dict
impacted_beacon_info_from_dict = ImpactedBeaconInfo.from_dict(impacted_beacon_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


