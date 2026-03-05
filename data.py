# =============================================================================
# data.py — CS Connect Mock Data Layer
# -----------------------------------------------------------------------------
# All hardcoded content lives here as Python dicts/lists.
# When you add a database, replace these variables with DB queries.
# Templates remain unchanged — Flask routes just pass different objects.
# =============================================================================

# ─── Site-wide ────────────────────────────────────────────────────────────────

NEWS_TICKER = (
    "📢 Admissions Open for 2026 Batch | "
    "🎉 Our Students crowned All Kerala Champions at APJ KTU Kerala Karate Championship | "
    "📅 Next Workshop: AI in Healthcare - Feb 20th | "
    "🏆 AISAT Achieved Autonomous Status For 5 Years 2026-2031 | "
    "🎓 Batch 9 (2024): 87% Placement | 💰 Highest Package: ₹8.22 LPA"
)

# ─── Home Page ────────────────────────────────────────────────────────────────

HOME_STATS = [
    {"value": 420,  "label": "STUDENTS"},
    {"value": 17,   "label": "FACULTY"},
    {"value": 98,   "label": "% PLACEMENT"},
    {"value": 22,   "label": "PUBLICATIONS"},
]

HOME_FEATURE_CARDS = [
    {
        "icon": "📚",
        "title": "Syllabus & Curriculum",
        "description": (
            "Access the latest KTU scheme, lecture notes, and lab manuals directly "
            "from the department repository."
        ),
    },
    {
        "icon": "🎓",
        "title": "Placements",
        "description": (
            "Our students are placed in top MNCs. Check out the latest placement "
            "statistics and recruitment drives."
        ),
    },
    {
        "icon": "🔬",
        "title": "Research Labs",
        "description": (
            "State-of-the-art IoT, AI, and Big Data labs available for student "
            "projects and research."
        ),
    },
    {
        "icon": "🏆",
        "title": "Achievements",
        "description": (
            "Celebrating the victories of our students in Hackathons, Sports, and "
            "Arts festivals."
        ),
    },
]

HOME_EVENTS = [
    {"date": "MAR 15", "title": "National Tech Fest",      "description": "Join us for the biggest tech fest in the region.",         "bg_color": "#ccc"},
    {"date": "APR 02", "title": "AI Workshop",             "description": "Hands-on session on Generative AI.",                        "bg_color": "#bbb"},
    {"date": "MAY 10", "title": "Alumni Meet",             "description": "Reconnecting with our past graduates.",                     "bg_color": "#aaa"},
    {"date": "JUN 01", "title": "Project Expo",            "description": "Final year project exhibition.",                           "bg_color": "#999"},
]

# ─── Faculty Page ─────────────────────────────────────────────────────────────

