$Headers = @{
    "Accept" = "application/vnd.github+json"
    "Authorization" = "Bearer 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"
    "X-GitHub-Api-Version" = "2022-11-28"
}

"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"

$Uri = "https://api.github.com/repos/nksharma/CICD_Project/commits"

$Response = Invoke-WebRequest -Uri $Uri -Headers $Headers -Method Get

$Response.Content

# You can access the response content as a string
#$Content = $Response.Content

#get-content -name $Content

# Or you can convert the response content to a PowerShell object
#$Object = $Response | ConvertFrom-Json


