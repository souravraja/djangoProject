let menu=document.querySelector('#menu-btn');
let navbar=document.querySelector('.navbar');
menu.onclick=()=>{
    menu.classList.toggle('fa-items');
    navbar.classList.toggle('active');
}
window.onscroll=()=>{
    menu.classList.remove('fa-items');
    navbar.classList.remove('active');
}