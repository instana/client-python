# SyntheticCredential


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_labels** | **List[str]** |  | [optional] 
**applications** | **List[str]** |  | [optional] 
**created_at** | **int** |  | [optional] 
**created_by** | **str** |  | [optional] 
**credential_name** | **str** |  | 
**credential_value** | **str** |  | 
**mobile_app_labels** | **List[str]** |  | [optional] 
**mobile_apps** | **List[str]** |  | [optional] 
**modified_at** | **int** |  | [optional] 
**modified_by** | **str** |  | [optional] 
**website_labels** | **List[str]** |  | [optional] 
**websites** | **List[str]** |  | [optional] 

## Example

```python
from instana_client.models.synthetic_credential import SyntheticCredential

# TODO update the JSON string below
json = "{}"
# create an instance of SyntheticCredential from a JSON string
synthetic_credential_instance = SyntheticCredential.from_json(json)
# print the JSON string representation of the object
print(SyntheticCredential.to_json())

# convert the object into a dict
synthetic_credential_dict = synthetic_credential_instance.to_dict()
# create an instance of SyntheticCredential from a dict
synthetic_credential_from_dict = SyntheticCredential.from_dict(synthetic_credential_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


