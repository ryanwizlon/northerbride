```javascript
document.addEventListener('DOMContentLoaded', (event) => {
    loadGallery();
});

function loadGallery() {
    fetch('/gallery')
        .then(response => response.json())
        .then(data => {
            data.forEach(artwork => {
                displayArtwork(artwork);
            });
            document.dispatchEvent(new Event('artwork-loaded'));
        })
        .catch(error => console.error('Error:', error));
}

function displayArtwork(artwork) {
    const galleryContainer = document.getElementById('gallery-container');
    const artworkItem = document.createElement('div');
    artworkItem.id = `artwork-item-${artwork.id}`;
    artworkItem.className = 'gallery-item';
    artworkItem.innerHTML = `
        <img src="${artwork.image_url}" alt="${artwork.title}">
        <h2>${artwork.title}</h2>
        <p>${artwork.description}</p>
        <button id="share-button-${artwork.id}" class="share-icon">Share</button>
    `;
    galleryContainer.appendChild(artworkItem);
    document.getElementById(`share-button-${artwork.id}`).addEventListener('click', () => shareArtwork(artwork.id));
}
```