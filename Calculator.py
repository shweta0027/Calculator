from tkinter import *
import tkinter.font as font


# Driver code 
if __name__ == "__main__": 
	#main window 
	main = Tk() 

	main.configure(background="blue") 

	main.title("Calculator") 

main.resizable(0, 0)

main.geometry("325x265") 
main.resizable(0, 0)


expression = "" 
def press(item): 
	global expression 

	expression = expression + str(item) 
	input_text.set(expression) 

def equalpress(): 
	try: 

		global expression 
		total = str(eval(expression)) 

		input_text.set(total) 
		expression = "" 

	except: 

		input_text.set(" Error ") 
		expression = "" 


def clear(): 
	global expression 
	expression = "" 
	input_text.set("") 



input_text = StringVar() 
myfont = font.Font(family='Helvetica',size=8, weight='bold')
     

expression_field = Entry(main,font=('arial', 18, 'bold'), textvariable=input_text, width=14, justify=RIGHT,bg="light green") 
expression_field.grid(columnspan=4, ipadx=70, ipady=10) 



button1 = Button(main, text=' 1 ', fg='black', bg='grey', 
					command=lambda: press(1), height=3, width=10) 
button1['font'] = myfont                    
button1.grid(row=4, column=0) 

button2 = Button(main, text=' 2 ', fg='black', bg='grey', 
					command=lambda: press(2), height=3, width=10) 
button2.grid(row=4, column=1)
button2['font'] = myfont                     

button3 = Button(main, text=' 3 ', fg='black', bg='grey', 
					command=lambda: press(3), height=3, width=10) 
button3.grid(row=4, column=2) 
button3['font'] = myfont

button4 = Button(main, text=' 4 ', fg='black', bg='grey', 
					command=lambda: press(4), height=3, width=10) 
button4.grid(row=3, column=0) 
button4['font'] = myfont

button5 = Button(main, text=' 5 ', fg='black', bg='grey', 
					command=lambda: press(5), height=3, width=10) 
button5.grid(row=3, column=1)
button5['font'] = myfont 

button6 = Button(main, text=' 6 ', fg='black', bg='grey', 
					command=lambda: press(6), height=3, width=10) 
button6.grid(row=3, column=2)
button6['font'] = myfont 

button7 = Button(main, text=' 7 ', fg='black', bg='grey', 
					command=lambda: press(7), height=3, width=10) 
button7.grid(row=2, column=0) 
button7['font'] = myfont

button8 = Button(main, text=' 8 ', fg='black', bg='grey', 
					command=lambda: press(8), height=3, width=10) 
button8.grid(row=2, column=1)
button8['font'] = myfont 

button9 = Button(main, text=' 9 ', fg='black', bg='grey', 
					command=lambda: press(9), height=3, width=10) 
button9.grid(row=2, column=2)
button9['font'] = myfont 

button0 = Button(main, text=' 0 ', fg='black', bg='grey', 
					command=lambda: press(0), height=3, width=10) 
button0.grid(row=5, column=0)
button0['font'] = myfont 

plus = Button(main, text=' + ', fg='white', bg='black', 
				command=lambda: press("+"), height=3, width=10) 
plus.grid(row=2, column=3)
plus['font'] = myfont

minus = Button(main, text=' - ', fg='white', bg='black', 
				command=lambda: press("-"), height=3, width=10) 
minus.grid(row=3, column=3)
minus['font'] = myfont 

multiply = Button(main, text=' x ', fg='white', bg='black', 
					command=lambda: press("*"), height=3, width=10) 
multiply.grid(row=4, column=3)
multiply['font'] = myfont 

divide = Button(main, text=' / ', fg='white', bg='black', 
					command=lambda: press("/"), height=3, width=10) 
divide.grid(row=5, column=3)
divide['font'] = myfont 

equal = Button(main, text=' = ', fg='white', bg='black', 
				command=equalpress, height=3, width=10) 
equal.grid(row=5, column=2) 
equal['font'] = myfont

clear = Button(main, text='Clear', fg='black', bg='red', 
				command=clear, height=3, width=10) 
clear.grid(row=5, column='1')
clear['font'] = myfont



main.mainloop() 