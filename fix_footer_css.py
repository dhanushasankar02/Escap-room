import glob
import re

files = glob.glob('d:/groww/room/*.html')

brand_pattern = re.compile(r'\.footer-brand\s*\{\s*flex:\s*1;\s*min-width:\s*200px;\s*\}')
brand_replacement = """.footer-brand {
      flex: 1;
      min-width: 250px;
      max-width: 320px;
    }"""

links_pattern = re.compile(r'\.footer-links\s*\{\s*display:\s*flex;\s*flex-wrap:\s*wrap;\s*gap:\s*3rem;\s*\}')
links_replacement = """.footer-links {
      display: flex;
      flex-wrap: wrap;
      gap: 2rem;
      flex: 2;
      justify-content: space-between;
    }"""

for fpath in files:
    try:
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = brand_pattern.sub(brand_replacement, content)
        new_content = links_pattern.sub(links_replacement, new_content)
        
        if content != new_content:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {fpath}")
    except Exception as e:
        print(f"Error on {fpath}: {e}")
