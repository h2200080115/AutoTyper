# Autotyper - Quick Clipboard to Text Tool

A simple Python tool that automatically types the content from your clipboard at high speed. Perfect for quickly transferring text from your phone to your computer using Phone Link.

## Features
- Auto-types clipboard content at high speed
- Hotkey controls (F8 to start, F7 to stop)
- Works with Phone Link's cross-device clipboard feature
- Types approximately 100 lines of code in 5 seconds

## Prerequisites
1. Python 3.x installed on your computer
2. Phone Link app installed on both:
   - Your Windows PC
   - Your mobile device (Android/iOS)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/autotyper.git
cd autotyper
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Setup Phone Link

1. Install Phone Link on your Windows PC from the Microsoft Store
2. Install Phone Link on your mobile device
3. Open Phone Link on your PC
4. Follow the pairing process to link your phone
5. Go to Settings -> Features
6. Enable "Cross-device copy and paste"

## Usage

1. Run the autotyper script:
```bash
python autotyper.py
```

2. Copy text on your phone (the text will automatically sync to your PC's clipboard via Phone Link)

3. Use the hotkeys:
   - Press `F8` to start auto-typing
   - Press `F7` to stop auto-typing

## Important Notes
- The tool types at maximum speed (no delay between characters)
- Make sure your cursor is in the correct position before starting
- The tool will type whatever is currently in your clipboard
- Works best with Phone Link's cross-device clipboard feature

## Use Case Example
This tool is particularly useful for:
- Quickly transferring code snippets from your phone to your computer
- Fast text entry during exams where you can't open other tabs
- Any situation requiring rapid text input from your phone to PC

## Safety Warning
Please ensure you're following your institution's academic integrity policies when using this tool during exams.

## License
MIT License - Feel free to use and modify as needed. 