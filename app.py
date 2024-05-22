from main import UserStats
from tkinter import *


print("start")
# profile = str(input())

link = "76561198201332390"

# zły link sprawdzać od strony użytnika

user = UserStats(link)

print(user.get_data())

print(user.get_table())


class Table:

    def __init__(self, root):

        for i in range(total_rows):
            for j in range(total_columns):

                self.e = Entry(root, width=40, fg='Black',
                               font=('Arial', 16, 'bold'))

                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])


lst = user.get_table()


total_rows = len(lst)
total_columns = len(lst[0])


root = Tk()

t = Table(root)
root.mainloop()
