from tkinter import *
from tkinter.messagebox import showinfo
import random
from tkinter import filedialog
import time

root = Tk()

root.title('Генератор паролей')
root.geometry("565x560")
root.resizable(width=False, height=False)
root.configure(bg='black')

chars = "abcdefghijklmnopqrstuvwxyz"
symbols = "[]{}()*'/.,_-!&?+%"
num = "0123456789"

chars = list(chars + chars.upper() + symbols + num)

def clear():
    text_field.delete(0.0, END) #0.0 - начало

def generate():
    if entry_count.get() == '':
        showinfo(title='Ошибка!', message='Необходимо ввести кол-во паролей.')
    elif entry_len.get() == '':
        showinfo(title='Ошибка!', message='Необходимо ввести длину пароля.')

    try:
        len_pass = int(entry_len.get())
        count_pass = int(entry_count.get())
    except:
        showinfo(title='Ошибка!', message='Необходимо вводить только цифры.')
    else:
        text_field.delete(0.0, END)

        for i in range(count_pass):
            password = ''
            for j in range(len_pass):
                password += random.choice(chars)
            text_field.insert(END, password + '\n')

def save():
    filepath = filedialog.asksaveasfilename(filetypes=(("TXT files", '*.txt'), ('ALL files', '*.*')))
    if filepath != "":
        text = text_field.get(0.0, END)
        with open(filepath, "w") as file:
            file.write(text)
            file.close()



#Количество паролей
col_pass = Label(root, text="Кол-во паролей: ", bg='black', fg='white').place(x=70, y=30)
entry_count = Entry(root, width=15)
entry_count.place(x=190, y=30)

#Длина паролей
dl_pass = Label(root, text="Длина пароля: ", bg='black', fg='white').place(x=70, y=60)
entry_len = Entry(root, width=15)
entry_len.place(x=190, y=60)

#Кнопки
btn_clear = Button(root, text='Очистить', command=clear).place(x=420, y=40)
btn_generate = Button(root, text='Генерировать', command=generate).place(x=330, y=40)
btn_save = Button(root, text='Сохранить', command=save).place(x=485, y=40)

#Текстовое поле
text_field = Text(root, width=69, height=25)
text_field.place(x=5, y=150)

root.mainloop()



#Консольный генератор паролей

# a = "abcdefghijklmnopqrstuvwxyz" #Буквы нижнего регистра
# b = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #Буквы высокого регистра
# c = "0123456789" #Цифры
# d = "[]{}()*'/.,_-!&?" #Символы
# all = a + b + c + d #Строка целиком
#
# length = 12 #длина пароля
#
# password = "".join(random.sample(all, length)) #Генерация пароля
#
# print("Генерируем пароль....")
# time.sleep(3)
# print("Пароль готов: " + password)

