// When the user scrolls the page, execute myFunction
var header = document.getElementsByTagName("header")[0];
var nav = document.getElementsByTagName("nav")[0];

window.onscroll = function(){
  if (window.pageYOffset > 50) {
    header.classList.add("scrolled");
    nav.classList.add("scrolled");
  } else {
    header.classList.remove("scrolled");
    nav.classList.remove("scrolled");
  }
};


$('nav li.onhover-effect>a').click(function(event){
    if( /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) ) {
        event.preventDefault();
    }
}); 