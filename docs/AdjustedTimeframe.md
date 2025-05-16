# AdjustedTimeframe

Time frame provided in API request is slightly adjusted in response for faster API response. For example, In request payload, if timeframe is 08:03 - 14:03, which is a 6 hour window size. It is adjusted to 08:05 - 14:00 Another example, In request payload, if timeframe is 08:20 - 08:20 (next day) which is a 24h window size. It is adjusted to 08:30 - 08:00 (next day) 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to** | **int** | end of timeframe expressed as the Unix epoch time in milliseconds. Eg: &#x60;ISO 8601&#x60; standard time &#x60;2024-06-27T05:05:55.615Z&#x60; can be represented as &#x60;1719464755615&#x60; in Unix epoch time in milliseconds. | 
**window_size** | **int** | windowSize in milliseconds | [optional] 

## Example

```python
from instana_client.models.adjusted_timeframe import AdjustedTimeframe

# TODO update the JSON string below
json = "{}"
# create an instance of AdjustedTimeframe from a JSON string
adjusted_timeframe_instance = AdjustedTimeframe.from_json(json)
# print the JSON string representation of the object
print(AdjustedTimeframe.to_json())

# convert the object into a dict
adjusted_timeframe_dict = adjusted_timeframe_instance.to_dict()
# create an instance of AdjustedTimeframe from a dict
adjusted_timeframe_from_dict = AdjustedTimeframe.from_dict(adjusted_timeframe_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


