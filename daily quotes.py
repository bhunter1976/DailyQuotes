# Daily Quotes is a simple text output program that outputs a random motivational quote.
# © Brock M Hunter dba Utech Software

# Freeware Version
# Version: 1.0
# Version Date: 07/11/2018

# Notes:
# added more content
# implemented more OOP
# Changed license to freeware

# Bugs or Other Issues:
# None identified

# Future Implementation Goals and Ideas:
# To-Do:
# Figure out how to make the packaged license read only.
# create loading splash screen
# Find other ways to make the code more efficient (maybe reuseable functions)

# Maybe: 
# add a custom user-defined list of quotes option
# Include a read-me file
# add a simple help system to explain how to use the program (Possibly Online)
# add text to speech support



# import pre-installed modules to facilitate various functions
import sys
import os
import configparser
import random

# import tkinter module to facilitate GUI
import tkinter as tk
from tkinter import Frame
from tkinter import Label
from tkinter import Button
from tkinter import Text
from tkinter import Grid
from tkinter import Menu
from tkinter import Toplevel
from tkinter import messagebox
from tkinter import font
from tkinter import Message
from tkinter import Checkbutton
from tkinter import BooleanVar
from tkinter import scrolledtext

# load preferences file
config = configparser.ConfigParser()
config.read('config.ini')

# create initial dictionary of quotes
quotes = {}
try:
    if config.getboolean('categories', 'adversity') == True:
        with open('adversity.py', 'r', encoding = 'UTF8') as file:
            quotes['adversity'] = file.readlines()
    else:
        pass

    if config.getboolean('categories', 'athletic') == True:
        with open('athletic.py', 'r', encoding = 'UTF8') as file:
            quotes['athletic'] = file.readlines()
    else:
        pass
    
    if config.getboolean('categories', 'business') == True:
        with open('business.py', 'r', encoding = 'UTF8') as file:
            quotes['business'] = file.readlines()
    else:
        pass

    if config.getboolean('categories', 'career') == True:
        with open('career.py', 'r', encoding = 'UTF8') as file:
            quotes['career'] = file.readlines()
    else:
        pass

    if config.getboolean('categories', 'christian') == True:
        with open('christian.py', 'r', encoding = 'UTF8') as file:
            quotes['christian'] = file.readlines()
    else:
        pass

    if config.getboolean('categories', 'confidence') == True:
        with open('confidence.py', 'r', encoding = 'UTF8') as file:
            quotes['confidence'] = file.readlines()
    else:
        pass

    if config.getboolean('categories', 'depression') == True:
        with open('depression.py', 'r', encoding = 'UTF8') as file:
            quotes['depression'] = file.readlines()
    else:
        pass
    
    if config.getboolean('categories', 'education') == True:
        with open('education.py', 'r', encoding = 'UTF8') as file:
            quotes['education'] = file.readlines()
    else:
        pass

    if config.getboolean('categories', 'goals') == True:
        with open('goals.py', 'r', encoding = 'UTF8') as file:
            quotes['goals'] = file.readlines()
    else:
        pass

    if config.getboolean('categories', 'health') == True:
        with open('health.py', 'r', encoding = 'UTF8') as file:
            quotes['health'] = file.readlines()
    else:
        pass

    if config.getboolean('categories', 'inspiration') == True:
        with open('inspiration.py', 'r', encoding = 'UTF8') as file:
            quotes['inspiration'] = file.readlines()
    else:
        pass

    if config.getboolean('categories', 'love') == True:
        with open('love.py', 'r', encoding = 'UTF8') as file:
            quotes['love'] = file.readlines()
    else:
        pass

    if config.getboolean('categories', 'money') == True:
        with open('money.py', 'r', encoding = 'UTF8') as file:
            quotes['money'] = file.readlines()
    else:
        pass

    if config.getboolean('categories', 'women') == True:
        with open('women.py', 'r', encoding = 'UTF8') as file:
            quotes['women'] = file.readlines()
    else:
        pass

    if quotes == {}:
        with open('default.py', 'r', encoding = 'UTF8') as file:
            quotes['default'] = file.readlines()
    else:
        pass

