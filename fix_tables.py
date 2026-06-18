import os

files_to_fix = [
    r'd:\groww\room\admin_dashboard.html',
    r'd:\groww\room\user_dashboard.html'
]

for file_path in files_to_fix:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We want to replace <table class="data-table"> with <div class="table-container">\n<table class="data-table">
    # BUT we need to make sure we don't double wrap if it's already wrapped.
    # We will search for '<table class="data-table">' and check if the previous non-whitespace characters are '<div class="table-container">'
    
    import re
    
    # Let's split by table start and end. A better approach is regex.
    # Find all <table ...> ... </table>
    # Replace with <div class="table-container">\n<table ...> ... </table>\n</div>
    # But only if not already preceded by <div class="table-container">
    
    # A simpler way since we control the files:
    # Just do a naive replace first to see. If there are no .table-container around tables currently.
    
    # Let's just do a manual replace, but we must be careful with indentation.
    lines = content.splitlines()
    new_lines = []
    
    in_table = False
    table_indent = ""
    
    for i, line in enumerate(lines):
        if '<table class="data-table">' in line:
            # Check if previous line has table-container
            if i > 0 and 'class="table-container"' in lines[i-1]:
                new_lines.append(line)
                continue
            indent = line[:len(line) - len(line.lstrip())]
            new_lines.append(indent + '<div class="table-container">')
            new_lines.append(line)
            in_table = True
            table_indent = indent
        elif '</table>' in line and in_table:
            new_lines.append(line)
            new_lines.append(table_indent + '</div>')
            in_table = False
        else:
            new_lines.append(line)
            
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(new_lines))
    print(f"Fixed {file_path}")

