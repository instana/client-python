# EndpointConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint_case** | **str** | This represents case sensitivity of endpoints of a service. Let&#39;s say in a service there are three endpoints, &#x60;user&#x60;, &#x60;Order&#x60; and &#x60;PAYMENT&#x60;:   For example, if &#x60;endpointCase&#x60; is &#x60;UPPER&#x60;, then endpoint names are converted to &#x60;USER&#x60;, &#x60;ORDER&#x60; and &#x60;PAYMENT&#x60;.   If &#x60;endpointCase&#x60; is &#x60;LOWER&#x60;, then endpoint names are converted to &#x60;user&#x60;, &#x60;order&#x60; and &#x60;payment&#x60;.   If &#x60;endpointCase&#x60; is &#x60;ORIGINAL&#x60;, then endpoint names are converted to &#x60;user&#x60;, &#x60;Order&#x60; and &#x60;PAYMENT&#x60;.  | 
**endpoint_name_by_collected_path_template_rule_enabled** | **bool** | The highest default precedence of endpoint rule is creating endpoint is based on path template. For example, &#x60;&#x60;&#x60; /hospital/1948/patient/291148 /hospital/728/patient/924892 /hospital/47/patient/25978 /hospital/108429/patient/1847 &#x60;&#x60;&#x60; can be considered as &#x60;/hospital/{hid}/patient/{pid}&#x60; if this rule is enabled. For most of the use cases, this rule should be enabled.  | [optional] 
**endpoint_name_by_first_path_segment_rule_enabled** | **bool** | There are endpoint extraction rules in Instana which take the first path segment from the HTTP request and turn this into an endpoint name. For example, given the following URLs &#x60;/users/123/profile&#x60; and &#x60;/users/123/settings&#x60;, the extraction rule will only take the first segment. As a result endpoint name will be &#x60;users&#x60;. Although this is useful in cases where broad overview of monitoring is required, lot of use cases are more specified. Considering the above example, if this rule is enabled, Instana can&#39;t distinguish between &#x60;profile&#x60; or &#x60;settings&#x60; as endpoints. For use cases where endpoints has to be monitored at fine granular level, this flag should be set to &#x60;false&#x60;.  | [optional] 
**rules** | [**List[HttpEndpointRule]**](HttpEndpointRule.md) | Specify custom rule configuration apart from Instana predefined rules. This rule has the highest precedence. This is only available for HTTP endpoints. | [optional] 
**service_id** | **str** | An Instana generated unique identifier for a Service. If specified, the list of results will be filtered for the specified Service ID. Eg: &#x60;3feb3dcd206c166ef2b41c707e0cd38d7cd325aa&#x60;. One can see the service id from Instana UI by going to a Service page. In the URL, there will be &#x60;serviceId&#x3D;3feb3dcd206c166ef2b41c707e0cd38d7cd325aa&#x60;. Alternatively, one can use &#x60;Get services&#x60; API endpoint to get the service id in &#x60;id&#x60; parameter.  | 

## Example

```python
from instana_client.models.endpoint_config import EndpointConfig

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointConfig from a JSON string
endpoint_config_instance = EndpointConfig.from_json(json)
# print the JSON string representation of the object
print(EndpointConfig.to_json())

# convert the object into a dict
endpoint_config_dict = endpoint_config_instance.to_dict()
# create an instance of EndpointConfig from a dict
endpoint_config_from_dict = EndpointConfig.from_dict(endpoint_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