FACULTY_DATA = [
    {
        "name": "Dr. Jeswin Roy Dcouth",
        "designation": "HoD & Asso. Professor",
        "designation_key": "hod",
        "qualification": "Ph.D Computer Science and Engineering, PGDCL",
        "joined": "02.06.2014",
        "research": "Cyber Security",
        "email": "jeswin@aisat.ac.in",
        "photo": "https://aisat.ac.in/wp-content/uploads/2024/01/dr.-jeswin-300x287.jpg",
    },
    {
        "name": "Ms. Divya Mohan",
        "designation": "Associate Professor",
        "designation_key": "assistant",
        "qualification": "M.Tech Software Engineering",
        "joined": "10.06.2015",
        "research": "Machine Learning",
        "email": "divya@aisat.ac.in",
        "photo": "https://aisat.ac.in/wp-content/uploads/2024/01/Ms.-Divya-Mohan-e1706040948144.jpg",
    },
    {
        "name": "Ms. Teenu Jose",
        "designation": "Assistant Professor",
        "designation_key": "assistant",
        "qualification": "M.Tech Computer Science & Engineering",
        "joined": "06.01.2020",
        "research": "Machine Learning",
        "email": "teenu@aisat.ac.in",
        "photo": "https://aisat.ac.in/wp-content/uploads/2024/01/teenu1-242x300-1-e1706205964261.png",
    },
    {
        "name": "Ms. Lima S Sebastian",
        "designation": "Assistant Professor",
        "designation_key": "assistant",
        "qualification": "M.Tech Computer Science and Engineering",
        "joined": "28.12.2014",
        "research": "Theory of Computation",
        "email": "lima@aisat.ac.in",
        "photo": "https://aisat.ac.in/wp-content/uploads/2024/01/lima-e1706206284280.jpg",
    },
    {
        "name": "Ms. Nisy John Panicker",
        "designation": "Assistant Professor (Sr.S)",
        "designation_key": "assistant",
        "qualification": "M.Tech CSE",
        "joined": "29.08.2022",
        "research": "Machine Learning, Data Science, AI",
        "email": "nisy@aisat.ac.in",
        "photo": "https://aisat.ac.in/wp-content/uploads/2024/01/nisy-e1706206510394.jpg",
    },
    {
        "name": "Dr. Lakshmi Babu",
        "designation": "Professor of Practice",
        "designation_key": "assistant",
        "qualification": "Ph.D",
        "joined": "Recent",
        "research": "Computer Science",
        "email": "lakshmi@aisat.ac.in",
        "photo": "https://via.placeholder.com/300x300/8F7A6E/FFFFFF?text=Dr.+Lakshmi+Babu",
    },
    {
        "name": "Ms. Krishna C J",
        "designation": "Assistant Professor",
        "designation_key": "assistant",
        "qualification": "M.Tech CSE",
        "joined": "25.08.2023",
        "research": "IOT, Cloud Computing",
        "email": "krishna@aisat.ac.in",
        "photo": "https://via.placeholder.com/300x300/8F7A6E/FFFFFF?text=Ms.+Krishna",
    },
    {
        "name": "Mr. Anson Antony Fertal",
        "designation": "Assistant Professor",
        "designation_key": "assistant",
        "qualification": "M.Tech CSE",
        "joined": "25.08.2023",
        "research": "Cloud Computing",
        "email": "anson@aisat.ac.in",
        "photo": "https://aisat.ac.in/wp-content/uploads/2024/01/Anson-Antony-Fertal-e1706206225672.jpeg",
    },
    {
        "name": "Ms. Sharija P M",
        "designation": "Assistant Professor",
        "designation_key": "assistant",
        "qualification": "M.Tech Computer Science & Engineering",
        "joined": "15.01.2024",
        "research": "Cyber Security",
        "email": "sharija@aisat.ac.in",
        "photo": "https://via.placeholder.com/300x300/8F7A6E/FFFFFF?text=Ms.+Sharija",
    },
    {
        "name": "Ms. Anna John Isabel",
        "designation": "Assistant Professor",
        "designation_key": "assistant",
        "qualification": "M.Tech Computer Science and Systems Engineering",
        "joined": "01.08.2024",
        "research": "Data Analytics",
        "email": "anna@aisat.ac.in",
        "photo": "https://via.placeholder.com/300x300/8F7A6E/FFFFFF?text=Ms.+Anna",
    },
    {
        "name": "Ms. Angel Mathai",
        "designation": "Assistant Professor",
        "designation_key": "assistant",
        "qualification": "M.Tech Computer Engineering",
        "joined": "01.06.2024",
        "research": "Computer Security",
        "email": "angel@aisat.ac.in",
        "photo": "https://via.placeholder.com/300x300/8F7A6E/FFFFFF?text=Ms.+Angel",
    },
    {
        "name": "Ms. Sinijoy P J",
        "designation": "Assistant Professor",
        "designation_key": "assistant",
        "qualification": "M.E Computer Science and Engineering",
        "joined": "02.06.2014",
        "research": "Cyber Physical Systems, Intrusion Detection",
        "email": "sini@aisat.ac.in",
        "photo": "https://aisat.ac.in/wp-content/uploads/2024/01/sini-e1706206307301.jpg",
    },
    {
        "name": "Ms. Sweety Joy C",
        "designation": "Assistant Professor",
        "designation_key": "assistant",
        "qualification": "M.Tech Computer Science & Engineering",
        "joined": "01.02.2024",
        "research": "Fuzzy Logic, Cyber Security",
        "email": "sweety@aisat.ac.in",
        "photo": "https://via.placeholder.com/300x300/8F7A6E/FFFFFF?text=Ms.+Sweety",
    },
    {
        "name": "Ms. Shruthi Chandran",
        "designation": "Assistant Professor",
        "designation_key": "assistant",
        "qualification": "M.Tech Computer Science and Engineering",
        "joined": "01.06.2025",
        "research": "Data Mining",
        "email": "shruthi@aisat.ac.in",
        "photo": "https://via.placeholder.com/300x300/8F7A6E/FFFFFF?text=Ms.+Shruthi",
    },
    {
        "name": "Ms. A Thilakavathy",
        "designation": "Assistant Professor",
        "designation_key": "assistant",
        "qualification": "M.Tech CSE",
        "joined": "07.02.2024",
        "research": "Network Security, Machine Learning",
        "email": "thilakavathy@aisat.ac.in",
        "photo": "https://via.placeholder.com/300x300/8F7A6E/FFFFFF?text=Ms.+Thilakavathy",
    },
    {
        "name": "Ms. Ashwathy Anda Chacko",
        "designation": "Assistant Professor",
        "designation_key": "assistant",
        "qualification": "M.Tech Computer Science and Engineering",
        "joined": "07.07.2024",
        "research": "Cloud Computing, Networking",
        "email": "ashwathy@aisat.ac.in",
        "photo": "https://via.placeholder.com/300x300/8F7A6E/FFFFFF?text=Ms.+Ashwathy",
    },
    {
        "name": "Dr. Wilson Peter Abrham",
        "designation": "Professor of Practice",
        "designation_key": "assistant",
        "qualification": "Ph.D",
        "joined": "Recent",
        "research": "Computer Science",
        "email": "wilson@aisat.ac.in",
        "photo": "https://via.placeholder.com/300x300/8F7A6E/FFFFFF?text=Dr.+Wilson+Peter",
    },
    {
        "name": "Ms. Thasneem MH",
        "designation": "Assistant Professor",
        "designation_key": "assistant",
        "qualification": "M.Tech",
        "joined": "Recent",
        "research": "Computer Science",
        "email": "thasneem@aisat.ac.in",
        "photo": "https://via.placeholder.com/300x300/8F7A6E/FFFFFF?text=Ms.+Thasneem",
    },
    {
        "name": "Ms. Thara Raveendran",
        "designation": "Assistant Professor",
        "designation_key": "assistant",
        "qualification": "M.Tech CSE",
        "joined": "01.07.2024",
        "research": "Data Analytics",
        "email": "thara@aisat.ac.in",
        "photo": "https://via.placeholder.com/300x300/8F7A6E/FFFFFF?text=Ms.+Thara",
    },
    {
        "name": "Ms. Lizabeth Roshin",
        "designation": "Assistant Professor (On Leave)",
        "designation_key": "assistant",
        "qualification": "M.Tech",
        "joined": "Recent",
        "research": "Computer Science",
        "email": "lizabeth@aisat.ac.in",
        "photo": "https://via.placeholder.com/300x300/8F7A6E/FFFFFF?text=Ms.+Lizabeth",
    },
]

