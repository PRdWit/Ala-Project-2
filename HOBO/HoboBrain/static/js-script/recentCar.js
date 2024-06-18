const carouselInner = document.getElementById("carousel-inner");
const totalItems = carouselInner.children.length;
let maxIndex = totalItems - maxItems;
let index = 0;

function carouselRecent(direction) {
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