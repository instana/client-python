# OpenAPI Issue Note: Filters API

**Spec file:** `openapi.yaml` (OpenAPI 3.0.1, spec version 1.328.1128)
**Related generated code:** `instana_client/api/default_api.py`
**Part of:** Problem 2, "Multiple API operations are poorly documented"
**Status:** Analysis only. No spec or SDK files were changed.

## 1. Affected operations

| Method | Path | operationId | Spec location |
|---|---|---|---|
| GET | `/api/filters` | `get` | `openapi.yaml` line 12856 |
| POST | `/api/filters` | `post` | `openapi.yaml` line 12864 |
| PUT | `/api/filters/{id}` | `put` | `openapi.yaml` line 12887 |
| DELETE | `/api/filters/{id}` | `delete` | `openapi.yaml` line 12873 |

## 2. What the spec contains today

Each of the four operations is defined only like this:

```yaml
/api/filters:
  get:
    operationId: get
    responses:
      default:
        content:
          application/json: {}
        description: default response
```

The `{id}` operations also have one path parameter, `id`, typed as a string and with no description.

The following are not defined for any of the four operations:

- summary
- description
- tags
- `security`
- `requestBody` (POST and PUT)
- success response (200, 201 or 204) and its schema
- error responses (400, 401, 403, 404)
- examples
- a description for the `id` parameter

There is also no global `security` in the spec, so nothing supplies a default.

## 3. Impact on the generated Python SDK

These points come from reading the generated code in `instana_client/api/default_api.py`. I did not run the calls against a live server.

### 3.1 Credentials are not sent
The spec has no `security` block on these operations, so the generator emits an empty auth list for every one of them:

```python
_auth_settings: List[str] = [
]
```

For example, `DELETE /api/filters/{id}` at `default_api.py` line 277 and `GET /api/filters` at line 1031. The `Authorization: apikey ...` header is therefore not attached, even when an API token is configured. If the server requires authentication, the calls would be rejected with 401. A caller has to work around this per call with `_request_auth` or `_headers`.

### 3.2 Filters cannot be created or updated
`POST /api/filters` and `PUT /api/filters/{id}` have no `requestBody`. The generated `post()` method takes no body argument, and `put()` takes only `id`. The SDK has no normal way to send a filter definition.

### 3.3 Nothing can be read back
The `default` response has an empty content object and no schema, so the response type map is empty (`_response_types_map = {}`) and every method is typed `-> None`. This means:

- `get()` returns no list of filters.
- `post()` and `put()` return no created or updated filter.

### 3.4 Method names are unusable
The generic operation IDs `get`, `post`, `put` and `delete` put these methods in `DefaultApi`, next to `get1`, `get2`, `get3` and `put1`, which belong to unrelated endpoints (license, terms of service, user settings). The numeric suffixes depend on the order of operations in the spec, so they can change between spec versions and silently break callers.

### 3.5 No error contract
No 400, 401, 403 or 404 is documented, so a client cannot tell a missing filter from a permission problem or an invalid payload.

## 4. Required changes

| # | Change | Depends on |
|---|---|---|
| 1 | Add `security: [{ApiKeyAuth: [<permission>]}]` to all four operations | Backend team confirms which permission guards filters |
| 2 | Add a tag such as `Filters`, which moves the operations out of `DefaultApi` | None |
| 3 | Replace the generic operation IDs with unique, meaningful ones, for example `getFilters`, `createFilter`, `updateFilter`, `deleteFilter` | None. Note that this renames SDK methods and is a breaking change for callers. |
| 4 | Add a summary and description for each operation | Backend or documentation team |
| 5 | Define a `Filter` schema and add it as the `requestBody` of POST and PUT | Backend team supplies the real filter shape |
| 6 | Add typed success responses: 200 with an array of `Filter` for GET, 200 or 201 with `Filter` for POST and PUT, and 204 or 200 for DELETE | Backend team confirms the status codes |
| 7 | Add 400, 401, 403 and 404 responses, referencing a shared error schema | Backend team defines the error shape |
| 8 | Describe the `id` path parameter and add examples for it and for each request and response body | Documentation team |

Items 1 to 4 and 7 are structural and don't depend on the filter schema, so they can be done first.

## 5. Open questions

1. What does a filter look like? Nothing in the spec or this repository defines it. I cannot propose the `Filter` schema without guessing, so it must come from the owning team or from a real response.
2. Which permission guards the filters endpoints?
3. What status code does each operation return on success, and what does POST return: the created object, its ID, or nothing?
4. What error body does the API return, and is there a shared error schema to reference?
5. Is `id` a UUID, a numeric string or another format? Does `PUT` require the same body as `POST`?

## 6. Information requested from the backend team

- One real `GET /api/filters` response.
- One `POST /api/filters` request and response pair.
- The status codes and error bodies returned for an unauthorized call and for an unknown `id`.

With these, items 5 and 6 can be written from real data.

## 7. Notes on the evidence

- The spec facts in sections 2 and 4 come from reading `openapi.yaml`.
- The SDK behaviour in section 3 comes from reading the generated `default_api.py`. It has not been verified at runtime, and the 401 behaviour in 3.1 is inferred from the empty auth settings.
- The working tree already contained many uncommitted changes to `openapi.yaml` and the generated SDK before this analysis. The line numbers above refer to that current state and may differ in other revisions.
