import customtkinter as ctk
import tkinter as tk
from menubar import menubar
import os
import re

current_file = 'Untitled'
current_file_saved = True
buffers = []
python_keywords = {
    "purple": ['import', 'as', 'from', 'with', 'if', 'else', 'elif', 'for'],
    "blue": ['True', 'False', 'def', 'lambda', 'None', 'global']
}

def checkFileSaved():
    global current_file_saved
    if current_file == 'Untitled' and len(textarea.get('1.0', tk.END)) > 0:
        current_file_saved = False
    if current_file_saved:
        # check if textarea content matches the file content
        with open(current_file, 'r') as file:
            if file:
                if not file.read() == textarea.get('1.0', tk.END):
                    current_file_saved = False
                    print('Set flag to false because textarea content != file content')
            else:
                current_file_saved = False
                print('set flag to false because file does not exist yet')

def newFile():
    if current_file_saved:
        pass
    else:
        tk.messagebox.showwarning('File not saved', 'Your current file is not saved')

def openFile():
    global current_file_saved
    print("Opening file")
    with tk.filedialog.askopenfile(initialdir = os.getcwd(), title = "Open file", filetypes = (("all files", "*.*"),)) as file:
        if file:
            file_content = file.read()
            # open a new buffer
            buffers.append(
                os.path.basename(file.name)
            )
            # add buffer to buffer_tab
            file_buffer = ctk.CTkFrame(bt_frame, corner_radius=0)
            bt_file = ctk.CTkButton(file_buffer, text=os.path.basename(file.name), corner_radius=0,
            command = lambda : displayFileOntoTextArea(
                file.name,
                file_content
            ))
            bt_cross = ctk.CTkButton(file_buffer, text="❌", corner_radius=0, width=40, fg_color='#ab242d', hover_color='#7d292f', command= lambda file_buffer : (
                closeBuffer(file_buffer)
            ))
            
            bt_file.pack(side="left", padx=(5,0), pady=1)
            bt_cross.pack(side="left", pady=1)
            file_buffer.pack(side="left", before=bt_plus)


            textarea.delete('1.0', tk.END)
            textarea.insert(tk.END, file_content)

            global current_file
            current_file = file.name
            sb_file_label.configure(text=current_file)
            current_file_saved = True

            syntaxHighlighting()

def displayFileOntoTextArea(filename, file_content):
    textarea.delete('1.0', tk.END)
    textarea.insert(tk.END, file_content)
    global current_file
    current_file = filename
    syntaxHighlighting()

def saveFile():
    if current_file:
        with open(current_file, 'w') as file:
            if file:
                content_to_write = textarea.get('1.0', tk.END)
                file.write(content_to_write)
                sb_file_label.configure(text=f"Saved {current_file}")
                global current_file_saved
                current_file_saved = True
            else:
                print("File does not exist, it may have been deleted or moved")
    else:
        # print("You need to save as")
        pass

def closeBuffer(file_buffer):
    textarea.delete('1.0', tk.END)
    file_buffer.pack_forget()

def syntaxHighlighting():
    
    file = os.path.basename(current_file)
    ext = os.path.splitext(file)[1]
    if ext == '.py':
        
        textarea.mark_set("matchStart", "1.0")
        textarea.mark_set("matchEnd", "1.0")
        textarea.tag_remove("purple", "1.0", "end")
        textarea.tag_remove("blue", "1.0", "end")
        textarea.tag_remove("yellow", "1.0", "end")
        textarea.tag_remove("red", "1.0", "end")
        textarea.tag_remove("lightblue", "1.0", "end")
        textarea.tag_remove("grey", "1.0", "end")
        data = textarea.get("1.0", "end-1c")

        for color, words in python_keywords.items():
            for word in words:
                matches = re.finditer(r'\b' + re.escape(word) + r'\b', data)
                for match in matches:
                    start_index = f"1.0+{match.start()}c"
                    end_index = f"1.0+{match.end()}c"
                    textarea.tag_add(color, start_index, end_index)
        
        matches = re.finditer(r'(["\'])(.*?)\1', data)
        for match in matches:
            start_index = f"1.0+{match.start()}c"
            end_index = f"1.0+{match.end()}c"
            textarea.tag_add("yellow", start_index, end_index)

        class_function_pattern = r'\b(?:class|def)\s+([a-zA-Z_]\w*)\s*\('
        matches = re.finditer(class_function_pattern, data)
        for match in matches:
            start_index = f"1.0+{match.start(1)}c"
            end_index = f"1.0+{match.end(1)}c"
            textarea.tag_add("red", start_index, end_index)
        
        keyword_arguments_pattern = r'\b(\w+)\s*=\s*'
        matches = re.finditer(keyword_arguments_pattern, data)
        for match in matches:
            start_index = f"1.0+{match.start(1)}c"
            end_index = f"1.0+{match.end(1)}c"
            textarea.tag_add("lightblue", start_index, end_index)
        
        comment_pattern = r'#.*?$'
        matches = re.finditer(comment_pattern, data, re.MULTILINE)
        for match in matches:
            start_index = f"1.0+{match.start()}c"
            end_index = f"1.0+{match.end()}c"
            textarea.tag_add("grey", start_index, end_index)

def changeAppearance():
    if ctk.get_appearance_mode() == 'Light':
        ctk.set_appearance_mode('dark')
    else:
        ctk.set_appearance_mode('light')

window = ctk.CTk()
window.title("Ojas Editor")
window.geometry("800x500")
ctk.set_appearance_mode('dark')

# Tags for syntax highlighting


bt_frame = ctk.CTkFrame(window, corner_radius=0)
buffer = ctk.CTkFrame(bt_frame, corner_radius=0)
bt_untitled = ctk.CTkButton(buffer, text="Untitled", corner_radius=0)
bt_cross = ctk.CTkButton(buffer, text="❌", corner_radius=0, width=40, fg_color='#ab242d', hover_color='#7d292f')
bt_plus = ctk.CTkButton(bt_frame, text="➕", corner_radius=0, width=40, fg_color='#26ad26', hover_color='#2a802a')
bt_untitled.pack(side="left", padx=(5,0), pady=1)
buffers.append(
    "untitled"
)
bt_cross.pack(side="left", pady=1)
buffer.pack(side="left")
bt_plus.pack(side="left", padx=5 , pady=1)
bt_frame.pack(fill="x")

textarea = ctk.CTkTextbox(window, border_width=1, border_color=('black', 'white'), font=("Courier", 20))
textarea.pack(expand=True, fill="both", padx=5, pady=2)
textarea.focus()
textarea.bind('<KeyRelease>', lambda x : checkFileSaved())
textarea.bind('<KeyRelease>', lambda x : syntaxHighlighting())

textarea.tag_config("purple", foreground='purple')
textarea.tag_config("blue", foreground='blue')
textarea.tag_config("yellow", foreground='yellow')
textarea.tag_config("red", foreground='red')
textarea.tag_config("lightblue", foreground='lightblue')
textarea.tag_config("grey", foreground='grey')

command_dict = {
    "new_file": newFile,
    "open_file": openFile,
    "save_as": None,
    "save": saveFile,
    "change_appearance": changeAppearance
}

menubar(window, command_dict)

sb_frame = ctk.CTkFrame(window, fg_color='#4a4842', corner_radius=0)
sb_file_label = ctk.CTkLabel(sb_frame, text = current_file or "Ready", text_color='white')
sb_file_label.pack(side="right", padx=10)
sb_frame.pack(fill="x")

window.mainloop()

