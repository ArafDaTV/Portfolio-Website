function menuClick() {
    document.getElementById('menu').classList.toggle('fa-times');
    document.getElementById('header').classList.toggle('toggle');
}

window.addEventListener('scroll', function () {
    document.getElementById('menu').classList.remove('fa-times');
    document.getElementById('header').classList.remove('toggle');
})