// Page-specific behavior for SolarTech Energia
const bill = document.querySelector('#bill');
const formatBRL = value => new Intl.NumberFormat('pt-BR',{style:'currency',currency:'BRL',maximumFractionDigits:0}).format(value);
function simulate(){const value=Math.max(0,Number(bill.value)||0);const month=value*.8;document.querySelector('[data-sim="month"]').textContent=formatBRL(month);document.querySelector('[data-sim="year"]').textContent=formatBRL(month*12);document.querySelector('[data-sim="long"]').textContent=formatBRL(month*12*25)}
bill.addEventListener('input',simulate);simulate();
