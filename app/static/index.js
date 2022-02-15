const RESULTS_URL = "/results";
const DELETE_FOLDER_URL = "/api/delete_folder";
const UPLOAD_URL = "/api/upload";

const textPlaceholderImage = "./images/txt.png";
let dropArea = document.getElementById("drop-area");

// Prevent default drag behaviors
["dragenter", "dragover", "dragleave", "drop"].forEach((eventName) => {
    dropArea.addEventListener(eventName, preventDefaults, false);
    document.body.addEventListener(eventName, preventDefaults, false);
});

// Highlight drop area when item is dragged over it
["dragenter", "dragover"].forEach((eventName) => {
    dropArea.addEventListener(eventName, highlight, false);
});
["dragleave", "drop"].forEach((eventName) => {
    dropArea.addEventListener(eventName, unhighlight, false);
});

// Handle dropped files
dropArea.addEventListener("drop", handleDrop, false);

function preventDefaults(e) {
    e.preventDefault();
    e.stopPropagation();
}

function highlight(e) {
    dropArea.classList.add("highlight");
    dropArea.classList.add("active");
}

function unhighlight(e) {
    dropArea.classList.remove("highlight");
    dropArea.classList.remove("active");
}

function handleDrop(e) {
    var dt = e.dataTransfer;
    var files = dt.files;

    handleFiles(files);
}

let uploadProgress = [];
let progressBar = document.getElementById("progress-bar");

function initializeProgress(numFiles) {
    progressBar.value = 0;
    uploadProgress = [];

    for (let i = numFiles; i > 0; i--) {
        uploadProgress.push(0);
    }
}

function updateProgress(fileNumber, percent) {
    uploadProgress[fileNumber] = percent;
    let total =
        uploadProgress.reduce((tot, curr) => tot + curr, 0) /
        uploadProgress.length;
    progressBar.value = total;
}

function handleFiles(files) {
    files = [...files];
    initializeProgress(files.length);
    files.forEach(uploadFile);
    files.forEach(previewFile);
}

function previewFile(file) {
    if (file.type.includes("image")) {
        let reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onloadend = function () {
            let img = document.createElement("img");
            img.src = reader.result;
            document.getElementById("gallery").appendChild(img);
        };
    }
    if (file.type == "text/plain") {
        let img = document.createElement("img");
        img.src = textPlaceholderImage;
        document.getElementById("gallery").appendChild(img);
    }
}

function uploadFile(file, i) {
    let formData = new FormData();
    formData.append("file", file);
    fetch(UPLOAD_URL, {
        method: "POST",
        body: formData,
    })
        .then(() => {
            updateProgress(i, 100); // запоняем прогрессбар для картинки/файла
        })
        .catch(() => {
            // Ошибка. Информируем пользователя
        });
}

function submitForm(e) {
    e.preventDefault();
    window.location.href = RESULTS_URL;
}

document.querySelector("#submitButton").addEventListener("click", submitForm);

document.addEventListener("beforeunload", () => {
    fetch(DELETE_FOLDER_URL, {
        method: "POST",
    }).catch(() => {
        // Ошибка. Информируем пользователя
    });
});
