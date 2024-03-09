const nav = document.querySelector(".nav");
const searchIcon = document.querySelector("#searchIcon");

if (searchIcon) { // Перевіряємо, чи існує searchIcon перед додаванням події
  searchIcon.addEventListener("click", () => {
    nav.classList.toggle("openSearch");
    if (nav.classList.contains("openSearch")) {
      searchIcon.classList.replace("uil-search", "uil-times");
    } else {
      searchIcon.classList.replace("uil-times", "uil-search");
    }
  });
}

const initSlider = () => {
  const imageList = document.querySelector(".slider-wrapper .image-list");
  const slideButtons = document.querySelectorAll(".slider-wrapper .slider-button");
  const scrollbarThumb = document.querySelector(".slider-scrollbar .scrollbar-thumb");
  let maxScrollLeft;

  const updateMaxScrollLeft = () => {
    maxScrollLeft = imageList.scrollWidth - imageList.clientWidth;
  };

  const handleSlideButtons = () => {
    slideButtons[0].style.display = imageList.scrollLeft <= 0 ? "none" : "block";
    slideButtons[1].style.display = imageList.scrollLeft >= maxScrollLeft ? "none" : "block";
  };

  const updateScrollThumbPosition = () => {
    if (scrollbarThumb) { // Перевіряємо, чи існує scrollbarThumb перед використанням
      const scrollPosition = imageList.scrollLeft;
      const thumbPosition = (scrollPosition / maxScrollLeft) * (imageList.clientWidth - scrollbarThumb.offsetWidth);
      scrollbarThumb.style.left = `${thumbPosition}px`;
    }
  };

  if (imageList) { // Перевіряємо, чи існує imageList перед додаванням події
    imageList.addEventListener("scroll", () => {
      handleSlideButtons();
      updateScrollThumbPosition();
    });
  }

  if (slideButtons) { // Перевіряємо, чи існує slideButtons перед додаванням події
    slideButtons.forEach(button => {
      button.addEventListener("click", () => {
        const direction = button.id === "prev-slide" ? -1 : 1;
        const scrollAmount = imageList.clientWidth * direction;
        imageList.scrollBy({ left: scrollAmount, behavior: "smooth" });
        updateScrollThumbPosition();
      });
    });
  }

  window.addEventListener("resize", () => {
    updateMaxScrollLeft();
    updateScrollThumbPosition();
  });
};

window.addEventListener("load", initSlider);

document.getElementById("searchInput").addEventListener("keydown", function(event) {
  if (event.key === "Enter") {
      event.preventDefault(); // Зупиняємо дію за замовчуванням, щоб форма не відправлялася двічі
      document.getElementById("searchForm").submit(); // Відправляємо форму
  }
});