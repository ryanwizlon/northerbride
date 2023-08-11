```javascript
document.addEventListener('DOMContentLoaded', function() {
    const commentSection = document.getElementById('comment-section');
    const commentForm = commentSection.querySelector('form');

    commentForm.addEventListener('submit', function(event) {
        event.preventDefault();
        postComment();
    });
});

function postComment() {
    const commentInput = document.getElementById('comment-input');
    const commentList = document.getElementById('comment-list');
    const newComment = document.createElement('li');

    newComment.textContent = commentInput.value;
    commentList.appendChild(newComment);
    commentInput.value = '';

    // Emit comment-posted event
    const event = new CustomEvent('comment-posted');
    document.dispatchEvent(event);
}
```