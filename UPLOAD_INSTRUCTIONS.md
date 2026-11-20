# Upload instructions — rumination syndrome article

## What is in this package

| File | Purpose |
|---|---|
| `rumination-syndrome-when-food-comes-back-without-vomiting.html` | The NEW bilingual article page (Arabic default + English toggle, site template, JSON-LD, booking CTA, "more articles" links) |
| `index.html` | Homepage — a new entry added FIRST in the articles data (it becomes the top card of the "مقالات طبية Medical articles" section, and opens in the popup with the full article text) |
| `articles.html` | Articles index — the new article added as the first item in the list |
| `sitemap.xml` | New article URL added + lastmod dates for the homepage and articles index bumped to 2026-11-20 |

Upload **all four files together** so the links stay consistent.

## Option A — Upload via the GitHub website (the way the site has been updated until now)

1. Download the 4 files from this chat (`article-site-update` folder, or the single zip).
2. Go to <https://github.com/dr-mahmoud-younis/dr-mahmoud-younis.github.io>
3. Click **Add file → Upload files**.
4. Drag all 4 files in. GitHub will say 3 of them already exist and will be replaced — that is correct.
5. Click **Commit changes** (message can be anything, e.g. "Add rumination syndrome article").
6. Wait 1–2 minutes for GitHub Pages to rebuild, then check:
   - <https://dr-mahmoud-younis.github.io/rumination-syndrome-when-food-comes-back-without-vomiting.html>
   - The homepage articles section (new card at the top)
   - <https://dr-mahmoud-younis.github.io/articles.html> (new first item)

## Option B — Push with git from your computer

```bash
git clone https://github.com/dr-mahmoud-younis/dr-mahmoud-younis.github.io.git
cd dr-mahmoud-younis.github.io
# copy the 4 files from the article-site-update folder into this directory (replacing the 3 existing ones)
git add rumination-syndrome-when-food-comes-back-without-vomiting.html index.html articles.html sitemap.xml
git commit -m "Add rumination syndrome article"
git push
```

## Article details

- **Arabic title:** متلازمة الاجترار: حين يعود الطعام إلى الفم من دون قيء
- **English title:** Rumination syndrome: when food comes back without vomiting
- **Length:** ~1,520 Arabic words + ~1,650 English words (10 sections each, incl. FAQ)
- **Angle:** general patient education + a dedicated section on rumination with diabetes, diabetic gastroparesis, GLP-1 (semaglutide-type) injections and post-bariatric surgery
- **Sections (both languages):** what it looks like / how it differs from vomiting, GERD, gastroparesis, achalasia, bulimia / the mechanism (learned abdominal-wall reflex) / who gets it / complications (dental erosion, weight loss, oesophagitis, social impact) / diagnosis + Rome IV criteria / treatment — diaphragmatic breathing step-by-step, habit reversal, baclofen, infant care / diabetes & weight-loss overlap / red flags / FAQ / summary + disclaimer
- **Facts checked against:** Rome Foundation Rome IV criteria, Murray et al. 2019 critical review (Am J Gastroenterol), Halland 2018 and Sasegbon 2022 reviews, Johns Hopkins patient page, StatPearls rumination disorder
- **Filename note:** the filename is the automatic slug of the English title (same rule the homepage popup uses to build the "Open as standalone page" link), so the homepage button links correctly
