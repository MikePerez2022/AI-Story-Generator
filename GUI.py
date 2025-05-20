import customtkinter as ctk;

def CreateGUI():
    window = ctk.CTk()
    window.title("Code Auto Commenter")
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")
    window.geometry("800x520")
    lable = ctk.CTkLabel(window, text="AI Code Commenter", anchor="center")
    lable.pack()
    
    filePath = ctk.CTkEntry(window, width=500, placeholder_text="Enter Story parameters")
    filePath.pack(pady=10)
    
    selectFile = ctk.CTkButton(window, text="Update AI prompt")
    selectFile.pack()
    
    display = ctk.CTkTextbox(window, wrap="word", text_color="orange")
    display.pack(pady=10, padx=20, fill="both", expand=True)
    
    displayBtn = ctk.CTkButton(window, text="Generate story")
    displayBtn.pack(pady=20)
    
    AIComment = ctk.CTkButton(window, text="Select download location")
    AIComment.pack(pady=20)
    
    downloadBtn = ctk.CTkButton(window, text="Download as file")
    downloadBtn.pack(pady=20)
    
    window.mainloop()


CreateGUI()