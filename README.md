# Leo-Ritual

A private daily habit tracker, pre-loaded with a morning wellness routine:
**Exercise**, **Breathing Exercise**, **Twin Heart Meditation**, and **Oil Pulling**.

## The app

Single `index.html` (everything inlined) + `manifest.json` + `sw.js` + two icons.
No build step needed — just open `index.html`, or the live URL once deployed.
All data lives in the browser's `localStorage` — nothing leaves the device.

Features:

- **Today view** — check off each habit for the day, with a running streak per habit
- **Habits** — add, rename, re-icon, archive, or delete habits; fully editable, not
  locked to the 4 starting habits
- **Best-practice guide per habit** — each habit opens to an editable reference page;
  the 4 starting habits come pre-filled with a short best-practice guide (e.g. correct
  oil-pulling technique, a Twin Heart Meditation walkthrough)
- **Streaks & history** — current streak, longest streak, total completions, and a
  per-habit monthly calendar of done/not-done days
- **Calendar** — month grid showing overall completion across all habits, click any
  date to jump to that day
- **Reminder** — in-app + browser notification at a set time, *while the tab is open*
  (this is a static offline app — no server, so there's no push when the tab/browser
  is closed)
- **Export / Import JSON** for backup (localStorage can be cleared by the browser)
- Installable **PWA**, offline via a cache-first service worker

## Rebuilding icons

```
cd build-scripts
python make_icons.py ..
```
