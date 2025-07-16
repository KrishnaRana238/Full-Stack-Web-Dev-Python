window.onload = async () => {
    const token = localStorage.getItem('token');
    const quizId = localStorage.getItem('quizId');
    if (!token || !quizId) {
        window.location.href = '/';
    }

    const response = await fetch(`/api/quizzes/${quizId}/`, {
        headers: {
            'Authorization': `Bearer ${token}`
        }
    });

    if (response.ok) {
        const quiz = await response.json();
        document.getElementById('quizTitle').textContent = quiz.title;
        const questionContainer = document.getElementById('questionContainer');
        quiz.questions.forEach(question => {
            const questionItem = document.createElement('div');
            questionItem.innerHTML = `
                <h3 class="text-lg font-bold">${question.text}</h3>
                <label><input type="radio" name="q${question.id}" value="option1"> ${question.option1}</label><br>
                <label><input type="radio" name="q${question.id}" value="option2"> ${question.option2}</label><br>
                <label><input type="radio" name="q${question.id}" value="option3"> ${question.option3}</label><br>
                <label><input type="radio" name="q${question.id}" value="option4"> ${question.option4}</label>
            `;
            questionContainer.appendChild(questionItem);
        });
    } else {
        alert('Failed to load quiz.');
    }
};

document.getElementById('quizForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const token = localStorage.getItem('token');
    const quizId = localStorage.getItem('quizId');
    const answers = {};
    const inputs = document.querySelectorAll('input[type="radio"]:checked');
    inputs.forEach(input => {
        answers[input.name] = input.value;
    });

    const response = await fetch('/api/submit/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({ quiz_id: quizId, answers })
    });

    if (response.ok) {
        const result = await response.json();
        localStorage.removeItem('quizId');
        window.location.href = `/results?score=${result.score}`;
    } else {
        alert('Failed to submit quiz.');
    }
});