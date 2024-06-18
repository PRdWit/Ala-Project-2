const inputField = document.getElementById('displayEpi');
const epiP = document.getElementById("currentEpi");

window.inputEpi = function(id, title) {
    inputField.value = id;
    epiP.innerHTML = title;
}
