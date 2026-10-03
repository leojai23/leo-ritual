# Leo-Ritual

A private daily habit tracker, pre-loaded with 20 habits across five areas of life:
**Physical**, **Mental**, **Official**, **Personal**, and **Financial**.

## The app

Single `index.html` (everything inlined) + `manifest.json` + `sw.js` + two icons.
No build step needed — just open `index.html`, or the live URL once deployed.
All data lives in the browser's `localStorage` — nothing leaves the device.

Pre-loaded habits (4 per category):

- **Physical** — Exercise / Gym, Oil Pulling & Brushing, Water on Waking, Cold Shower
- **Mental** — Breathing Exercise, Twin Heart Meditation, Gratitude Journaling, Daily Reading
- **Official** — Top-3 Daily Priorities, Deep Work Block, End-of-Day Shutdown, Learn One New Thing
- **Personal** — Consistent Sleep/Wake Time, Screen-Off Wind-Down, Connect with a Loved One, Declutter One Small Space
- **Financial** — Review Portfolio, Finance Tracking, Savings, Read About Investments

Features:

- **Today view** — check off each individual habit, grouped by category, with a
  per-habit streak, a per-category done count + category streak (all habits in that
  category done that day), and chips to show/hide whole categories
- **Habits** — add, rename, re-icon, re-categorize, archive, or delete habits;
  fully editable, not locked to the starting 16
- **Best-practice guide per habit** — each habit opens to an editable reference page;
  every starting habit comes pre-filled with a short best-practice guide and a sample
  where relevant (e.g. correct oil-pulling technique, a Twin Heart Meditation
  walkthrough, a gratitude-journal sample entry)
- **Streaks & history** — current streak, longest streak, total completions, and a
  per-habit monthly calendar of done/not-done days
- **Calendar** — month grid showing overall completion across all habits, click any
  date to jump to that day
- **Review** — 7-day and 30-day completion trends, overall and per category
- **Categories** — Physical / Mental / Official / Personal out of the box, but fully
  editable in Settings: rename, re-icon, reorder, add, or delete (deleting moves its
  habits to another category rather than losing them)
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
