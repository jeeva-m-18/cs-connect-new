// ===================================
// CS CONNECT - SHARED UTILITIES
// Used on all pages
// ===================================

// 1. SCROLL REVEAL ANIMATION
function reveal() {
  const reveals = document.querySelectorAll(".reveal");
  reveals.forEach((el) => {
    const top = el.getBoundingClientRect().top;
    if (top < window.innerHeight - 150) {
      el.classList.add("active");
    }
  });
}

window.addEventListener("scroll", reveal);
reveal(); // Trigger once on page load

// 2. STATS COUNTER (home page)
document.addEventListener("DOMContentLoaded", () => {
  const statsSection = document.querySelector(".stats-strip");
  if (!statsSection) return;

  const animateCounters = () => {
    document.querySelectorAll(".stat-number").forEach((counter) => {
      const updateCount = () => {
        const target = +counter.getAttribute("data-target");
        const count = +counter.innerText;
        const inc = target / 200;
        if (count < target) {
          counter.innerText = Math.ceil(count + inc);
          setTimeout(updateCount, 20);
        } else {
          counter.innerText = target;
        }
      };
      updateCount();
    });
  };

  const observer = new IntersectionObserver((entries) => {
    if (entries[0].isIntersecting) {
      animateCounters();
      observer.disconnect();
    }
  }, { threshold: 0.5 });

  observer.observe(statsSection);
});
