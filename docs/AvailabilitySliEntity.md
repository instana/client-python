# AvailabilitySliEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_id** | **str** | Specifies the ID of the Application that is to be monitored by the SLO | [optional] 
**bad_event_filter_expression** | [**TagFilterExpressionElement**](TagFilterExpressionElement.md) |  | [optional] 
**bad_event_filters** | [**List[TagFilter]**](TagFilter.md) | Defines the logical expression to filter data and classify events as Bad Events | [optional] 
**boundary_scope** | **str** | Defines the boundary of calls to be monitored, specifying whether to track all calls or only inbound calls | 
**endpoint_id** | **str** | Specifies the ID of the Endpoint to be monitored by the availability-based application SLO | [optional] 
**good_event_filter_expression** | [**TagFilterExpressionElement**](TagFilterExpressionElement.md) |  | [optional] 
**good_event_filters** | [**List[TagFilter]**](TagFilter.md) | Defines the logical expression to filter data and classify events as Good Events | [optional] 
**include_internal** | **bool** | Boolean value indicating whether internal calls should be included in the monitoring process | [optional] 
**include_synthetic** | **bool** | Boolean value indicating whether synthetic calls should be included in the monitoring process | [optional] 
**service_id** | **str** | Identifies the service to be monitored by the availability-based application SLO | [optional] 

## Example

```python
from instana_client.models.availability_sli_entity import AvailabilitySliEntity

# TODO update the JSON string below
json = "{}"
# create an instance of AvailabilitySliEntity from a JSON string
availability_sli_entity_instance = AvailabilitySliEntity.from_json(json)
# print the JSON string representation of the object
print(AvailabilitySliEntity.to_json())

# convert the object into a dict
availability_sli_entity_dict = availability_sli_entity_instance.to_dict()
# create an instance of AvailabilitySliEntity from a dict
availability_sli_entity_from_dict = AvailabilitySliEntity.from_dict(availability_sli_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


