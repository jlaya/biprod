function showLightbox() {
    document.getElementById('menu-side').style.transform='translate(0%, 0)';
    document.getElementById('fade').style.display='block';
    document.getElementById('menu-icon-clear').style.display='block';
}
function hideLightbox() {
    document.getElementById('menu-side').style.transform='translate(-100%, 0)';
    document.getElementById('fade').style.display='none';
    document.getElementById('menu-icon-clear').style.display='none';
}
