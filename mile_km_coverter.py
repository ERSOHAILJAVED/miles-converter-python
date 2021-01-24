from tkinter import*

# function to convert the miles into km
def miles_To_Km():
    miles=float(input_Entry.get())
    km=miles*1.609
    result_Lable.config(text=f"{km}")

# making the windows
windows=Tk()
windows.title("miles to km coverter")
windows.config(padx=20,pady=20)
# windows.minsize(400,100)

# creating the widest

input_Entry=Entry(width=7)
input_Entry.grid(column=1,row=0)

miles_Lable=Label(text="MILES")
miles_Lable.grid(column=2,row=0)


isequalto_Lable=Label(text="is equal to")
isequalto_Lable.grid(column=0, row=1)

result_Lable=Label(text="0")
result_Lable.grid(column=1, row=1)


kilometer_Lable=Label(text="Km")
kilometer_Lable.grid(column=2, row=1)


cal_btn=Button(text="calculate",command=miles_To_Km)
cal_btn.grid(column=1, row=2)




#  window display
windows.mainloop()