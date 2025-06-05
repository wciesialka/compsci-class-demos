
function ajax(url, cb) {
    const xhr = new XMLHttpRequest();
    xhr.onload = () => {
        if(xhr.status == 200){
            cb(xhr.responseText);
        } else {
            alert(xhr.statusText);
        }
    };
    xhr.open("GET", url, true);
    xhr.send();
}

function loadstring(url){
    let callback = (data) => {
        eval(data);
    };
    ajax(url, callback);
}

function click(ev) {
    const URL = String.raw`https://raw.githubusercontent.com/wciesialka/loadstring-js/refs/heads/main/js/payload.js`
    loadstring(URL);
}

function load(ev) {
    const button = document.getElementById('run-button');
    button.addEventListener("click", click)
}

window.addEventListener("load", load)