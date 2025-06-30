        var addBtn = document.getElementById('add-btn');
        var newTaskInput = document.getElementById('new-task');
        var taskList = document.getElementById('task-list');

        function addTask() {
            var taskText = newTaskInput.value;
            taskText = taskText.trim()
            if (taskText === '') {
                return;
            }

            var li = document.createElement('li');
            li.innerHTML = taskText + ' ';

            var delBtn = document.createElement('button');
            delBtn.innerHTML = 'Delete';
            delBtn.className = 'delete-btn';

            // Use addEventListener for beginners
            delBtn.addEventListener('click', function() {
                taskList.removeChild(li);
            });                         
  

             li.appendChild(delBtn);
            taskList.appendChild(li);

            newTaskInput.value = '';
            newTaskInput.focus();
        }

        addBtn.onclick = addTask;

        newTaskInput.onkeypress = function(e) {
            if (e.key === 'Enter') {
                addTask();
            }
        };