except:
    with open('default.py', 'r', encoding = 'UTF8') as file:
        quotes['default'] = file.readlines()

# Begin testing code block
#print('Adversity=', config.getboolean('categories','adversity'))
#print('Athletic=', config.getboolean('categories','athletic'))
#print('Business=', config.getboolean('categories','business'))
#print('Career=', config.getboolean('categories','career'))
#print('Christian=', config.getboolean('categories','christian'))
#print('Confidence=', config.getboolean('categories','confidence'))
#print('Depression=', config.getboolean('categories','depression'))
#print('Education=', config.getboolean('categories','education'))
#print('Goals=', config.getboolean('categories','goals'))
#print('Health=', config.getboolean('categories','health'))
#print('Inspiration=', config.getboolean('categories','inspiration'))
#print('Love=', config.getboolean('categories','love'))
#print('Money=', config.getboolean('categories','money'))
#print('Women=', config.getboolean('categories','women'))
#print('Default=', config.getboolean('categories','default'),'\n')
#print('Dictionary Keys:')
#for key in quotes:
#    print(key)
#print('\n')
# End testing code block

# define random_quote variable that displays initial quote on startup
random_quote = random.choice(list(quotes.values()))

# create the GUI and widgets
class Application(Frame):

    # Constructor
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    # Create widgets
    def create_widgets(self):
        # Initial window label
        # self.label = Label(self, text = "FREEWARE VERSION")
        # self.label.grid(row = 0, column = 0, columnspan = 2, sticky = 'W')

        # menu bar functions
        # About menu dialogue box
        def showAbout():
            messagebox.showinfo(message='Daily Quotes Freeware v1.0\n\n© 2018 UTech Software.\n\nAll Rights Reserved as Indicated in the EULA (license.txt)')

        # License menu show license option
        def showLicense():
            os.startfile('license.txt', 'open')

        # create menu bar
        menu = Menu(self.master)
        self.master.config(menu=menu)
        filemenu = Menu(menu, tearoff=0)
        filemenu.add_command(label="Preferences", command=Preferences)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=sys.exit)
        menu.add_cascade(label="File", menu=filemenu)

        helpmenu = Menu(menu, tearoff=0)
        helpmenu.add_command(label="About", command=showAbout)
        helpmenu.add_command(label="View License", command=showLicense)
        menu.add_cascade(label="About", menu=helpmenu)

        # Button 1 to trigger the display_quote function to display another quote
        self.button1 = Button(self, text = 'Refresh', width = 6, height = 2)
        self.button1["command"] = self.display_quote
        self.button1.grid(row = 50, columnspan=5)

        # Text box widget to display quotes
        self.text = Text(self, width = 49, height = 8, wrap = tk.WORD)
        self.text.config(state='normal', font = 'Arial 12 bold')
        self.text.insert(0.0, (random.choice(random_quote)))
        self.text.config(state='disabled')
        self.text.grid(row = 1, column = 0, columnspan = 2, sticky = 'N', padx = 10, pady = 10)

    # select random list from current dictionary values then update and return random_quote string from selected random list
    def update_quote(self):
        global random_quote
        random_list = random.choice(list(quotes.values()))
        random_quote = random.choice(list(random_list))
        return random_quote

    # call random_quote function then output random quote string to text widget with new quote
    def display_quote(self):
        self.update_quote()
        self.text.config(state='normal')
        self.text.delete(0.0, tk.END)
        self.text.insert(0.0, random_quote)
        self.text.config(state='disabled')

