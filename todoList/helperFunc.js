function tester() {
    console.log('test successful');
}

function themeRotation() {
    let body = document.getElementsByTagName("BODY")[0];
    const currTheme = themes.indexOf(body.className);
    body.className = themes[(currTheme + 1) % themes.length];
    $('#backdrop').attr('src', './css/catBG_'+body.className+'.png');
    taskList.content.cookies.theme = body.className;
    saveTaskFile();
}

function toggleClass(div, className) {
    if (div.classList.contains(className)) {
        div.classList.remove(className);
    } else {
        div.classList.add(className);
    }
}

function toggleVisibility(className) {
    if ($('.' + className + ':first').is(':hidden')) {
        $('.' + className).show();
    } else {
        $('.' + className).hide();
    }
}

function clearCache() {
    let temp = {
      "title": "toDoList",
      "maxKey": 0,
      "tasks": {},
    };
    temp['cookies'] = cookies;
    temp['reminder'] = taskList.content.reminder;
    taskList.content = temp;
    saveTaskFile();
    location.reload();
}

function toggleTextContent(id, cookieVal, text) {
    let mode;
    if (cookies[cookieVal]) {
        mode = 'hide ';
    } else {
        mode = 'show ';
    }
    $('#' + id).text(mode + text);
    taskList.content.cookies[cookieVal] = !(cookies[cookieVal]);
    console.log(cookies[cookieVal], !(cookies[cookieVal]));
    console.log(taskList.content);
    saveTaskFile();
}

function updateReminder() {
    taskList.content.reminder = $("#reminderText").val();
    console.log(taskList.content);
    saveTaskFile();
}

function saveTaskFile() {
    fetch('http://localhost:3000/todoList/notes', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(taskList),
    })
    .then(response => response.json())
    .catch(error => {
        console.error('Error creating note:', error);
        // alert('Error creating note. See console for details.');
    });
}

function insert(wrapper, div) {     // small to large by data-val value in HTML
    $('.' + wrapper).each(function(index) {
        if ($(this).data('val') > parseInt(div.dataset.val)) {
            $(this).before(div);
            return false;       // must return false to break the .each() loop
        }
        // insert to end
        if (index == $('.' + wrapper).length - 1) {
            $(this).after(div);
        }
    });
}
