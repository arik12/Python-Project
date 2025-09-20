
import pyautogui  # Import pyautogui for automating keyboard/mouse actions
import time        # Import time for adding delays

pyautogui.FAILSAFE = False  # Disable fail-safe (moving mouse to corner won't stop the script)

# Loop 6 times
for i in range(0, 6):
    
    time.sleep(4)          # Wait 4 seconds before starting each iteration
    pyautogui.press('j')   # Simulate pressing the 'j' key
    time.sleep(2)          # Wait 2 seconds
    pyautogui.press('l')   # Simulate pressing the 'l' key
    time.sleep(2)          # Wait 2 seconds
    pyautogui.press('right')  # Simulate pressing the 'right arrow' key
    time.sleep(2)          # Wait 2 seconds
    pyautogui.press('Enter')  # Simulate pressing the 'Enter' key
