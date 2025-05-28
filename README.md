# mikeydesktoppet
Mike Walters desktop pet :)

Mike sleeps, walks, and goes on his laptop. He cannot interact with your windows or collect any data about what is on your screen. Works on Windows. 

The python code was taken from this tutorial: https://medium.com/analytics-vidhya/create-your-own-desktop-pet-with-python-5b369be18868

Art was made by CIMEJIC and should not be used for anything else. Setup assistance and instructional video by @kubitsss <3

INSTRUCTIONS: 

Download the zip file and extract the files from it OR download all of the gifs and the .py file, then put them in a new folder. (Both options have the same outcome, the second option is just safer because you can see what you download. Don't download random zip files guys)

Type "python" in your terminal to install python from the Microsoft store. In your terminal, then type "pip install pyautogui" to install one of the needed libraries for the deskpet. Find information on pyautogui here: https://pyautogui.readthedocs.io/en/latest/ 

Open the .py file. Edit this section: [impath = 'C:/PATHWAYHERE'] so that it displays the pathway of the folder holding the gifs. You can get this pathway by right clicking on the folder and selecting "copy path(s)". It will copy the slashes like this: C:\ ...\ ... change the backslashes to forward slashes so it looks like this: C:/.../...

If you are using a compiler, execute the code from there. If you are using a basic text editor, open your terminal. Type "python3 [pathway]/mikey_desktop.py". You will have to do this every time you want to make Mikey appear. 

Mikey should appear on your screen! 

If he does not appear, he may be off screen. Try changing this section of the .py file: [window.geometry('150x150+'+str(x)+'+0')] The 0 affects Mikey's Y postion. Change the X position further up in the code where it says [x = 100]. 

Close the terminal to remove Mikey from your screen. 
