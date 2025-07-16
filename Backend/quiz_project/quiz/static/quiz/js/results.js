window.onload = () => {
    const score = new URLSearchParams(window.location.search).get('score');
    if (score) {
        document.getElementById('score').textContent = `Your score: ${score}`;
    } else {
        alert('No score found.');
        window.location.href = '/dashboard';
    }
};

function goToDashboard() {
    window.location.href = '/dashboard';
}