STAFF_DATA = [
    {"name": "Ms. Saranya PK",   "role": "Lab Instructor", "icon": "fas fa-desktop"},
    {"name": "Ms. Ashmy Antony", "role": "Lab Instructor", "icon": "fas fa-desktop"},
    {"name": "Ms. Aleena Presathe", "role": "Lab Instructor", "icon": "fas fa-desktop"},
]

# ─── About CSE Page ───────────────────────────────────────────────────────────

DEPT_STATS_OVERVIEW = [
    {"value": "32+", "label": "Faculty Members"},
    {"value": "450+","label": "Students"},
    {"value": "4",   "label": "Advanced Labs"},
    {"value": "98%", "label": "Placement Rate"},
]

DEPT_STATS_GLANCE = [
    {"icon": "👨‍🏫", "value": "32+",   "label": "Experienced Faculty"},
    {"icon": "👨‍🎓", "value": "450+",  "label": "Current Students"},
    {"icon": "🔬",   "value": "4",     "label": "Advanced Labs"},
    {"icon": "📚",   "value": "22",    "label": "Research Publications"},
    {"icon": "🏆",   "value": "25+",   "label": "Awards & Recognitions"},
    {"icon": "💼",   "value": "98%",   "label": "Placement Rate"},
    {"icon": "🤝",   "value": "20+",   "label": "Industry Partners"},
    {"icon": "🌍",   "value": "1000+", "label": "Alumni Network"},
]

