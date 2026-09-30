const buttons = [...document.querySelectorAll('[data-filter]')];
const search = document.querySelector('#project-search');
const cards = [...document.querySelectorAll('.project-card')];
const count = document.querySelector('.result-count');
const empty = document.querySelector('.empty');
const normalize = value => value.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLocaleLowerCase('pt-BR');
let category = 'Todos';

function filterProjects() {
  const term = normalize(search.value.trim());
  let visible = 0;
  cards.forEach(card => {
    const match = (category === 'Todos' || card.dataset.category === category)
      && normalize(card.dataset.search).includes(term);
    card.hidden = !match;
    if (match) visible++;
  });
  count.textContent = `Mostrando ${visible} projeto${visible === 1 ? '' : 's'}`;
  empty.hidden = visible !== 0;
}

buttons.forEach(button => button.addEventListener('click', () => {
  category = button.dataset.filter;
  buttons.forEach(item => item.setAttribute('aria-pressed', String(item === button)));
  filterProjects();
}));
search.addEventListener('input', filterProjects);
