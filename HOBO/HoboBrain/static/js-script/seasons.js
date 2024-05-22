function filterepisodes() {
    const selectedSeason = document.getElementById('seizoenen').value;
    const episodes = document.querySelectorAll(".episode");

    for (episode of episodes) {
        if (episode.classList.contains(selectedSeason)) {
            episode.style.display = 'block';
        }
        else {
            episode.style.display = 'none';
        }
    }
}

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('seizoenen').value = '1';  // Assuming '1' is the first season
    filterepisodes()();
});