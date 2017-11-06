function toggleNavBar() {
    var menu = document.getElementById('nav-menu');
    if (menu.classList.contains('menu-hidden'))
        menu.classList.remove('menu-hidden');
    else
        menu.classList.add('menu-hidden');
}