PEOS = [
    {"title": "Evolve",      "description": "Evolve as globally competent IT professionals, researchers and entrepreneurs in the field of Computer Science."},
    {"title": "Develop",     "description": "Develop innovative computing solutions for real world problems."},
    {"title": "Demonstrate", "description": "Demonstrate communication skills, leadership skills, ethical values and team work in IT professions."},
]

PSOS = [
    {"code": "PS1", "description": "Design and develop computer programs and computer based systems of moderate complexity in the areas relevant to the current computational demands of the global society."},
    {"code": "PS2", "description": "Gather knowledge in the various domains of computer science and identify a suitable career path to succeed in life."},
    {"code": "PS3", "description": "Apply the fundamentals of computer science in order to evaluate potential risks and provide creative solutions to meet the needs of society."},
]

MILESTONES = [
    {"year": "2002", "title": "Department Establishment",   "description": "CSE Department established with first B.Tech batch of 60 students.", "icon": "fas fa-flag"},
    {"year": "2008", "title": "Publications",               "description": "Faculty and students started research publications in reputed international journals and conferences.", "icon": "fas fa-book"},
    {"year": "2012", "title": "Research Lab Setup",         "description": "Established advanced research laboratories for IoT, AI, and Network Security.", "icon": "fas fa-flask"},
    {"year": "2015", "title": "M.Tech Program Launch",      "description": "Introduced M.Tech program in Computer Science, expanding academic offerings to postgraduate level.", "icon": "fas fa-graduation-cap"},
    {"year": "2018", "title": "100% Placement Achievement", "description": "Achieved unprecedented 100% placement record with students placed in top MNCs.", "icon": "fas fa-briefcase"},
    {"year": "2020", "title": "Industry Collaboration",     "description": "Established MOUs with leading tech companies for internships, training and research.", "icon": "fas fa-handshake"},
    {"year": "2022", "title": "AI Lab Inauguration",        "description": "Launched state-of-the-art AI and Machine Learning lab with high-performance computing infrastructure.", "icon": "fas fa-robot"},
    {"year": "2024", "title": "NBA Accreditation",          "description": "Received NBA accreditation, validating our commitment to quality education.", "icon": "fas fa-award"},
]

# ─── About AISAT Page ─────────────────────────────────────────────────────────

ACCREDITATIONS = [
    {"name": "NAAC", "full_name": "National Assessment and Accreditation Council", "grade": "A Grade",    "icon": "fas fa-star",          "color": "#0066cc"},
    {"name": "NBA",  "full_name": "National Board of Accreditation",               "grade": "Accredited", "icon": "fas fa-certificate",   "color": "#ff6b35"},
    {"name": "AICTE","full_name": "All India Council for Technical Education",      "grade": "Approved",   "icon": "fas fa-award",         "color": "#28a745"},
    {"name": "KTU",  "full_name": "APJ Abdul Kalam Technological University",       "grade": "Affiliated", "icon": "fas fa-graduation-cap","color": "#6f42c1"},
]

