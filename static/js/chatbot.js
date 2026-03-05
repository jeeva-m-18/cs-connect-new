// =============================================================================
// chatbot.js — CS Connect Floating Chatbot
// Loaded on every page via base.html
// =============================================================================

// ── State ──────────────────────────────────────────────────────────────────
let floatingChatOpen = false;
let floatingMessageCount = 0;

// ── Knowledge Base ────────────────────────────────────────────────────────
const floatingKB = {
    admissions: {
        keywords: ["admission", "admissions", "join", "enroll", "apply"],
        response: "📚 Admissions are open for 2026!\n\nB.Tech: 120 seats\nM.Tech: 18 seats\n\nVisit our Academics page for details!",
        quickReplies: ["Eligibility", "Fee Structure", "Apply Now"],
    },
    syllabus: {
        keywords: ["syllabus", "curriculum", "course", "subjects"],
        response: "📖 Our curriculum follows KTU 2019 scheme with industry-aligned courses.\n\nView semester-wise syllabus on our Academics page!",
        quickReplies: ["View Syllabus", "Download Notes"],
    },
    faculty: {
        keywords: ["faculty", "teachers", "professors", "hod"],
        response: "👨‍🏫 17 experienced faculty members led by Dr. Jeswin Roy Dcouth (HOD).\n\nVisit Faculty page to know more!",
        quickReplies: ["View Faculty", "Contact Faculty"],
    },
    library: {
        keywords: ["library", "books", "borrow", "qr"],
        response: "📚 1000+ books with QR code-based system!\n\nFeatures:\n• Online book issue\n• Digital resources\n• Study materials",
        quickReplies: ["Browse Library", "QR Scanner"],
    },
    placement: {
        keywords: ["placement", "job", "career", "package"],
        response: "💼 87% Placement Rate (Batch 9)!\n\nHighest: ₹8.22 LPA\nTop companies: TCS, Infosys, Accenture, UST Global",
        quickReplies: ["View Companies", "Statistics"],
    },
    contact: {
        keywords: ["contact", "phone", "email", "address"],
        response: "📞 Contact Us:\n\n📧 cse@aisat.ac.in\n📱 0484-2532120\n\n📍 Kalamassery, Kochi, Kerala",
        quickReplies: ["Get Directions", "Email Us"],
    },
    about: {
        keywords: ["about", "aisat", "college", "history", "established"],
        response: "🏛️ AISAT was established in 2002 by Bethany Educational Society.\nKalamassery, Kochi, Kerala.\n\nAffiliates: KTU | Approved: AICTE | Accredited: NAAC A Grade",
        quickReplies: ["About CSE", "About AISAT"],
    },
};

// ── Toggle Chat Window ─────────────────────────────────────────────────────
function toggleFloatingChat() {
    const chatWindow = document.getElementById("floatingChatWindow");
    const chatFloat = document.getElementById("chatbotFloat");
    if (!chatWindow) return;

    floatingChatOpen = !floatingChatOpen;

    if (floatingChatOpen) {
        chatWindow.classList.add("active");
        chatFloat.classList.add("chat-open");
        chatFloat.innerHTML = "✕";
        hideNotification();
        scrollFloatingToBottom();
    } else {
        chatWindow.classList.remove("active");
        chatFloat.classList.remove("chat-open");
        chatFloat.innerHTML = "💬";
    }
}

// ── Send Message ───────────────────────────────────────────────────────────
function sendFloatingMessage() {
    const input = document.getElementById("floatingInput");
    const message = input.value.trim();
    if (!message) return;

    document.getElementById("floatingWelcome").style.display = "none";
    addFloatingMessage(message, "user");
    input.value = "";
    showFloatingTyping();

    setTimeout(() => {
        const response = getFloatingResponse(message);
        hideFloatingTyping();
        addFloatingMessage(response.text, "bot", response.quickReplies);
    }, 900);
}

// ── Add Message to DOM ─────────────────────────────────────────────────────
function addFloatingMessage(text, type, quickReplies = null) {
    const messagesDiv = document.getElementById("floatingChatMessages");
    const messageDiv = document.createElement("div");
    messageDiv.className = `floating-message ${type}`;

    const time = new Date().toLocaleTimeString("en-US", { hour: "2-digit", minute: "2-digit" });

    let quickRepliesHTML = "";
    if (quickReplies) {
        quickRepliesHTML = `<div class="floating-quick-replies">
            ${quickReplies.map(r => `<button class="floating-quick-reply" onclick="sendFloatingQuick('${r}')">${r}</button>`).join("")}
        </div>`;
    }

    messageDiv.innerHTML = `
        <div class="floating-message-avatar">${type === "bot" ? "🤖" : "👤"}</div>
        <div>
            <div class="floating-message-bubble">${text.replace(/\n/g, "<br>")}</div>
            <div class="floating-message-time">${time}</div>
            ${quickRepliesHTML}
        </div>`;

    messagesDiv.appendChild(messageDiv);
    scrollFloatingToBottom();
    floatingMessageCount++;
}

// ── Get Response from KB ───────────────────────────────────────────────────
function getFloatingResponse(message) {
    const lower = message.toLowerCase();
    for (const [, data] of Object.entries(floatingKB)) {
        if (data.keywords && data.keywords.some(kw => lower.includes(kw))) {
            return { text: data.response, quickReplies: data.quickReplies };
        }
    }
    return {
        text: "I can help with:\n• Admissions\n• Syllabus\n• Faculty\n• Library\n• Placements\n• Contact\n\nWhat would you like to know?",
        quickReplies: ["Admissions", "Faculty", "Library"],
    };
}

// ── Quick Reply ────────────────────────────────────────────────────────────
function sendFloatingQuick(message) {
    document.getElementById("floatingInput").value = message;
    sendFloatingMessage();
}

// ── Typing Indicator ───────────────────────────────────────────────────────
function showFloatingTyping() {
    const el = document.getElementById("floatingTyping");
    if (el) { el.classList.add("active"); scrollFloatingToBottom(); }
}

function hideFloatingTyping() {
    const el = document.getElementById("floatingTyping");
    if (el) el.classList.remove("active");
}

// ── Scroll & Notifications ────────────────────────────────────────────────
function scrollFloatingToBottom() {
    const el = document.getElementById("floatingChatMessages");
    if (el) el.scrollTop = el.scrollHeight;
}

function handleFloatingEnter(event) {
    if (event.key === "Enter") { event.preventDefault(); sendFloatingMessage(); }
}

function clearFloatingChat() {
    if (!confirm("Clear chat history?")) return;
    const el = document.getElementById("floatingChatMessages");
    el.innerHTML = `
        <div class="floating-welcome" id="floatingWelcome">
            <div class="floating-welcome-icon">👋</div>
            <h4>Chat Cleared!</h4>
            <p>How can I help you?</p>
        </div>
        <div class="floating-typing" id="floatingTyping">
            <div class="floating-message-avatar" style="background:var(--primary-red);color:white">🤖</div>
            <div class="floating-typing-dots">
                <div class="floating-typing-dot"></div>
                <div class="floating-typing-dot"></div>
                <div class="floating-typing-dot"></div>
            </div>
        </div>`;
    floatingMessageCount = 0;
}

function showNotification() {
    const el = document.getElementById("chatNotification");
    if (el) el.style.display = "flex";
}

function hideNotification() {
    const el = document.getElementById("chatNotification");
    if (el) el.style.display = "none";
}

// Show notification badge after 5 seconds if chat not opened
setTimeout(() => {
    if (!floatingChatOpen && floatingMessageCount === 0) showNotification();
}, 5000);
