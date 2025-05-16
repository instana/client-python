# UserImpactMobileAppTimeThreshold


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**impact_measurement_method** | **str** |  | 
**user_percentage** | **float** |  | [optional] 
**users** | **int** |  | [optional] 

## Example

```python
from instana_client.models.user_impact_mobile_app_time_threshold import UserImpactMobileAppTimeThreshold

# TODO update the JSON string below
json = "{}"
# create an instance of UserImpactMobileAppTimeThreshold from a JSON string
user_impact_mobile_app_time_threshold_instance = UserImpactMobileAppTimeThreshold.from_json(json)
# print the JSON string representation of the object
print(UserImpactMobileAppTimeThreshold.to_json())

# convert the object into a dict
user_impact_mobile_app_time_threshold_dict = user_impact_mobile_app_time_threshold_instance.to_dict()
# create an instance of UserImpactMobileAppTimeThreshold from a dict
user_impact_mobile_app_time_threshold_from_dict = UserImpactMobileAppTimeThreshold.from_dict(user_impact_mobile_app_time_threshold_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


