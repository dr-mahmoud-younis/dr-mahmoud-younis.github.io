# Upload instructions — new reel video

## What is in this package

| File | Purpose |
|---|---|
| `reel-diet-moderation.mp4` | Your video (4.8 MB, 1080x1920, 95 s, already remuxed with "faststart" so it streams immediately on the web) |
| `reel-diet-moderation.jpg` | Poster image generated from the opening title scene (1080x1920) |
| `index.html` | Your homepage with the new video card added as the FIRST card in the "فيديوهات Videos" section |

## Option A — Upload via the GitHub website (the way your site has been updated until now)

1. Download the 3 files from the `site-update` folder in this chat.
2. Go to <https://github.com/dr-mahmoud-younis/dr-mahmoud-younis.github.io>
3. Click **Add file → Upload files**.
4. Drag all 3 files into the upload area. GitHub will warn that `index.html` already exists — that is correct, it replaces it with the new version.
5. Click **Commit changes** (message can be anything, e.g. "Add diet reel video").
6. Wait 1–2 minutes for GitHub Pages to rebuild, then open <https://dr-mahmoud-younis.github.io> and scroll to the Videos section — the new reel appears at the top with the title card poster and a 1:35 duration.

## Option B — Push with git from your computer

```bash
git clone https://github.com/dr-mahmoud-younis/dr-mahmoud-younis.github.io.git
cd dr-mahmoud-younis.github.io
# copy the 3 files from the site-update folder into this directory (replacing index.html)
git add index.html reel-diet-moderation.mp4 reel-diet-moderation.jpg
git commit -m "Add diet reel video"
git push
```

## What was changed in index.html

Exactly 3 lines were added, right after the Videos section heading
(`<section id="v"><h2>...فيديوهات...</h2>`) and **before** the existing
"ترتيب الأكل: هل يفرق في سكر الدم؟" card:

- A new `<div class="vid">` card with `<video poster="reel-diet-moderation.jpg" src="reel-diet-moderation.mp4">`
- Bilingual title: **أحسن قاعدة للنظام الغذائي** / **The best diet rule**
- Bilingual description summarising the reel's 9 scenes (moderation + thirds of
  the stomach, natural food, "before the factory" — white sugar / white flour /
  processed meats / fizzy drinks, breakfast the most important meal), ending
  with the same education disclaimer used by your other videos.

No other lines of the page were touched.
