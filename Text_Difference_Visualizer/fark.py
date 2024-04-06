import tkinter as tk
from difflib import SequenceMatcher

def calculate_difference():
    text1 = text_box1.get("1.0", "end-1c")
    text2 = text_box2.get("1.0", "end-1c")

    matcher = SequenceMatcher(None, text1, text2)
    match = matcher.find_longest_match(0, len(text1), 0, len(text2))

    result_text.delete("1.0", tk.END)

    # Aynı olan kısımları yeşil renkte ekle
    result_text.tag_configure('green', foreground='green')
    result_text.insert(tk.END, text1[:match.a], 'red')
    result_text.insert(tk.END, text1[match.a:match.a + match.size], 'green')

    # Farklı olan kısımları kırmızı renkte ekle
    result_text.tag_configure('red', foreground='red')
    result_text.insert(tk.END, text1[match.a + match.size:], 'red')

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

# Tkinter penceresini başlat
window.mainloop()
