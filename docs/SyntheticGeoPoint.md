# SyntheticGeoPoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city_name** | **str** |  | 
**country_name** | **str** |  | 
**latitude** | **float** |  | 
**longitude** | **float** |  | 

## Example

```python
from instana_client.models.synthetic_geo_point import SyntheticGeoPoint

# TODO update the JSON string below
json = "{}"
# create an instance of SyntheticGeoPoint from a JSON string
synthetic_geo_point_instance = SyntheticGeoPoint.from_json(json)
# print the JSON string representation of the object
print(SyntheticGeoPoint.to_json())

# convert the object into a dict
synthetic_geo_point_dict = synthetic_geo_point_instance.to_dict()
# create an instance of SyntheticGeoPoint from a dict
synthetic_geo_point_from_dict = SyntheticGeoPoint.from_dict(synthetic_geo_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


