import os
from tkinter import Tk, Text, Menu, Scrollbar, N, S, E, W, RIGHT, Y, END
from tkinter.messagebox import showinfo
from tkinter.filedialog import asksaveasfilename, askopenfilename


class RightClicker:
    def __init__(self, event):
        right_click_menu = Menu(None, tearoff=0, takefocus=0)

        for txt in ['Cut', 'Copy', 'Paste']:
            right_click_menu.add_command(
                label=txt, command=lambda event=event, text=txt:
                self.right_click_command(event, text))

        right_click_menu.tk_popup(event.x_root, event.y_root, entry='0')

    def right_click_command(self, event, cmd):
        event.widget.event_generate(f'<<{cmd}>>')


class Notepad:

    def __init__(self, **kwargs):
        self.file_name = None
        self.root = Tk()
        self.root.title("Untitled - Notepad")
        self.text_area = Text(self.root)

        menu_bar = Menu(self.root)
        file_menu = Menu(menu_bar, tearoff=0)
        edit_menu = Menu(menu_bar, tearoff=0)
        help_menu = Menu(menu_bar, tearoff=0)
        self.root.config(menu=menu_bar)

        scrollbar = Scrollbar(self.text_area)
        scrollbar.pack(side=RIGHT, fill=Y)
        scrollbar.config(command=self.text_area.yview)
        self.text_area.config(yscrollcommand=scrollbar.set)

        self.text_area.bind('<Button-3>', RightClicker)

        # set icon and window size (default is 300 x 300)
        try:
            self.root.wm_iconbitmap("Notepad.ico")
        except:   #pylint: disable=W0702
            pass

        try:
            width = kwargs['width']
        except KeyError:
            width = 300

        try:
            height = kwargs['height']
        except KeyError:
            height = 300

        # place notepad in the center of the screen
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        left = (screen_width / 2) - (width / 2)
        top = (screen_height / 2) - (height / 2)
        self.root.geometry('%dx%d+%d+%d' % (width, height, left, top))

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.text_area.grid(sticky=N + E + S + W)

        # file menu controls
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit_application)
        menu_bar.add_cascade(label="File", menu=file_menu)

        # edit menu controls
        edit_menu.add_command(label="Cut", command=self.cut_text)
        edit_menu.add_command(label="Copy", command=self.copy_text)
        edit_menu.add_command(label="Paste", command=self.paste_text)
        menu_bar.add_cascade(label="Edit", menu=edit_menu)

        # help menu controls
        help_menu.add_command(label="About Notepad", command=self.show_about)
        menu_bar.add_cascade(label="Help", menu=help_menu)

    def quit_application(self):
        self.root.destroy()

    def show_about(self):
        showinfo("Notepad", "Mrinal Verma")

    def open_file(self):
        self.file_name = askopenfilename(
            defaultextension=".txt",
            filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

        if self.file_name == "":
            self.file_name = None

        else:
            self.root.title(os.path.basename(self.file_name) + " - Notepad")
            self.text_area.delete(1.0, END)

            with open(self.file_name, 'r') as file:
                self.text_area.insert(1.0, file.read())

    def new_file(self):
        self.root.title("Untitled - Notepad")
        self.file_name = None
        self.text_area.delete(1.0, END)

    def save_file(self):
        if self.file_name is None:
            self.file_name = asksaveasfilename(
                initialfile='Untitled.txt', defaultextension=".txt",
                filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

            if self.file_name == "":
                self.file_name = None

            else:
                with open(self.file_name, 'w') as file:
                    file.write(self.text_area.get(1.0, END))

                self.root.title(os.path.basename(self.file_name) + " - Notepad")

        else:
            with open(self.file_name, 'w') as file:
                file.write(self.text_area.get(1.0, END))

    def cut_text(self):
        self.text_area.event_generate("<<Cut>>")

    def copy_text(self):
        self.text_area.event_generate("<<Copy>>")

    def paste_text(self):
        self.text_area.event_generate("<<Paste>>")

    def run_notepad(self):
        self.root.mainloop()


def main():
    notepad = Notepad(width=800, height=600)
    notepad.run_notepad()


if __name__ == '__main__':
    main()

