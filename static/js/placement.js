// Animated Counter Function
function animateCounters() {
  const counters = document.querySelectorAll(".stat-number");
  const speed = 200;

  counters.forEach((counter) => {
    const target = +counter.getAttribute("data-target");
    const isDecimal = counter.getAttribute("data-decimal") === "true";

    const updateCount = () => {
      const count = +counter.innerText;
      const inc = target / speed;

      if (count < target) {
        let nextVal = count + inc;
        if (nextVal > target) nextVal = target;
        counter.innerText = isDecimal ? nextVal.toFixed(2) : Math.ceil(nextVal);
        setTimeout(updateCount, 1);
      } else {
        counter.innerText = isDecimal ? target.toFixed(2) : target;
      }
    };
    updateCount();
  });
}

// Scroll Reveal Implementation
function scrollReveal() {
  const reveals = document.querySelectorAll(".reveal");
  for (let i = 0; i < reveals.length; i++) {
    const windowHeight = window.innerHeight;
    const elementTop = reveals[i].getBoundingClientRect().top;
    const elementVisible = 150;
    if (elementTop < windowHeight - elementVisible) {
      reveals[i].classList.add("active");
    }
  }
}

// Chart.js Initialization
function initCharts() {
  const chartConfigs = {
    'batch9': {
      labels: ['IT/Software', 'Core Engineering', 'Finance', 'Others'],
      data: [65, 20, 10, 5],
      colors: ['#a41f13', '#292f36', '#8f7a6e', '#e0dbd8']
    },
    'batch10': {
      labels: ['IT/Software', 'Core Engineering', 'Sales', 'Others'],
      data: [70, 15, 10, 5],
      colors: ['#a41f13', '#292f36', '#8f7a6e', '#e0dbd8']
    }
  };

  Object.keys(chartConfigs).forEach(batchKey => {
    const ctx = document.getElementById(`chart-${batchKey}`);
    if (ctx) {
      new Chart(ctx, {
        type: 'doughnut',
        data: {
          labels: chartConfigs[batchKey].labels,
          datasets: [{
            data: chartConfigs[batchKey].data,
            backgroundColor: chartConfigs[batchKey].colors,
            borderWidth: 0
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: { position: 'bottom' },
            title: { display: true, text: 'Industry Sector Distribution' }
          }
        }
      });
    }
  });
}

// Year Tab Logic
function initTabs() {
  const tabs = document.querySelectorAll(".year-tab");
  const contents = document.querySelectorAll(".year-content");

  tabs.forEach(tab => {
    tab.addEventListener("click", () => {
      tabs.forEach(t => t.classList.remove("active"));
      contents.forEach(c => c.classList.remove("active"));

      tab.classList.add("active");
      const target = tab.getAttribute("data-year");
      document.getElementById(`year-${target}`).classList.add("active");
    });
  });
}

// Alumni Slider Logic
let currentSlide = 0;
function initSlider() {
  const track = document.querySelector(".alumni-track");
  const cards = document.querySelectorAll(".alumni-card");
  const nextBtn = document.querySelector(".slider-btn.next");
  const prevBtn = document.querySelector(".slider-btn.prev");

  if (!track || cards.length === 0) return;

  const updateSlider = () => {
    const cardWidth = cards[0].offsetWidth + 32; // width + gap
    track.style.transform = `translateX(-${currentSlide * cardWidth}px)`;
  };

  nextBtn?.addEventListener("click", () => {
    const visibleCards = window.innerWidth > 968 ? 3 : (window.innerWidth > 600 ? 2 : 1);
    if (currentSlide < cards.length - visibleCards) {
      currentSlide++;
      updateSlider();
    }
  });

  prevBtn?.addEventListener("click", () => {
    if (currentSlide > 0) {
      currentSlide--;
      updateSlider();
    }
  });

  window.addEventListener("resize", updateSlider);
}

// Marquee Filter logic
function initMarqueeFilter() {
  const buttons = document.querySelectorAll(".cat-btn");
  const logos = document.querySelectorAll(".company-logo");

  buttons.forEach(btn => {
    btn.addEventListener("click", () => {
      buttons.forEach(b => b.classList.remove("active"));
      btn.classList.add("active");

      const sector = btn.getAttribute("data-sector");
      logos.forEach(logo => {
        if (sector === "all" || logo.getAttribute("data-sector") === sector) {
          logo.style.display = "flex";
          logo.style.opacity = "1";
        } else {
          logo.style.opacity = "0.2"; // Dim instead of hiding to prevent marquee jumps
        }
      });
    });
  });
}

// Flash Notice Utility
window.flashNotice = function (msg) {
  alert(msg); // Placeholder for a prettier toast
};

// Global Chatbot Toggle (handled by base.html / chatbot.js)
// But we can trigger it here too if needed.

// Initialize Everything
document.addEventListener("DOMContentLoaded", () => {
  window.addEventListener("scroll", scrollReveal);
  scrollReveal();
  animateCounters();
  initCharts();
  initTabs();
  initSlider();
  initMarqueeFilter();
});
