# Occurrence

Time window of the Maintence Window configuration occurrences.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end** | **int** |  | [optional] 
**start** | **int** |  | [optional] 

## Example

```python
from instana_client.models.occurrence import Occurrence

# TODO update the JSON string below
json = "{}"
# create an instance of Occurrence from a JSON string
occurrence_instance = Occurrence.from_json(json)
# print the JSON string representation of the object
print(Occurrence.to_json())

# convert the object into a dict
occurrence_dict = occurrence_instance.to_dict()
# create an instance of Occurrence from a dict
occurrence_from_dict = Occurrence.from_dict(occurrence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


