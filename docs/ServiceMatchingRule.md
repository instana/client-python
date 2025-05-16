# ServiceMatchingRule

Calls will be matched with the array of key-value tags present in this field.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | In Instana UI, this is shown as &#x60;Tag&#x60;. One can select a variety of pre-defined tags. Eg: &#x60;host.fqdn&#x60;, &#x60;container.label&#x60; etc.  | 
**value** | **str** | In Instana UI, this is known as &#39;key&#x60;. Eg: if one labels Docker containers such as com.acme.service-name:myservice, to map services from this label, the &#x60;key&#x60; aka &#x60;tag&#x60; would be &#x60;docker.label&#x60; and &#x60;value&#x60; aka &#x60;key&#x60; would be &#x60;com.acme.service-name&#x60;.  | 

## Example

```python
from instana_client.models.service_matching_rule import ServiceMatchingRule

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceMatchingRule from a JSON string
service_matching_rule_instance = ServiceMatchingRule.from_json(json)
# print the JSON string representation of the object
print(ServiceMatchingRule.to_json())

# convert the object into a dict
service_matching_rule_dict = service_matching_rule_instance.to_dict()
# create an instance of ServiceMatchingRule from a dict
service_matching_rule_from_dict = ServiceMatchingRule.from_dict(service_matching_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


