# NewApplicationConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_rules** | [**List[AccessRule]**](AccessRule.md) | Defines permissions and access relationships.  | 
**boundary_scope** | **str** | **INBOUND**: Inbound calls are calls initiated from outside the application and where the destination service is part of the selected application perspective.  **ALL**: Results and metrics for not only calls at the application perspective boundary, but also those occurring within the application perspective.  **DEFAULT**: Default value, for Application Perspectives created before the introduction of &#x60;ALL&#x60; and &#x60;INBOUND&#x60;. At present, whenever new Application Perspectives are created, there are only 2 options to select: &#x60;ALL&#x60; or &#x60;INBOUND&#x60;. It is recommended to use either &#x60;ALL&#x60; or &#x60;INBOUND&#x60; as &#x60;DEFAULT&#x60; is deprecated. &#x60;DEFAULT&#x60; is treated as &#x60;INBOUND&#x60;.  | 
**label** | **str** | Name of the Application Perspective. Eg: &#x60;app1&#x60;. | 
**match_specification** | [**MatchExpressionDTO**](MatchExpressionDTO.md) |  | [optional] 
**scope** | **str** | **INCLUDE_NO_DOWNSTREAM** : Only the selected services from the filters are included (call this the core set). This is useful when you treat the services as opaque. An example would be the services that represent 3rd party APIs.  **INCLUDE_IMMEDIATE_DOWNSTREAM_DATABASE_AND_MESSAGING** : Include the core set of services from the filters and then expand this core set to include the database and messaging services that the core set directly interacts with. This is useful if you are want to monitor a set of services and their direct dependencies. For example, a development team responsible for several micro-services.  **INCLUDE_ALL_DOWNSTREAM** : It effortlessly and automatically includes all the services that form the entire end-to-end dependency chain of the core set of services. This is useful if the AP will be used for troubleshooting.  | 
**tag_filter_expression** | [**TagFilterExpressionElement**](TagFilterExpressionElement.md) |  | [optional] 

## Example

```python
from instana_client.models.new_application_config import NewApplicationConfig

# TODO update the JSON string below
json = "{}"
# create an instance of NewApplicationConfig from a JSON string
new_application_config_instance = NewApplicationConfig.from_json(json)
# print the JSON string representation of the object
print(NewApplicationConfig.to_json())

# convert the object into a dict
new_application_config_dict = new_application_config_instance.to_dict()
# create an instance of NewApplicationConfig from a dict
new_application_config_from_dict = NewApplicationConfig.from_dict(new_application_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


