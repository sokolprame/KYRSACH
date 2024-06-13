// script.js
document.addEventListener('DOMContentLoaded', function () {
    const searchButton = document.getElementById('searchButton');
    const searchBar = document.getElementById('searchBar');

    searchButton.addEventListener('click', () => {
        searchBar.classList.toggle('open');
    });
});
