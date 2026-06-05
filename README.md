# 🗂️ File Organizer — Python Automation

A Python automation tool that instantly sorts a messy folder into organized subfolders by file extension — built using the `os` and `shutil` libraries.

---

## 💡 The Real Scenario

You're an IT administrator. Your manager asks you to find the **employee database file** from a shared folder.

You open the folder and find **100+ mixed files**:

```
photo_1.jpg, movie.avi, script.py, backup.zip, song.mp3,
report.pdf, employees.db, animation.swift, archive.rar ...
```

❌ **Without the organizer** — you scroll through 100+ files trying to spot `employees.db`. Takes minutes. Easy to miss.

✅ **With the organizer** — run the script. Files are sorted instantly:

```
My_Files/
├── Database/
│   └── employees.db   ← found in 1 second
├── Images/
├── Videos/
├── Documents/
├── Code/
└── ...
```

---

## 🚀 How to Use

### Step 1 — Generate the demo folder
Run `Creating_files.py` to instantly create 100+ mixed files including the employee database:
```bash
python Creating_files.py
```

### Step 2 — Your manager asks you to contact the HR recruiter to send them an urgent email. The file is somewhere in this folder as database — find it, open it, and look up Doroteo Arnaiz's email.
Open `My_Files/` — good luck finding it among 100+ files.

### Step 3 — Run the organizer
```bash
python File_organizer.py
```

### Step 4 — Find Doroteo Arnaiz's email now.
Open `My_Files/Database/` — it's right there.

---

## 📁 Supported Categories

| Category | Extensions |
|---|---|
| Images | jpg, jpeg, png, gif, bmp, svg, ico, tif, raw, psd, webp |
| Videos | mp4, avi, mov, mkv, wmv, flv, webm, mpeg, 3gpp |
| Documents | pdf, doc, docx, xls, xlsx, ppt, pptx, txt, csv, rtf |
| Code | py, js, html, css, json, java, cpp, php, ts, jsx, swift, dart |
| Audio | mp3, wav, aac, flac, ogg, m4a, wma, opus, aiff |
| Archives | zip, rar, tar, gz, 7z, bz2, cab |
| Executables | exe, msi, apk, deb, rpm |
| Fonts | ttf, otf, woff, woff2 |
| Database | sqlite, sql, db, mdb |
| Ebooks | epub, mobi, cbr, azw3 |
| Disk Images | iso, img, bin, vmdk |
| Backup | bak, bkp, tmp |
| System | dll, sys, ini, cfg, bat, log, reg, conf |
| Others | anything not listed above |

---

## 🐢 Want to Watch It Happen in Slow Motion?

The code includes two commented lines that add a 0.5s delay between each file move — so you can visually watch each file being organized one by one.

To enable it, uncomment these two lines in `File_organizer.py`:

```python
# import time        ← uncomment this (line 3)
# time.sleep(0.5)    ← uncomment this (inside the loop)
```

---

## 🛠️ Built With

- Python 3
- `os` module — for reading and navigating the file system
- `shutil` module — for moving files between folders

---

## 👤 Author

**Ibrahim Mejjadi** — [linkedin.com/in/ibrahimmejjadi](https://linkedin.com/in/ibrahimmejjadi) · [github.com/ibrahimmejjadi](https://github.com/ibrahimmejjadi)
