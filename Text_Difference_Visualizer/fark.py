import tkinter as tk
from tkinter import ttk
from difflib import SequenceMatcher

# Varsayılan renkler
DEFAULT_MATCH_COLOR = 'green'
DEFAULT_DIFF_COLOR = 'red'

def calculate_difference():
    text1 = text_box1.get("1.0", "end-1c")
    text2 = text_box2.get("1.0", "end-1c")

    matcher = SequenceMatcher(None, text1, text2)
    differences = list(matcher.get_opcodes())

    result_text.delete("1.0", tk.END)

    for tag, i1, i2, j1, j2 in differences:
        if tag == 'equal':
            result_text.insert(tk.END, text1[i1:i2], 'match_color')
        elif tag in ('delete', 'replace'):
            result_text.insert(tk.END, text1[i1:i2], 'diff_color')
        elif tag == 'insert':
            result_text.insert(tk.END, text2[j1:j2], 'diff_color')

def change_match_color():
    color = match_color_var.get()
    result_text.tag_configure('match_color', foreground=color)

def change_diff_color():
    color = diff_color_var.get()
    result_text.tag_configure('diff_color', foreground=color)

# Tkinter penceresi oluşturuluyor
window = tk.Tk()
window.title("Text Difference Calculator")

# İlk metin kutusu
label1 = tk.Label(window, text="Text 1:")
label1.grid(row=0, column=0, padx=10, pady=10)

text_box1 = tk.Text(window, height=5, width=50)
text_box1.grid(row=0, column=1, padx=10, pady=10)

# İkinci metin kutusu
label2 = tk.Label(window, text="Text 2:")
label2.grid(row=1, column=0, padx=10, pady=10)

text_box2 = tk.Text(window, height=5, width=50)
text_box2.grid(row=1, column=1, padx=10, pady=10)

# Farkı gösteren metin kutusu
result_label = tk.Label(window, text="Difference:")
result_label.grid(row=2, column=0, padx=10, pady=10)

result_text = tk.Text(window, height=5, width=50)
result_text.grid(row=2, column=1, padx=10, pady=10)

# Farkı hesapla düğmesi
calculate_button = tk.Button(window, text="Calculate Difference", command=calculate_difference)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

# Renk ayarları
result_text.tag_configure('match_color', foreground=DEFAULT_MATCH_COLOR)
result_text.tag_configure('diff_color', foreground=DEFAULT_DIFF_COLOR)

# Ayarlar menüsü
settings_frame = ttk.LabelFrame(window, text="Settings")
settings_frame.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky='we')

# Eşleşen kısımlar için renk ayarı
match_color_var = tk.StringVar(value=DEFAULT_MATCH_COLOR)
match_color_label = ttk.Label(settings_frame, text="Match Color:")
match_color_label.grid(row=0, column=0, padx=5, pady=5)
match_color_entry = ttk.Entry(settings_frame, textvariable=match_color_var)
match_color_entry.grid(row=0, column=1, padx=5, pady=5)
match_color_button = ttk.Button(settings_frame, text="Set", command=change_match_color)
match_color_button.grid(row=0, column=2, padx=5, pady=5)

# Farklı kısımlar için renk ayarı
diff_color_var = tk.StringVar(value=DEFAULT_DIFF_COLOR)
diff_color_label = ttk.Label(settings_frame, text="Difference Color:")
diff_color_label.grid(row=1, column=0, padx=5, pady=5)
diff_color_entry = ttk.Entry(settings_frame, textvariable=diff_color_var)
diff_color_entry.grid(row=1, column=1, padx=5, pady=5)
diff_color_button = ttk.Button(settings_frame, text="Set", command=change_diff_color)
diff_color_button.grid(row=1, column=2, padx=5, pady=5)

# Tkinter penceresini başlat
window.mainloop()
