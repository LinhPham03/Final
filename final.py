from tkinter import *
import tkinter as tk
import sys
from tkinter import messagebox as mb
import random

class login:
    def __init__(self,root):
        self.root =root
        self.root.geometry('1199x600+100+50')  
        self.root.title('Login Form')
        self.root.config(bg ='Light Blue')

        self.frame = Frame(self.root, bg = 'white')
        self.frame.place(x=330,y=150,width=500, height=400)
        

        # label
        heading =  Label(self.frame, text = 'Sign in Here', font = ('Cambria',35, 'bold'), bg  = 'white',fg = 'Blue')
        heading.place(x=90,y=30)
        sub =  Label(self.frame, text = '....', font = ('Cambria',15, 'bold'), bg  = 'white',fg = 'Blue')
        sub.place(x=90,y=100)

        userlabel = Label(self.frame, text = 'Username', font = ('Cambria', 15, 'bold'), bg  = 'white',fg = 'Black')
        userlabel.place(x=90,y=140)

        self.user= Entry(self.frame, font = ('Cambria',15), bg  ='silver')
        self.user.place(x=90,y=170,width=320,height=35)

        mklabel = Label(self.frame, text = 'Password', font = ('Cambria', 15, 'bold'), bg  = 'white',fg = 'Black')
        mklabel.place(x=90,y=210)

        self.mk= Entry(self.frame, font = ('Cambria',15), bg  ='silver')
        self.mk.place(x=90,y=240,width=320,height=35)

        login= Button(self.frame,text = 'Log in',bd = 0,font = ('Cambria', 12),bg='Blue', fg='white', command= self. check_function)
        login.place(x=90, y= 300,width=150,height=40)

        exit= Button(self.frame,text = 'Exit',bd = 0,font = ('Cambria', 12),bg='Blue', fg='white',command=self.stop)
        exit.place(x=260, y= 300,width=150,height=40)
    def stop(self):
        root.destroy()
    def check_function(self):
        if self.user.get()=='' or self.mk.get()=='':
            mb.showerror('Error','All fields are required',parent = self.root)
        elif self.user.get() == 'k' and self.mk.get() == '89':
            self.newwindow()
        else: 
            mb.showerror('Error','Invalid username',parent = self.root)
    
    def newwindow(self):
        self.newwindow= Toplevel(self.root)
        self.app= intro(self.newwindow)

class intro:
    def __init__(self,root):
        self.root =root
        self.root.geometry('1199x600+100+50')  
        self.root.title('Option')
        self.root.config(bg ='Light Blue')

        self.frame = Frame(self.root, bg = 'white')
        self.frame.place(x=200,y=150,width=800, height=400)

        heading =  Label(self.frame, text = 'Welcome to Flashcards', font = ('Cambria',35, 'bold'), bg  = 'white',fg = 'Blue')
        heading.place(x=90,y=30)
        sub =  Label(self.frame, text = 'Choose your option', font = ('Cambria',15, 'bold'), bg  = 'white',fg = 'Blue')
        sub.place(x=90,y=100)

        button= Frame(self.frame, bg= 'white')
        button.place(x=90,y=140)


        self.btnEdit = Button(button, text = 'Edit', font = ('arial',20,'bold'),height=1, width =10, bd =4,command= self.new1)
        self.btnEdit.grid(row=0,columnspan=2)

        self.btnStudy = Button(button, text = 'Study', font = ('arial',20,'bold'),height=1, width =10, bd =4,command= self.new2)
        self.btnStudy.grid(row=1,columnspan=2)

        self.btnTest = Button(button, text = 'Test', font = ('arial',20,'bold'),height=1, width =10, bd =4,command= self.new3)
        self.btnTest.grid(row=2,columnspan=2)

        self.btnBack = Button(button, text = 'Back', font = ('arial',20,'bold'),height=1, width =10, bd =4,command= exit)
        self.btnBack.grid(row=3,columnspan=2)

    def new1(self):
        self.new1= Toplevel(self.root)
        self.app= CRUD(self.new1)
    
    def new2(self):
        self.new2= Toplevel(self.root)
        self.app= study(self.new2)

    def new3(self):
        self.new3= Toplevel(self.root)
        self.app= quiz(self.new3)

