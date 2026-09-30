// Page-specific behavior for Atlas Construções
const comparison=document.querySelector('.compare-box');const slider=comparison.querySelector('input');slider.addEventListener('input',()=>comparison.style.setProperty('--pos',slider.value+'%'));
