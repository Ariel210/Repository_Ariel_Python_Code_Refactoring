from tkinter import filedialog

road_2 = filedialog.askopenfilename(filetypes=(("test_text", "*.txt"),
                                               ("test_document","*.doc"),
                                               ("All Files", "*.*")))
print(road_2)

