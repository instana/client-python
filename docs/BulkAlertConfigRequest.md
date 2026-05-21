# BulkAlertConfigRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configs** | **Dict[str, List[str]]** |  | 

## Example

```python
from instana_client.models.bulk_alert_config_request import BulkAlertConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkAlertConfigRequest from a JSON string
bulk_alert_config_request_instance = BulkAlertConfigRequest.from_json(json)
# print the JSON string representation of the object
print(BulkAlertConfigRequest.to_json())

# convert the object into a dict
bulk_alert_config_request_dict = bulk_alert_config_request_instance.to_dict()
# create an instance of BulkAlertConfigRequest from a dict
bulk_alert_config_request_from_dict = BulkAlertConfigRequest.from_dict(bulk_alert_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


