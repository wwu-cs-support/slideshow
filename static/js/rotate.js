var body = document.getElementsByTagName("body")[0];
var path = "/static/pictures/";
var allPics = ['pookie.jpeg', 'pool.jpg', 'sea_urchin.tiff', 'singapore.png', 'snake.png', 'standing_buddha.jpg'];
var i = 0;
var intervalID = window.setInterval(slideshow, 5000);

function slideshow() {
    var pic = "url(" + path + allPics[i] + ")";
    body.style.backgroundImage = pic;
    if(i == (allPics.length -1)){
        i = 0;
    }
    else{
        i++;
    }
}
