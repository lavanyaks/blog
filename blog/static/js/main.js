window.onload = function () {
    var showMenu = document.getElementsByClassName('mobile-menu-icon');
    var closeMenu = document.getElementsByClassName('mobile-menu-close');
    var navMenu = document.getElementsByClassName('nav');

    showMenu[0].addEventListener('click', function () {
        if(navMenu[0].classList.contains('open')) {
            navMenu[0].classList.remove('open');
        }
        else {
            navMenu[0].className += " open";
        }
    });

    closeMenu[0].addEventListener('click', function () {
        navMenu[0].classList.remove('open');
    })
};
