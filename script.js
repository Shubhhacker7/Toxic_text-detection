document.getElementById('classifyButton').addEventListener('click', function() {
    const comment = document.getElementById('comment').value;

    fetch('/classify', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ comment: comment })
    })
    .then(response => response.json())
    .then(data => {
        const resultDiv = document.getElementById('result');
        if (data.isToxic) {
            resultDiv.innerHTML = "The comment is toxic.";
        } else {
            resultDiv.innerHTML = "The comment is not toxic.";
        }
    })
    .catch(error => console.error('Error:', error));
});