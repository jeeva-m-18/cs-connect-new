import glob
import re

files = glob.glob('templates/*.html')
files.extend(glob.glob('templates/*/*.html'))

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if "{ session.get('name','F')[0].upper() }" in content:
        # Regex to match the sidebar bottom and the element specifically with this icon string.
        pattern = r'<div class="dash-sidebar-bottom">\s*<div style="width:36px; height:36px; border-radius:10px; background:linear-gradient\(135deg,var\(--accent-crimson\),var\(--accent-dark\)\); display:flex; align-items:center; justify-content:center; font-size:12px; font-weight:600; color:white; border: 1px solid rgba\(255,255,255,0\.1\);">\s*\{\s*session\.get\(\'name\',\'F\'\)\[0\]\.upper\(\)\s*\}\s*</div>\s*</div>'
        new_content = re.sub(pattern, '', content)
        if new_content != content:
            with open(f, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print("Replaced in:", f)
        else:
            print("Found but could not pattern match in:", f)
