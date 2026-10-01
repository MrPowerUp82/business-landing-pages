"""Quick static checks for the generated GitHub Pages site."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
from xml.etree import ElementTree
from build import SITES, SITE_URL

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
        self.lang = None
        self.metadata = {}
        self.canonicals = []
    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        if tag == 'html':
            self.lang = data.get('lang')
        if tag == 'meta':
            key = data.get('property') or data.get('name')
            if key:
                self.metadata.setdefault(key, []).append(data.get('content', ''))
        if tag == 'link' and data.get('rel') == 'canonical':
            self.canonicals.append(data.get('href', ''))
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
if len(PAGES) != len(SITES) + 1:
    errors.append(f'Expected {len(SITES) + 1} HTML pages, found {len(PAGES)}')
for page in PAGES:
    parser = Links()
    parser.feed(page.read_text(encoding='utf-8'))
    if parser.titles != 1 or parser.descriptions != 1:
        errors.append(f'{page}: missing title or description')
    path = '' if page == ROOT / 'index.html' else page.parent.relative_to(ROOT).as_posix() + '/'
    canonical = SITE_URL + '/' + path
    if parser.lang != 'pt-BR' or parser.canonicals != [canonical]:
        errors.append(f'{page}: incorrect language or canonical URL')
    for key in ('description', 'robots', 'og:type', 'og:locale', 'og:site_name',
                'og:title', 'og:description', 'og:url', 'og:image', 'og:image:alt',
                'twitter:card', 'twitter:title', 'twitter:description', 'twitter:image', 'twitter:image:alt'):
        values = parser.metadata.get(key, [])
        if len(values) != 1 or not values[0].strip():
            errors.append(f'{page}: missing, duplicate or empty {key}')
    if parser.metadata.get('og:url') != [canonical] or parser.metadata.get('og:locale') != ['pt_BR']:
        errors.append(f'{page}: incorrect Open Graph URL or locale')
    for key in ('og:image', 'twitter:image'):
        for ref in parser.metadata.get(key, []):
            if not ref.startswith(SITE_URL + '/') or not (ROOT / unquote(ref.removeprefix(SITE_URL + '/'))).is_file():
                errors.append(f'{page}: invalid sharing image {ref}')
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

sitemap = ROOT / 'sitemap.xml'
if sitemap.is_file():
    tree = ElementTree.parse(sitemap)
    urls = [node.text for node in tree.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
    expected = [SITE_URL + '/', *(SITE_URL + '/projects/' + site['slug'] + '/' for site in SITES)]
    if sorted(urls) != sorted(expected):
        errors.append('Sitemap must include every canonical URL exactly once')
else:
    errors.append('Missing sitemap.xml')
robots = ROOT / 'robots.txt'
if not robots.is_file() or 'Sitemap: ' + SITE_URL + '/sitemap.xml' not in robots.read_text(encoding='utf-8'):
    errors.append('Missing robots.txt or incorrect sitemap reference')

if errors:
    print('\n'.join(errors))
    raise SystemExit(1)
print(f'OK: {len(PAGES)} pages; internal files, anchors, metadata and demo notices verified.')