INFRASTRUCTURE = [
    {"title": "Advanced Laboratories", "description": "Fully equipped computer labs with latest hardware and software for hands-on learning.",
     "icon": "fas fa-laptop-code", "gradient": "linear-gradient(135deg, #667eea, #764ba2)",
     "tags": ["IoT Lab", "AI Lab", "Network Lab"]},
    {"title": "Central Library", "description": "Extensive collection of books, journals, and digital resources for academic research.",
     "icon": "fas fa-book-reader", "gradient": "linear-gradient(135deg, #f093fb, #f5576c)",
     "tags": ["10,000+ Books", "E-Library", "Digital Access"]},
    {"title": "Smart Classrooms", "description": "Modern classrooms with ICT-enabled teaching aids and comfortable seating.",
     "icon": "fas fa-building", "gradient": "linear-gradient(135deg, #4facfe, #00f2fe)",
     "tags": ["Smartboards", "AC Labs", "Wi-Fi"]},
    {"title": "Sports & Recreation", "description": "Comprehensive sports facilities and recreational areas for student well-being.",
     "icon": "fas fa-dumbbell", "gradient": "linear-gradient(135deg, #43e97b, #38f9d7)",
     "tags": ["Gymnasium", "Badminton Court", "Swimming Pool", "Basketball Court", "Turf"]},
    {"title": "Cafeteria & Hostel", "description": "Hygienic cafeteria and comfortable hostel facilities for students.",
     "icon": "fas fa-utensils", "gradient": "linear-gradient(135deg, #fa709a, #fee140)",
     "tags": ["Snacks & Coolbar", "Meals", "Separate Hostels", "24/7 Security"]},
    {"title": "Placement Cell", "description": "Dedicated placement cell with strong industry connections for career opportunities.",
     "icon": "fas fa-briefcase", "gradient": "linear-gradient(135deg, #30cfd0, #330867)",
     "tags": ["Training", "Internships", "Counseling"]},
]

# ─── Academics Page ───────────────────────────────────────────────────────────

PROGRAMS = [
    {
        "name": "B.Tech in Computer Science & Engineering",
        "duration": "4 Years (8 Semesters)",
        "intake": "120 Students per year",
        "eligibility": "10+2 with Physics, Mathematics & Chemistry/Computer Science",
        "extra_icon": "🏫", "extra_label": "Affiliation", "extra_value": "APJ Abdul Kalam Technological University (KTU)",
        "highlights": [
            "Industry-aligned curriculum with latest technologies",
            "Hands-on training in AI, ML, Data Science, Cloud Computing",
            "State-of-the-art computer labs and research facilities",
            "Strong industry partnerships and internship opportunities",
            "Focus on innovation, entrepreneurship, and problem-solving",
        ],
    },
    {
        "name": "M.Tech in Computer Science & Engineering",
        "duration": "2 Years (4 Semesters)",
        "intake": "18 Students per year",
        "eligibility": "B.Tech/B.E in CSE or related disciplines with valid GATE score",
        "extra_icon": "🔬", "extra_label": "Specialization", "extra_value": "Advanced Computing & Research",
        "highlights": [
            "Research-oriented curriculum with thesis component",
            "Advanced courses in Machine Learning, Big Data, Cybersecurity",
            "Opportunities to publish in international journals and conferences",
            "Industry collaboration for live projects and research",
            "Excellent placement support in R&D roles",
        ],
    },
]

