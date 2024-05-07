let margin = 10;

let item = document.querySelector(".carousel-item").getBoundingClientRect();
let width = item.width;
let itemWidth = width+margin;


let screenSize = window.innerWidth;
let maxItems = screenSize / (itemWidth);

const carouselInner = document.getElementById("carousel-inner");
const totalItems = carouselInner.children.length;

let index = 0;
let maxIndex = totalItems - maxItems;

function scrollCarousel(direction) {
  index += direction;

  if (index < 0) {
    index = 0;
  }
  else if (index > maxIndex) {
    index = maxIndex;
  }

  let mover = -index * itemWidth;
  carouselInner.style.transform = `translateX(${mover}px)`;
}

//   const visibleItems = 4;
 
//   const maxIndex = totalItems - visibleItems; // Maximum index where scrolling stops
//   currentIndex += direction;
 
//   // Ensure the currentIndex stays within the valid range
//   if (currentIndex < 0) {
//     currentIndex = 0;
//   } else if (currentIndex > maxIndex) {
//     currentIndex = maxIndex; // Prevent overscrolling beyond the last item
//   }
 
//   const translateX = -currentIndex * itemWidth; // Calculate translation
//   carouselInner.style.transform = `translateX(${translateX}px)`;
// }
