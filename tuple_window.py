from tkinter import *

root = Tk()
root.title("tuple")
root.geometry("700x800")
root.configure(background="yellow3")

months = ("January","Febuary","March",'April','May','June','July','August','September','October','November',"December")
profits = (70000,65888,93723,100000,7000,50000,8400,24000,65000,69000,92000,75000)
label_months = Label(root,text=months)
label_prices = Label(root,text=profits)
label_proft= Label(root)
label_loss= Label(root)

def tuple_max():
    maxmimum_profit = max(profits)
    index_month = profits.index(maxmimum_profit)
    max_proft_month = months[index_month]
    label_proft["text"]="Maximum profit of " + str(maxmimum_profit) + " was recorded in the month of " + str(max_proft_month)

def tuple_min():
    minimum_profit = min(profits)
    index_month_min = profits.index(minimum_profit)
    min_profit_month = months[index_month_min]
    label_loss["text"]="Minimum profit of " + str(minimum_profit) + " was recorded in the month of " + str(min_profit_month)


button1 = Button(root,text="Show most profitable month",command=tuple_max,bg="SteelBlue1")
label_months.place(relx=0.5,rely=0.3,anchor=CENTER)
label_prices.place(relx=0.5,rely=0.4,anchor=CENTER)
button1.place(relx=0.5,rely=0.5,anchor=CENTER)
label_proft.place(relx=0.5,rely=0.6,anchor=CENTER)
button2=Button(root,text="Show the least profitable month",command=tuple_min,bg="SteelBlue1")
button2.place(relx=0.5,rely=0.7,anchor=CENTER)
label_loss.place(relx=0.5,rely=0.8,anchor=CENTER)

root.mainloop()