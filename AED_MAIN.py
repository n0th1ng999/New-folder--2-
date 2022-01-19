import tkinter as tk

        self.data_folder = "InfoCursos\\"+self.Universidade+"\\"

#Get the current screen width and height
screen_width = Main.winfo_screenwidth()
screen_height = Main.winfo_screenheight()

#
greeting = tk.Label(text="Hello, Tkinter")
greeting.pack()

# setting attribute
Main.attributes('-fullscreen', True)
Main.resizable(False, False)
Main.title("")


Focus = tk.LabelFrame(Main, text='' , width= screen_width-200 , height = screen_height-200  , bg = '#fff' ,  borderwidth= 0, highlightcolor='#f43', highlightthickness= 0)
Focus.place(x = 200 , y = 200 )

SideNav = tk.LabelFrame(Main, text='' , width= 300 , height = screen_height-200  , bg = '#023' ,  borderwidth= 0, highlightcolor='#f43', highlightthickness= 0)
SideNav.place(x = 0 , y = 200 )
Navbar = tk.LabelFrame(Main, text='' , width= screen_width , height = 200  , bg='#f23',  borderwidth= 0 ,highlightcolor='#f23', highlightthickness= 0  )
Navbar.place(x = 0 , y= 0)





Main.mainloop()




