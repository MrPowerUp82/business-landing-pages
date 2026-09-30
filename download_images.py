"""Refresh local, optimized demo photos from Unsplash."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.request import urlopen
from build import SITES, SECONDARY, PHOTO

DEST = Path(__file__).parent / 'assets' / 'images'
DEST.mkdir(parents=True, exist_ok=True)

def download(item):
    slug, image_id, suffix = item
    target = DEST / f"{slug}{suffix}.jpg"
    url = f"{PHOTO}{image_id}?auto=format&fit=crop&w=1400&h=1000&q=78"
    with urlopen(url, timeout=30) as response:
        data = response.read()
    if len(data) < 1000:
        raise RuntimeError(f"Image too small: {slug}")
    target.write_bytes(data)
    return slug+suffix, len(data)

if __name__ == '__main__':
    items = [(s['slug'], s['image'], '') for s in SITES]
    items += [(s['slug'], SECONDARY[s['slug']], '-detail') for s in SITES]
    with ThreadPoolExecutor(max_workers=6) as pool:
        for name, size in pool.map(download, items):
            print(f'{name}: {size // 1024} KB')
