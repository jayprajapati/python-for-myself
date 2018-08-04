import webbrowser,pyautogui,time

while 1:

	i,j=pyautogui.position() #taking intial coordinate of mouse-pointer

	webbrowser.open_new_tab('http://www.google.com') # open extra-tab

	pyautogui.moveTo(90, 90) #mouse move to first tab
	pyautogui.click() 
	pyautogui.click() #giving control to browser
	pyautogui.press('f5')  #refresh page
	pyautogui.hotkey('ctrl', 'shift','tab') #move to last tab
	pyautogui.hotkey('ctrl', 'w') #close tab
	pyautogui.moveTo(1314, 41) #minimize window
	pyautogui.click() 
	pyautogui.moveTo(i,j) #ser pointer to intial coordianate
	time.sleep(5)
