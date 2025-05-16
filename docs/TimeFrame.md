# TimeFrame

Time range for which the data should be retrieved.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to** | **int** | end of timeframe expressed as the Unix epoch time in milliseconds. Eg: &#x60;ISO 8601&#x60; standard time &#x60;2024-06-27T05:05:55.615Z&#x60; can be represented as &#x60;1719464755615&#x60; in Unix epoch time in milliseconds. | [optional] 
**window_size** | **int** | windowSize in milliseconds | [optional] 

## Example

```python
from instana_client.models.time_frame import TimeFrame

# TODO update the JSON string below
json = "{}"
# create an instance of TimeFrame from a JSON string
time_frame_instance = TimeFrame.from_json(json)
# print the JSON string representation of the object
print(TimeFrame.to_json())

# convert the object into a dict
time_frame_dict = time_frame_instance.to_dict()
# create an instance of TimeFrame from a dict
time_frame_from_dict = TimeFrame.from_dict(time_frame_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


