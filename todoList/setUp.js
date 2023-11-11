let taskList;   // fetched task json
let themes = ['red', 'winter', 'summer', 'night'];
let cookies;

async function onStart() {
    const response = await fetch("http://localhost:3000/todoList/notes/");
    taskList = await response.json();
    taskList = taskList[0];
    taskList.content = JSON.parse(taskList.content);

    buildTasks(taskList);
    $('#saveTask').click(newTask);
    $('#toggleTheme').click(themeRotation);
    document.getElementById('toggleFinishedTasks').addEventListener("click", () => {
        toggleVisibility('done');
        toggleTextContent('toggleFinishedTasks', 'done', 'finished tasks');
    });
    document.getElementById('toggleLateTasks').addEventListener("click", () => {
        toggleVisibility('late');
        toggleTextContent('toggleLateTasks', 'late', 'late tasks');
    });
    clearNewTask();
    $('.warning').hide();

    cookies = taskList.content.cookies;
    document.getElementsByTagName("BODY")[0].className = cookies.theme;
    $('#backdrop').attr('src', './css/catBG_'+cookies.theme+'.png');
    $('#reminderText').val(taskList.content.reminder);
    $('#reminderText').change(updateReminder);
    // implement cookies for hiding tasks
    if (cookies.done) {
        $(".done").hide();
        $("#toggleFinishedTasks").text('show finished tasks');
    }
    if (cookies.late) {
        $('.late').hide();
        $('#toggleLateTasks').text('show late tasks');
    }
    $('#clearCache').click(clearCache);
}

onStart();
