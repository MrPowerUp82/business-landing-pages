// Page-specific behavior for BlackCar Detail
const comparison=document.querySelector('.compare-box');const slider=comparison.querySelector('input');slider.addEventListener('input',()=>comparison.style.setProperty('--pos',slider.value+'%'));
