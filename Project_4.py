#Ankit Anand


from random import randint
import tkinter as tk

lst =["def frequency_table(name):", "    result = {}", "    file = open(name, 'r')", "    while True:", "        line = file.readline()", "        if line == '':", "            break", "        words = line.split(' ')", "        for word in words:", "            if word in result:", "                result[word] += 1", "            else:", "                result[word] = 1", "    return result", "def main():", "    name = input('Give a file name : ')", "    freq = frequency_table(name)", "    print(freq)", "    print('number of words :', len(freq))", "if __name__ == '__main__':", "    main()", "import turtle", "DIM = min(turtle.window_width(), turtle.window_height())", "from random import randint", "def random_frequencies(nbr, mxf):", "    result = {}", "    for k in range(nbr):", "        result[str(k)] = randint(1, mxf)", "    return result", "def show_frequencies(freq, tosort=False):", "    from turtle import Turtle", "    from math import pi, cos, sin", "    show = Turtle()", "    show.penup()", "    vals = list(freq.values())", "    if tosort:", "        vals.sort()", "    maxval = max(vals)", "    # print('the maximum value :', maxval)", "    factor = (DIM-40)/(2*maxval)", "    # print('the factor :', factor)", "    lenfreq = len(vals)", "    anginc = 2*pi/lenfreq", "    angle = 0", "    for value in vals:", "        show.goto(0, 0)", "        radius = value*factor", "        endx = radius*cos(angle)", "        endy = radius*sin(angle)", "        # print('radius = ', radius)", "        show.pendown()", "        show.goto(endx, endy)", "        show.pendown()", "        angle = angle + anginc", "    show.penup()", "    show.goto(-DIM/2+5, -DIM/2+5)", "def random_test():", "    nbr = int(input('Give the number of items : '))", "    mxf = int(input('Give the largest value : '))", "    ans = input('Sort the data ? (y/n) ')", "    freq = random_frequencies(nbr, mxf)", "    print(freq)", "    show_frequencies(freq, ans == 'y')", "def main():", "    name = input('Give a file name : ')", "    if name == '':", "        random_test()", "    else:", "        from makefreq import", "frequency_table", "        freq = frequency_table(name)", "        if '' in freq:", "            freq[''] = 0", "        print(freq)", "        show_frequencies(freq, True)", "    input('hit enter to exit')", "main()", "    citupp = place.upper()", "    if verbose:", "        print('opening ' + url + ' ...\n')", "        print('the place :', citupp)", "FCST encountered", "    while True:", "        line = data.readline().decode()", "        if line == '':", "             break","        L = line.split(' ')", "        if 'FCST' in L:", "            line = data.readline().decode()", "            if verbose:print(line + data.readline().decode())", "     else: line = data.readline().decode()" ]
lst = '\n'.join(lst)
file1 = open("project_sample_code.txt","w") #Writing a new file named project_sample_code.txt to store all the wordle words from the list, with one word on every line so 2309 lines

for i in lst: #looping through the list to add all values in the text file

 file1.write(i) #Writing key and values in text file

file1.close()


class GUI: # Defining Class
    def __init__(self):
        self.root = tk.Tk()     # Defining the main window
        self.root.geometry("800x600")# Defining dimensions of main window
        self.root.configure(bg="#000000")# Defining background color of main window
        self.root.title("Fake Code Typist") # Defining the title  of main window
        self.verticalPosition = 25  # Defining Conditions necessary 
        self.drawFirstLine = True
        self.drawNewLine = False
        self.drawEmptyLine = False
        self.previousLine = ""
        self.window = tk.Canvas(self.root,width=800,height=600,bg="#111111", highlightthickness=0)# Defining a canvas for fake code
        self.window.pack()
        self.draw()
        self.root.bind('<KeyRelease>', self.on_key_down)    # Binding the main window with keys
        self.file = open("project_sample_code.txt","r")     # Opening the text file with fake code
        self.fakeCode = self.file.readlines()   # Defining a list for fake code
    def draw(self):
        if self.drawFirstLine:
            # writing the first line on canvas
            self.text = self.window.create_text(0,10,fill="#20c20e",font=("consolas",13))
            self.window.move(self.text,100,0)
            self.drawFirstLine = False
        elif self.drawNewLine: 
            # If the text goes out of window, then creating a new canvas
            if self.verticalPosition > 600 - 20:
                self.verticalPosition = 20
                self.window.delete('all')

            if self.drawEmptyLine:
                # If pressed Enter, blank line is written
                self.newLine = ""
            else:
                self.newLine = self.getNewLine()

            self.text = self.window.create_text(0,self.verticalPosition,fill="#20c20e",font=("consolas",13),text=self.newLine)
            # Writing the new line in canvas
            self.window.move(self.text,len(self.newLine)*5,0)
            self.previousLine = self.newLine
            self.verticalPosition+=20

            self.drawNewLine = False
            if self.drawEmptyLine:
                self.drawEmptyLine = False
        else:
            if self.verticalPosition >= 20:
                self.verticalPosition-=20


    def on_key_down(self,event):
        # Checking for keys pressed and taking actions
        if event.keysym=='Escape':
            self.root.destroy()
        elif event.keysym=='BackSpace':
            self.drawNewLine = False
        elif event.keysym=='Return':
            self.drawNewLine = True
            self.drawEmptyLine = True
        else:
            self.drawNewLine = True
        self.draw()

    def getNewLine(self):   
        # Randomly picking a line from the list   
        possibleLine = self.fakeCode[randint(0, len(self.fakeCode)-1)]
        if possibleLine == self.previousLine:
            return self.getNewLine()
        else:
            return possibleLine   
a = GUI()
tk.mainloop()
