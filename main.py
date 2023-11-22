import tkinter as tk
import tkinter.filedialog as tfd
import tkinter.messagebox as tkm

window = tk.Tk()
window.title('Office Notepad')
window.geometry('400x400')
file_name = ''


def open_file():
    global file_name
    content_text.delete(1.0, "end")
    file_name = tfd.askopenfilename()
    with open(file_name) as file:
        content_text.insert(1.0, file.read())


def new_file():
    global file_name
    if tkm.askokcancel('creating a new file', 'are you sure? Unsaved text will be deleted'):
        file_name = ''
        content_text.delete(1.0, "end")


def save_as_file():
    global file_name
    file_name = tfd.asksaveasfilename()
    content = content_text.get(1.0, "end")
    with open(file_name, 'w') as file:
        file.write(content)


def save_file():
    global file_name
    if file_name == '':
        save_as_file()
    else:
        content = content_text.get(1.0, "end")
        with open(file_name, 'w') as file:
            file.write(content)


content_text = tk.Text(window, wrap="word")
content_text.place(x=0, y=0, relwidth=1, relheight=1)

main_menu = tk.Menu(window)
window.configure(menu=main_menu)
file_menu = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='file', menu=file_menu)

new_file_icon = tk.PhotoImage(file='icons/new_file.gif')
open_file_icon = tk.PhotoImage(file='icons/open_file.gif')
save_file_icon = tk.PhotoImage(file='icons/save_file.gif')
save_as_file_icon = tk.PhotoImage(file='icons/save_file.gif')

file_menu.add_command(label='new file', image=new_file_icon, compound='left', command=new_file)
file_menu.add_command(label='open', image=open_file_icon, compound='left', command=open_file)
file_menu.add_command(label='save ', image=save_file_icon, compound='left', command=save_file)
file_menu.add_command(label='save as', image=save_as_file_icon, compound='left', command=save_as_file)

with open('languages.txt') as file:
    print(file.read())

with open('languages.txt') as file:
    for line in file:
        print(f'languages: {line}')

with open('file_blank.txt', 'w') as file:
    file.write("new text")

with open('file_blank.txt') as file:
    print(file.read())

with open('file_blank.txt', 'w') as file:
    file.write("110100101")

with open('file_blank.txt') as file:
    print(file.read())

with open('file_blank.txt', 'a') as file:
    file.write("\ntesting append")

with open('file_blank.txt') as file:
    print(file.read())

with open('languages.txt', 'a') as file:
    file.write("\nC#")

window.mainloop()
