# python-for-myself
Daily use of python scripts
-----
My Instittute provides internet access using some kind of firewall. User have to authenticate to use internet. On Successfuly authenctication "SESSION TAB" is opened. 
SESSION TAB must remain open for active connection also, this tab open only for 2000 seconds.
After 2000 seconds, user must reauthenticate for the same connection.

OVERHEAD!!!
------
To this scenario , i have created simple script that will execute after 1900 seconds and reloads the SESSION TAB . 

I HAVE USED
---
* python2.7
* pyautogui library
* webbrowser library
* ubuntu FIREFOX
