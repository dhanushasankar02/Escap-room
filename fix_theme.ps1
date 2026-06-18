$scriptBlock = @"
  <script>
    (function() {
      const isDark = localStorage.getItem('venue_theme_dark');
      const htmlEl = document.documentElement;
      let currentTheme = htmlEl.getAttribute('data-theme');
      const isAdmin = currentTheme && currentTheme.includes('admin');
      
      if (isDark === 'true') {
        htmlEl.setAttribute('data-theme', isAdmin ? 'admin-dark' : 'dark');
      } else if (isDark === 'false') {
        if (isAdmin) {
          htmlEl.setAttribute('data-theme', 'admin-light');
        } else if (currentTheme === 'dark' || currentTheme === 'light') {
          htmlEl.setAttribute('data-theme', 'light');
        } else {
          htmlEl.removeAttribute('data-theme');
        }
      }

      document.addEventListener('DOMContentLoaded', () => {
        document.body.addEventListener('click', (e) => {
          const toggleBtn = e.target.closest('#theme-toggle, #mobile-theme-toggle');
          if (toggleBtn) {
            setTimeout(() => {
              const theme = document.documentElement.getAttribute('data-theme');
              const darkActive = theme === 'dark' || theme === 'admin-dark';
              localStorage.setItem('venue_theme_dark', darkActive);
            }, 50);
          }
        });

        setTimeout(() => {
          const theme = document.documentElement.getAttribute('data-theme');
          const darkActive = theme === 'dark' || theme === 'admin-dark';
          
          const themeIcons = document.querySelectorAll('#theme-icon, #theme-toggle i, #mobile-theme-icon');
          themeIcons.forEach(icon => {
            if (darkActive) {
              icon.classList.remove('fa-moon');
              icon.classList.add('fa-sun');
            } else {
              icon.classList.remove('fa-sun');
              icon.classList.add('fa-moon');
            }
          });
        }, 100);
      });
    })();
  </script>
</head>
"@

$files = Get-ChildItem -Path . -Filter *.html
foreach ($file in $files) {
    $content = Get-Content -Path $file.FullName -Raw
    if ($content -notmatch "venue_theme_dark") {
        $content = $content -replace "(?i)</head>", $scriptBlock
        Set-Content -Path $file.FullName -Value $content -Encoding UTF8 -NoNewline
        Write-Output "Updated $($file.Name)"
    } else {
        Write-Output "Skipped $($file.Name) (already injected)"
    }
}
