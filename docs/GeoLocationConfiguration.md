# GeoLocationConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geo_detail_removal** | **str** |  | 
**geo_mapping_rules** | [**List[GeoMappingRule]**](GeoMappingRule.md) |  | [optional] 

## Example

```python
from instana_client.models.geo_location_configuration import GeoLocationConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of GeoLocationConfiguration from a JSON string
geo_location_configuration_instance = GeoLocationConfiguration.from_json(json)
# print the JSON string representation of the object
print(GeoLocationConfiguration.to_json())

# convert the object into a dict
geo_location_configuration_dict = geo_location_configuration_instance.to_dict()
# create an instance of GeoLocationConfiguration from a dict
geo_location_configuration_from_dict = GeoLocationConfiguration.from_dict(geo_location_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


