"use strict";

var timeout = 0;

function displaySlide(pic) {
    let url = `url("${pic.path}")`;
    let body = document.getElementsByTagName('body')[0];
    timeout = timeout + parseInt(pic.duration, 10);
    window.setTimeout(() => { body.style.backgroundImage = url; }, timeout);
}


function loadPictures(url) {
  let req = new XMLHttpRequest();
  req.onreadystatechange = () => {
    if (req.readyState === XMLHttpRequest.DONE) {
      if (req.status === 200) {
        let metadata = JSON.parse(req.responseText);
        metadata.pictures.forEach(displaySlide);
        loadPictures(url);
      }
    }
  }

  req.open('GET', '/pictures', true);
  req.send();
}
