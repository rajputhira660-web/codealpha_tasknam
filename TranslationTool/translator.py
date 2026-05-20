import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

# Translation Function
def translate_text():
    try:
        text = input_text.get("1.0", tk.END).strip()

        source = source_lang_var.get()
        target = target_lang_var.get()

        translated = GoogleTranslator(
            source=source,
            target=target
        ).translate(text)

        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated)

    except Exception as e:
        messagebox.showerror("Error", str(e))


# Main Window
root = tk.Tk()
root.title("Language Translation Tool")
root.geometry("600x500")

# Input Label
tk.Label(root, text="Enter Text").pack(pady=5)

# Input Text Box
input_text = tk.Text(root, height=5, width=60)
input_text.pack()

# Source Language
tk.Label(root, text="Source Language").pack(pady=5)

source_lang_var = tk.StringVar(value="english")

source_menu = ttk.Combobox(root, textvariable=source_lang_var)
source_menu['values'] = (
    "english",
    "urdu",
    "french",
    "spanish",
    "german"
)
source_menu.pack()

# Target Language
tk.Label(root, text="Target Language").pack(pady=5)

target_lang_var = tk.StringVar(value="urdu")

target_menu = ttk.Combobox(root, textvariable=target_lang_var)
target_menu['values'] = (
    "english",
    "urdu",
    "french",
    "spanish",
    "german"
)
target_menu.pack()

# Translate Button
translate_btn = tk.Button(
    root,
    text="Translate",
    command=translate_text
)
translate_btn.pack(pady=10)

# Output Label
tk.Label(root, text="Translated Text").pack(pady=5)

# Output Text Box
output_text = tk.Text(root, height=5, width=60)
output_text.pack()

# Run App
root.mainloop()