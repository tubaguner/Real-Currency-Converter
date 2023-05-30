import tkinter as Tk
from tkinter import ttk
import requests



def convert_currency():
    url = f"http://www.floatrates.com/daily/usd.json"
    response = requests.get(url)
    data = response.json()
    amount = float(amount.get())
    global exchange_rate
    available_currencies = data.keys()
    if exchange_rate == available_currencies:
       exchange_rate = data["rate"][from_currency]
    to_currency = float(amount * exchange_rate)
    Result.set(f"Result: {to_currency:.2f}")

def input():
    from_currency = input("Enter the currency to convert from: ").upper()
    from_currency.get()
    print("Entered currency: ", from_currency)

def output():
    to_currency = input("Enter the currency to convert to: ").upper()
    to_currency.get()
    print("Entered currency: ",to_currency)

def return_amount(*args):
    amount_value = float(amount)
    print("Entered amount: ", amount_value)



root = Tk.Tk()
root.title('Currency Converter')
root.geometry("420x520")

from_currency = ttk.Entry(root, text='From:')
from_currency.pack()
from_currency.bind('<Return>', input)



to_currency = ttk.Entry(root,text='To:')
to_currency.pack()
to_currency.bind('<Return>', output)



style = ttk.Style()
style.configure('Pink.TButton', background='#F0F0F8',foreground='#404040',font=('Arial Bold',16))


amount = Tk.StringVar()
amount_entry = ttk.Entry(root, textvariable=amount)
amount_entry.pack(fill='x',expand=True)
amount.get()
amount_entry.focus()
amount.trace('w', return_amount)
    

Result = Tk.StringVar()
result_entry = ttk.Entry(root,textvariable=Result)
result_entry.pack(fill='x', expand=True)
Result.get()
result_entry.focus()

convert_button = ttk.Button(root,text="Convert",style='Pink.TButton',command=convert_currency)
convert_button.pack(fill='y', expand=False, pady=10)

style = ttk.Style()
style.configure('TLabel', background='#FFFF00')

root.configure(bg='#FFFF00')

root.mainloop()
