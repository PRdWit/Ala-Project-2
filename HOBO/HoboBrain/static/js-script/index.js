let margin = 10;

let item = document.querySelector(".carousel-trending").getBoundingClientRect();
let width = item.width;

let itemWidth = width+margin;

let screenSize = window.innerWidth - 25;

let maxItems = screenSize / (itemWidth);

const carouselInner2 = document.getElementById("carousel-inner2");
const carouselInner3 = document.getElementById("carousel-inner3");

const totalItems2 = carouselInner2.children.length;
const totalItems3 = carouselInner3.children.length;

let maxIndex2 = totalItems2 - maxItems;
let maxIndex3 = totalItems3 - maxItems;

let index2 = 0;
let index3 = 0;

function carouselTrending(direction) {
  index2 += direction;

  if (index2 < 0) {
    index2 = 0;
  }
  else if (index2 > maxIndex2) {
    index2 = maxIndex2;
  }

  let mover = -index2 * itemWidth;
  carouselInner2.style.transform = `translateX(${mover}px)`;
}

function carouselEditor(direction) {
  index3 += direction;

  if (index3 < 0) {
    index3 = 0;
  }
  else if (index3 > maxIndex3) {
    index3 = maxIndex3;
  }

  let mover = -index3 * itemWidth;
  carouselInner3.style.transform = `translateX(${mover}px)`;
}