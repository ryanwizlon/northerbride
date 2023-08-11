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
        })
        .catch(error => console.error('Error:', error))
        .finally(() => console.log('Artworks loaded'));
}

function displayArtwork(artwork) {
    let container = document.getElementById('gallery-container');
    let artworkItem = document.createElement('div');
    artworkItem.id = 'artwork-item';
    artworkItem.innerHTML = `
        <img src="${artwork.image_url}" alt="${artwork.title}">
        <h2>${artwork.title}</h2>
        <p>${artwork.description}</p>
        <button id="share-button" onclick="shareArtwork('${artwork.id}')">Share</button>
        <div id="comment-section"></div>
    `;
    container.appendChild(artworkItem);
    loadComments(artwork.id);
}

function loadComments(artworkId) {
    fetch(`/comment?artworkId=${artworkId}`)
        .then(response => response.json())
        .then(data => {
            let commentSection = document.getElementById('comment-section');
            data.forEach(comment => {
                let commentItem = document.createElement('p');
                commentItem.innerText = comment.text;
                commentSection.appendChild(commentItem);
            });
        })
        .catch(error => console.error('Error:', error))
        .finally(() => console.log('Comments loaded'));
}

function postComment(artworkId, text) {
    fetch('/comment', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ artworkId, text }),
    })
    .then(response => response.json())
    .then(data => console.log('Comment posted:', data))
    .catch((error) => console.error('Error:', error));
}

function shareArtwork(artworkId) {
    fetch(`/share?artworkId=${artworkId}`)
        .then(response => response.json())
        .then(data => console.log('Artwork shared:', data))
        .catch((error) => console.error('Error:', error));
}

function getUserProfile(userId) {
    fetch(`/user?userId=${userId}`)
        .then(response => response.json())
        .then(data => {
            let userProfile = document.getElementById('user-profile');
            userProfile.innerText = `User: ${data.username}`;
        })
        .catch((error) => console.error('Error:', error));
}
```