import tkinter as tk

def greeting():
    print('Hello stdout world!...')

def main():
    root = tk.Tk()   
    root.title('Exemplo Pratico 13')
    win = tk.Frame(root)
    win.pack()
    
    tk.Label(win, text='Label txt').pack(side=tk.RIGHT) 
    tk.Entry(win).pack(side=tk.LEFT) 
    
    tk.Button(win, text='Alterar', command=root.quit).pack(side=tk.RIGHT,anchor=tk.S)
    tk.Button(win, text='Limpar', command=root.quit).pack(side=tk.LEFT)
    text_content = tk.Entry.get('1.0','end')
    tk.Button(win, text='Quit', command=root.quit).pack(side=tk.LEFT)
    root.mainloop()

if __name__ == '__main__':
    main()