# preferences new window
class Preferences(Toplevel):
    # Initialize the window
    def __init__(self):
        Toplevel.__init__(self)
        self.title("PREFERENCES")
        self.geometry('310x240+550+250')
        self.resizable(False, False)
        self.label = Label(self, text = "SELECT YOUR DESIRED CATEGORIES:", font = 'Arial 10 bold')
        self.label.grid(row = 0, column = 0, columnspan = 2, sticky = 'N')
        self.grid()
        self.widgets()
        self.focus_set()

    # Preferences Widgets
    def widgets(self):
        # Button to close and save preferences window
        self.button1 = Button(self, text = 'Save', command = self.save_prefs, width = 6, height = 2)
        self.button1.grid(row = 8, columnspan=2)

        # Adversity check button to call update_adversity function and add/remove adversity category quotes to/from the dictionary
        self.adversity = BooleanVar()
        self.adv = Checkbutton(self, text = 'Adversity/Hardship', variable = self.adversity, command = self.update_adversity)
        self.adv.grid(row = 1, column = 0, sticky = 'W', padx = 0, pady = 0)
        if 'adversity' in quotes:
            self.adversity.set(1)
        elif 'adversity' not in quotes:
            self.adversity.set(0)

        # Athletic check button to call update_athletic function and add/remove athletic category quotes to/from the dictionary
        self.athletic = BooleanVar()
        self.athlete = Checkbutton(self, text = 'Athletic/Sports', variable = self.athletic, command = self.update_athletic)
        self.athlete.grid(row = 1, column = 1, sticky = 'W', padx = 0, pady = 0)
        if 'athletic' in quotes:
            self.athletic.set(1)
        elif 'athletic' not in quotes:
            self.athletic.set(0)
            
        # Business check button to call update_business function and add/remove business category quotes to/from the dictionary
        self.business = BooleanVar()
        self.biz = Checkbutton(self, text = 'Business/Entrepreneurship', variable = self.business, command = self.update_business)
        self.biz.grid(row = 2, column = 0, sticky = 'W', padx = 0, pady = 0)
        if 'business' in quotes:
            self.business.set(1)
        elif 'business' not in quotes:
            self.business.set(0)

        # Career check button to call update_career function and add/remove career category quotes to/from the dictionary
        self.career = BooleanVar()
        self.careers = Checkbutton(self, text = 'Career/Work', variable = self.career, command = self.update_career)
        self.careers.grid(row = 2, column = 1, sticky = 'W', padx = 0, pady = 0)
        if 'career' in quotes:
            self.career.set(1)
        elif 'career' not in quotes:
            self.career.set(0)

        # Christian check button to call update_christian function and add/remove christian category quotes to/from the dictionary
        self.christian = BooleanVar()
        self.christians = Checkbutton(self, text = 'Christian/Bible', variable = self.christian, command = self.update_christian)
        self.christians.grid(row = 3, column = 0, sticky = 'W', padx = 0, pady = 0)
        if 'christian' in quotes:
            self.christian.set(1)
        elif 'christian' not in quotes:
            self.christian.set(0)

        # Confidence check button to call update_confidence function and add/remove confidence category quotes to/from the dictionary
        self.confidence = BooleanVar()
        self.conf = Checkbutton(self, text = 'Confidence/Fears', variable = self.confidence, command = self.update_confidence)
        self.conf.grid(row = 3, column = 1, sticky = 'W', padx = 0, pady = 0)
        if 'confidence' in quotes:
            self.confidence.set(1)
        elif 'confidence' not in quotes:
            self.confidence.set(0)

        # Depression/Sadness check button to call update_depression function and add/remove depression category quotes to/from the dictionary
        self.depression = BooleanVar()
        self.depressed = Checkbutton(self, text = 'Depression/Sadness', variable = self.depression, command = self.update_depression)
        self.depressed.grid(row = 4, column = 0, sticky = 'W', padx = 0, pady = 0)
        if 'depression' in quotes:
            self.depression.set(1)
        elif 'depression' not in quotes:
            self.depression.set(0)

        # Education check button to call update_education function and add/remove education category quotes to/from the dictionary
        self.education = BooleanVar()
        self.ed = Checkbutton(self, text = 'Education/Student', variable = self.education, command = self.update_education)
        self.ed.grid(row = 4, column = 1, sticky = 'W', padx = 0, pady = 0)
        if 'education' in quotes:
            self.education.set(1)
        elif 'education' not in quotes:
            self.education.set(0)

        # Goals/Dreams check button to call update_goals function and add/remove goals category quotes to/from the dictionary
        self.goals = BooleanVar()
        self.goal = Checkbutton(self, text = 'Goals/Dreams', variable = self.goals, command = self.update_goals)
        self.goal.grid(row = 5, column = 0, sticky = 'W', padx = 0, pady = 0)
        if 'goals' in quotes:
            self.goals.set(1)
        elif 'goals' not in quotes:
            self.goals.set(0)

        # Health check button to call update_health function and add/remove health category quotes to/from the dictionary
        self.health = BooleanVar()
        self.heal = Checkbutton(self, text = 'Health/Fitness', variable = self.health, command = self.update_health)
        self.heal.grid(row = 5, column = 1, sticky = 'W', padx = 0, pady = 0)
        if 'health' in quotes:
            self.health.set(1)
        elif 'health' not in quotes:
            self.health.set(0)

        # Inspiration check button to call update_inspiration function and add/remove inspiration category quotes to/from the dictionary
        self.inspiration = BooleanVar()
        self.inspire = Checkbutton(self, text = 'Inspiration/Motivation', variable = self.inspiration, command = self.update_inspiration)
        self.inspire.grid(row = 6, column = 0, sticky = 'W', padx = 0, pady = 0)
        if 'inspiration' in quotes:
            self.inspiration.set(1)
        elif 'inspiration' not in quotes:
            self.inspiration.set(0)

        # Love check button to call update_love function and add/remove love category quotes to/from the dictionary
        self.love = BooleanVar()
        self.loves = Checkbutton(self, text = 'Love/Relationships', variable = self.love, command = self.update_love)
        self.loves.grid(row = 6, column = 1, sticky = 'W', padx = 0, pady = 0)
        if 'love' in quotes:
            self.love.set(1)
        elif 'love' not in quotes:
            self.love.set(0)

        # Money check button to call update_money function and add/remove money category quotes to/from the dictionary
        self.money = BooleanVar()
        self.monies = Checkbutton(self, text = 'Money/Finance', variable = self.money, command = self.update_money)
        self.monies.grid(row = 7, column = 0, sticky = 'W', padx = 0, pady = 0)
        if 'money' in quotes:
            self.money.set(1)
        elif 'money' not in quotes:
            self.money.set(0)

        # Women check button to call update_women function and add/remove women category quotes to/from the dictionary
        self.women = BooleanVar()
        self.woman = Checkbutton(self, text = 'For Women', variable = self.women, command = self.update_women)
        self.woman.grid(row = 7, column = 1, sticky = 'W', padx = 0, pady = 0)
        if 'women' in quotes:
            self.women.set(1)
        elif 'women' not in quotes:
            self.women.set(0)

    # Writes config settings to file and closes window
    def save_prefs(self):
        with open('config.ini', 'w') as f:
            config.write(f)
        self.destroy()

        # Begin testing code block
