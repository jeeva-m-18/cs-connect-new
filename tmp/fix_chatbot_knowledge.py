"""
Fix chatbot: seed institutional leadership data into website_content
"""
import sys, os
os.environ['PYTHONIOENCODING'] = 'utf-8'
sys.path.insert(0, r'c:\Users\LENOVO\Desktop\Mini project\cs_connect')
os.chdir(r'c:\Users\LENOVO\Desktop\Mini project\cs_connect')
from dotenv import load_dotenv
load_dotenv()
import psycopg2

conn = psycopg2.connect(os.environ.get('LOCAL_DATABASE_URL'))
cur = conn.cursor()

leadership_entries = [
    (
        "https://www.aisat.ac.in/about/",
        "AISAT Institutional Leadership - Principal, HOD, Manager, Vice Principal",
        """AISAT Institutional Leadership

Principal: Dr. Veena V.
Role: Principal of AISAT (Albertian Institute of Science and Technology)
Qualification: Ph.D. Engineering
She is the Academic Head of AISAT.

Manager / Chairman: Rev. Fr. Antony Vacko Arackal
Role: Manager and Chairman of AISAT
Organization: Diocese of Ernakulam-Angamaly

Assistant Manager: Rev. Fr. Manoj Francis Marottickal
Role: Assistant Manager
Responsibilities: Management Operations

Vice Principal (Administration): Prof. Paul Ansel V.
Role: Vice Principal overseeing Administration at AISAT

Vice Principal (Academics): Prof. Kanaka Xavier
Role: Vice Principal overseeing Academics at AISAT

HOD (Head of Department) CSE: Dr. Jeswin Roy Dcouth
Role: Head of Department (HoD) of Computer Science and Engineering (CSE) at AISAT
Designation: HoD and Associate Professor
Email: jeswin@aisat.ac.in

The HOD of AISAT CSE department is Dr. Jeswin Roy Dcouth.
The Principal of AISAT is Dr. Veena V.
The Manager of AISAT is Rev. Fr. Antony Vacko Arackal.
"""
    ),
    (
        "https://www.aisat.ac.in/departments/cse/",
        "AISAT HOD - Head of Department CSE - Dr. Jeswin Roy Dcouth",
        """Head of Department (HOD) - CSE

Name: Dr. Jeswin Roy Dcouth
Designation: HoD and Associate Professor
Department: Computer Science and Engineering (CSE)
College: AISAT (Albertian Institute of Science and Technology), Kalamassery, Ernakulam, Kerala
Email: jeswin@aisat.ac.in

Dr. Jeswin Roy Dcouth is the HOD (Head of Department) of the CSE department at AISAT.
He is also an Associate Professor in the department.
"""
    ),
    (
        "https://www.aisat.ac.in/principal/",
        "AISAT Principal - Dr. Veena V.",
        """Principal of AISAT

Name: Dr. Veena V.
Designation: Principal
Institution: AISAT (Albertian Institute of Science and Technology), Kalamassery, Kerala
Qualification: Ph.D. Engineering

Dr. Veena V. is the Principal and Academic Head of AISAT Engineering College.
"""
    ),
]

for url, title, content in leadership_entries:
    cur.execute("SELECT id FROM website_content WHERE title = %s", (title,))
    existing = cur.fetchone()
    if existing:
        cur.execute(
            "UPDATE website_content SET content = %s, url = %s WHERE title = %s",
            (content, url, title)
        )
        print(f"[UPDATE] {title}")
    else:
        cur.execute(
            "INSERT INTO website_content (url, title, content) VALUES (%s, %s, %s)",
            (url, title, content)
        )
        print(f"[INSERT] {title}")

conn.commit()

# Verify
cur.execute("SELECT COUNT(*) FROM website_content")
print(f"\nTotal website_content rows: {cur.fetchone()[0]}")

# Test the search - simulate what the chatbot does for 'who is hod'
print("\n=== Simulating chatbot search for 'hod' ===")
patterns = ['%hod%']
query_string = 'hod'
cur.execute("""
    SELECT 'FACULTY' as cat, name as title, 
           'Designation: ' || designation as details,
           similarity(name, %s) as score
    FROM faculty 
    WHERE name ILIKE ANY(%s) OR designation ILIKE ANY(%s)
    UNION ALL
    SELECT 'INFO' as cat, title as title, 
           LEFT(content, 200) as details,
           similarity(title, %s) as score
    FROM website_content 
    WHERE title ILIKE ANY(%s) OR content ILIKE ANY(%s)
    ORDER BY score DESC LIMIT 8
""", (query_string, patterns, patterns, query_string, ['%hod%', '%head of department%', '%HOD%'], ['%hod%', '%head of department%']))
rows = cur.fetchall()
print(f"Results: {len(rows)}")
for r in rows:
    print(f"  [{r[0]}] {r[1][:60]} | score={r[3]:.3f}")

cur.close()
conn.close()
print("\nDone!")
