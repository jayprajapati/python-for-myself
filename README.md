# python-for-myself
Daily use of python scripts
-----
My Institute provides internet access with some kind of firewall. So user have to authenticate themselves first to use internet. On Successful authentication "SESSION TAB" is opened. 
SESSION TAB must remain open for an active internet access, but this tab remain open only for 2000 seconds.
After 2000 seconds, user must reauthenticate for the active internet connection.

OVERHEAD!!!
------
To this scenario , I have created simple script that will execute after 1900 seconds and reloads the SESSION TAB . 

I HAVE USED
---
* python2.7
* pyautogui library
* webbrowser library
* ubuntu FIREFOX


# UPDATE

I got another idea for the same problem. I can use the Chrome Extension for the same. 
we can use chrome.tabs api for listing all tab and control specific tab.