SEMESTERS = [
    {
        "title": "Semester 1 - Foundation",
        "subjects": [
            {"code": "MAT101", "name": "Calculus",                               "credits": 4},
            {"code": "PHY110", "name": "Engineering Physics",                    "credits": 3},
            {"code": "CYT100", "name": "Engineering Chemistry",                  "credits": 3},
            {"code": "EST100", "name": "Engineering Graphics",                   "credits": 4},
            {"code": "BEC101", "name": "Basics of Civil & Mechanical Engineering","credits": 2},
        ],
    },
    {
        "title": "Semester 2 - Core Fundamentals",
        "subjects": [
            {"code": "MAT102", "name": "Linear Algebra & Complex Analysis",      "credits": 4},
            {"code": "PHY120", "name": "Physics Lab",                            "credits": 1},
            {"code": "BEE101", "name": "Basics of Electrical Engineering",       "credits": 3},
            {"code": "CST101", "name": "Introduction to Computing",              "credits": 3},
            {"code": "EST110", "name": "Engineering Mechanics",                  "credits": 4},
        ],
    },
    {
        "title": "Semester 3 - Programming & Logic",
        "subjects": [
            {"code": "MAT201", "name": "Discrete Mathematics",                   "credits": 4},
            {"code": "CST201", "name": "Data Structures",                        "credits": 4},
            {"code": "CST203", "name": "Logic System Design",                    "credits": 3},
            {"code": "CST205", "name": "Computer Organization & Architecture",   "credits": 4},
            {"code": "CST207", "name": "Object Oriented Programming using Java", "credits": 3},
        ],
    },
    {
        "title": "Semester 4 - Advanced Concepts",
        "subjects": [
            {"code": "CST202", "name": "Database Management Systems",            "credits": 4},
            {"code": "CST204", "name": "Operating Systems",                      "credits": 4},
            {"code": "CST206", "name": "Computer Networks",                      "credits": 3},
            {"code": "CST208", "name": "Microprocessor & Microcontroller",       "credits": 4},
        ],
    },
]

# ─── Library Page ─────────────────────────────────────────────────────────────

BOOKS_DATA = [
    {"title": "Data Structures and Algorithms",      "author": "Thomas H. Cormen",          "category": "textbook",  "status": "available","shelf": "A-42","cover_gradient": "linear-gradient(135deg,#667eea,#764ba2)","cover_icon": "fas fa-book-open"},
    {"title": "Operating System Concepts",           "author": "Abraham Silberschatz",       "category": "textbook",  "status": "issued",   "shelf": "A-38","cover_gradient": "linear-gradient(135deg,#f093fb,#f5576c)","cover_icon": "fas fa-laptop"},
    {"title": "Machine Learning",                    "author": "Tom M. Mitchell",            "category": "reference", "status": "available","shelf": "B-15","cover_gradient": "linear-gradient(135deg,#4facfe,#00f2fe)","cover_icon": "fas fa-brain"},
    {"title": "Computer Networks",                   "author": "Andrew S. Tanenbaum",        "category": "textbook",  "status": "available","shelf": "A-29","cover_gradient": "linear-gradient(135deg,#43e97b,#38f9d7)","cover_icon": "fas fa-network-wired"},
    {"title": "IEEE Transactions on AI",             "author": "IEEE",                       "category": "journal",   "status": "available","shelf": "C-12","cover_gradient": "linear-gradient(135deg,#fa709a,#fee140)","cover_icon": "fas fa-newspaper"},
    {"title": "Artificial Intelligence: A Modern Approach","author": "Stuart Russell & Peter Norvig","category": "reference","status": "available","shelf": "B-08","cover_gradient": "linear-gradient(135deg,#30cfd0,#330867)","cover_icon": "fas fa-robot"},
    {"title": "Computer Organization and Design",   "author": "David A. Patterson",         "category": "textbook",  "status": "available","shelf": "A-55","cover_gradient": "linear-gradient(135deg,#a18cd1,#fbc2eb)","cover_icon": "fas fa-microchip"},
    {"title": "Database System Concepts",            "author": "Silberschatz, Korth",        "category": "textbook",  "status": "issued",   "shelf": "A-61","cover_gradient": "linear-gradient(135deg,#fccb90,#d57eeb)","cover_icon": "fas fa-database"},
]

# ─── Placement Page ───────────────────────────────────────────────────────────

PLACEMENT_SUMMARY = [
    {"icon": "💰", "value": "8.22", "label": "Highest Package (LPA)", "decimal": True,  "company": "Emirates Prefabrication Industries"},
    {"icon": "📊", "value": 87,     "label": "Overall Placement % (Batch 9)", "decimal": False, "company": None},
    {"icon": "🎓", "value": 30,     "label": "CSE Students Placed (Batch 9)", "decimal": False, "company": None},
    {"icon": "🏢", "value": 41,     "label": "Companies (Batch 10)",           "decimal": False, "company": None},
]

