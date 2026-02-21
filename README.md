# 🗓️ Daily Dot Wallpaper (Year Progress)

![Status](https://img.shields.io/badge/Status-Automated-brightgreen?style=for-the-badge&logo=githubactions&logoColor=white) 
![Language](https://img.shields.io/badge/Python-3.14-blue?style=for-the-badge&logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-iOS-lightgrey?style=for-the-badge&logo=apple&logoColor=white)

<p align="center">
  <img src="https://raw.githubusercontent.com/Atharva-tech046/DAILY-DOTS/main/wallpaper.png" width="300" alt="Wallpaper Preview">
  <br>
  <i>"Don't break the chain." A minimalist lockscreen that visually tracks your journey through the year.</i>
</p>

---

## 🚀 How It Works

1. **⚡ The Generator:** A Python script calculates the current day of the year and draws a grid of 365 dots.
2. **☁️ The Hosting:** The fresh `wallpaper.png` is stored in this GitHub repository.
3. **📲 The Sync:** Your iPhone pulls the image from GitHub and updates your Lock Screen automatically using iOS Shortcuts.

---

## 🛠️ Tech Stack

* **Language:** Python 3.14 (using the Pillow library for image processing).
* **Version Control:** Git & GitHub for image hosting.
* **Automation:** iOS Shortcuts & Time-of-Day Automations.

---

## 📲 Setup Instructions for iPhone

Follow these steps to link your device to this repository:

### 1. Get the Direct Image Link
Copy the **Raw** URL of your wallpaper. It should look like this:
`https://raw.githubusercontent.com/Atharva-tech046/DAILY-DOTS/main/wallpaper.png`

### 2. Create the iOS Shortcut
* Open the **Shortcuts** app on your iPhone.
* Create a new shortcut named **"Update Year Dots"**.
* Add Action: **"Get Contents of URL"** and paste your Raw link.
* Add Action: **"Set Wallpaper Photo"**.
  * *Tip: Tap the blue arrow in the action and turn **OFF** "Show Preview" so it updates silently.*

### 3. Automate Daily
* Go to the **Automation** tab in the Shortcuts app.
* Tap **+** and select **Time of Day** (e.g., 00:01 AM).
* Set it to **Run Immediately** (do not choose "Notify when run").
* Select your **"Update Year Dots"** shortcut.

---

## 🎨 Customization

You can personalize the look by editing the constants in `wall.py`:

| Variable | Description | Default Value |
| :--- | :--- | :--- |
| `DOT_COLOR_DONE` | Color for days passed | `(255, 255, 255)` (White) |
| `DOT_COLOR_TODO` | Color for future days | `(44, 44, 46)` (Dark Grey) |
| `SPACING` | Gap between dots | `45` |
| `DOT_SIZE` | Diameter of each dot | `25` |

---

<p align="center">Made with ❤️ for the minimalist aesthetic.</p>
