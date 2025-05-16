# ServiceMapConnection

A list which indicates which services are consumers and which are providers in the communication chain.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calls** | **int** | The number of calls between the 2 services. Eg: The number of calls from &#x60;24558242fdeb52571cfb9fa42f1b334aa65d7e61&#x60; service to &#x60;3feb3dcd206c166ef2b41c707e0cd38d7cd325aa&#x60; service over the mentioned timeframe is &#x60;200&#x60;.   If no timeframe (&#x60;to&#x60; and &#x60;windowSize&#x60; in query paramter) is mentioned, the timeframe is taken as last hour.  | [optional] 
**error_rate** | **float** | The error rate of the calls between the 2 services. Eg: The error rate of calls from &#x60;24558242fdeb52571cfb9fa42f1b334aa65d7e61&#x60; service to &#x60;3feb3dcd206c166ef2b41c707e0cd38d7cd325aa&#x60; service over the mentioned timeframe is &#x60;0.1&#x60;.   The value is between 0 and 1.   If no timeframe (&#x60;to&#x60; and &#x60;windowSize&#x60; in query paramter) is mentioned, the timeframe is taken as last hour.  | [optional] 
**var_from** | **str** | The service that initiates a request to another service. It contains a unique service id. Eg: &#x60;24558242fdeb52571cfb9fa42f1b334aa65d7e61&#x60;.  | 
**latency** | **float** | The mean latency of the calls between the 2 services. Eg: The mean latency of calls from &#x60;24558242fdeb52571cfb9fa42f1b334aa65d7e61&#x60; service to &#x60;3feb3dcd206c166ef2b41c707e0cd38d7cd325aa&#x60; service over the mentioned timeframe is &#x60;4.46&#x60;.   The value is in milliseconds.   If no timeframe (&#x60;to&#x60; and &#x60;windowSize&#x60; in query paramter) is mentioned, the timeframe is taken as last hour.  | [optional] 
**to** | **str** | The service that receives the request sent by the source service. It contains a unique service id. Eg: &#x60;3feb3dcd206c166ef2b41c707e0cd38d7cd325aa&#x60;.  | 

## Example

```python
from instana_client.models.service_map_connection import ServiceMapConnection

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceMapConnection from a JSON string
service_map_connection_instance = ServiceMapConnection.from_json(json)
# print the JSON string representation of the object
print(ServiceMapConnection.to_json())

# convert the object into a dict
service_map_connection_dict = service_map_connection_instance.to_dict()
# create an instance of ServiceMapConnection from a dict
service_map_connection_from_dict = ServiceMapConnection.from_dict(service_map_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


