// Page-specific behavior for CodeStart Academy
const target=new Date();target.setDate(target.getDate()+21);const counter=document.querySelector('[data-countdown]');function updateCountdown(){const days=Math.max(0,Math.ceil((target-new Date())/86400000));counter.textContent=days+' dias'}updateCountdown();setInterval(updateCountdown,3600000);
