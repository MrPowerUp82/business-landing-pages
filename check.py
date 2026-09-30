"""Quick static checks for the generated GitHub Pages site."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).parent
PAGES = [ROOT / 'index.html', *sorted((ROOT / 'projects').glob('*/index.html'))]

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.refs = []
        self.anchors = set()
        self.titles = 0
        self.descriptions = 0
        self.images = 0
    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        if data.get('id'):
            self.anchors.add(data['id'])
        if tag == 'title':
            self.titles += 1
        if tag == 'meta' and data.get('name') == 'description':
            self.descriptions += 1
        if tag == 'img':
            self.images += 1
            assert data.get('alt') is not None, 'Missing image alt'
        for attr in ('href','src'):
            if data.get(attr):
                self.refs.append(data[attr])

errors = []
if len(PAGES) != 21:
    errors.append(f'Expected 21 HTML pages, found {len(PAGES)}')
for page in PAGES:
    parser = Links()
    parser.feed(page.read_text(encoding='utf-8'))
    if parser.titles != 1 or parser.descriptions != 1:
        errors.append(f'{page}: missing title or description')
    for ref in parser.refs:
        url = urlsplit(ref)
        if url.scheme in ('https','http','mailto','tel') or ref.startswith('//'):
            continue
        if url.path:
            target = (page.parent / unquote(url.path)).resolve()
            if not target.is_file():
                errors.append(f'{page}: broken file {ref}')
        if url.fragment:
            target_page = (page.parent / unquote(url.path)).resolve() if url.path else page
            if target_page.suffix == '.html' and target_page.exists():
                target_parser = Links()
                target_parser.feed(target_page.read_text(encoding='utf-8'))
                if url.fragment not in target_parser.anchors:
                    errors.append(f'{page}: broken anchor {ref}')
    if page.parent.name != 'business-landing-pages':
        text = page.read_text(encoding='utf-8')
        if 'Projeto demonstrativo desenvolvido para fins de portfólio.' not in text:
            errors.append(f'{page}: missing demo notice')
        for filename in ('style.css','script.js'):
            if not (page.parent / filename).is_file():
                errors.append(f'{page}: missing {filename}')

if errors:
    print('\n'.join(errors))
    raise SystemExit(1)
print(f'OK: {len(PAGES)} pages; internal files, anchors, metadata and demo notices verified.')
