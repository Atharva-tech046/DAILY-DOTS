# 🗓️ Daily Dot Wallpaper (Year Progress)

A minimalist, automated wallpaper generator for iOS that tracks your year progress. Every day, the script calculates the current day of the year and fills in a dot on a 365-dot grid, which is then automatically updated on your iPhone Lock Screen.

## 🚀 How It Works
1. **The Generator (Python):** A script runs (on your laptop or via GitHub Actions) that creates a 1179x2556 PNG image. It draws 365 dots; dots for past/current days are white, and future days are dark grey.
2. **The Hosting (GitHub):** The generated `wallpaper.png` is pushed to this repository.
3. **The Client (iOS Shortcuts):** Your iPhone fetches the "Raw" image from this repo daily and sets it as your wallpaper.

## 🛠️ Tech Stack
* **Language:** Python 3.14
* **Library:** Pillow (PIL) for image generation
* **Version Control:** Git & GitHub
* **Automation:** iOS Shortcuts & Automations

## 📲 Setup Instructions for iOS

Follow these steps to get the wallpaper on your iPhone:

### 1. Get the Image URL
* Navigate to `wallpaper.png` in this repository.
* Click the **Download** icon or the **Raw** button to get the direct image link.
* It should look like: `https://raw.githubusercontent.com/Atharva-tech046/DAILY-DOTS/main/wallpaper.png`

### 2. Create the iOS Shortcut
* Open the **Shortcuts** app on your iPhone.
* Create a new shortcut named **"Update Year Dots"**.
* Add Action: **Get Contents of URL** and paste your Raw GitHub link.
* Add Action: **Set Wallpaper Photo**. 
    * Tap the arrow in the action and turn **OFF** "Show Preview" for a seamless update.

### 3. Automate It
* Go to the **Automation** tab in the Shortcuts app.
* Tap **+** and select **Time of Day** (e.g., 00:01 AM).
* Set it to **Run Immediately**.
* Select your **"Update Year Dots"** shortcut.

## 🎨 Customization
You can modify `wall.py` to change the look:
* **Colors:** Edit `DOT_COLOR_DONE` for a different "completed" color (e.g., Ferrari Red).
* **Layout:** Adjust `COLS` or `SPACING` to change the grid density.
