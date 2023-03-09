# pdf-widget
A tkinter window that displays a single PDF file. Made to keep my schedules downloaded as PDFs from Notion on my Desktop to keep me focused...
It isn't helping much :l
 
This is my first tkinter application so it has a very basic UI. Feel free to commit improvements ;;__;; 

Yes, I know tkPDFViewer exists. I couldn't run it, it had internal method name conflicts I did not know how to fix. This script simply converts PDFs to images and then puts them in Label widgets. The Label widgets are in a scrollable Canvas container. 

WARNING!!! 
Do not run or instantiate this script multiple times on Windows. The root.destroy() method is bugged and does not kill the process in Windows systems, making it consume a lot of RAM.
If you have to, make sure to kill python.exe from the Task Manager. You can also convert the script into an executable using pyinstaller. To kill the executable process, just press the Quit button. Do not press the X button on the title bar, it does not completely clear the program from memory.
