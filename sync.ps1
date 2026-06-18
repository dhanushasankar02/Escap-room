$files = @("book_rooms.html", "Contact.html", "digital_waivers.html", "home2.html", "navbar.html", "packages.html", "packages_test.html", "digital_waivers_test.html", "safety demos.html", "team_rosters.html")

$indexHtml = Get-Content -Path index.html -Raw

$navMatch = [regex]::Match($indexHtml, '(?s)<nav class="navbar">.*?</nav>')
$footerMatch = [regex]::Match($indexHtml, '(?s)<footer id="contact" class="footer">.*?</footer>')

if ($navMatch.Success -and $footerMatch.Success) {
    foreach ($file in $files) {
        $content = Get-Content -Path $file -Raw
        $content = $content -replace '(?s)<nav class="navbar">.*?</nav>', $navMatch.Value
        $content = $content -replace '(?s)<footer class="footer">.*?</footer>', $footerMatch.Value
        Set-Content -Path $file -Value $content -NoNewline
        Write-Output "Updated $file"
    }
} else {
    Write-Output "Could not find nav or footer in index.html"
}
