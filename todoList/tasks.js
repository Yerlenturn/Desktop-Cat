function newTask() {
    console.log("penis")
    const noTask = $('.newTask .task').val() == '';
    const noDate = $('.newTask .date').val() == '';
    if (noTask || noDate) {
        if (noTask) {
            $('#taskWarning').show();
        }
        if (noDate) {
            $('#dateWarning').show();
        }
    } else {
        $('.warning').hide();

        taskList.content.maxKey++;
        console.log(taskList)
        console.log($('.newTask'));
        console.log(taskList.content.maxKey);
        const key = 'task' + taskList.content.maxKey;
        const data = {
            "task": $('.newTask .task').val(),
            'done': $('.newTask .checkbox').prop('checked'),
            'date': $('.newTask .date').val()
        };
        taskList.content.tasks[key] = data;

        clearNewTask();

        if ($('.savedTask').length > 0){
            insert('savedTask', createTask(key, data));
        } else {
            $('#taskColumn').append(createTask(key, data));
        }
        
        saveTaskFile();
    }
}

function deleteTask(key) {
    $('#' + key).remove();
    delete taskList.content.tasks[key];

    saveTaskFile();
}

function clearNewTask() {
    document.getElementById('newTask').value = "";
    document.getElementById('newDate').value = "";
    document.getElementById('newCheckbox').checked = false;
}

function buildTasks() {
    console.log(typeof taskList.content)
    const keys = Object.keys(taskList.content.tasks);
    keys.forEach(task => {
        if ($('.savedTask').length > 0){
            insert('savedTask', createTask(task, taskList.content.tasks[task]));
        } else {
            $('#taskColumn').append(createTask(task, taskList.content.tasks[task]));
        }
    });
}

// task style
//     <div class="taskWrapper savedTask">
//         <input class="checkbox" type="checkbox" />
//         <textarea class="task" name="task"></textarea>
//         <input class="date" type="date" />
//         <div class="sideButton">☒</div>
//     </div>

function createTask(key, data) {
    const wrapper = document.createElement('div');
    wrapper.classList.add('taskWrapper');
    wrapper.classList.add('savedTask');
    wrapper.id = key;

    // checkbox
    const c = document.createElement('input');
    c.classList.add('checkbox');
    c.type = 'checkbox';
    c.addEventListener("click", () => {
        toggleClass(wrapper, 'done');
        taskList.content.tasks[key].done = !(taskList.content.tasks[key].done);
        console.log(taskList.content);
        saveTaskFile();
    }); 

    // task
    const t = document.createElement('textarea');
    t.classList.add('task');
    t.classList.add('input');
    t.disabled = true;
    t.name = 'task';

    // date
    const d = document.createElement('input');
    d.classList.add('date', 'input');
    d.type = 'date';
    d.disabled = true;
    wrapper.dataset.val = 0;

    // button
    const b = document.createElement('div');
    b.classList.add('sideButton');
    b.textContent = '☒';
    b.addEventListener("click", () => {
        deleteTask(key);
    });

    // apply data
    if (data) {
        c.checked = data.done;
        if (data.done) {
            wrapper.classList.add('done');
        }
        t.value = data.task;
        d.value = data.date;
        wrapper.dataset.val = parseInt(data.date.replace(/-/g, ''));
        if (new Date(data.date) < new Date()) {
            wrapper.classList.add('late');
        }
    }

    wrapper.appendChild(c);
    wrapper.appendChild(t);
    wrapper.appendChild(d);
    wrapper.appendChild(b);
    
    return wrapper;
}
