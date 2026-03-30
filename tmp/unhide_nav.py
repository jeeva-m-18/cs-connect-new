import glob
import re

files = glob.glob('templates/faculty_*.html')
files.extend(['templates/enter_marks.html', 'templates/my_students.html'])

for f in files:
    try:
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
            
        # 1. Update stroke color to Golden Cap if not dashboard
        # Actually I just want to match the logo color used recently in dashboard
        new_content = re.sub(r'stroke="#(?:F5E6BE|D4AF37)"', 'stroke="#D4AF37"', content)
        
        # 2. Remove the nav, .news-ticker CSS rule that hides them
        new_content = re.sub(r'nav,\s*\.news-ticker\s*\{\s*display:\s*none\s*!important;\s*\}', '', new_content)
        
        if new_content != content:
            with open(f, 'w', encoding='utf-8') as out:
                out.write(new_content)
            print('Updated style/logo across', f)
    except Exception as e:
        print('Error processing', f, e)
