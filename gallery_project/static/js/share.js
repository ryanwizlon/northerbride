document.addEventListener('DOMContentLoaded', (event) => {
    const shareButtons = document.querySelectorAll('.share-button');

    shareButtons.forEach(button => {
        button.addEventListener('click', shareArtwork);
    });
});

function shareArtwork(event) {
    const artworkId = event.target.dataset.artworkId;
    const shareUrl = `/share?artworkId=${artworkId}`;

    fetch(shareUrl, {
        method: 'POST',
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Artwork successfully shared!');
        } else {
            alert('Failed to share artwork. Please try again.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}