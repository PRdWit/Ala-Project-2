const itemWidth = 210;
let currentIndex = 0;

function scrollCarousel(direction) {
  const carouselInner = document.getElementById("carousel-inner");
  const totalItems = carouselInner.children.length;

  const visibleItems = 3;

  const maxScroll = (totalItems - visibleItems) * itemWidth;

  currentIndex += direction;

  if (currentIndex < 0) {
    currentIndex = 0;
  } else if (currentIndex * itemWidth > maxScroll) {
    currentIndex = Math.floor(maxScroll / itemWidth);
  }

  carouselInner.style.transform = `translateX(${-currentIndex * itemWidth}px)`;
}

