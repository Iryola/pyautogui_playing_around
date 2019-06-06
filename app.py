import pyautogui
pyautogui.PAUSE = 0.45

currentMouseX, currentMouseY = pyautogui.position()
pyautogui.moveTo(614, 753)
pyautogui.click()
pyautogui.moveTo(512, 753)
pyautogui.click()
pyautogui.moveTo(125, 753)
pyautogui.click()
pyautogui.typewrite(['s', 'l', 'a', 'c', 'k', 'enter'], interval=.20)
pyautogui.typewrite('enter')
# print(pyautogui.KEYBOARD_KEYS)
# print(currentMouseX, currentMouseY)