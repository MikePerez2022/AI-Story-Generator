# AI-Story-Generator

This is a user-friendly desktop application that uses local AI models to generate short, customizable stories based on user input. With a clean graphical interface, users can select from various genres, tones, styles, and lengths to create unique stories, which can then be saved for further use.

Built with `tkinter` and `customtkinter`, the app runs as a Windows executable and leverages local models through **Ollama**.

---

## Features

* **Genre, Tone, and Style Selection** – Customize story generation based on your preferences.
* **Language and Length Controls** – Choose the story's language and whether it should be short, medium, or long.
* **Prompt Field** – Enter a custom story idea or theme.
* **Model Selection** – Choose which LLM (e.g., `mistral`, `deepseek-llm`, `llama3`) to use.
* **Generate & Save** – Instantly generate stories and save them as `.txt` files.
* **Modern UI** – Simple, clean interface made with `customtkinter`.

---

## Technologies Used

* **Python 3.11**
* **tkinter** / **customtkinter**
* **Ollama (for local LLMs)**
* **PyInstaller** (for packaging as executable)

---

## Getting Started

### Option 1: Clone and Run with Python

```bash
git clone https://github.com/YourUsername/AIStoryGenerator.git
cd AIStoryGenerator
python Application.py
```

Make sure you have:

* Python 3.11 installed
* Ollama installed and running with your desired model (e.g. `mistral`)

---

### Option 2: Run the Standalone Executable

1. Download the pre-built `.exe` file from the [Releases](https://github.com/MikePerez2022/AI-Story-Generator/releases/tag/story-generator-v1).
2. Double-click to launch the app.
3. Make sure Ollama is installed and your model is pulled and running.

---

## How to Use

1. Select options for **Genre**, **Language**, **Tone**, **Length**, and **Style**.
2. Type a short custom prompt or theme.
3. Select the AI model you'd like to use.
4. Click **Generate** to create a story.
5. Click **Save** to export the story as a `.txt` file.

---

## Requirements

* **Windows OS**
* **Ollama installed** – [Download from ollama.com](https://ollama.com)
* **Model pulled and running:**

This app uses a local LLM accessed through Ollama. You must **pull the model manually before using the app**.

### ⚙️ First-time setup (example for Mistral):

* **Open up windows command prompt** - Type cmd into windows search bar
* **Run the command below once for each model** - Replace `model_name` with `mistral:instruct` or `deepseek-r1:latest`

```bash
ollama pull model_name
```

> ⚠️ If the model used hasn't been pulled or started, the app will not be able to generate stories.