class CRUD:
    def __init__(self,root):
        self.win = root
        self.win.title("...........")
        self.win.geometry("1350x750")
        self.win.config(bg= 'light blue')

        ##############################
        mainframe = Frame(self.win, bg = 'white',height=1000)
        mainframe.place(x=100,y=150)

        titFrame = Frame(mainframe, bd = 0, padx = 54, pady =8, bg = 'white')
        titFrame.pack(side= TOP)

        self.lblTit = Label(titFrame,font=('arial',47, 'bold'),text= 'Database',bg= 'white')
        self.lblTit.grid()

        buttonframe= Frame(mainframe, width = 1350, height = 400, padx =20, pady=20, bg = 'white')
        buttonframe.pack(side= BOTTOM)

        dataframe= Frame(mainframe, width = 1300, height = 400, padx =20, pady=20, bg = 'white')
        dataframe.pack(side= BOTTOM)

        #########################################

        self.lblQ = Label(dataframe,font=('arial',20, 'bold'),text= 'Question',padx = 2, pady =4, bg= 'white')
        self.lblQ.grid(row=0, column=0, sticky= W)

        self.Q = Entry(dataframe,font=('arial',20, 'bold'),width=39)
        self.Q.grid(row=0, column=1)

        self.lblans = Label(dataframe,font=('arial',20, 'bold'),text= 'Key',padx = 2, pady =10, bg= 'white')
        self.lblans.grid(row=1, column=0, sticky= W)

        self.answer = Entry(dataframe,font=('arial',20, 'bold'),width=39)
        self.answer.grid(row=1, column=1)

        self.btnAdd = Button(buttonframe, text = 'Add', font = ('arial',20,'bold'),height=1, width =10, bd =4,command= self.add_flash_card)
        self.btnAdd.grid(row=0, column=0)

        self.btnUpadte = Button(buttonframe, text = 'Update', font = ('arial',20,'bold'),height=1, width =10, bd =4, command = self.update_flash_cards)
        self.btnUpadte.grid(row=0, column=1)

        self.btnShow = Button(buttonframe, text = 'Show', font = ('arial',20,'bold'),height=1, width =10, bd =4,command = self.show_flashcards)
        self.btnShow.grid(row=0, column=2)

        self.btnDel = Button(buttonframe, text = 'Delete', font = ('arial',20,'bold'),height=1, width =10, bd =4,command = self.remove_flashcard)
        self.btnDel.grid(row=0, column=3)

        self.btnCls = Button(buttonframe, text = 'Clear', font = ('arial',20,'bold'),height=1, width =10, bd =4,command= self.cleardata)
        self.btnCls.grid(row=0, column=4)

        self.btnBack = Button(buttonframe, text = 'Back', font = ('arial',20,'bold'),height=1, width =10, bd =4,command= self.back)
        self.btnBack.grid(row=0, column=5)

    #########################################

    
    global flash_cards
    flash_cards={}
    with open("flash_cards.txt", "r") as f:
        for line in f:
            line = line.strip()
            split_index = line.index("=")
            quest = line[0: split_index].strip()
            answ = line[split_index + 1: len(line)].strip()
            flash_cards[quest] = answ


    def write_flash_cards_to_text_file():
        """Will line by line write the name and definition for each flash card to a file for saving"""
        global flash_cards

        with open("flash_cards.txt", "w+") as f:
            for question,answer in flash_cards.items():
                f.write(question,' = ',answer)

    def update_flash_cards( self,question,delete_flash_card=False):
        """Will be called whenever adding or deleting or replacing a flash card"""
        global flash_cards
        new_answer= self.answer
        if delete_flash_card:
            del flash_cards[question]
        else:
            flash_cards[question] = new_answer
            self.write_flash_cards_to_text_file()

    def add_flash_card(self):
        global flash_cards
        """Will be called from main menu to create or update flash card"""
        question = self.Q
        answer = self.answer
        if question not in flash_cards:
            self.update_flash_cards(question,answer)
        else:
            mb.showinfo('This question has existed in flashcards')


    def remove_flashcard(self):
        global flash_cards
        """Will be called from main menu to delete a flash card"""
        question = self.Q
        if question not in flash_cards:
            mb("This question is not in flash cards")
        else:
            self.update_flash_cards(question, "", delete_flash_card=True)

    def show_flashcards(self):
        global flash_cards
        newWindow = Toplevel(root)
        newWindow.title("Database")
        with open ("flash_cards.txt", "r") as myfile:
            data = myfile.read()
        Label(newWindow, text= data, font=('Time New Roman', 18), fg="black").pack()
    
    def back():
        root.destroy()
    def cleardata(self):
        self.Q.delete(0,END)
        self.answer.delete(0,END)

        ########################################