#        print('Adversity=', config.getboolean('categories','adversity'))
#        print('Athletic=', config.getboolean('categories','athletic'))
#        print('Business=', config.getboolean('categories','business'))
#        print('Career=', config.getboolean('categories','career'))
#        print('Christian=', config.getboolean('categories','christian'))
#        print('Confidence=', config.getboolean('categories','confidence'))
#        print('Depression=', config.getboolean('categories','depression'))
#        print('Education=', config.getboolean('categories','education'))
#        print('Goals=', config.getboolean('categories','goals'))
#        print('Health=', config.getboolean('categories','health'))
#        print('Inspiration=', config.getboolean('categories','inspiration'))
#        print('Love=', config.getboolean('categories','love'))
#        print('Money=', config.getboolean('categories','money'))
#        print('Women=', config.getboolean('categories','women'))
#        print('Default=', config.getboolean('categories','default'),'\n')
#        print('Dictionary Keys:')
#        for key in quotes:
#            print(key)
#        print('\n')
        # End testing code block

    # add/remove adversity list in dictionary based on checkbutton value
    def update_adversity(self):
        if self.adversity.get() == True:
            config.set('categories', 'adversity', 'True') # updates config file
            with open('adversity.py', 'r', encoding = 'UTF8') as f:
                new_quotes_added = f.readlines()
                quotes['adversity'] = new_quotes_added
                try:
                    del quotes['default']
                    config.set('categories', 'default', 'False') # updates config file
                    return quotes
                except:
                    return quotes
        elif self.adversity.get() == False:
            config.set('categories', 'adversity', 'False') # updates config file
            try:
                del quotes['adversity']
                if quotes == {}:
                    with open('default.py', 'r', encoding = 'UTF8') as f:
                        quotes['default'] = f.readlines()
                        config.set('categories', 'default', 'True') # updates config file
                    return quotes
                else:
                    return quotes
            except:
                return quotes
            
        # add/remove athletic list in dictionary based on checkbutton value
    def update_athletic(self):
        if self.athletic.get() == True:
            config.set('categories', 'athletic', 'True') # updates config file
            with open('athletic.py', 'r', encoding = 'UTF8') as f:
                new_quotes_added = f.readlines()
                quotes['athletic'] = new_quotes_added
                try:
                    del quotes['default']
                    config.set('categories', 'default', 'False') # updates config file
                    return quotes
                except:
                    return quotes
        elif self.athletic.get() == False:
            config.set('categories', 'athletic', 'False') # updates config file
            try:
                del quotes['athletic']
                if quotes == {}:
                    with open('default.py', 'r', encoding = 'UTF8') as f:
                        quotes['default'] = f.readlines()
                        config.set('categories', 'default', 'True') # updates config file
                    return quotes
                else:
                    return quotes
            except:
                return quotes
            
    # add/remove business list in dictionary based on checkbutton value
    def update_business(self):
        if self.business.get() == True:
            config.set('categories', 'business', 'True') # updates config file
            with open('business.py', 'r', encoding = 'UTF8') as f:
                new_quotes_added = f.readlines()
                quotes['business'] = new_quotes_added
                try:
                    del quotes['default']
                    config.set('categories', 'default', 'False') # updates config file
                    return quotes
                except:
                    return quotes
        elif self.business.get() == False:
            config.set('categories', 'business', 'False') # updates config file
            try:
                del quotes['business']
                if quotes == {}:
                    with open('default.py', 'r', encoding = 'UTF8') as f:
                        quotes['default'] = f.readlines()
                        config.set('categories', 'default', 'True') # updates config file
                    return quotes
                else:
                    return quotes
            except:
                return quotes

    # add/remove career list in dictionary based on checkbutton value
    def update_career(self):
        if self.career.get() == True:
            config.set('categories', 'career', 'True') # updates config file
            with open('career.py', 'r', encoding = 'UTF8') as f:
                new_quotes_added = f.readlines()
                quotes['career'] = new_quotes_added
                try:
                    del quotes['default']
                    config.set('categories', 'default', 'False') # updates config file
                    return quotes
                except:
                    return quotes
        elif self.career.get() == False:
            config.set('categories', 'career', 'False') # updates config file
            try:
                del quotes['career']
                if quotes == {}:
                    with open('default.py', 'r', encoding = 'UTF8') as f:
                        quotes['default'] = f.readlines()
                        config.set('categories', 'default', 'True') # updates config file
                    return quotes
                else:
                    return quotes
            except:
                return quotes

        # add/remove christian list in dictionary based on checkbutton value
    def update_christian(self):
        if self.christian.get() == True:
            config.set('categories', 'christian', 'True') # updates config file
            with open('christian.py', 'r', encoding = 'UTF8') as f:
                new_quotes_added = f.readlines()
                quotes['christian'] = new_quotes_added
                try:
                    del quotes['default']
                    config.set('categories', 'default', 'False') # updates config file
                    return quotes
                except:
                    return quotes
        elif self.christian.get() == False:
            config.set('categories', 'christian', 'False') # updates config file
            try:
                del quotes['christian']
                if quotes == {}:
                    with open('default.py', 'r', encoding = 'UTF8') as f:
                        quotes['default'] = f.readlines()
                        config.set('categories', 'default', 'True') # updates config file
                    return quotes
                else:
                    return quotes
            except:
                return quotes

    # add/remove confidence list in dictionary based on checkbutton value
    def update_confidence(self):
        if self.confidence.get() == True:
            config.set('categories', 'confidence', 'True') # updates config file
            with open('confidence.py', 'r', encoding = 'UTF8') as f:
                new_quotes_added = f.readlines()
                quotes['confidence'] = new_quotes_added
                try:
                    del quotes['default']
                    config.set('categories', 'default', 'False') # updates config file
                    return quotes
                except:
                    return quotes
        elif self.confidence.get() == False:
            config.set('categories', 'confidence', 'False') # updates config file
            try:
                del quotes['confidence']
                if quotes == {}:
                    with open('default.py', 'r', encoding = 'UTF8') as f:
                        quotes['default'] = f.readlines()
                        config.set('categories', 'default', 'True') # updates config file
                    return quotes
                else:
                    return quotes
            except:
                return quotes

    # add/remove depression list in dictionary based on checkbutton value
    def update_depression(self):
        if self.depression.get() == True:
            config.set('categories', 'depression', 'True') # updates config file
            with open('depression.py', 'r', encoding = 'UTF8') as f:
                new_quotes_added = f.readlines()
                quotes['depression'] = new_quotes_added
                try:
                    del quotes['default']
                    config.set('categories', 'default', 'False') # updates config file
                    return quotes
                except:
                    return quotes
        elif self.depression.get() == False:
            config.set('categories', 'depression', 'False') # updates config file
            try:
                del quotes['depression']
                if quotes == {}:
                    with open('default.py', 'r', encoding = 'UTF8') as f:
                        quotes['default'] = f.readlines()
                        config.set('categories', 'default', 'True') # updates config file
                    return quotes
                else:
                    return quotes
            except:
                return quotes

    # add/remove education list in dictionary based on checkbutton value
    def update_education(self):
        if self.education.get() == True:
            config.set('categories', 'education', 'True') # updates config file
            with open('education.py', 'r', encoding = 'UTF8') as f:
                new_quotes_added = f.readlines()
                quotes['education'] = new_quotes_added
                try:
                    del quotes['default']
                    config.set('categories', 'default', 'False') # updates config file
                    return quotes
                except:
                    return quotes
        elif self.education.get() == False:
            config.set('categories', 'education', 'False') # updates config file
            try:
                del quotes['education']
                if quotes == {}:
                    with open('default.py', 'r', encoding = 'UTF8') as f:
                        quotes['default'] = f.readlines()
                        config.set('categories', 'default', 'True') # updates config file
                    return quotes
                else:
                    return quotes
            except:
                return quotes

    # add/remove goals list in dictionary based on checkbutton value
    def update_goals(self):
        if self.goals.get() == True:
            config.set('categories', 'goals', 'True') # updates config file
            with open('goals.py', 'r', encoding = 'UTF8') as f:
                new_quotes_added = f.readlines()
                quotes['goals'] = new_quotes_added
                try:
                    del quotes['default']
                    config.set('categories', 'default', 'False') # updates config file
                    return quotes
                except:
                    return quotes
        elif self.goals.get() == False:
            config.set('categories', 'goals', 'False') # updates config file
            try:
                del quotes['goals']
                if quotes == {}:
                    with open('default.py', 'r', encoding = 'UTF8') as f:
                        quotes['default'] = f.readlines()
                        config.set('categories', 'default', 'True') # updates config file
                    return quotes
                else:
                    return quotes
            except:
                return quotes

    # add/remove health list in dictionary based on checkbutton value
    def update_health(self):
        if self.health.get() == True:
            config.set('categories', 'health', 'True') # updates config file
            with open('health.py', 'r', encoding = 'UTF8') as f:
                new_quotes_added = f.readlines()
                quotes['health'] = new_quotes_added
                try:
                    del quotes['default']
                    config.set('categories', 'default', 'False') # updates config file
                    return quotes
                except:
                    return quotes
        elif self.health.get() == False:
            config.set('categories', 'health', 'False') # updates config file
            try:
                del quotes['health']
                if quotes == {}:
                    with open('default.py', 'r', encoding = 'UTF8') as f:
                        quotes['default'] = f.readlines()
                        config.set('categories', 'default', 'True') # updates config file
                    return quotes
                else:
                    return quotes
            except:
                return quotes

    # add/remove inspiration list in dictionary based on checkbutton value
    def update_inspiration(self):
        if self.inspiration.get() == True:
            config.set('categories', 'inspiration', 'True') # updates config file
            with open('inspiration.py', 'r', encoding = 'UTF8') as f:
                new_quotes_added = f.readlines()
                quotes['inspiration'] = new_quotes_added
                try:
                    del quotes['default']
                    config.set('categories', 'default', 'False') # updates config file
                    return quotes
                except:
                    return quotes
        elif self.inspiration.get() == False:
            config.set('categories', 'inspiration', 'False') # updates config file
            try:
                del quotes['inspiration']
                if quotes == {}:
                    with open('default.py', 'r', encoding = 'UTF8') as f:
                        quotes['default'] = f.readlines()
                        config.set('categories', 'default', 'True') # updates config file
                    return quotes
                else:
                    return quotes
            except:
                return quotes

    # add/remove love list in dictionary based on checkbutton value
    def update_love(self):
        if self.love.get() == True:
            config.set('categories', 'love', 'True') # updates config file
            with open('love.py', 'r', encoding = 'UTF8') as f:
                new_quotes_added = f.readlines()
                quotes['love'] = new_quotes_added
                try:
                    del quotes['default']
                    config.set('categories', 'default', 'False') # updates config file
                    return quotes
                except:
                    return quotes
        elif self.love.get() == False:
            config.set('categories', 'love', 'False') # updates config file
            try:
                del quotes['love']
                if quotes == {}:
                    with open('default.py', 'r', encoding = 'UTF8') as f:
                        quotes['default'] = f.readlines()
                        config.set('categories', 'default', 'True') # updates config file
                    return quotes
                else:
                    return quotes
            except:
                return quotes

    # add/remove money list in dictionary based on checkbutton value
    def update_money(self):
        if self.money.get() == True:
            config.set('categories', 'money', 'True') # updates config file
            with open('money.py', 'r', encoding = 'UTF8') as f:
                new_quotes_added = f.readlines()
                quotes['money'] = new_quotes_added
                try:
                    del quotes['default']
                    config.set('categories', 'default', 'False') # updates config file
                    return quotes
                except:
                    return quotes
        elif self.money.get() == False:
            config.set('categories', 'money', 'False') # updates config file
            try:
                del quotes['money']
                if quotes == {}:
                    with open('default.py', 'r', encoding = 'UTF8') as f:
                        quotes['default'] = f.readlines()
                        config.set('categories', 'default', 'True') # updates config file
                    return quotes
                else:
                    return quotes
            except:
                return quotes

    # add/remove women list in dictionary based on checkbutton value
    def update_women(self):
        if self.women.get() == True:
            config.set('categories', 'women', 'True') # updates config file
            with open('women.py', 'r', encoding = 'UTF8') as f:
                new_quotes_added = f.readlines()
                quotes['women'] = new_quotes_added
                try:
                    del quotes['default']
                    config.set('categories', 'default', 'False') # updates config file
                    return quotes
                except:
                    return quotes
        elif self.women.get() == False:
            config.set('categories', 'women', 'False') # updates config file
            try:
                del quotes['women']
                if quotes == {}:
                    with open('default.py', 'r', encoding = 'UTF8') as f:
                        quotes['default'] = f.readlines()
                        config.set('categories', 'default', 'True') # updates config file
                    return quotes
                else:
                    return quotes
            except:
                return quotes

# create root window
root = tk.Tk()

# reserved for splash screen


# define root window
root.title("DAILY QUOTES")
root.geometry("465x225+500+250")
root.resizable(False, False)
app = Application(root)

#main loop
root.mainloop()