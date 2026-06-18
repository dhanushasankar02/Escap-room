import glob
import re

files = glob.glob('d:/groww/room/*.html')

# Flexible regex for the Legal column
legal_col_pattern = re.compile(
    r'\s*<div class="footer-column">\s*<h4>Legal</h4>\s*<a href="[^"]*" class="footer-link">Privacy Policy</a>\s*<a href="[^"]*" class="footer-link">Terms of Service</a>\s*<a href="[^"]*" class="footer-link">Cookie Policy</a>\s*</div>',
    re.MULTILINE | re.IGNORECASE
)

# Alternative more robust regex for Legal column (incase of javascript:void(0) etc.)
legal_col_pattern = re.compile(
    r'\s*<div class="footer-column">\s*<h4>Legal</h4>\s*<a[^>]*>Privacy Policy</a>\s*<a[^>]*>Terms of Service</a>\s*<a[^>]*>Cookie Policy</a>\s*</div>',
    re.MULTILINE | re.IGNORECASE
)

newsletter_pattern = re.compile(r'<div class="footer-column newsletter-col"\s*style="max-width:\s*280px;">')
newsletter_replacement = '<div class="footer-column newsletter-col" style="flex: 1.5; min-width: 260px; max-width: 350px;">'

count = 0
for fpath in files:
    try:
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = legal_col_pattern.sub('', content)
        new_content = newsletter_pattern.sub(newsletter_replacement, new_content)
        
        if content != new_content:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {fpath}")
            count += 1
    except Exception as e:
        print(f"Error on {fpath}: {e}")

print(f"Total files updated: {count}")