import random

# Python program to create a simple GUI
# Simple Quiz using Tkinter

#import everything from tkinter
from tkinter import *

# and import messagebox as mb from tkinter
from tkinter import messagebox as mb

#class to define the components of the GUI
class quiz():
	
	def __init__(self,gui):
		self.gui = gui
		self.gui.geometry("800x450")
		self.gui.title(" Quiz")

		self.question_blocks=dict()
		self.question=[]
		self.answer=[]
		with open("flash_cards.txt") as f:
			for line in f:
				(key, val) = line.split('=')
				self.question_blocks[key] = val
				self.question.append(key)
				self.answer.append(val)

		# set question number to 0
		self.q_no=0
		
		# assigns ques to the display_question function to update later.
		self.display_title()
		self.opt_selected= IntVar()
		# display options for the current question
		self.display_options(self.question_blocks)
		
		# displays the button for next and exit.
		self.buttons()
		
		# no of questions
		self.data_size=len(self.question_blocks)
		
		# keep a counter of correct answers
		self.correct=0

	
	def display_result(self):
		
		# calculates the wrong count
		wrong_count = self.data_size - self.correct
		correct = f"Correct: {self.correct}"
		wrong = f"Wrong: {wrong_count}"
		
		# calcultaes the percentage of correct answers
		score = int(self.correct / self.data_size * 100)
		result = f"Score: {score}%"
		
		# Shows a message box to display the result
		mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")


	# This method checks the Answer after we click on Next.
	def check_ans(self, answer):

		# checks for if the selected option is correct
		if self.opt_selected.get() == answer:
			# if the option is correct it return true
			return True

	def next_btn(self):
		
		# Check if the answer is correct
		if self.opt_selected.get() == dapan:
		
			# if the answer is correct it increments the correct by 1
			self.correct += 1
		
		# Moves to next Question by incrementing the q_no counter
		self.q_no += 1
		
		# checks if the q_no size is equal to the data size
		if self.q_no==self.data_size:
			
			# if it is correct then it displays the score
			self.display_result()
			
			# destroys the GUI
			self.gui.destroy()
		else:
			# shows the next question
			self.display_options(self.question_blocks)

	def buttons(self):
		
		
		# next Question
		next_button = Button(self.gui, text="Next",command=self.next_btn,
		width=10,bg="blue",fg="white",font=("ariel",16,"bold"))
		
		
		next_button.place(x=350,y=380)
		

		quit_button = Button(self.gui, text="Quit", command=gui.destroy,
		width=5,bg="black", fg="white",font=("ariel",16," bold"))

		quit_button.place(x=700,y=50)


	# radio button 

	def display_options(self,question_blocks):
		question = []
		answer = []
		for key,value in question_blocks.items():
			question.append(key)
			answer.append(value)
		random.shuffle(question)
		for el in question:
			global dapan
			dapan = question_blocks[el]
			options = [dapan]
			while len(options) < 4:
				random_ans = random.choice(answer)
				if random_ans not in options:
					options.append(random_ans)
			random.shuffle(options) 
			
			q_no = Label(self.gui, text= el, width=60, font=( 'ariel' ,16, 'bold' ), anchor= 'w' )

			q_no.place(x=70, y=100)
	
			y_pos = 150
		# text of the radio buttons.
			for i in range(4):
				radio_btn= Radiobutton (self.gui,text=options[i],variable = self.opt_selected, 
										value = i,font = ("ariel",14))
				radio_btn.place(x = 100, y = y_pos)		
				y_pos += 60
		
		#################################

	def display_title(self):
		
		# The title to be shown
		title = Label(self.gui, text="QUIZ",
		width=50, bg="green",fg="white", font=("ariel", 20, "bold"))
		
		# place of the title
		title.place(x=0, y=2)


