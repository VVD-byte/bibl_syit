$(document).ready(function color_nav(){
    if (window.screen.width <= 991){
        document.getElementsByTagName('nav')[0].style.setProperty("background-color", "#0D3541", "important");
    }
    else{document.getElementsByTagName('nav')[0].style.setProperty("background-color", "#FFFFFF", "important");}
})