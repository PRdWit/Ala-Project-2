let displayedItemsCount;

function countDisplayedItems() {
    const episodes = document.querySelectorAll(".episode");
    let totalDisplayedItems = 0;

    episodes.forEach(episode => {
        if (window.getComputedStyle(episode).display === 'block') {
            totalDisplayedItems++;
        }
    });

    return totalDisplayedItems;
}

function filterepisodes() {
    const selectedSeason = document.getElementById('seizoenen').value;
    const episodes = document.querySelectorAll(".episode");

    for (let episode of episodes) {
        if (episode.classList.contains(selectedSeason)) {
            episode.style.display = 'block';
        }
        else {
            episode.style.display = 'none';
        }
    }

    carouselEpi(0);
}

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('seizoenen').value = '1';
    filterepisodes();

    displayedItemsCount = countDisplayedItems();
    console.log("Total displayed items:", displayedItemsCount);
});


let margin = 10;

let item = document.querySelector(".episode").getBoundingClientRect();
let width = item.width;
let itemWidth = width+margin;

let screenSize = window.innerWidth - 25;

let maxItems = screenSize / (itemWidth);

const inner = document.getElementById("afleveringen");
let index = 0

function carouselEpi(direction) {
    let maxIndex = displayedItemsCount - maxItems;
    index += direction;

    if (index < 0) {
        index = 0;
    }
    else if (index > maxIndex) {
        index = maxIndex;
    }

    let mover = -index * itemWidth;
    inner.style.transform = `translate(${mover}px)`;
}