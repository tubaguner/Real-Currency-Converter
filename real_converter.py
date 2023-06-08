import tkinter as Tk
from tkinter import ttk
import requests

from_currency ='' 
to_currency = ''


def convert_currency():
    url = f"http://www.floatrates.com/daily/{from_currency}.json"
    response = requests.get(url)
    data = response.json()
    rates = data.keys()
    to_currency_rate = data[to_currency.get()]['rate']
    result_money = float(amount.get()) * to_currency_rate
    Result.set(f"Result: {result_money:.2f}")

def input():
    from_currency = input("Enter the currency to convert from: ")
    from_currency.get()
    print("Entered currency: ", from_currency)

def output():
    to_currency = input("Enter the currency to convert to: ")
    to_currency.get()
    print("Entered currency: ",to_currency)


root = Tk.Tk()
root.title('Currency Converter')
root.geometry("420x500")

from_currency = ttk.Label(text='Enter currency to convert from:',font=('Helvetica 14 bold'))
from_currency.pack(fill='x', expand=True, padx=50, pady=10)
from_currency = ttk.Entry(root)
from_currency.pack(fill='y',expand=True)
from_currency.bind('<Return>', input)

to_currency = ttk.Label(text='Enter currency to convert to:',font=('Helvetica 14 bold'))
to_currency.pack(fill='x', expand=True, padx=50, pady=10)
to_currency = ttk.Entry(root)
to_currency.pack(fill='y', expand=True)
to_currency.bind('<Return>', output)

style = ttk.Style()
style.configure('Pink.TButton', background='#F0F0F8',foreground='forest green',font=('Helvetica 14 bold'))

amount = ttk.Label(text='Enter amount:',font=('Helvetica 14 bold'))
amount.pack(fill='y', expand=True)
amount = Tk.StringVar()
amount_entry = ttk.Entry(root, textvariable=amount)
amount_entry.pack(fill='x',expand=True, padx=60, pady=10)
amount.get()
amount_entry.focus()

result = ttk.Label(text='Result:',font=('Helvetica 14 bold'))
result.pack(fill='y',expand=True)
Result = Tk.StringVar()
result_entry = ttk.Entry(root,textvariable=Result)
result_entry.pack(fill='x', expand=True, padx=60, pady=10)
Result.get()
result_entry.focus()


convert_button = ttk.Button(root,text="Convert",style='Pink.TButton',command=convert_currency)
convert_button.pack(fill='y', expand=False, padx=15,pady=15)

style = ttk.Style()
style.configure('TLabel', background='lime green')

root.configure(bg='lime green')

root.mainloop()
