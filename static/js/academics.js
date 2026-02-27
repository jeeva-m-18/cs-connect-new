// Accordion Toggle Function
function toggleAccordion(header) {
  const content = header.nextElementSibling;
  const icon = header.querySelector(".accordion-icon");

  // Close all other accordions
  document.querySelectorAll(".accordion-content").forEach((item) => {
    if (item !== content) {
      item.classList.remove("active");
      item.previousElementSibling.classList.remove("active");
    }
  });

  // Toggle current accordion
  content.classList.toggle("active");
  header.classList.toggle("active");
}

// Smooth scroll to syllabus section
document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
  anchor.addEventListener("click", function (e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute("href"));
    if (target) {
      target.scrollIntoView({
        behavior: "smooth",
        block: "start",
      });
    }
  });
});
