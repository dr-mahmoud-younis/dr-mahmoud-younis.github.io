# Upload Instructions — Videos Section: Show 3 Videos + "Open All Videos" Button

## What changed

Only **one file** was modified: `index.html`

The videos section (فيديوهات) previously showed all 9 videos at once. Now:

- Only the **first 3 videos** are visible when the page loads
  1. أحسن قاعدة للنظام الغذائي — The best diet rule
  2. ترتيب الأكل: هل يفرق في سكر الدم؟ — Food order
  3. ليه بعض الناس مابتخسّش بحقن التخسيس؟ — Weight-loss injections & genes
- Below them there is a centered button box:
  - Arabic: «عرض جميع الفيديوهات (9)»
  - English: "Open all videos (9)"
- Clicking it reveals all 9 videos, and the button becomes «إظهار أقل» / "Show fewer videos"
- Clicking again collapses back to 3 videos and **automatically pauses** any video that is still playing in the hidden cards (so audio never keeps playing from a hidden video)
- Works in both Arabic and English modes, on desktop and mobile

## How to upload (GitHub web interface)

1. Go to https://github.com/dr-mahmoud-younis/dr-mahmoud-younis.github.io
2. Click **Add file → Upload files**
3. Drag & drop the `index.html` file from this folder
4. Commit message (optional): `Videos section: show 3 videos with "Open all videos" button`
5. Click **Commit changes**

## Verify after upload (wait ~1 minute, then hard-refresh with Ctrl+F5)

- Open https://dr-mahmoud-younis.github.io/
- The videos section shows exactly 3 videos with the button «عرض جميع الفيديوهات (9)» below them
- Click the button: all 9 videos appear; the button becomes «إظهار أقل»
- Switch to English: button reads "Open all videos (9)" → "Show fewer videos"

No other files need to be uploaded. The video files themselves are unchanged.
