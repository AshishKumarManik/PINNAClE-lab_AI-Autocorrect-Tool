import tkinter as tk
from tkinter import messagebox
from textblob import TextBlob
import language_tool_python

# this is a simple GUI application that uses TextBlob for spelling correction and LanguageTool for grammar correction....
tool = language_tool_python.LanguageTool('en-US')

def correct_text():
    user_input = input_text.get("1.0", tk.END).strip()
    
    if not user_input:
        messagebox.showwarning("Input Error", "Please enter some text to correct.")
        return

    # it will correct spelling errors in the input text by using TextBlob....
    blob = TextBlob(user_input)
    spelling_corrected = str(blob.correct())

    # it will correct grammar errors in the input text by using LanguageTool....
    matches = tool.check(spelling_corrected)
    final_text = language_tool_python.utils.correct(spelling_corrected, matches)

    # it will display the corrected text in the output text area....
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, final_text)

# it will create the main window for the GUI application....
root = tk.Tk()
root.title("AI Autocorrect Tool")
root.geometry("700x500")
root.resizable(False, False)

# this is the GUI layout with labels, text areas, and buttons....
title_label = tk.Label(root, text="AI Autocorrect Tool", font=("Helvetica", 18, "bold"))
title_label.pack(pady=10)

input_label = tk.Label(root, text="Enter text:", font=("Helvetica", 12))
input_label.pack()

input_text = tk.Text(root, height=8, width=80, font=("Consolas", 11))
input_text.pack(pady=5)

correct_button = tk.Button(root, text="Correct Text", command=correct_text, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"))
correct_button.pack(pady=10)

output_label = tk.Label(root, text="Corrected text:", font=("Helvetica", 12))
output_label.pack()

output_text = tk.Text(root, height=8, width=80, font=("Consolas", 11), fg="blue")
output_text.pack(pady=5)

# it will run the main loop of the GUI application....
root.mainloop()
