# ScriptRunner

Simply, ScriptRunner is a very simple tool i created for Raspberry Pi's. It allows you to collect, select and run python scripts. It does this using a GUI that is entirely navigateable by a touch screen interface only.


All you need to do is to unzip the ScriptRunner archive to a dedicated folder of your choice, and run the ScriptRunner V1.0.py file within. Once started, you will be able to select from the 5 included .py scripts. You will also be able to both install new scripts, and remove them if necessary.


Ultimately, the main purpose of this tool was to organise, run and manage all Python scripts a raspberry pi user will need to run, without having to use a keyboard. I originally designed this as the file copier for copying the index.html file to my webserver folder server in /var/www/ after i had made updates to my website, however i scope-creeped this in the tool you see now. 



The 5 scripts are included are;-   

File Copier - This simply uses a GUI to allow you to select a file, a destination and copy said file there.

File Deleter - Deletes a file of your choice

Symlink Creator - Allows you to select a file, and will then create a symlink of that file on the desktop

System Updater - Basically prompts for the sudo password, then runs a sudo apt-get update and then a sudo apt-get full-upgrade

Dice Roller - This was mainly for Tabletop Game use. allows a user to specify an unlimited number and any sided dice up to 20 sides, roll them, and show the total result (as well as the individual dice roll results). It also has the facility to add a modifier on top of a number between 1-100.
