window.onload = async () => {
    const token = localStorage.getItem('token');
    if (!token) {
        window.location.href = '/';
    }

    const response = await fetch('/api/quizzes/', {
        headers: {
            'Authorization': `Bearer ${token}`
        }
    });

    if (response.ok) {
        const quizzes = await response.json();
        const quizList = document.getElementById('quizList');
        quizzes.forEach(quiz => {
            const quizItem = document.createElement('li');
            quizItem.classList.add('bg-white', 'p-4', 'rounded', 'shadow', 'hover:bg-gray-100');
            quizItem.innerHTML = `
                <h3 class="text-lg font-bold">${quiz.title}</h3>
                <button onclick="startQuiz(${quiz.id})" class="bg-blue-500 text-white p-2 rounded-md hover:bg-blue-600">Start Quiz</button>
            `;
            quizList.appendChild(quizItem);
        });
    } else {
        alert('Failed to load quizzes.');
    }
};

function startQuiz(quizId) {
    localStorage.setItem('quizId', quizId);
    window.location.href = '/quiz';
}

function logout() {
    localStorage.removeItem('token');
    window.location.href = '/';
}