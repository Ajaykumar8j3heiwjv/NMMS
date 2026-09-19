# NMMS Tamil Nadu — Bilingual Learning Portal

A mobile-first NMMS preparation portal for Tamil Nadu Class 8 State Board students,
in Tamil and English. No build step, no framework, no backend — open `index.html`
and it runs.

```
LEARN → PRACTICE → TEST → ANALYSE → IMPROVE
```

## Run it

Double-clicking `index.html` works, but a local server is better (some browsers
restrict `localStorage` on `file://`):

```bash
# VS Code: install the "Live Server" extension, right-click index.html → Open with Live Server
# or:
python3 -m http.server 5173
# then open http://localhost:5173
```

## Project layout

```
index.html            page shell, nav, script tags
css/styles.css        all styling, design tokens at the top under :root
js/i18n.js            UI strings — every entry is [Tamil, English]
js/data/bank.js       question bank + flashcards (the file you will edit most)
js/app.js             router, quiz engine, mock test, progress, awareness pages
dist/                 single-file build, for sharing over WhatsApp or hosting as one file
```

## Adding a question

Open `js/data/bank.js` and append to the `BANK` array:

```js
{
  id: 200,                 // must be unique
  c: "Science",            // "MAT" | "Mathematics" | "Science" | "Social Science"
  t: "Light",              // topic — used by filters and the weak-topic report
  y: 2024,                 // exam year, shown in the past-papers tab
  qe: "English question text",
  qt: "தமிழ் வினா",
  oe: ["opt A", "opt B", "opt C", "opt D"],
  ot: ["விடை அ", "விடை ஆ", "விடை இ", "விடை ஈ"],   // optional: omit for numeric options
  a: 2,                    // index of the correct option, 0–3
  ee: "Why this answer is right, in English.",
  et: "ஏன் இந்த விடை சரி என்பதற்கான விளக்கம்."
}
```

Rules the app relies on:

- `oe` must have exactly 4 entries; `a` must be 0–3.
- `ot`, `qt` and `et` fall back to their English counterparts when omitted — fine for
  numbers, not fine for anything a Tamil-medium student has to read.
- Anything in `t` automatically appears in the topic filter, the subject breakdown
  and the weak-topic list. No other file needs touching.

A quick sanity check before committing:

```bash
node -e "const s=require('fs').readFileSync('js/data/bank.js','utf8');eval(s);
BANK.forEach(q=>{if(q.oe.length!==4||q.a<0||q.a>3||!q.qt||!q.et)console.log('check id',q.id)});
console.log(BANK.length+' questions, ids unique:',new Set(BANK.map(q=>q.id)).size===BANK.length)"
```

## Adding UI text

Add a key to `T` in `js/i18n.js` as `key:["தமிழ்","English"]`, then call `t('key')`
in `js/app.js`. For one-off strings use `L('தமிழ்','English')` inline.

## How state is stored

Everything lives in `localStorage` under the key `nmms_tn_v1`: language, theme,
exam date, answer log, mock test history, daily-question answers and the streak.
It never leaves the device. `wipe()` in `js/app.js` clears it.

## Rebuilding the single file in dist/

```bash
python3 build.py
```

Inlines the CSS and the three JS files back into one HTML file.

## Roadmap (deliberately not in version 1)

The original brief listed these — none are built yet, and the MVP works without them:

- Supabase or Firebase backend, student and admin accounts, role-based routes
- Admin CRUD so teachers can add questions without touching this repo
- PDF upload for full past papers and answer keys
- Announcements, leaderboard, parent dashboard, PWA install

If you move to a backend, `BANK` is already shaped like a database table — swap the
array for a fetch and the rest of the app is unchanged.

## Question source

Questions are transcribed from the Tamil Nadu NMMS Class VIII papers (2023, MAT and
SAT). Verify answers against the official key before publishing to students.
Eligibility rules change yearly — confirm with your school headmaster.
# NMMS
