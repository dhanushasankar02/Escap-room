$files = Get-ChildItem -Path . -Filter *.html

foreach ($file in $files) {
    $content = Get-Content -Path $file.FullName -Raw
    $original = $content

    # Inject color: #fff; into hero titles if missing
    $content = [regex]::Replace($content, '(\.(?:hero-main-title|split-hero-title|hero-title)\s*\{)(?![^}]*?color:)', '$1 color: #fff;')

    if ($original -ne $content) {
        Set-Content -Path $file.FullName -Value $content -Encoding UTF8 -NoNewline
        Write-Output "Fixed missing white color in hero title of $($file.Name)"
    }
}
Write-Output "All files processed."
