var body = document.getElementsByTagName("body")[0];
var path = "/static/pictures/";
var allPics = ['pookie.jpeg', 'pool.jpg', 'sea_urchin.tiff', 'singapore.png', 'snake.png', 'standing_buddha.jpg'];
var timeout = 0;

for (pic of allPics){
    slideshow(pic, timeout);
    timeout = timeout + 2000;
}

function slideshow(pic, timeout) {
    var pic = "url(" + path + pic + ")";
    window.setTimeout(function(){ body.style.backgroundImage = pic;}, timeout)
}
