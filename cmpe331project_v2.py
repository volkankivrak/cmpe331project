"""
    Stage: Development-01
     @author: Ayşenur Hanlı, 120202073
     @author: Volkan Kıvrak, 120202101

    Stage: Development-02
     @author: Mohammed Ghassan Nassseir, 119200029
     @author: Elif Tuğ, 119202032 

    Stage: Code Review
    @author: Gökalp Çevik, 120202074
    @author: Mohammad Hamed 120200155
"""

import tkinter as tk
from ast import Break
from stat import UF_IMMUTABLE
import tkinter as tk


class LoginWindow: #Development-01
    # constructor
    def __init__(self):
        self.window = tk.Tk()

        self._initializeGUI()
        self._addGUIElementsToFrame()

        # start the GUI frame
        self.window.mainloop()


    """
        Initialize GUI elements. If it is necessary, you can add
        more elements.
        ! PLEASE RENAME THE OBJECTS ACCORDING TO THEIR PURPOSES !
        ! YOU CAN ADD MORE ELEMENTS IF IT IS NECESSARY !
    """
    def _initializeGUI(self):
        self.lbl01 = tk.Label(text="Label-01")
        self.lbl02 = tk.Label(text="Label-02")

        self.txt01 = tk.Entry()
        self.txt02 = tk.Entry()

        self.btn01 = tk.Button(text="Btn-01")
        self.btn02 = tk.Button(text="Btn-02")

        self.btn01.bind("<Button-1>", self.handle_click)
        self.btn02.bind("<Button-1>", self.handle_click)


    """
        Add GUI elements to the layout of the frame. If it is necessary,
        you can add more elements.
    """
    def _addGUIElementsToFrame(self):
        self.lbl01.grid(row=0, column=0, padx=10, pady=5)
        self.txt01.grid(row=0, column=1, padx=10, pady=5)

        self.lbl02.grid(row=1, column=0, padx=10, pady=5)
        self.txt02.grid(row=1, column=1, padx=10, pady=5)

        self.btn01.grid(row=2, column=0, padx=10, pady=5)
        self.btn02.grid(row=2, column=1, padx=10, pady=5)


    """
        Action listener for the buttons. If "event.widget" is from
        one of the buttons, apply the related operation.
        :param event: action event for detecting which button is clicked
    """
    def handle_click(self, event):
        pass

# New class done in Development-02

class WelcomePage:
    def __init__(self):
        self.window = tk.Tk()
        self._initializeGUI()
        self._addGUIElementsToFrame()
        self.window.mainloop()

    def _initializeGUI(self):
        self.lblLogged = tk.Label(text="Super Market")
        self.btnItem1 = tk.Button(text="Item 1")
        self.btnItem2 = tk.Button(text="Item 2")
        self.btnItem3 = tk.Button(text="Item 3")
        self.btnItem1.bind("<Button-1>", self.handle_click)
        self.btnItem2.bind("<Button-1>", self.handle_click)
        self.btnItem3.bind("<Button-1>", self.handle_click)

    def _addGUIElementsToFrame(self):
        self.lblLogged.pack(side='top', fill='both', expand=True)
        self.btnItem1.pack(side='left', fill='both', expand=True)
        self.btnItem2.pack(side='left', fill='both', expand=True)
        self.btnItem3.pack(side='left', fill='both', expand=True)

# popup 
    def handle_click(self, event):
        popup = tk.Toplevel()
        popup.title('Pop-up Window')
        tk.Label(popup, text='Item has been added').pack()
        tk.Button(popup, text='Close', command=popup.destroy).pack()


            


# main method for testing the application
if __name__ == "__main__":
    LoginWindow()
    WelcomePage()

# The below part "class Supermarket" was done in Development 1, by  @author: Ayşenur Hanlı, 120202073 @author: Volkan Kıvrak, 120202101.

# class superMarket:
#     # -----------------SUPERMARKET MANAGEMENT SYSTEM--------------------
#     items = []
#     while True:
#         display = input('Press enter to continue.')
#         print('------------------Welcome to the supermarket------------------')
#         print('1. View items\n2. Add items for sale\n3. Purchase items\n4. Search items \n5. Edit items\n6. Exit')
#         choice = input('Enter the number of your choice : ')

#         if choice == '1':
#             print('------------------View Items------------------')
#             print('The number of items in the inventory are : ', len(items))
#             while len(items) != 0:
#                 print('Here are all the items available in the supermarket.')
#                 for item in items:
#                     for key, value in item.items():
#                         print(key, ':', value)
#                 break

#         elif choice == '2':
#             print('------------------Add items------------------')
#             print('To add an item fill in the form')
#             # while True:
#             #     try:
#             #         number_items = int(input('Enter the number of items you want to add in the inventory : '))
#             #         break
#             #     except ValueError:
#             #         print('Number of items should only be in digits')
#             # for num in range(number_items):
#             item = {}
#             item['name'] = input('Item name : ')
#             while True:
#                 try:
#                     item['quantity'] = int(input('Item quantity : '))
#                     break
#                 except ValueError:
#                     print('Quantity should only be in digits')
#             while True:
#                 try:
#                     item['price'] = int(input('Price $ : '))
#                     break
#                 except ValueError:
#                     print('Price should only be in digits')
#             print('Item has been successfully added.')
#             items.append(item)

#         elif choice == '3':
#             print('------------------purchase items------------------')
#             print(items)
#             purchase_item = input('which item do you want to purchase? Enter name : ')
#             for item in items:
#                 if purchase_item.lower() == item['name'].lower():
#                     if item['quantity'] != 0:
#                         print('Pay ', item['price'], 'at checkout counter.')
#                         item['quantity'] -= 1
#                     else:
#                         print('item out of stock.')

#         elif choice == '4':
#             print('------------------search items------------------')
#             find_item = input('Enter the item\'s name to search in inventory : ')
#             for item in items:
#                 if item['name'].lower() == find_item.lower():
#                     print('The item named ' + find_item + ' is displayed below with its details')
#                     print(item)
#                 else:
#                     print('item not found.')

#         elif choice == '5':
#             print('------------------edit items------------------')
#             item_name = input('Enter the name of the item that you want to edit : ')
#             for item in items:
#                 if item_name.lower() == item['name'].lower():
#                     print('Here are the current details of ' + item_name)
#                     print(item)
#                     item['name'] = input('Item name : ')
#                     while True:
#                         try:
#                             item['quantity'] = int(input('Item quantity : '))
#                             break
#                         except ValueError:
#                             print('Quantity should only be in digits')
#                     while True:
#                         try:
#                             item['price'] = int(input('Price $ : '))
#                             break
#                         except ValueError:
#                             print('Price should only be in digits')
#                     print('Item has been successfully updated.')
#                     print(item)
#                 else:
#                     print('Item not found')

#         elif choice == '6':
#             print('------------------exited------------------')
#             break

#         else:
#             print('You entered an invalid option')