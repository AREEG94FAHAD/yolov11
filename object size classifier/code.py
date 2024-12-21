import tkinter as tk
from tkinter import filedialog
import os
import matplotlib.pyplot as plt
from PIL import Image, ImageTk

def run_processing():
    # Get image size from input fields
    width = image_size_width_entry.get()
    height = image_size_height_entry.get()

    # Use default values if the input fields are empty or invalid
    if not width or not height or not width.isdigit() or not height.isdigit():
        width = 640
        height = 640
    else:
        width = int(width)
        height = int(height)

    # Run processing with the specified image size
    process_files(directory_entry.get(), width, height)

def browse_directory():
    directory = filedialog.askdirectory()
    if directory:
        directory_entry.delete(0, tk.END)  # Clear any previous text
        directory_entry.insert(tk.END, directory)

def process_files(directory, width, height):
    number_obj = 0
    small_obj = 0
    medium_obj = 0
    large_obj = 0
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r') as file:
                for line in file:
                    values = line.strip().split()
                    if values:
                        try:
                            number_obj += 1
                            w, h = map(float, values[-2:])
                            result = w * width * height * h
                            if result <= 32**2:
                                small_obj += 1
                            elif result > 32**2 and result < 96**2:
                                medium_obj += 1
                            elif result >= 96**2:
                                large_obj += 1
                        except ValueError:
                            print("Error processing line in {}: {}".format(filename, line))
    
    # Display final results
    result_text = "Total objects: {}\nSmall objects: {}\nMedium objects: {}\nLarge objects: {}".format(number_obj, small_obj, medium_obj, large_obj)
    result_label.config(text=result_text)

    # Create a bar chart
    labels = ['Small Objects', 'Medium Objects', 'Large Objects']
    values = [small_obj, medium_obj, large_obj]
    plt.figure(figsize=(6, 4))
    plt.bar(labels, values, color=['blue', 'orange', 'green'])
    plt.xlabel('Object Size')
    plt.ylabel('Count')
    plt.title('Object Size Distribution')
    plt.tight_layout()
    plt.savefig('object_size_distribution.png')  # Save the bar chart as an image
    plt.close()

    # Display the bar chart image
    img = Image.open('object_size_distribution.png')
    img.thumbnail((300, 300))
    img = ImageTk.PhotoImage(img)
    chart_label.config(image=img)
    chart_label.image = img

    # Enable or disable the save button based on result availability
    if number_obj > 0:
        save_button.config(state=tk.NORMAL)
    else:
        save_button.config(state=tk.DISABLED)

def save_image(file_path):
    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
    if save_path:
        img = Image.open(file_path)
        img.save(save_path)
        print("Image saved successfully.")

# Create tkinter window
root = tk.Tk()
root.title("ObjectSizeClassifier")
root.geometry("620x350")
root.iconbitmap('87578.ico')

# Set background color
root.configure(bg='#ffffff')

# Column 1: Directory selection button and entry
directory_frame = tk.Frame(root, bg='#ffffff')
directory_frame.pack(pady=10)

directory_label = tk.Label(directory_frame, text="Dir/", bg='#ffffff')
directory_label.grid(row=0, column=0, padx=(10, 5), sticky="w")

directory_entry = tk.Entry(directory_frame, width=70)
directory_entry.grid(row=0, column=1, padx=(0, 5))

browse_button = tk.Button(directory_frame, text="...", command=browse_directory)
browse_button.grid(row=0, column=2)

# Column 2: Image size
image_size_frame = tk.Frame(root, bg='#ffffff')
image_size_frame.pack(pady=5)

image_size_width_label = tk.Label(image_size_frame, text="Width:", bg='#ffffff')
image_size_width_label.grid(row=0, column=0, padx=(10, 5), sticky="w")

image_size_width_entry = tk.Entry(image_size_frame, width=10)
image_size_width_entry.grid(row=0, column=1, padx=(0, 5), sticky="w")

image_size_height_label = tk.Label(image_size_frame, text="Height:", bg='#ffffff')
image_size_height_label.grid(row=0, column=2, padx=(10, 5), sticky="w")

image_size_height_entry = tk.Entry(image_size_frame, width=10)
image_size_height_entry.grid(row=0, column=3, padx=(0, 5), sticky="w")

# Column 3: Statistical results
result_label = tk.Label(root, text="", anchor="w", justify="left", padx=20, pady=10, font=("Arial", 12), bg='#ffffff')
result_label.pack(side="left", fill="both", expand=True)

# Column 4: Bar chart
chart_frame = tk.Frame(root, bg='#ffffff')
chart_frame.pack(side="right", padx=20)

chart_label = tk.Label(chart_frame, bg='#ffffff')
chart_label.pack(pady=10)

# Run button
run_button = tk.Button(root, text="Run", command=run_processing)
run_button.pack(side="bottom", pady=5)

# Save button
save_button = tk.Button(root, text="Save Image", state=tk.DISABLED, command=lambda: save_image('object_size_distribution.png'))
save_button.pack(side="bottom", pady=5)

# Run the tkinter event loop
root.mainloop()
