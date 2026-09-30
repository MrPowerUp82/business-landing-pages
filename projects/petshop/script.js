// Page-specific behavior for AuMigos Pet
const comparison=document.querySelector('.compare-box');const slider=comparison.querySelector('input');slider.addEventListener('input',()=>comparison.style.setProperty('--pos',slider.value+'%'));
