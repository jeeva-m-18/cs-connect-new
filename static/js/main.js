// 1. CHATBOT TOGGLE LOGIC
function toggleChat() {
    const chat = document.getElementById("chatWindow");
    if (chat) {
        if (chat.style.display === "flex") {
            chat.style.display = "none";
        } else {
            chat.style.display = "flex";
        }
    }
}

// 2. STATS COUNTER LOGIC
const animateCounters = () => {
    const counters = document.querySelectorAll('.stat-number');
    counters.forEach(counter => {
        const target = +counter.getAttribute('data-target');
        const count = +counter.innerText;
        const increment = target / 100;

        if (count < target) {
            counter.innerText = Math.ceil(count + increment);
            setTimeout(animateCounters, 20);
        } else {
            counter.innerText = target;
        }
    });
};

// Start animation when stats are visible
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            animateCounters();
            observer.disconnect(); // Run once
        }
    });
}, { threshold: 0.5 });

document.addEventListener("DOMContentLoaded", () => {
    const statsSection = document.querySelector('.stats-strip');
    if (statsSection) observer.observe(statsSection);
});