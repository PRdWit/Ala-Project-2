const itemWidth = 250;
let currentIndex = 0;

function scrollCarousel(direction) {
  const carouselInner = document.getElementById("carousel-inner");
  const totalItems = carouselInner.children.length; // Total number of carousel items
  
  const visibleItems = 4;
  
  const maxIndex = totalItems - visibleItems; // Maximum index where scrolling stops
  currentIndex += direction;

  // Ensure the currentIndex stays within the valid range
  if (currentIndex < 0) {
    currentIndex = 0;
  } else if (currentIndex > maxIndex) {
    currentIndex = maxIndex; // Prevent overscrolling beyond the last item
  }

  const translateX = -currentIndex * itemWidth; // Calculate translation
  carouselInner.style.transform = `translateX(${translateX}px)`;
}




