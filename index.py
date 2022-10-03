import tkinter as tk
from tkinter.filedialog import *
from photo_sorting import *
 
def open_dir_in():
    dir = askdirectory()
    if not dir:
        return
    lb1_dir['text'] = dir
    window.update()
 
def open_dir_out():
    dir = askdirectory()
    if not dir:
        return
    lb2_dir['text'] = dir
    window.update()

def do_it():
    message = ''
    if lb1_dir['text'] == '...' or lb2_dir['text'] == '...':
        if lb1_dir['text'] == '...':
            message += 'Укажите каталог, откуда брать фотографии.\n '
        if lb2_dir['text'] == '...':
            message += 'Укажите каталог, куда складывать фотографии' 
        lb3['text'] = message
        window.update()
        return
    lb3['text'] = 'Выполняется'
    window.update()
    main(lb1_dir['text'], lb2_dir['text'])
    lb3['text'] = 'Готово!'
    window.update()


window = tk.Tk()
window.geometry('800x300')
window.resizable(height=False, width=False)
window.title('Сортировка фотографий')

frm1 = tk.Frame(master=window, relief=tk.GROOVE, borderwidth=1, width=800, height=100)
frm1.pack()
btn1 = tk.Button(master=frm1, width=10, height=5, text='Выбрать', bg='light grey', command=open_dir_in)
btn1.place(x = 45, rely = 0.5, anchor=tk.CENTER)
lb1 = tk.Label(master=frm1, text='Откуда взять фотографии:')
lb1.place(relx = 0.55, rely = 0.2, anchor=tk.CENTER)
lb1_dir = tk.Label(master=frm1, text='...')
lb1_dir.place(relx = 0.55, rely = 0.7, anchor=tk.CENTER)


frm2 = tk.Frame(master=window, relief=tk.GROOVE, borderwidth=1, width=800, height=100)
frm2.pack()
btn2 = tk.Button(master=frm2, width=10, height=5, text='Выбрать', bg='light grey', command=open_dir_out)
btn2.place(x = 45, rely = 0.5, anchor=tk.CENTER)
lb2 = tk.Label(master=frm2, text='Куда положить фотографии')
lb2.place(relx = 0.55, rely = 0.2, anchor=tk.CENTER)
lb2_dir = tk.Label(master=frm2, text='...')
lb2_dir.place(relx = 0.55, rely = 0.7, anchor=tk.CENTER)


frm3 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=5, width=800, height=100, bg = 'snow2')
frm3.pack()
lb3 = tk.Label(master=frm3, text='', width=80, height=5, fg='red', bg = 'snow2')
lb3.place(relx = 0.36, rely = 0.5, anchor=tk.CENTER)
btn3 = tk.Button(master=frm3, width=20, height=5, text='Запустить', bg='light grey', command=do_it)
btn3.place(relx = 0.9, rely = 0.5, anchor=tk.CENTER)




window.mainloop()













 
# def open_file():
#     """Открываем файл для редактирования"""
#     filepath = askdirectory()
    
#     if not filepath:
#         return
#     # txt_edit.delete("1.0", tk.END)
#     # with open(filepath, "r") as input_file:
#     #     text = input_file.read()
#     #     txt_edit.insert(tk.END, text)
#     # window.title(f"Простой текстовый редактор - {filepath}")
 
 
# window = tk.Tk()
# window.title("Простой текстовый редактор")
 
# window.rowconfigure(0, minsize=800, weight=1)
# window.columnconfigure(1, minsize=800, weight=1)
 
# # txt_edit = tk.Text(window)
# fr_buttons = tk.Frame(window)
# btn_open = tk.Button(fr_buttons, text="Открыть", command=open_file)
# dir1 = tk.Label(window, text='jgjgjgjjg')
# btn_save = tk.Button(fr_buttons, text="Сохранить как...")
 
# btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
# dir1.grid(row=0, column=0, sticky="ew")
# btn_save.grid(row=1, column=0, sticky="ew", padx=5)
 
# fr_buttons.grid(row=0, column=0, sticky="ns")
# # txt_edit.grid(row=0, column=1, sticky="nsew")
 
# print(dir())

# window.mainloop()