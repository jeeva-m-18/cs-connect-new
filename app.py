from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

# Import mock data (replace with DB queries later)
from data import (
    NEWS_TICKER,
    HOME_STATS, HOME_FEATURE_CARDS, HOME_EVENTS,
    FACULTY_DATA, STAFF_DATA,
    DEPT_STATS_OVERVIEW, DEPT_STATS_GLANCE, PEOS, PSOS, MILESTONES,
    ACCREDITATIONS, INFRASTRUCTURE,
    PROGRAMS, SEMESTERS,
    BOOKS_DATA,
    PLACEMENT_SUMMARY, PLACEMENT_BATCHES,
    PLACEMENT_COMPANY_LOGOS, ALUMNI_SUCCESS, INTERNSHIPS, PLACEMENT_TEAM,
)

app = Flask(__name__)
app.secret_key = "csconnectsecret"

DATABASE = "csconnect.db"

# ─────────────────────────────────────────────────
# CONTEXT PROCESSOR — injects globals into every template
# ─────────────────────────────────────────────────
@app.context_processor
def inject_globals():
    return {
        "ticker_text": NEWS_TICKER,
        "active_page": "",   # overridden per route
    }


# ─────────────────────────────────────────────────
# DATABASE SETUP
# ─────────────────────────────────────────────────
def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            user_id TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            role TEXT DEFAULT 'student'
        )
    """)
    conn.commit()
    conn.close()


# ─────────────────────────────────────────────────
# PAGE ROUTES
# ─────────────────────────────────────────────────

@app.route('/')
def home():
    return render_template(
        'indexn.html',
        active_page='home',
        stats=HOME_STATS,
        feature_cards=HOME_FEATURE_CARDS,
        events=HOME_EVENTS,
    )


@app.route('/faculty')
def faculty():
    return render_template(
        'faculty/faculty.html',
        active_page='faculty',
        faculty=FACULTY_DATA,
        staff_members=STAFF_DATA,
    )


@app.route('/about-cse')
def about_cse():
    return render_template(
        'about/about-cse.html',
        active_page='about_cse',
        dept_stats=DEPT_STATS_OVERVIEW,
        dept_glance=DEPT_STATS_GLANCE,
        peos=PEOS,
        psos=PSOS,
        milestones=MILESTONES,
    )


@app.route('/about-aisat')
def about_aisat():
    return render_template(
        'about/about-aisat.html',
        active_page='about_aisat',
        accreditations=ACCREDITATIONS,
        infrastructure=INFRASTRUCTURE,
    )


@app.route('/academics')
def academics():
    return render_template(
        'academics/academics.html',
        active_page='academics',
        programs=PROGRAMS,
        semesters=SEMESTERS,
    )


@app.route('/library')
def library():
    return render_template(
        'library/library.html',
        active_page='library',
        books=BOOKS_DATA,
    )


@app.route('/placements')
def placements():
    return render_template(
        'placement.html',
        active_page='placements',
        placement_summary=PLACEMENT_SUMMARY,
        batches=PLACEMENT_BATCHES,
        companies=PLACEMENT_COMPANY_LOGOS,
        alumni=ALUMNI_SUCCESS,
        internships=INTERNSHIPS,
        team=PLACEMENT_TEAM,
    )


# ─────────────────────────────────────────────────
# API ENDPOINTS — JSON for AJAX / JS dynamic loading
# ─────────────────────────────────────────────────

@app.route('/api/faculty')
def api_faculty():
    """Return all faculty as JSON. Supports ?search=name query."""
    search = request.args.get('search', '').lower()
    designation = request.args.get('designation', 'all')

    results = FACULTY_DATA
    if search:
        results = [f for f in results if search in f['name'].lower()]
    if designation and designation != 'all':
        results = [f for f in results if f['designation_key'] == designation]

    return jsonify(results)


@app.route('/api/books')
def api_books():
    """Return books as JSON. Supports ?search= and ?category= query params."""
    search = request.args.get('search', '').lower()
    category = request.args.get('category', 'all')
    status = request.args.get('status', 'all')

    results = BOOKS_DATA
    if search:
        results = [b for b in results
                   if search in b['title'].lower() or search in b['author'].lower()]
    if category and category != 'all':
        results = [b for b in results if b['category'] == category]
    if status and status != 'all':
        results = [b for b in results if b['status'] == status]

    return jsonify(results)


@app.route('/api/placements')
def api_placements():
    """Return placement data as JSON."""
    return jsonify({
        "summary": PLACEMENT_SUMMARY,
        "batches": PLACEMENT_BATCHES,
    })


@app.route('/api/stats')
def api_stats():
    """Return homepage stats as JSON."""
    return jsonify(HOME_STATS)


# ─────────────────────────────────────────────────
# AUTH ROUTES
# ─────────────────────────────────────────────────

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = generate_password_hash(request.form["password"])
        user_id = request.form["user_id"]
        role = request.form.get("role", "student")

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO users (name, email, user_id, password, role) VALUES (?, ?, ?, ?, ?)",
                (name, email, user_id, password, role)
            )
            conn.commit()
            flash("Account Created Successfully!", "success")
        except sqlite3.IntegrityError:
            flash("Email or User ID already exists!", "danger")
        finally:
            conn.close()

        return redirect(url_for("login"))

    return render_template("register.html", active_page='')


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        user = cursor.fetchone()
        conn.close()

        if user and check_password_hash(user[4], password):
            session["user_id"] = user[0]
            session["name"] = user[1]
            flash("Login successful!", "success")
            return redirect(url_for("home"))
        else:
            flash("Invalid email or password!", "danger")

    return render_template("login.html", active_page='')


@app.route('/logout')
def logout():
    session.clear()
    flash("Logged out successfully!", "success")
    return redirect(url_for("login"))


# ─────────────────────────────────────────────────
# RUN
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    init_db()
    app.run(debug=True)