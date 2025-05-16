# MetricsTestResultItem

A description of the Synthetic test associated with the result item.  This information will be included if the request was grouped by synthetic.testId or if includeAggregatedTestId was true on the request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_id** | **str** | An identifier of an application associated with the Synthetic test.  This field is deprecated and will be replace by the applicationIds field. | [optional] 
**application_ids** | **List[str]** | A list of the applications associated with the Synthetic test. | [optional] 
**location_id** | **List[str]** | A list of the locations associated with the Synthetic test. | [optional] 
**mobile_application_ids** | **List[str]** | A list of the mobile applications associated with the Synthetic test. | [optional] 
**service_id** | **str** | A service associated with the Synthetic test. | [optional] 
**test_id** | **str** | The testId for the Synthetic test. | 
**test_name** | **str** | The Synthetic test&#39;s name. | [optional] 
**website_ids** | **List[str]** | A list of the websites associated with the Synthetic test. | [optional] 

## Example

```python
from instana_client.models.metrics_test_result_item import MetricsTestResultItem

# TODO update the JSON string below
json = "{}"
# create an instance of MetricsTestResultItem from a JSON string
metrics_test_result_item_instance = MetricsTestResultItem.from_json(json)
# print the JSON string representation of the object
print(MetricsTestResultItem.to_json())

# convert the object into a dict
metrics_test_result_item_dict = metrics_test_result_item_instance.to_dict()
# create an instance of MetricsTestResultItem from a dict
metrics_test_result_item_from_dict = MetricsTestResultItem.from_dict(metrics_test_result_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