gui=Tk()
a= quiz(gui)
gui.mainloop()

class study:
	
	def __init__(self,gui):
		self.gui = gui
		self.gui.geometry("1199x600+100+50")
		self.gui.title(" Quiz")
		self.gui.config(bg='light blue')
		
		self.q_no=0

		self.question = []
		self.answer = []
		global question_blocks

		with open("flash_cards.txt") as f:
			question_blocks=dict()
			for line in f:
				line = line.strip()
				split_index = line.index("=")
				quest = line[0: split_index].strip()
				answ = line[split_index + 1: len(line)].strip()
				question_blocks[quest] = answ

				self.question.append(quest)
				self.answer.append(answ)

		self.data_size=len(question_blocks)


		self.lblQ = Label(self.gui, text = 'Question', font = ('Cambria', 15, 'bold'),bg='light blue',fg = 'Black')
		self.lblQ.place(x=30,y=30)
		
		self.Q = Label(self.gui,padx = 2, pady =4, bg= 'white',font='black')
		self.Q.place(x=30,y=60)

		self.lblans = Label(self.gui, text = 'Key', font = ('Cambria', 15, 'bold'),bg='light blue',fg = 'Black')
		self.lblans.place(x=30,y=250)

		self.ans = Label(self.gui,padx = 2, pady =4, bg= 'white')
		self.ans.place(x=30, y= 280)

		next_button = Button(self.gui, text="Next",command=self.next_btn, width=10,bg="blue",fg="white",font=("ariel",16,"bold"))
		next_button.pack(side=BOTTOM)

		quit_button = Button(self.gui, text="Quit", command= gui.destroy,
		width=5,bg="black", fg="white",font=("ariel",16," bold"))

		quit_button.place(x=1000,y=50)

		que = Label(self.Q, text= self.question[0], width=60, font=( 'ariel' ,16, 'bold' ), anchor= 'w' )
		que.pack()
		ans = Label(self.ans, text= self.answer[0], width=60, font=( 'ariel' ,16, 'bold' ), anchor= 'w' )
		ans.pack()
	
	def display_options(self):
		que = Label(self.Q, text= self.question[self.q_no], width=60, font=( 'ariel' ,16, 'bold' ), anchor= 'w' )
		que.pack()
		ans = Label(self.ans, text= self.answer[self.q_no], width=60, font=( 'ariel' ,16, 'bold' ), anchor= 'w' )
		ans.pack()
	
	def next_btn(self):
		self.q_no+=1
		# checks if the q_no size is equal to the data size
		if self.q_no==self.data_size:
			
			# if it is correct then it displays the score
			mb.showinfo("Finished",f"You've learned all!")
			
			# destroys the GUI
			root.destroy()
		else:
			# shows the next question
			self.display_options()

root=Tk()
a= login(root)
root.mainloop()






