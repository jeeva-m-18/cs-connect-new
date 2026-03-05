// =============================================================================
// library.js — CS Connect Library Page
// Handles search, filter, and premium interactions
// =============================================================================

document.addEventListener("DOMContentLoaded", () => {
    // ── Live Search ──────────────────────────────────────────────────────
    const searchInput = document.getElementById("searchInput");
    if (searchInput) {
        searchInput.addEventListener("input", searchBooks);
    }

    // ── Scroll Reveal ────────────────────────────────────────────────────
    const revealElements = document.querySelectorAll(".reveal");
    const revealOnScroll = () => {
        revealElements.forEach(el => {
            const rect = el.getBoundingClientRect();
            if (rect.top < window.innerHeight * 0.9) {
                el.classList.add("active");
            }
        });
    };
    window.addEventListener("scroll", revealOnScroll);
    revealOnScroll(); // Initial check
});

// ── Search Books ───────────────────────────────────────────────────────────
function searchBooks() {
    const searchTerm = document.getElementById("searchInput").value.toLowerCase();
    const books = document.querySelectorAll(".book-card");
    let visibleCount = 0;

    books.forEach(book => {
        const title = (book.getAttribute("data-title") || "").toLowerCase();
        const author = (book.getAttribute("data-author") || "").toLowerCase();
        const show = title.includes(searchTerm) || author.includes(searchTerm);
        book.style.display = show ? "block" : "none";
        if (show) visibleCount++;
    });

    const noResults = document.getElementById("noResults");
    if (noResults) noResults.style.display = visibleCount === 0 ? "block" : "none";
}

// ── Filter Books ───────────────────────────────────────────────────────────
function filterBooks(filter) {
    const books = document.querySelectorAll(".book-card");
    const chips = document.querySelectorAll(".filter-chip");
    let visibleCount = 0;

    chips.forEach(chip => chip.classList.remove("active"));
    if (event && event.target) event.target.classList.add("active");

    books.forEach(book => {
        const category = book.getAttribute("data-category");
        const status = book.getAttribute("data-status");
        const show = filter === "all" || category === filter || status === filter;
        book.style.display = show ? "block" : "none";
        if (show) visibleCount++;
    });

    const noResults = document.getElementById("noResults");
    if (noResults) noResults.style.display = visibleCount === 0 ? "block" : "none";
}

// ── Library Notices ────────────────────────────────────────────────────────
function flashNotice(message) {
    const notice = document.createElement('div');
    notice.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background: var(--dark-charcoal);
        color: white;
        padding: 1rem 2rem;
        border-radius: 12px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        z-index: 9999;
        font-weight: 600;
        animation: slideIn 0.3s ease-out;
    `;
    notice.innerHTML = `<i class="fas fa-info-circle" style="color: var(--primary-red); margin-right: 10px;"></i> ${message}`;
    document.body.appendChild(notice);

    setTimeout(() => {
        notice.style.opacity = '0';
        notice.style.transform = 'translateY(-20px)';
        notice.style.transition = '0.3s all ease';
        setTimeout(() => notice.remove(), 300);
    }, 3000);
}

// Add animation keyframes for notice
const style = document.createElement('style');
style.textContent = `
    @keyframes slideIn {
        from { transform: translateX(100%); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
`;
document.head.appendChild(style);
