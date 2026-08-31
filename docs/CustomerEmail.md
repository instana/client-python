# CustomerEmail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_email** | **str** |  | [optional] 
**email** | **str** |  | [optional] 

## Example

```python
from instana_client.models.customer_email import CustomerEmail

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerEmail from a JSON string
customer_email_instance = CustomerEmail.from_json(json)
# print the JSON string representation of the object
print(CustomerEmail.to_json())

# convert the object into a dict
customer_email_dict = customer_email_instance.to_dict()
# create an instance of CustomerEmail from a dict
customer_email_from_dict = CustomerEmail.from_dict(customer_email_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


