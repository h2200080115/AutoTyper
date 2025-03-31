# Autotyper - Quick Clipboard to Text Tool

<div align="center">
  <img src="images/logo.png" alt="Autotyper Logo" width="200"/>
  <p><em>Fast clipboard to text automation tool</em></p>
</div>

A simple Python tool that automatically types the content from your clipboard at high speed. Perfect for quickly transferring text from your phone to your computer using either Phone Link or KDE Connect.

## Features
- ⚡ Auto-types clipboard content at high speed
- ⌨️ Hotkey controls (F8 to start, F7 to stop)
- 🔄 Works with Phone Link's cross-device clipboard feature
- 🔌 Works with KDE Connect's clipboard sync
- ⚡ Types approximately 100 lines of code in 5 seconds

## Prerequisites
1. Python 3.x installed on your computer
2. Either:
   - Phone Link app (Windows + Mobile), or
   - KDE Connect (Linux/Windows + Mobile)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/h2200080115/AutoTyper.git
cd autotyper
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Setup Options

### Option 1: Phone Link Setup
<div align="center">
  <img src="images/phone-link-setup.png" alt="Phone Link Setup" width="600"/>
</div>

1. Install Phone Link on your Windows PC from the Microsoft Store
2. Install Phone Link on your mobile device
3. Open Phone Link on your PC
4. Follow the pairing process to link your phone
5. Go to Settings -> Features
6. Enable "Cross-device copy and paste"

### Option 2: KDE Connect Setup (Alternative)
<div align="center">
  <img src="images/kde-connect-setup.png" alt="KDE Connect Setup" width="600"/>
</div>

1. Install KDE Connect on your computer:
   - Windows: Download from Microsoft Store
   - Linux: `sudo apt install kdeconnect` (Ubuntu/Debian) or equivalent for your distribution
2. Install KDE Connect on your mobile device from:
   - Android: Google Play Store
   - iOS: App Store
3. Open KDE Connect on both devices
4. Pair devices using Bluetooth
5. On both devices, enable "Send clipboard" in the KDE Connect settings

## Usage

<div align="center">
  <img src="images/usage-demo.gif" alt="Usage Demo" width="600"/>
  <p><em>Watch how it works!</em></p>
</div>

1. Run the autotyper script:
```bash
python autotyper.py
```

2. Copy text on your phone (the text will automatically sync to your PC's clipboard via either Phone Link or KDE Connect)

3. Use the hotkeys:
   - Press `F8` to start auto-typing
   - Press `F7` to stop auto-typing

## Important Notes
- ⚡ The tool types at maximum speed (no delay between characters)
- 🎯 Make sure your cursor is in the correct position before starting
- 📋 The tool will type whatever is currently in your clipboard
- 🔄 Works with both Phone Link and KDE Connect clipboard sync
- 📱 For KDE Connect users, ensure Bluetooth is enabled on both devices

## Use Case Example
This tool is particularly useful for:
- 💻 Quickly transferring code snippets from your phone to your computer
- 📝 Fast text entry during exams where you can't open other tabs
- 🔄 Any situation requiring rapid text input from your phone to PC

## Safety Warning
⚠️ Please ensure you're following your institution's academic integrity policies when using this tool during exams.

## License
MIT License - Feel free to use and modify as needed.

---
<div align="center">
  <p>Made with ❤️ for faster typing</p>
</div> 