# GeoMappingRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accuracy_radius** | **int** |  | [optional] 
**cidr** | **str** |  | 
**city** | **str** |  | [optional] 
**continent** | **str** |  | [optional] 
**continent_code** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**latitude** | **float** |  | [optional] 
**least_specific_subdivision** | [**GeoSubdivision**](GeoSubdivision.md) |  | [optional] 
**longitude** | **float** |  | [optional] 
**subdivisions** | [**List[GeoSubdivision]**](GeoSubdivision.md) |  | 

## Example

```python
from instana_client.models.geo_mapping_rule import GeoMappingRule

# TODO update the JSON string below
json = "{}"
# create an instance of GeoMappingRule from a JSON string
geo_mapping_rule_instance = GeoMappingRule.from_json(json)
# print the JSON string representation of the object
print(GeoMappingRule.to_json())

# convert the object into a dict
geo_mapping_rule_dict = geo_mapping_rule_instance.to_dict()
# create an instance of GeoMappingRule from a dict
geo_mapping_rule_from_dict = GeoMappingRule.from_dict(geo_mapping_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


