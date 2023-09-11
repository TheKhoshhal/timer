from time import *
import os
import webbrowser

f = open('index.html', 'w')

html_template = """
<html>
<head>
    <title>Time Over</title>
    <style>
        body {
            height:100vh;

            display:flex;
            align-items:center;
            justify-content:center;
        }

        h1 {
            font-size: 72px;
            color:red;
        }
    </style>
</head>
<body>
    <h1>Time Is Over</h1>
</body>
</html>
"""

f.write(html_template)
f.close()
filename = 'file:///'+os.getcwd()+'/' + 'index.html'

count = input("[m]inute or [s]econd: ")
count.lower()

timer = int(input("Enter the time: "))

if count == "m":
    timer = timer * 60
    while timer > 0:    
        mins, secs = divmod(timer, 60)
        clock = "{:02d}:{:02d}".format(mins, secs)
        print(clock, end="\r")
        sleep(1)
        timer -= 1

    if timer == 0:
        print("time is over")
        webbrowser.open_new_tab(filename)
elif count == "s":
    while timer > 0:    
        mins, secs = divmod(timer, 60)
        clock = "{:02d}:{:02d}".format(mins, secs)
        print(clock, end="\r")
        sleep(1)
        timer -= 1

    if timer == 0:
        print("time is over")
        webbrowser.open_new_tab(filename)
else: 
    print("Error")
