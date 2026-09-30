# Graph Report - business-landing-pages  (2026-09-30)

## Corpus Check
- 30 files · ~760,644 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 97 nodes · 95 edges · 32 communities (9 shown, 8 thin omitted)
- Extraction: 97% EXTRACTED · 3% INFERRED · 0% AMBIGUOUS · INFERRED: 3 edges (avg confidence: 0.85)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `86738769`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- build.py
- Business Landing Page Showcase
- showcase.js
- esc
- site.js
- Links
- link
- main
- school/script.js
- solar-energy/script.js
- download_images.py
- aesthetic-clinic/script.js
- auto-detailing/script.js
- construction/script.js
- petshop/script.js
- photographer/script.js
- restaurant/script.js

## God Nodes (most connected - your core abstractions)
1. `esc()` - 12 edges
2. `Business Landing Page Showcase` - 8 edges
3. `main()` - 6 edges
4. `img()` - 5 edges
5. `link()` - 4 edges
6. `page_html()` - 4 edges
7. `Links` - 4 edges
8. `section_gallery()` - 3 edges
9. `section_contact()` - 3 edges
10. `page_css()` - 3 edges

## Surprising Connections (you probably didn't know these)
- `page_html()` --calls--> `esc()`  [EXTRACTED]
  build.py → build.py  _Bridges community 3 → community 6_
- `section_gallery()` --calls--> `esc()`  [EXTRACTED]
  build.py → build.py  _Bridges community 3 → community 0_
- `showcase()` --calls--> `esc()`  [EXTRACTED]
  build.py → build.py  _Bridges community 3 → community 7_
- `main()` --calls--> `page_html()`  [EXTRACTED]
  build.py → build.py  _Bridges community 6 → community 7_
- `main()` --calls--> `page_css()`  [EXTRACTED]
  build.py → build.py  _Bridges community 0 → community 7_

## Import Cycles
- None detected.

## Communities (32 total, 8 thin omitted)

### Community 0 - "build.py"
Cohesion: 0.33
Nodes (6): img(), page_css(), Generate the standalone demo pages from editorial content below. Run `python…, section_comparison(), section_gallery(), section_instagram()

### Community 1 - "Business Landing Page Showcase"
Cohesion: 0.22
Nodes (8): Business Landing Page Showcase, Como executar, Créditos e licença, Estrutura, Objetivo, Projetos, Screenshots, Tecnologias

### Community 2 - "showcase.js"
Cohesion: 0.29
Nodes (7): buttons, cards, count, empty, filterProjects(), normalize(), search

### Community 3 - "esc"
Cohesion: 0.25
Nodes (8): esc(), section_about(), section_detail(), section_faq(), section_floorplans(), section_process(), section_review(), section_services()

### Community 4 - "site.js"
Cohesion: 0.29
Nodes (5): labels, menuButton, revealElements, siteNav, today

### Community 5 - "Links"
Cohesion: 0.33
Nodes (3): Links, Quick static checks for the generated GitHub Pages site., HTMLParser

### Community 6 - "link"
Cohesion: 0.50
Nodes (4): link(), page_html(), section_contact(), wa()

### Community 7 - "main"
Cohesion: 0.50
Nodes (4): main(), page_js(), readme(), showcase()

### Community 9 - "solar-energy/script.js"
Cohesion: 0.67
Nodes (3): bill, formatBRL(), simulate()

## Knowledge Gaps
- **30 isolated node(s):** `buttons`, `search`, `cards`, `count`, `empty` (+25 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 59 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **8 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `esc()` connect `esc` to `build.py`, `link`, `main`?**
  _High betweenness centrality (0.006) - this node is a cross-community bridge._
- **What connects `buttons`, `search`, `cards` to the rest of the system?**
  _30 weakly-connected nodes found - possible documentation gaps or missing edges._