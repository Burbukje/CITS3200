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
}

function previewFile(file) {
  const output = document.getElementById('gallery');
  output.textContent = '';
  const li = document.createElement('li');
  li.textContent = file.name;
  output.appendChild(li);
}

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