PLACEMENT_BATCHES = [
    {
        "key": "batch9",
        "label": "Batch 9 (2020–2024)",
        "stats": [
            {"value": "57",   "label": "CSE Total Students"},
            {"value": "30",   "label": "CSE Students Placed"},
            {"value": "₹8.22L","label": "Highest Package (LPA)"},
            {"value": "87%",  "label": "Overall Placement"},
            {"value": "30",   "label": "Companies Visited"},
        ],
        "companies": [
            {"name": "Emirates Prefabrication Industries", "students": 1,  "ctc": 8.22},
            {"name": "CODEYOUNG",                          "students": 1,  "ctc": 7.36},
            {"name": "Capital Survey LLC",                 "students": 1,  "ctc": 6.00},
            {"name": "ACCENTURE",                          "students": 2,  "ctc": 4.53},
            {"name": "TERAWE TECHNOLOGIES",                "students": 3,  "ctc": 4.50},
            {"name": "UST GLOBAL",                         "students": 3,  "ctc": 4.25},
            {"name": "OCS Services (India) Pvt. Ltd",      "students": 1,  "ctc": 4.10},
            {"name": "TECHMAGHI",                          "students": 6,  "ctc": 4.00},
            {"name": "TECHNOLOGICS GLOBAL",                "students": 4,  "ctc": 4.00},
            {"name": "TCS",                                "students": 4,  "ctc": 3.36},
            {"name": "SUTHERLAND",                         "students": 87, "ctc": 3.00},
            {"name": "CRI Pumps",                          "students": 12, "ctc": 2.64},
            {"name": "SFO Technologies",                   "students": 13, "ctc": 2.40},
            {"name": "TEMSTECH SOLUTIONS",                 "students": 3,  "ctc": 2.40},
            {"name": "XOGO",                               "students": 1,  "ctc": 2.40},
        ],
    },
    {
        "key": "batch10",
        "label": "Batch 10 (2021–2025)",
        "stats": [
            {"value": "61",   "label": "CSE Total Students"},
            {"value": "31",   "label": "CSE Students Placed"},
            {"value": "₹6.50L","label": "Highest Package (LPA)"},
            {"value": "76%",  "label": "Overall Placement"},
            {"value": "41",   "label": "Companies Visited"},
        ],
        "companies": [
            {"name": "Intrainz Innovation",                            "students": 14, "ctc": 6.50},
            {"name": "Plastic Omnium Auto Exteriors India Ltd",        "students": 1,  "ctc": 6.45},
            {"name": "K12 Technoservices",                             "students": 5,  "ctc": 6.00},
            {"name": "UST Global",                                     "students": 1,  "ctc": 4.25},
            {"name": "Terawe",                                         "students": 3,  "ctc": 4.20},
            {"name": "Amazon Development Center",                      "students": 1,  "ctc": 4.00},
            {"name": "INFOSYS",                                        "students": 4,  "ctc": 3.60},
            {"name": "10xDS Exponential Digital Services",             "students": 2,  "ctc": 3.50},
            {"name": "Evision Technoservice",                          "students": 6,  "ctc": 3.50},
            {"name": "Sutherland",                                     "students": 68, "ctc": 2.65},
            {"name": "Onflap Technologies",                            "students": 3,  "ctc": 2.50},
            {"name": "Montra Electric",                                "students": 9,  "ctc": 2.04},
            {"name": "Sundaram Fasteners - TVS",                       "students": 2,  "ctc": 2.05},
            {"name": "AARBEE Structures",                              "students": 2,  "ctc": 2.40},
            {"name": "PKJ Technologies Pvt Ltd",                       "students": 3,  "ctc": 3.00},
        ],
    },
]

# ─── New Placement Dashboard Data ───────────────────────────────────────────

