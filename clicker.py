import time
import pyautogui
import keyboard

# ---------------------------
# Ustawienia
# ---------------------------

CLICK_AREA = (900, 500)   # współrzędne miejsca kliknięcia, np. "ziarno / moneta / przycisk"
UPGRADE_BUTTONS = [
    (1200, 350),  # upgrade 1
    (1200, 420),  # upgrade 2
    (1200, 490),  # upgrade 3
]

CLICK_INTERVAL = 0.05      # sekund pomiędzy kliknięciami
UPGRADE_INTERVAL = 0.3     # sekund pomiędzy kliknięciami upgrade
AUTO_MODE = True

# ---------------------------
# Funkcje pomocnicze
# ---------------------------

def click_area():
    pyautogui.click(CLICK_AREA[0], CLICK_AREA[1])

def click_upgrade_buttons():
    for x, y in UPGRADE_BUTTONS:
        try:
            pyautogui.click(x, y)
            time.sleep(0.05)
        except Exception:
            pass

def toggle_auto():
    global AUTO_MODE
    AUTO_MODE = not AUTO_MODE
    print("AUTO MODE:", "ON" if AUTO_MODE else "OFF")

# ---------------------------
# Klawisze sterujące
# ---------------------------

keyboard.add_hotkey("f6", toggle_auto)
keyboard.add_hotkey("esc", lambda: exit())

print("Skrypt uruchomiony.")
print("F6 - włącz/wyłącz auto klik")
print("Esc - wyjście")

# Mały odstęp przed startem
time.sleep(2)

# Główna pętla
while True:
    if AUTO_MODE:
        click_area()
        click_upgrade_buttons()
        time.sleep(CLICK_INTERVAL)
