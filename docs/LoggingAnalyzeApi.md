# instana_client.LoggingAnalyzeApi

All URIs are relative to *https://unit-tenant.instana.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_log_volume_usage**](LoggingAnalyzeApi.md#get_log_volume_usage) | **GET** /api/logging/logs/getLogVolumeUsage | Get Log Volume Usage
[**get_logs**](LoggingAnalyzeApi.md#get_logs) | **POST** /api/logging/logs/getLogs/v1 | Retrieve logs via REST API


# **get_log_volume_usage**
> LogVolumeUsageResult get_log_volume_usage(from_ts, to_ts, grouping_tag=grouping_tag)

Get Log Volume Usage

Returns aggregated log volume usage data for a specified time range and optional grouping tag.
`fromTs` and `toTs` are required and must define a valid time range (i.e., `fromTs` <= `toTs`).
Refer to the query parameter description for valid `groupingTag` values.


### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.log_volume_usage_result import LogVolumeUsageResult
from instana_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://unit-tenant.instana.io
# See configuration.py for a list of all supported configuration parameters.
configuration = instana_client.Configuration(
    host = "https://unit-tenant.instana.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with instana_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = instana_client.LoggingAnalyzeApi(api_client)
    from_ts = 1682899200 # int | Start timestamp in seconds. Must be <= `toTs`.
    to_ts = 1682899201 # int | End timestamp in seconds. Must be >= `fromTs`.
    grouping_tag = 'zone' # str | Optional tag to group volume usage by. Valid groupingTag values are: `kubernetes_cluster_name`, `kubernetes_daemonset_name`, `kubernetes_namespace_name`, `kubernetes_deployment_name`, `host_name`, `zone`.  (optional)

    try:
        # Get Log Volume Usage
        api_response = api_instance.get_log_volume_usage(from_ts, to_ts, grouping_tag=grouping_tag)
        print("The response of LoggingAnalyzeApi->get_log_volume_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoggingAnalyzeApi->get_log_volume_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_ts** | **int**| Start timestamp in seconds. Must be &lt;&#x3D; &#x60;toTs&#x60;. | 
 **to_ts** | **int**| End timestamp in seconds. Must be &gt;&#x3D; &#x60;fromTs&#x60;. | 
 **grouping_tag** | **str**| Optional tag to group volume usage by. Valid groupingTag values are: &#x60;kubernetes_cluster_name&#x60;, &#x60;kubernetes_daemonset_name&#x60;, &#x60;kubernetes_namespace_name&#x60;, &#x60;kubernetes_deployment_name&#x60;, &#x60;host_name&#x60;, &#x60;zone&#x60;.  | [optional] 

### Return type

[**LogVolumeUsageResult**](LogVolumeUsageResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved log volume usage data |  -  |
**400** | Invalid request (e.g., missing or incorrect time parameters) |  -  |
**500** | Unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logs**
> LogsApiResponse get_logs(logs_query)

Retrieve logs via REST API

Returns logs (up to the specified retrievalSize) for a given time range with optional filters to help users
efficiently troubleshoot and resolve issues.

**The JSON payload must include:**

- `timeConfig`: Time range configuration with `to` (Unix timestamp in milliseconds) and `windowSize` (duration in ms).

- `retrievalSize`: Maximum number of logs to return per request (required, range: `1`-`200`).
  * If you specify a value > `200`, it will be automatically reduced to `200`.
  * Returns `HTTP 500 Internal Server Error` for values < `0`, non-integer types, or if missing.

- `orderDirection`: Sort order - "ASC" (oldest first) or "DESC" (newest first).

- `offset`: (<u>Optional</u>) Pagination offset specifies the number of log entries to skip before returning results.
  * Defaults to `0`, with permitted value range: [`0`,`2000`].
  * This field controls pagination by skipping a specified number of logs from the beginning of the result set.
  * Example: With retrievalSize=`200` and offset=`0`, you get logs `1`-`200`. To get the next page, set offset=`200` to skip the first `200` logs and retrieve logs `201`-`400`.
  * Example: Setting offset=10 skips the first `10` log entries and starts returning results from the 11th entry onwards
  * Returns `HTTP 500 Internal Server Error` response if value is negative or non-integer.

- `tagFilterExpression`: (<u>Optional</u>) Filter criteria for log attributes.

- `requestedTags`: Array of tag names to include in the response.
  * You can select up to 10 tags from the available list:
  ```
  aws.ecs.containerId
  aws.ecs.containerName
  containerd.containerId
  crio.containerId
  docker.containerId
  docker.containerName
  expiration.ts.seconds
  garden.containerId
  host.name
  kubernetes.cluster.name
  kubernetes.container.name
  kubernetes.deployment.name
  kubernetes.namespace.name
  kubernetes.node.name
  kubernetes.pod.name
  log.applications
  log.custom
  log.exception.message
  log.exception.stackTrace
  log.exception.type
  log.file.path
  log.hostId
  log.level
  log.message
  log.streamName
  log.timestamp
  log.traceId
  process.id
  ```

**Response Payload Fields:**

- `items`: Array of log entries matching the query criteria.

- `totalHits`: Total number of log entries matching the query across all pages (not just the current page).
  * Use this value to calculate total pages or display result counts to users.
  * Example: If totalHits=`450` and retrievalSize=`200`, you have 3 pages total (200 + 200 + 50).

- `canLoadMore`: Boolean indicating whether more log entries are available beyond the current page.
  * When true, increment the offset parameter to retrieve the next page.
  * Example: If retrievalSize=`200`, offset=`0`, and canLoadMore=`true`, set offset=`200` for the next request.
  * When false, you have reached the end of the result set.

- `adjustedTimeFrame`: Reserved for future use (currently always null).
  * This field may be used in the future to indicate if the requested time range was automatically adjusted.

Refer to the RequestBody section for the complete LogsQuery schema.

When using the UI to construct the curl request, select the desired filters and time window, then click the "API Query" button to automatically generate a curl request with current UI selections. By default, 4 tags are always included in requests generated by the "API Query" button, but may be changed as needed.

```"log.timestamp", "log.level", "log.message", "log.custom"```

Example curl request (can be auto-generated via the "API Query" button in the Instana UI):
 ```
    curl -X POST <Host>/api/logging/logs/getLogs/v1 \
      -H "Authorization: apiToken YOUR_API_TOKEN" \
      -H "Content-Type: application/json" \
      -d '{
        "timeConfig": {
          "to": 1711800000000,
          "focusedMoment": 1711800000000,
          "autoRefresh": false,
          "windowSize": 3600000
        },
        "requestedTags": [
          "log.traceId",
          "log.applications",
          "process.id",
          "host.name",
          "docker.containerName",
          "kubernetes.pod.name"
        ],
        "tagFilterExpression": {
         "type": "EXPRESSION",
         "logicalOperator": "AND",
         "elements": [
           {
            "type": "TAG_FILTER",
             "name": "log.streamName",
             "operator": "EQUALS",
             "entity": "NOT_APPLICABLE",
             "value": "log.go"
            },
            {
             "type": "TAG_FILTER",
             "name": "service.name",
             "operator": "EQUALS",
             "entity": "DESTINATION",
              "value": "dispatch"
            }
          ]
        },
        "retrievalSize": 200,
        "offset": 0,
        "orderDirection": "DESC"
      }'
 ```


### Example

* Api Key Authentication (ApiKeyAuth):

```python
import instana_client
from instana_client.models.logs_api_response import LogsApiResponse
from instana_client.models.logs_query import LogsQuery
from instana_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://unit-tenant.instana.io
# See configuration.py for a list of all supported configuration parameters.
configuration = instana_client.Configuration(
    host = "https://unit-tenant.instana.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with instana_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = instana_client.LoggingAnalyzeApi(api_client)
    logs_query = {"timeConfig":{"to":1711800000000,"focusedMoment":1711800000000,"autoRefresh":false,"windowSize":3600000},"requestedTags":["log.traceId","log.applications","process.id","host.name","docker.containerName","kubernetes.pod.name"],"tagFilterExpression":{"type":"EXPRESSION","logicalOperator":"AND","elements":[{"type":"TAG_FILTER","name":"log.streamName","operator":"EQUALS","entity":"NOT_APPLICABLE","value":"log.go"},{"type":"TAG_FILTER","name":"service.name","operator":"EQUALS","entity":"DESTINATION","value":"dispatch"}]},"retrievalSize":200,"offset":0,"orderDirection":"DESC"} # LogsQuery | 

    try:
        # Retrieve logs via REST API
        api_response = api_instance.get_logs(logs_query)
        print("The response of LoggingAnalyzeApi->get_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoggingAnalyzeApi->get_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logs_query** | [**LogsQuery**](LogsQuery.md)|  | 

### Return type

[**LogsApiResponse**](LogsApiResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved logs matching the query criteria. Returns an array of log items with metadata and pagination information. |  -  |
**500** | Unexpected server error - An internal error occurred while processing the request. |  -  |
**503** | Service unavailable - The logging service is temporarily unavailable. Please retry after some time. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

