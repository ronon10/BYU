
function saveFavoriteCar(carName) {
    let favorites = JSON.parse(localStorage.getItem("favorites")) || [];
    
    if (!favorites.includes(carName)) {
        favorites.push(carName);
        localStorage.setItem("favorites", JSON.stringify(favorites));
        alert(carName + " has been added to your favorites!");
    } else {
        alert(carName + " is already in your favorites!");
    }
}


function displayFavorites() {
    const favorites = JSON.parse(localStorage.getItem("favorites")) || [];
    const favoritesList = document.getElementById("favorites-list");

    if (favorites.length > 0) {
        favoritesList.innerHTML = "<h3>Favorite Cars:</h3><ul>" + 
            favorites.map(car => `<li>${car}</li>`).join('') + "</ul>";
    } else {
        favoritesList.innerHTML = "<p>You don't have any favorite cars yet.</p>";
    }
}


function removeFavoriteCar(carName) {
    let favorites = JSON.parse(localStorage.getItem("favorites")) || [];
    favorites = favorites.filter(car => car !== carName);
    localStorage.setItem("favorites", JSON.stringify(favorites));
    alert(carName + " has been removed from your favorites!");
}


document.addEventListener("DOMContentLoaded", function() {
    displayFavorites();  
});


const addToFavoritesButtons = document.querySelectorAll('.add-to-favorites');
addToFavoritesButtons.forEach(button => {
    button.addEventListener('click', function() {
        const carName = button.getAttribute('data-car-name');
        saveFavoriteCar(carName);
    });


    window.addEventListener("DOMContentLoaded", function() {
        const lastModified = document.lastModified;
        document.getElementById("last-modified").textContent = lastModified;
    });
    
    
});
