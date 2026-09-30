const menuButton = document.querySelector('.menu-toggle');
const siteNav = document.querySelector('.site-nav');

if (menuButton && siteNav) {
  menuButton.addEventListener('click', () => {
    const open = siteNav.classList.toggle('open');
    menuButton.setAttribute('aria-expanded', String(open));
    menuButton.setAttribute('aria-label', open ? 'Fechar menu' : 'Abrir menu');
  });

  siteNav.querySelectorAll('a').forEach(link => link.addEventListener('click', () => {
    siteNav.classList.remove('open');
    menuButton.setAttribute('aria-expanded', 'false');
    menuButton.setAttribute('aria-label', 'Abrir menu');
  }));
}

const revealElements = document.querySelectorAll('.reveal');
if ('IntersectionObserver' in window && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
  const observer = new IntersectionObserver(entries => entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      observer.unobserve(entry.target);
    }
  }), { threshold: 0.08 });
  revealElements.forEach(element => observer.observe(element));
} else {
  revealElements.forEach(element => element.classList.add('visible'));
}

const labels = {
  nome: 'Nome', telefone: 'WhatsApp', pet: 'Pet', servico: 'Serviço',
  dia: 'Dia', horario: 'Horário', mensagem: 'Mensagem', interesse: 'Interesse'
};
const pad = value => String(value).padStart(2, '0');
const today = new Date();
const todayString = `${today.getFullYear()}-${pad(today.getMonth() + 1)}-${pad(today.getDate())}`;
document.querySelectorAll('input[type="date"]').forEach(input => input.min = todayString);

document.querySelectorAll('[data-demo-form]').forEach(form => {
  const phone = form.querySelector('[name="telefone"]');
  phone.addEventListener('input', () => phone.setCustomValidity(''));

  form.addEventListener('submit', event => {
    event.preventDefault();
    const feedback = form.querySelector('.form-feedback');
    const prepared = form.querySelector('.prepared-link');
    prepared.hidden = true;

    if (!form.checkValidity()) {
      form.reportValidity();
      feedback.textContent = 'Confira os campos obrigatórios antes de continuar.';
      return;
    }
    if (phone.value.replace(/\D/g, '').length < 10) {
      phone.setCustomValidity('Informe um WhatsApp com DDD.');
      phone.reportValidity();
      feedback.textContent = 'Informe um WhatsApp com DDD.';
      return;
    }

    const data = new FormData(form);
    const lines = [
      `Olá! Vi o site da ${form.dataset.business} e gostaria de conversar.`,
      ...Array.from(data.entries()).map(([key, value]) => `${labels[key] || key}: ${String(value).trim()}`)
    ];
    prepared.href = 'https://wa.me/5516999999999?text=' + encodeURIComponent(lines.join('\n'));
    prepared.hidden = false;
    feedback.textContent = 'Mensagem preparada! Clique no link abaixo para abrir o WhatsApp. Nenhum dado foi enviado por este site.';
    form.reset();
  });
});
