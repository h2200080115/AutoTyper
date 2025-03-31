import keyboard
import pyperclip
import threading
import time

stop_typing = False
typing_thread = None

def type_clipboard_text():
    global stop_typing
    text = pyperclip.paste()
    if text and not stop_typing:
        start_time = time.time()  # Measure start time
        keyboard.write(text, delay=0)  # Set delay to 0 for maximum speed
        elapsed_time = time.time() - start_time
        print(f"Typed {len(text)} characters in {elapsed_time:.3f} seconds "
              f"({len(text)/elapsed_time:.1f} chars/sec)")

def start_typing():
    global stop_typing, typing_thread
    if typing_thread is None or not typing_thread.is_alive():
        stop_typing = False
        typing_thread = threading.Thread(target=type_clipboard_text)
        typing_thread.start()

def stop_typing_func():
    global stop_typing
    stop_typing = True

keyboard.add_hotkey("F8", start_typing)
keyboard.add_hotkey("F7", stop_typing_func)

keyboard.wait()