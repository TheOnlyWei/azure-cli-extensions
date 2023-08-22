# Connectedk8s Testing
Tests need to be configured before running.

1. Make a copy of `config.json.dist` and rename it to `config.json` (the config.json is git ignored).
1. Fill in the details of the newly created `config.json` file:
    - customLocationsOid: The custom locations RP service principal object id. You may search for it via AAD graph via the following `$filter` query in az rest in PowerShell (make sure to fill in the tenant id):
        ```powershell
        az rest --method get --url "https://graph.windows.net/<tenant id>/servicePrincipals?`$filter=startswith(displayName,'Custom Locations')&api-version=1.6"
        ```
    - For more information about AAD graph queries: https://learn.microsoft.com/en-us/graph/migrate-azure-ad-graph-request-differences
1. The previous step should return a JSON response with an `objectId` property. Copy this into the `customLocationsOid` property in the `config.json` file.