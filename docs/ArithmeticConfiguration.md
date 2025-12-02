# ArithmeticConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregation** | **str** |  | 
**cross_series_aggregation** | **str** |  | [optional] 
**granularity** | **int** |    * If granularity is not specified an aggregated value for the selected timeframe is returned.    * If granularity is specified data points are returned with the specified granularity     * The granularity should not be greater than the &#x60;windowSize&#x60; (important: &#x60;windowSize&#x60; is expressed in milliseconds)     * The granularity should not be set too small relative to the &#x60;windowSize&#x60; to avoid creating an excessively large number of data points (max 600)  | [optional] 
**metric** | **str** |  | 
**missing_value** | **float** |  | [optional] 
**regex** | **bool** |  | [optional] 
**required** | **bool** | When true, metric must be present with values | [optional] 
**operation** | [**ArithmeticOperation**](ArithmeticOperation.md) |  | [optional] 

## Example

```python
from instana_client.models.arithmetic_configuration import ArithmeticConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of ArithmeticConfiguration from a JSON string
arithmetic_configuration_instance = ArithmeticConfiguration.from_json(json)
# print the JSON string representation of the object
print(ArithmeticConfiguration.to_json())

# convert the object into a dict
arithmetic_configuration_dict = arithmetic_configuration_instance.to_dict()
# create an instance of ArithmeticConfiguration from a dict
arithmetic_configuration_from_dict = ArithmeticConfiguration.from_dict(arithmetic_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


