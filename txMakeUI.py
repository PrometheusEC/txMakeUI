import customtkinter as ctk
import tkinter
from tx import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename


def clear():
    input_entry.delete(0, 'end')
    input_entry.configure(placeholder_text='Images Directory')
    output_entry.delete(0, 'end')
    output_entry.configure(placeholder_text ='TEX Directory')
    print ('Resetted entries')

def cleartext():
    txt_output.delete(0.0, 'end')

ctk.set_appearance_mode("dark")  #sets appearance mode
ctk.set_default_color_theme("dark-blue") #sets colour theme  
resXY=[800,350] #initialize res in X and Y coordinates [0] for x and [1] for y 
#args_TxMake=[] #for Future iterations of the program, to append advanced methods of TxMake



app = ctk.CTk()  
app.geometry(str(resXY[0])+'x'+str(resXY[1])) #setting resolution as string value
app.resizable(width=False, height=False)
app.title('txMake UI - made by Edgar Aguirre - v0.1.1')


########### GRID SETUP #########################
app.rowconfigure((0,1),weight = 1)
app.columnconfigure(0, weight = 1)




########### FRAMING ############################
#~~~~~~~~~~~~~~~~~TopFrame!~~~~~~~~~~~~~~~~~~~~~
top_frame = ctk.CTkFrame(app, fg_color='gray')
top_frame.grid(row=0, column=0, sticky='nsew')
top_frame.rowconfigure((0,1,2,3), weight=1)
top_frame.columnconfigure((0,2,3), weight=1)
top_frame.columnconfigure(1, weight=4)
top_frame.columnconfigure(2, weight=1)


#~~~~~~~~~~~~~~~BottomFrame!~~~~~~~~~~~~~~~~~~~~~
bottom_frame= ctk.CTkFrame(app, fg_color='black')
bottom_frame.grid(row=1, column=0, sticky='nsew')
#-------------------Text output-----------------
txt_output = ctk.CTkTextbox(bottom_frame, 
    width=resXY[0]-30, 
    height=(resXY[1]/2)-30,
    wrap = 'word')
#txt_output.configure(state='disabled')
txt_output.pack(pady=20)


########### ENTRY CREATION ########################
input_entry = ctk.CTkEntry(top_frame, placeholder_text ='Images Directory')
input_entry.grid(row=1, column=1, sticky='ew')

output_entry = ctk.CTkEntry(top_frame, placeholder_text ='TEX Directory')
output_entry.grid(row=2, column=1, sticky='ew')

######## Button creation ###########################

search = ctk.CTkButton(top_frame, text='select Directory', command=lambda: (getDirectory(input_entry, output_entry)))
search.grid(row=1, column=2)

search_file = ctk.CTkButton(top_frame, text='select File', command=lambda: getFile(input_entry, output_entry))
search_file.grid(row=1, column=3)


clear = ctk.CTkButton(top_frame, text='clear selection', command= clear)
clear.grid(row=2, column=2)

#txMaker = ctk.CTkButton(top_frame, text='Tx \n make', command=lambda: txFilter(input_entry, output_entry))
txMaker = ctk.CTkButton(top_frame, fg_color='Green', text='Tx Make', command=lambda: txMake(input_entry, output_entry, txt_output))
txMaker.grid(row=2, column=3)

clear_txt = ctk.CTkButton(bottom_frame, text='clear text', command= cleartext)
clear_txt.pack(pady=10)
app.mainloop()