import re
import os

files = [
    "templates/faculty_dashboard.html",
    "templates/faculty_timetable.html",
    "templates/enter_marks.html",
    "templates/faculty_library.html",
    "templates/faculty_upload_material.html",
    "templates/faculty_send_circular.html",
    "templates/my_students.html"
]

sidebar_template = """  <aside class="dash-sidebar">
    <div class="dash-sidebar-logo">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#F5E6BE" stroke-width="2"><path d="M22 10v6M2 10l10-5 10 5-10 5z"></path><path d="M6 12v5c3 3 9 3 12 0v-5"></path></svg>
    </div>
    <nav class="dash-sidebar-items">
      <div class="dash-sidebar-item {active_dash}" title="Dashboard" onclick="location.href='/faculty-dashboard'">
        <i data-lucide="layout-dashboard"></i>
        <span class="nav-label">Dashboard</span>
      </div>
      <div class="dash-sidebar-item {active_classes}" title="My Classes" onclick="location.href='/timetable'">
        <i data-lucide="book-open"></i>
        <span class="nav-label">My Classes</span>
      </div>
      <div class="dash-sidebar-item {active_marks}" title="Marks" onclick="location.href='/marks-entry'">
        <i data-lucide="edit-3"></i>
        <span class="nav-label">Marks</span>
      </div>
      <div class="dash-sidebar-item {active_lib}" title="Library" onclick="location.href='/faculty-dashboard/library'">
        <i data-lucide="library"></i>
        <span class="nav-label">Library Portal</span>
      </div>
      <div class="dash-sidebar-item {active_up}" title="Upload" onclick="location.href='/faculty/upload-material'">
        <i data-lucide="upload-cloud"></i>
        <span class="nav-label">Upload</span>
      </div>
      <div class="dash-sidebar-item {active_circ}" title="Circular" onclick="location.href='/faculty/send-circular'">
        <i data-lucide="send"></i>
        <span class="nav-label">Circular</span>
      </div>
    </nav>
    <div class="dash-sidebar-bottom">
      <div style="width:36px; height:36px; border-radius:10px; background:linear-gradient(135deg,var(--accent-crimson),var(--accent-dark)); display:flex; align-items:center; justify-content:center; font-size:12px; font-weight:600; color:white; border: 1px solid rgba(255,255,255,0.1);">
        {{ session.get('name','F')[0].upper() }}
      </div>
    </div>
  </aside>"""

for f in files:
    if not os.path.exists(f): 
        print(f"Skipping {f}")
        continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    act = { 'active_dash': '', 'active_classes': '', 'active_marks': '', 'active_lib': '', 'active_up': '', 'active_circ': '' }
    if 'faculty_dashboard' in f: act['active_dash'] = 'active'
    elif 'timetable' in f or 'my_students' in f: act['active_classes'] = 'active'
    elif 'enter_marks' in f: act['active_marks'] = 'active'
    elif 'library' in f: act['active_lib'] = 'active'
    elif 'upload' in f: act['active_up'] = 'active'
    elif 'circular' in f: act['active_circ'] = 'active'

    new_sidebar = sidebar_template.format(**act)
    
    # regex substitution
    if '<aside class="dash-sidebar">' in content or '<aside class="sidebar">' in content:
        content = re.sub(r'<aside class="(?:dash-sidebar|sidebar)">.*?</aside>', new_sidebar, content, flags=re.DOTALL)
    
    # ensure dashboard_shared.css
    if 'dashboard_shared.css' not in content:
        content = content.replace('</head>', '  <link rel="stylesheet" href="{{ url_for(\'static\', filename=\'css/dashboard_shared.css\') }}">\n</head>')
    
    # ensure lucide
    if 'lucide@latest' not in content:
        script = '\n  <script src="https://unpkg.com/lucide@latest"></script>\n  <script>\n    if (typeof lucide !== \'undefined\') {\n      lucide.createIcons();\n    }\n  </script>\n'
        content = content.replace('</body>', script + '</body>')

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Updated {f}")
