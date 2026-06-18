$adminFile = "admin_dashboard.html"
$userFile = "user_dashboard.html"

# Fix admin_dashboard.html
$admin = Get-Content -Path $adminFile -Raw
# Fix inline styles for h3 and h4
$admin = [regex]::Replace($admin, '(<h[34][^>]*?)color:\s*#fff([^>]*?>)', '$1color: var(--text-main)$2')
# Fix .brand-name
$admin = [regex]::Replace($admin, '(\.brand-name\s*\{[^}]*?)color:\s*#fff([^}]*\})', '$1color: var(--text-main)$2')
# Fix .section-title
$admin = [regex]::Replace($admin, '(\.section-title\s*\{[^}]*?)color:\s*#fff([^}]*\})', '$1color: var(--text-main)$2')
Set-Content -Path $adminFile -Value $admin -Encoding UTF8 -NoNewline

# Fix user_dashboard.html
$user = Get-Content -Path $userFile -Raw
# Fix .section-title gradient
$user = [regex]::Replace($user, '(\.section-title\s*\{[^}]*?background:\s*linear-gradient\([^,]+,\s*)#fff([^)]*\))', '$1var(--text-main)$2')
Set-Content -Path $userFile -Value $user -Encoding UTF8 -NoNewline

Write-Output "Fixed visibility issues in both dashboards"
