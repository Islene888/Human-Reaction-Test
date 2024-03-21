import tkinter as tk
from tkinter import ttk, messagebox
import json
import subprocess

def save_and_launch_test():
    # Check if the name field is empty
    if not name_entry.get().strip():
        messagebox.showerror("Missing Information", "Name is a required field. Please enter your name.")
        return
    if not input_method_var.get().strip():
        messagebox.showerror("Missing Information",
                             "Preferred Input Method is a required field. Please select an input method.")
        return
    if not level_var.get().strip():
        messagebox.showerror("Missing Information", "Test Level is a required field. Please select a test level.")
        return

    user_info = {
        "name": name_entry.get().strip(),
        "gender": gender_var.get(),
        "education": education_entry.get(),
        "age": age_entry.get(),
        "underlying_conditions": conditions_entry.get(),
        "color_blind": color_blind_var.get(),
        "vision": vision_entry.get(),
        "input_method": input_method_var.get(),
        "level": level_var.get()
    }

    with open('user_settings.json', 'w') as f:
        json.dump(user_info, f, indent=4)

    # Launch the test based on the selected level
    level_script = f"level_{level_var.get().lower()}_user_preferences.py"
    try:
        subprocess.run(["python", level_script], check=True)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Failed to launch the test: {str(e)}")
        return  # Return to avoid closing the window in case of error

    root.destroy()

root = tk.Tk()
root.title("User Setup for Reaction Time Test")

# Creating form fields
ttk.Label(root, text="*Name:").grid(row=0, column=0, padx=10, pady=10)
name_entry = ttk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=10)

ttk.Label(root, text="Gender:").grid(row=1, column=0, padx=10, pady=10)
gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(root, textvariable=gender_var, values=["Male", "Female", "Other"])
gender_combobox.grid(row=1, column=1, padx=10, pady=10)

ttk.Label(root, text="Education Level:").grid(row=2, column=0, padx=10, pady=10)
education_entry = ttk.Entry(root)
education_entry.grid(row=2, column=1, padx=10, pady=10)

ttk.Label(root, text="Age:").grid(row=3, column=0, padx=10, pady=10)
age_entry = ttk.Entry(root)
age_entry.grid(row=3, column=1, padx=10, pady=10)

ttk.Label(root, text="Underlying Health Conditions:").grid(row=4, column=0, padx=10, pady=10)
conditions_entry = ttk.Entry(root)
conditions_entry.grid(row=4, column=1, padx=10, pady=10)

ttk.Label(root, text="Color Blind (Yes/No):").grid(row=5, column=0, padx=10, pady=10)
color_blind_var = tk.StringVar()
color_blind_combobox = ttk.Combobox(root, textvariable=color_blind_var, values=["Yes", "No"])
color_blind_combobox.grid(row=5, column=1, padx=10, pady=10)

ttk.Label(root, text="Vision (e.g., normal, glasses):").grid(row=6, column=0, padx=10, pady=10)
vision_entry = ttk.Entry(root)
vision_entry.grid(row=6, column=1, padx=10, pady=10)

ttk.Label(root, text="*Preferred Input Method:").grid(row=7, column=0, padx=10, pady=10)
input_method_var = tk.StringVar()
input_method_combobox = ttk.Combobox(root, textvariable=input_method_var, values=["buttons", "keyboard"])
input_method_combobox.grid(row=7, column=1, padx=10, pady=10)

ttk.Label(root, text="*Test Level (A/B/C/D):").grid(row=8, column=0, padx=10, pady=10)
level_var = tk.StringVar()
level_combobox = ttk.Combobox(root, textvariable=level_var, values=["A", "B", "C", "D"])
level_combobox.grid(row=8, column=1, padx=10, pady=10)

# Save button
save_button = ttk.Button(root, text="Save and Start Test", command=save_and_launch_test)
save_button.grid(row=9, column=1, padx=10, pady=10)

root.mainloop()
