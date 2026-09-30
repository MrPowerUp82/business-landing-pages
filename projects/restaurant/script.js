// Page-specific behavior for Brasa Burger
const menu=document.querySelector('.menu-dialog');document.querySelector('[data-menu-open]').addEventListener('click',()=>menu.showModal());document.querySelector('[data-menu-close]').addEventListener('click',()=>menu.close());menu.addEventListener('click',event=>{if(event.target===menu)menu.close()});
