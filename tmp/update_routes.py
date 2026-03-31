import os
import re

# Update library_routes.py
lib_path = "routes/library_routes.py"
with open(lib_path, "r", encoding="utf-8") as f:
    lib_content = f.read()

lib_content = re.sub(
    r'redirect\(url_for\([\'"]login[\'"]\)\)',
    r'redirect(url_for("login", next=request.path))',
    lib_content
)

with open(lib_path, "w", encoding="utf-8") as f:
    f.write(lib_content)
print("Updated library_routes.py")

# Update login.html
login_path = "templates/login.html"
with open(login_path, "r", encoding="utf-8") as f:
    login_content = f.read()

# Add hidden input for next
if "{% if next_url %}" not in login_content:
    target = '<form method="POST" action="{{ url_for(\'login\') }}">'
    replacement = target + '\n          {% if next_url %}\n          <input type="hidden" name="next" value="{{ next_url }}">\n          {% endif %}'
    login_content = login_content.replace(target, replacement)

with open(login_path, "w", encoding="utf-8") as f:
    f.write(login_content)
print("Updated login.html")
