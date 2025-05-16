# GeoSubdivision


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**name** | **str** |  | 

## Example

```python
from instana_client.models.geo_subdivision import GeoSubdivision

# TODO update the JSON string below
json = "{}"
# create an instance of GeoSubdivision from a JSON string
geo_subdivision_instance = GeoSubdivision.from_json(json)
# print the JSON string representation of the object
print(GeoSubdivision.to_json())

# convert the object into a dict
geo_subdivision_dict = geo_subdivision_instance.to_dict()
# create an instance of GeoSubdivision from a dict
geo_subdivision_from_dict = GeoSubdivision.from_dict(geo_subdivision_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