PLACEMENT_COMPANY_LOGOS = [
    {"name": "Google",      "url": "https://via.placeholder.com/150x80/FFFFFF/DB4437?text=Google",    "sector": "IT"},
    {"name": "Microsoft",   "url": "https://via.placeholder.com/150x80/FFFFFF/00A4EF?text=Microsoft", "sector": "IT"},
    {"name": "Amazon",      "url": "https://via.placeholder.com/150x80/FFFFFF/FF9900?text=Amazon",    "sector": "IT"},
    {"name": "TCS",         "url": "https://via.placeholder.com/150x80/FFFFFF/4B2C84?text=TCS",       "sector": "IT"},
    {"name": "Infosys",     "url": "https://via.placeholder.com/150x80/FFFFFF/007CC3?text=Infosys",   "sector": "IT"},
    {"name": "Accenture",   "url": "https://via.placeholder.com/150x80/FFFFFF/A100FF?text=Accenture", "sector": "IT"},
    {"name": "L&T",         "url": "https://via.placeholder.com/150x80/FFFFFF/000000?text=L%26T",     "sector": "Core"},
    {"name": "TVS",         "url": "https://via.placeholder.com/150x80/FFFFFF/EE1B24?text=TVS",       "sector": "Core"},
    {"name": "HDFC Bank",   "url": "https://via.placeholder.com/150x80/FFFFFF/004C8F?text=HDFC",      "sector": "Finance"},
    {"name": "Goldman Sachs","url": "https://via.placeholder.com/150x80/FFFFFF/7399C6?text=GS",       "sector": "Finance"},
]

ALUMNI_SUCCESS = [
    {
        "name": "Arjun S",
        "batch": "2020-2024",
        "company": "Emirates Prefabrication",
        "package": "₹8.22 LPA",
        "photo": "https://via.placeholder.com/120x120/8F7A6E/FFFFFF?text=Arjun",
        "testimonial": "AISAT CSE provided me with the solid foundation needed to excel in a global engineering environment. The faculty's guidance was invaluable."
    },
    {
        "name": "Meera Nair",
        "batch": "2019-2023",
        "company": "Amazon",
        "package": "₹12.0 LPA",
        "photo": "https://via.placeholder.com/120x120/8F7A6E/FFFFFF?text=Meera",
        "testimonial": "The hands-on coding labs and hackathons at AISAT helped me sharpen my problem-solving skills, which were key to cracking the Amazon interview."
    },
    {
        "name": "Kevin Paul",
        "batch": "2021-2025",
        "company": "Intrainz",
        "package": "₹6.5 LPA",
        "photo": "https://via.placeholder.com/120x120/8F7A6E/FFFFFF?text=Kevin",
        "testimonial": "Being part of the Batch 10 placement drive was an amazing experience. The placement cell really works hard to bring in diverse opportunities."
    }
]

INTERNSHIPS = [
    {
        "title": "Software Development Intern",
        "company": "UST Global",
        "domain": "IT",
        "location": "Trivandrum/Hybrid",
        "description": "Work on enterprise-level Java/Spring Boot applications. Knowledge of REST APIs and Git is preferred.",
        "link": "#"
    },
    {
        "title": "Embedded Systems Intern",
        "company": "SFO Technologies",
        "domain": "Core",
        "location": "Kochi",
        "description": "Help develop firmware for IoT devices. Experience with C/C++ and microcontrollers required.",
        "link": "#"
    },
    {
        "title": "Data Analytics Intern",
        "company": "10xDS",
        "domain": "IT",
        "location": "Kochi",
        "description": "Assist in building data visualization dashboards using Power BI and Python.",
        "link": "#"
    }
]

PLACEMENT_TEAM = {
    "faculty_coordinator": {
        "name": "Ms. Divya Mohan",
        "designation": "Placement Coordinator & Asso. Professor",
        "email": "divya@aisat.ac.in",
        "photo": "https://aisat.ac.in/wp-content/uploads/2024/01/Ms.-Divya-Mohan-e1706040948144.jpg"
    },
    "student_coordinators": [
        {"name": "Abhijith R", "email": "abhijith.cse24@aisat.ac.in"},
        {"name": "Sara Thomas", "email": "sara.cse24@aisat.ac.in"}
    ]
}
