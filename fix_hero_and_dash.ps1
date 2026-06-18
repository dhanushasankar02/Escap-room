$files = Get-ChildItem -Path . -Filter *.html

foreach ($file in $files) {
    $content = Get-Content -Path $file.FullName -Raw
    $original = $content
    
    # 1. Darken --text-muted in light mode for better visibility (particularly affects dashboards)
    $content = $content -replace '--text-muted:\s*#64748b', '--text-muted: #475569'
    
    # 2. Fix hero descriptions using text-secondary which disappear in light mode
    # Matches any class with 'hero' in it, finding 'color: var(--text-secondary)' and replacing it with a light grey
    $content = [regex]::Replace($content, '(\.(?:[a-zA-Z0-9_-]*hero[a-zA-Z0-9_-]*)\s*\{[^\}]*?color:\s*)var\(--text-secondary\)', '${1}#e2e8f0')

    if ($original -ne $content) {
        Set-Content -Path $file.FullName -Value $content -Encoding UTF8 -NoNewline
        Write-Output "Fixed visibility in $($file.Name)"
    }
}
