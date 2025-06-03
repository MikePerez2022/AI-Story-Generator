import FileSystem as fs
import StoryGenerator as sg
import customtkinter as ctk
import threading

def CreateGUI():
    window = ctk.CTk()
    window.title("AI Story Generator")
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")
    window.geometry("800x600")

    label = ctk.CTkLabel(window, text="AI Story Generator", font=("Arial", 20, "bold"), anchor="center")
    label.pack(pady=10)

    prompt = ctk.CTkEntry(window, width=600, placeholder_text="Enter your custom story prompt")
    prompt.pack(pady=10)
    
    dropdown_frame = ctk.CTkFrame(window)
    dropdown_frame.pack(pady=10)

    genre = ctk.StringVar(value="Fantasy")
    genre_dropdown = ctk.CTkOptionMenu(dropdown_frame, variable=genre, values=["Fantasy", "Sci-Fi", "Mystery", "Horror", "Romance", "Adventure"])
    genre_dropdown.grid(row=0, column=0, padx=5)
    
    language = ctk.StringVar(value="English")
    language_dropdown = ctk.CTkOptionMenu(dropdown_frame, variable=language, values=["English", "Spanish", "French"])
    language_dropdown.grid(row=0, column=1, padx=5)

    audience = ctk.StringVar(value="General")
    audience_dropdown = ctk.CTkOptionMenu(dropdown_frame, variable=audience, values=["Adults", "Teens", "Children", "General"])
    audience_dropdown.grid(row=0, column=2, padx=5)

    length = ctk.StringVar(value="Short")
    length_dropdown = ctk.CTkOptionMenu(dropdown_frame, variable=length, values=["Short", "Medium", "Long"])
    length_dropdown.grid(row=0, column=3, padx=5)

    style = ctk.StringVar(value="Descriptive")
    style_dropdown = ctk.CTkOptionMenu(dropdown_frame, variable=style, values=["Descriptive", "Dialog-Heavy", "Action-Packed", "Humorous", "Dark", "Whimsical"])
    style_dropdown.grid(row=0, column=4, padx=5)
    
    model_frame = ctk.CTkFrame(window)
    model_frame.pack(pady=10)
    
    model_label = ctk.CTkLabel(model_frame, text="AI Model:")
    model_label.grid(row=0, column=0, padx=5)
    
    model = ctk.StringVar(value="mistral:instruct")
    model_dropdown = ctk.CTkOptionMenu(model_frame, variable=model, values=["mistral:instruct", "deepseek-r1"])
    model_dropdown.grid(row=0, column=1, padx=5)

    display = ctk.CTkTextbox(window, wrap="word", text_color="white")
    display.pack(pady=10, padx=20, fill="both", expand=True)
    
    actions_frame = ctk.CTkFrame(window)
    actions_frame.pack(pady=20)

    generate_btn = ctk.CTkButton(actions_frame, text="Generate Story", command=lambda: GenerateStory(prompt.get(), language.get(), genre.get(), audience.get(), length.get(), style.get(), display, model.get()))
    generate_btn.grid(row=0, column=0, padx=5)

    download_btn = ctk.CTkButton(actions_frame, text="Download Story as .txt", command=lambda: fs.DownloadFileGUI("AI_Story", display.get(0.0, ctk.END)))
    download_btn.grid(row=0, column=1, padx=5)

    clear_btn = ctk.CTkButton(actions_frame, text="Clear Output", command=lambda: display.delete(1.0, ctk.END))
    clear_btn.grid(row=0, column=2, padx=5)

    window.mainloop()

def GenerateStory(prompt, Language, genre, audience, length, style, display, name):
    print("Prompting...")
    full_prompt = f"Boundaries: Don't generate anything harmful or inappropriate in a college setting, Language: {Language}, Genre: {genre}, Audience: {audience}, Length: {length}, Writing Style: {style}\nPrompt: {prompt}"
    print("Prompt created.")
    display.delete(1.0, ctk.END)

    def stream_to_display():
        for chunk in sg.stream_generate(full_prompt, name):
            if chunk:
                display.insert(ctk.END, chunk)
                display.update_idletasks()
        print("Story displayed.")

    threading.Thread(target=stream_to_display, daemon=True).start()

CreateGUI()