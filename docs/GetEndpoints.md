# GetEndpoints


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_boundary_scope** | **str** | Use when querying calls of an application:  &#x60;INBOUND&#x60;: only inbound calls   &#x60;ALL&#x60;: all the calls to that application (inbound + internal) | [optional] 
**application_id** | **str** | An Instana generated unique identifier for an Application. If specified, the list of results will be filtered for the specified Application ID. Eg: &#x60;Av62RoIKQv-A3n6DbMQh9g&#x60;. One can see the application id from Instana UI by going to an Application Perspective page. In the URL, there will be &#x60;appId&#x3D;Av62RoIKQv-A3n6DbMQh9g&#x60;. Alternatively, one can use &#x60;Get applications&#x60; API endpoint to get the application id in &#x60;id&#x60; parameter.  | [optional] 
**endpoint_id** | **str** | An Instana generated unique identifier for an Endpoint. If specified, the list of results will be filtered for the specified Endpoint ID. Eg &#x60;NCRq5oYnan5x-PkdTPQwLLUdu5M&#x60;. One can see the endpoint id from Instana UI by going to an Endpoint page. In the URL, there will be &#x60;endpointId&#x3D;NCRq5oYnan5x-PkdTPQwLLUdu5M&#x60;. Alternatively, one can use &#x60;Get endpoints&#x60; API endpoint to get the endpoint id in &#x60;id&#x60; parameter.  | [optional] 
**endpoint_types** | **List[str]** | A list of endpoint types, each of which is a string. An endpoint can specified for a database, an SDK, etc. | [optional] 
**exclude_synthetic** | **bool** | A variable used to specify whether synthetic endpoints should be excluded. If set to &#39;true&#39;, synthetic endpoints will be excluded from the result. | [optional] 
**metrics** | [**List[AppDataMetricConfiguration]**](AppDataMetricConfiguration.md) | A list of objects each of which defines a metric and the (statistical) aggregation -- MEAN, SUM, MAX, etc -- that should be used to summarize it for the defined time frame. Eg: &#x60;[{ &#39;metric&#39;: &#39;latency&#39;, &#39;aggregation&#39;: &#39;MEAN&#39;}]&#x60;. To know more about supported metrics and its aggregation, See &#x60;Get Metric catalog&#x60;. | 
**name_filter** | **str** | filter by endpoint name with &#x60;contains&#x60; semantic. Eg: Let&#39;s say there are 2 Endpoint names &#x60;GET /api/fetch&#x60; and &#x60;GET /api/update&#x60;, you can set &#x60;GET /api/&#x60; here to include the two Endpoints. | [optional] 
**order** | [**Order**](Order.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**service_id** | **str** | An Instana generated unique identifier for a Service. If specified, the list of results will be filtered for the specified Service ID. Eg: &#x60;3feb3dcd206c166ef2b41c707e0cd38d7cd325aa&#x60;. One can see the service id from Instana UI by going to a Service page. In the URL, there will be &#x60;serviceId&#x3D;3feb3dcd206c166ef2b41c707e0cd38d7cd325aa&#x60;. Alternatively, one can use &#x60;Get services&#x60; API endpoint to get the service id in &#x60;id&#x60; parameter.  | [optional] 
**time_frame** | [**TimeFrame**](TimeFrame.md) |  | [optional] 

## Example

```python
from instana_client.models.get_endpoints import GetEndpoints

# TODO update the JSON string below
json = "{}"
# create an instance of GetEndpoints from a JSON string
get_endpoints_instance = GetEndpoints.from_json(json)
# print the JSON string representation of the object
print(GetEndpoints.to_json())

# convert the object into a dict
get_endpoints_dict = get_endpoints_instance.to_dict()
# create an instance of GetEndpoints from a dict
get_endpoints_from_dict = GetEndpoints.from_dict(get_endpoints_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


