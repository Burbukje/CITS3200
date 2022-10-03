"use strict";

// Drag and drop
let dropArea = document.getElementById("drop-area");

// Prevent default drag behaviors
;['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
  dropArea.addEventListener(eventName, preventDefaults, false);
  document.body.addEventListener(eventName, preventDefaults, false);
})

// Highlight drop area when item is dragged over it
;['dragenter', 'dragover'].forEach(eventName => {
  dropArea.addEventListener(eventName, highlight, false);
})

// Unhighlight drop area after item is dropped
;['dragleave', 'drop'].forEach(eventName => {
  dropArea.addEventListener(eventName, unhighlight, false);
})

// Handle dropped files
dropArea.addEventListener('drop', handleDrop, false);

function preventDefaults (e) {
  e.preventDefault();
  e.stopPropagation();
}

function highlight(e) {
  dropArea.classList.add('highlight');
}

function unhighlight(e) {
  dropArea.classList.remove('highlight');
}

function handleDrop(e) {
  var dt = e.dataTransfer;
  var files = dt.files;
  handleFiles(files);
}

function handleFiles(files) {
  files = [...files]; // convert fileList to array to make iteration easier
  files.forEach(previewFile);
  // initializeProgress(files.length)
  // files.forEach(uploadFile)
}

function previewFile(file) {
  const output = document.getElementById('gallery');
  output.textContent = '';
  const li = document.createElement('li');
  li.textContent = file.name;
  output.appendChild(li);
}

/*
let uploadProgress = []
let progressBar = document.getElementById('progress-bar')
function initializeProgress(numFiles) {
  progressBar.value = 0
  uploadProgress = []
  for(let i = numFiles; i > 0; i--)
    uploadProgress.push(0)
}
function updateProgress(fileNumber, percent) {
  uploadProgress[fileNumber] = percent
  let total = uploadProgress.reduce((tot, curr) => tot + curr, 0) / uploadProgress.length
  progressBar.value = total
}
function uploadFile(file, i) {
  var url = 'https://api.cloudinary.com/v1_1/joezimim007/image/upload'
  var xhr = new XMLHttpRequest()
  var formData = new FormData()
  xhr.open('POST', url, true)
  xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest')
  // Update progress (can be used to show progress indicator)
  xhr.upload.addEventListener("progress", function(e) {
    updateProgress(i, (e.loaded * 100.0 / e.total) || 100)
  })
  xhr.addEventListener('readystatechange', function(e) {
    if (xhr.readyState == 4 && xhr.status == 200) {
      updateProgress(i, 100) // <- Add this
    }
    else if (xhr.readyState == 4 && xhr.status != 200) {
      // Error. Inform the user
    }
  })
  formData.append('upload_preset', 'ujpu6gyk')
  formData.append('file', file)
  xhr.send(formData)
}
*/

// Get the modal
//var modal = document.getElementById("myModal");

// Get the button that opens the modal
// var btn = document.getElementById("upload-btn");

// Get the <span> (x) element that closes the modal
// var cross = document.getElementsByClassName("close")[0];

// Get the cancel button that closes the modal
// var cancelButton = document.getElementById("cancel-btn");

// When the user clicks the button, open the modal 
// btn.onclick = function() {
//   modal.style.display = "block";
// }

// When the user clicks on <span> (x) close the modal
// cross.onclick = function() {
//   modal.style.display = "none";
// }

// When the user clicks the button, close the modal
// cancelButton.onclick = function() {
//   modal.style.display ="none";
// }

// When the user clicks anywhere outside of the modal, close it
// window.onclick = function(event) {
//   if (event.target == modal) {
//     modal.style.display = "none";
//   }
// }

// Button to show and hide password
function showHidePassword() {
  var buttonName = document.getElementById("show-hide");
  var pInput = document.getElementById("pass-input");
  if (pInput.type == "password") {
      pInput.type = "text";
      buttonName.innerHTML = "Hide";
  }  
  else {
      pInput.type = "password";
      buttonName.innerHTML = "Show";
  }
}