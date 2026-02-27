// ===================================
// CS CONNECT - FLOATING CHATBOT
// Shared across all pages
// ===================================

let floatingChatOpen = false;
let floatingMessageCount = 0;

// Knowledge Base
const floatingKB = {
  admissions: {
    keywords: ["admission", "admissions", "join", "enroll", "apply"],
    response:
      "📚 Admissions are open for 2026!\n\nB.Tech: 120 seats\nM.Tech: 18 seats\n\nVisit our Admissions page for details!",
    quickReplies: ["Eligibility", "Fee Structure", "Apply Now"],
  },
  syllabus: {
    keywords: ["syllabus", "curriculum", "course", "subjects"],
    response:
      "📖 Our curriculum follows KTU 2019 scheme with industry-aligned courses.\n\nView semester-wise syllabus on our Academics page!",
    quickReplies: ["View Syllabus", "Download Notes"],
  },
  faculty: {
    keywords: ["faculty", "teachers", "professors", "hod"],
    response:
      "👨‍🏫 32+ experienced faculty members led by Dr. Jeswin Roy Decouth (HOD).\n\nVisit Faculty page to know more!",
    quickReplies: ["View Faculty", "Contact Faculty"],
  },
  library: {
    keywords: ["library", "books", "borrow", "qr"],
    response:
      "📚 1000+ books with QR code-based system!\n\nFeatures:\n• Online book issue\n• Digital resources\n• Study materials",
    quickReplies: ["Browse Library", "QR Scanner"],
  },
  placement: {
    keywords: ["placement", "job", "career", "package"],
    response:
      "💼 98% Placement Rate!\n\nHighest: ₹45 LPA\nAverage: ₹6.5 LPA\n\nTop companies: TCS, Infosys, Wipro",
    quickReplies: ["View Companies", "Statistics"],
  },
  contact: {
    keywords: ["contact", "phone", "email", "address"],
    response:
      "📞 Contact Us:\n\n📧 cse@aisat.ac.in\n📱 +91 98765 43210\n\n📍 Kalamassery, Kochi, Kerala",
    quickReplies: ["Get Directions", "Email Us"],
  },
};

function toggleFloatingChat() {
  const chatWindow = document.getElementById("floatingChatWindow");
  const chatFloat = document.getElementById("chatbotFloat");

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

function sendFloatingMessage() {
  const input = document.getElementById("floatingInput");
  const message = input.value.trim();

  if (message) {
    document.getElementById("floatingWelcome").style.display = "none";
    addFloatingMessage(message, "user");
    input.value = "";
    showFloatingTyping();

    setTimeout(() => {
      const response = getFloatingResponse(message);
      hideFloatingTyping();
      addFloatingMessage(response.text, "bot", response.quickReplies);
    }, 1000);
  }
}

function addFloatingMessage(text, type, quickReplies = null) {
  const messagesDiv = document.getElementById("floatingChatMessages");
  const messageDiv = document.createElement("div");
  messageDiv.className = `floating-message ${type}`;

  const time = new Date().toLocaleTimeString("en-US", {
    hour: "2-digit",
    minute: "2-digit",
  });

  let quickRepliesHTML = "";
  if (quickReplies) {
    quickRepliesHTML = `
      <div class="floating-quick-replies">
        ${quickReplies
          .map(
            (reply) =>
              `<button class="floating-quick-reply" onclick="sendFloatingQuick('${reply}')">${reply}</button>`
          )
          .join("")}
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

function getFloatingResponse(message) {
  const messageLower = message.toLowerCase();

  for (const [key, data] of Object.entries(floatingKB)) {
    if (data.keywords && data.keywords.some((keyword) => messageLower.includes(keyword))) {
      return { text: data.response, quickReplies: data.quickReplies };
    }
  }

  return {
    text: "I can help with:\n• Admissions\n• Syllabus\n• Faculty\n• Library\n• Placements\n\nWhat would you like to know?",
    quickReplies: ["Admissions", "Faculty", "Library"],
  };
}

function sendFloatingQuick(message) {
  document.getElementById("floatingInput").value = message;
  sendFloatingMessage();
}

function showFloatingTyping() {
  document.getElementById("floatingTyping").classList.add("active");
  scrollFloatingToBottom();
}

function hideFloatingTyping() {
  document.getElementById("floatingTyping").classList.remove("active");
}

function scrollFloatingToBottom() {
  const messagesDiv = document.getElementById("floatingChatMessages");
  messagesDiv.scrollTop = messagesDiv.scrollHeight;
}

function handleFloatingEnter(event) {
  if (event.key === "Enter") {
    event.preventDefault();
    sendFloatingMessage();
  }
}

function clearFloatingChat() {
  if (confirm("Clear chat history?")) {
    document.getElementById("floatingChatMessages").innerHTML = `
      <div class="floating-welcome" id="floatingWelcome">
        <div class="floating-welcome-icon">👋</div>
        <h4>Chat Cleared!</h4>
        <p>How can I help you?</p>
      </div>
      <div class="floating-typing" id="floatingTyping">
        <div class="floating-message-avatar" style="background: var(--primary-red, #a41f13); color: white;">🤖</div>
        <div class="floating-typing-dots">
          <div class="floating-typing-dot"></div>
          <div class="floating-typing-dot"></div>
          <div class="floating-typing-dot"></div>
        </div>
      </div>`;
    floatingMessageCount = 0;
  }
}

function openFullChatbot() {
  window.location.href = "/chatbot";
}

function showNotification() {
  document.getElementById("chatNotification").style.display = "flex";
}

function hideNotification() {
  document.getElementById("chatNotification").style.display = "none";
}

// Auto-show notification after 5 seconds if chat hasn't been opened
setTimeout(() => {
  if (!floatingChatOpen && floatingMessageCount === 0) {
    showNotification();
  }
}, 5000);
