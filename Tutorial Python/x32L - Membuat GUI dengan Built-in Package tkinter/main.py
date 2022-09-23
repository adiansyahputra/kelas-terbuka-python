import tkinter
from tkinter import Pack, mainloop

main_window = tkinter.Tk()


def event_tekan():
    label2 = tkinter.Label(main_window, text="Akuh di tekan ^_^ ")
    label2.pack()


label = tkinter.Label(
    main_window, text="Halo, saya adalah \n GUI sederhana dengan \n menggunakan python")

tombol = tkinter.Button(main_window, text="tekan akuh", command=event_tekan)

main_window.mainloop()
label.pack()
