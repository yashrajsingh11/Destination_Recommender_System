import tkinter as tk
from tkinter import ttk
import numpy as np
import pandas as pd
from tkinter import *
import webbrowser
from tkinter import messagebox
from googlesearch import search

root = tk.Tk()
root.geometry("")
root.title("Find your destination")
root.resizable(0, 0)
name_var = tk.StringVar()
month_var = tk.StringVar()
newDF = list()

def callback(tag):
	for j in search(tag,tld = 'com', start = 0, num = 1, stop = 1):
		url = j
		print(j)
	webbrowser.open_new_tab(url)

def submit():
	if name_entry.get() == "" or month_combo.get() == "":
		messagebox.showerror('Error message box', 'Fill the blank field', parent = root)
		name_entry.focus_force()
		return
	res.grid(columnspan = 2, pady = 10)
	name=name_var.get()
	name=name.upper()
	m = month_var.get()
	month = month_dict[m]
	month = int(month)
	name = "'" + name + "'"
	print("The name is : " + name)

	l1 = twoDArray[newDF.index(name)]

	dictionary = {}
	for i in range(len(l1)):
		dictionary[newDF[i]] = l1[i]
	nayaVariable = sorted(dictionary.items(), key=lambda x: x[1][month], reverse = True)

	tag1 = name + " to " + nayaVariable[0][0]
	res_label1 = tk.Label(result_frame, text = tag1, font = ('calibre', 12, 'normal'), fg = '#001379', cursor = "hand2")
	res_label1.bind("<Button-1>", lambda e: callback(tag1))
	res_label1.grid(row = 1, column = 0, pady = 5, columnspan = 2)

	tag2 = name +" to " +  nayaVariable[1][0]
	res_label2 = tk.Label(result_frame, text = tag2, font = ('calibre', 12, 'normal'), fg = '#001379', cursor = "hand2")
	res_label2.bind("<Button-1>", lambda e: callback(tag2))
	res_label2.grid(row = 2, column = 0, pady = 5)

	tag3 = name + " to " + nayaVariable[2][0]
	res_label3 = tk.Label(result_frame, text = tag3, font = ('calibre', 12, 'normal'), fg = '#001379', cursor = "hand2")
	res_label3.bind("<Button-1>", lambda e: callback(tag3))
	res_label3.grid(row = 3, column = 0, pady = 5)

	tag4 = name +" to " + nayaVariable[3][0]
	res_label4 = tk.Label(result_frame, text = tag4, font = ('calibre', 12, 'normal'), fg = '#001379', cursor = "hand2")
	res_label4.bind("<Button-1>", lambda e: callback(tag4))
	res_label4.grid(row = 4, column = 0, pady = 5)

	tag5 = name + " to " + nayaVariable[4][0]
	res_label5 = tk.Label(result_frame, text = tag5, font = ('calibre', 12, 'normal'), fg = '#001379', cursor = "hand2")
	res_label5.bind("<Button-1>", lambda e: callback(tag5))
	res_label5.grid(row = 5, column = 0, pady = 5)

	tag6 = name + " to " + nayaVariable[5][0]
	res_label6 = tk.Label(result_frame, text = tag6, font = ('calibre', 12, 'normal'), fg = '#001379', cursor = "hand2")
	res_label6.bind("<Button-1>", lambda e: callback(tag6))
	res_label6.grid(row = 6, column = 0, pady = 5)

	tag7 = name + " to " + nayaVariable[6][0]
	res_label7 = tk.Label(result_frame, text = tag7, font = ('calibre', 12, 'normal'), fg = '#001379', cursor = "hand2")
	res_label7.bind("<Button-1>", lambda e: callback(tag7))
	res_label7.grid(row = 7, column = 0, pady = 5)

	tag8 = name + " to " + nayaVariable[7][0]
	res_label8 = tk.Label(result_frame, text = tag8, font = ('calibre', 12, 'normal'), fg = '#001379', cursor = "hand2")
	res_label8.bind("<Button-1>", lambda e: callback(tag8))
	res_label8.grid(row = 8, column = 0, pady = 5)

	tag9 = name + " to " + nayaVariable[8][0]
	res_label9 = tk.Label(result_frame, text = tag9, font = ('calibre', 12, 'normal'), fg = '#001379', cursor = "hand2")
	res_label9.bind("<Button-1>", lambda e: callback(tag9))
	res_label9.grid(row = 9, column = 0, pady = 5)

	tag10 = name + " to " + nayaVariable[9][0]
	res_label10 = tk.Label(result_frame, text = tag10, font = ('calibre', 12, 'normal'), fg = '#001379', cursor = "hand2")
	res_label10.bind("<Button-1>", lambda e: callback(tag10))
	res_label10.grid(row = 10, column = 0, pady = 5)
		
	name_var.set("")
	month_var.set("")
	
f = open("newDF.txt","rt")
lines = f.readlines()

for line in lines:
	newDF.append(line.strip())

loadedArr = pd.read_csv("chhehKalol.csv", header = None, delimiter=",")
loadedArr = loadedArr.to_numpy()
twoDArray = loadedArr.reshape(loadedArr.shape[0], loadedArr.shape[1] // 13, 13)

base_frame = tk.Label(root, bg = '#454545')
base_frame.grid(row = 0, column = 0, sticky = 'NSEW')

title = tk.Label(base_frame, text="    Find your destination", font = ('calibre', 20, 'bold'), bg = '#454545', fg = '#f4f0ef', width = 20, anchor = 'center')
title.grid(row = 0, rowspan = 2, pady = 10)

txt = "Select your source airport and this will give you"+"\n"+ "the top 10 visited destination from this source for the given month."
desc = tk.Label(base_frame, text = txt, font = ('calibre', 10, 'normal'), bg = '#454545', fg = '#f4f0ef', anchor = 'e')
desc.grid(row = 2, column = 0, sticky = 'E', pady = 5)

query_frame = tk.Frame(root,bg = '#454545')
query_frame.grid(row = 1, column = 0, sticky = 'NSEW', ipadx = 20)

result_frame = tk.Frame(root)
result_frame.grid(row = 2, column = 0, sticky = 'NSEW', ipadx = 20)

months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
month_dict = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12} 

name_label = tk.Label(query_frame, text = 'Enter your nearest airport code : ', font = ('calibre', 10, 'bold'), bg = '#454545', fg = '#f4f0ef')
name_entry = tk.Entry(query_frame, textvariable = name_var, font = ('calibre', 10, 'normal'))

month_label = tk.Label(query_frame, text = 'Enter the month you want to visit : ', font = ('calibre', 10, 'bold'), bg = '#454545', fg = '#f4f0ef')
month_combo = ttk.Combobox(query_frame, values = months, textvariable = month_var)

res = tk.Label(result_frame, text = 'People generally travel', font = ('calibre', 15, 'bold'))

sub_btn=tk.Button(query_frame, text = 'Submit', command = submit, bg = '#d98768', fg = '#f4f0ef', relief = 'raised', cursor = "hand2")

name_label.grid(row = 3, column = 0, pady = 5)
name_entry.grid(row = 3, column = 1, padx = 5, pady = 5)
month_label.grid(row = 4, column = 0, pady = 5)
month_combo.grid(row = 4, column = 1, padx = 5, pady = 5)
sub_btn.grid(row = 5, pady = 15, columnspan = 2, ipady = 3, ipadx = 5)

query_frame.grid_columnconfigure(0, weight = 1)
result_frame.grid_columnconfigure(0, weight = 1)
root.grid_rowconfigure(0, weight = 1)
root.grid_columnconfigure(0, weight = 1)

root.mainloop()