import pyautogui
from pynput import keyboard
from io import BytesIO
from win32 import win32clipboard
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter, ImageOps
from datetime import datetime, timedelta

font = ImageFont.truetype(r'C:\fonts\Impact.ttf', 20)


def minimap_screen():
    image = pyautogui.screenshot(region=(1605,850,290,210))
    send_to_clipboard(image)

def portal_screen():
    mouse_loc = pyautogui.position()
    image = pyautogui.screenshot(region=(mouse_loc[0]-183,mouse_loc[1]-140,367,115))
    time = datetime.utcnow()
    time = time.strftime("%Y-%m-%d %H:%M:%S")
    with image:
        draw=ImageDraw.Draw(image)
        draw.text((5, 90),time,font=font)
        image.save
    image = image.resize((295,92),resample=Image.LANCZOS)
    send_to_clipboard(image)
    

        

def send_to_clipboard(image):
    output = BytesIO()
    image.convert('RGB').save(output, 'BMP')
    data = output.getvalue()[14:]
    output.close()

    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    win32clipboard.CloseClipboard()    


with keyboard.GlobalHotKeys({
        '<alt>+<ctrl>+x': minimap_screen,
        '<alt>+<ctrl>+y': portal_screen}) as h:
    h.join()
