"use strict";

var timeout = 0;

function displaySlide(pic) {
    let url = `url("${pic.path}")`;
    let body = document.getElementsByTagName('body')[0];
    window.setTimeout(() => { body.style.backgroundImage = url; }, timeout);
    timeout = timeout + parseInt(pic.duration, 10);
}

//Total time of slideshow.
//Value returned is used to 'refresh' the page.
function getTotalTimeout(metadata) {
  let total = 0;
  metadata.forEach( (pic) => {
    total = total + parseInt(pic.duration);
  });

  return total;
}

function loadPictures(url) {
  let req = new XMLHttpRequest();
  req.onreadystatechange = () => {
    if (req.readyState === XMLHttpRequest.DONE) {
      if (req.status === 200) {
        let metadata = JSON.parse(req.responseText);
        metadata.pictures.forEach(displaySlide);
        let totalTime = getTotalTimeout(metadata.pictures);
        console.log(totalTime);
        window.setTimeout(() => { loadPictures(url); }, totalTime);
      }
    }
  }

  req.open('GET', '/pictures', true);
  req.send();
}
