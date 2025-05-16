# Order

Specifies the ordering of the results. It contains fields that define the sorting criteria, the collation for sorting, and the direction in which the results should be ordered. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**by** | **str** | If the granularity is set to &#x60;1&#x60; you can use the metric name eg. &#x60;latency.p95&#x60; to order by that value. | 
**collation** | **str** | Language code used for sorting. Ignored for infrastructure queries. | [optional] 
**direction** | **str** | The order in which results will be sorted, either &#x60;ASC&#x60; for ascending or &#x60;DESC&#x60; for descending. | 

## Example

```python
from instana_client.models.order import Order

# TODO update the JSON string below
json = "{}"
# create an instance of Order from a JSON string
order_instance = Order.from_json(json)
# print the JSON string representation of the object
print(Order.to_json())

# convert the object into a dict
order_dict = order_instance.to_dict()
# create an instance of Order from a dict
order_from_dict = Order.from_dict(order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


