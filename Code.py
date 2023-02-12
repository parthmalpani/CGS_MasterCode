import tkinter as tk
import tkinter.ttk as ttk
import random

# Creating the main window
root = tk.Tk()
root.title("Binary Search with GUI")
root.geometry("500x500")
root.configure(bg="#E5E5E5")

# Function to perform binary search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return None

# Function to display the result of binary search
def display_result(index, color):
    result_label.config(text="Index: {}".format(index), font=("Helvetica", 16), bg="#E5E5E5")
    for i in range(15):
        if i == index:
            boxes[i].config(bg=color)
        else:
            boxes[i].config(bg="#FFFFFF")

# Function to handle the button click event
def search():
    # Get the value entered by the user
    target = int(input_entry.get())

    # Call the binary search function
    index = binary_search(numbers, target)

    # Check if the target was found
    if index is None:
        display_result(None, "#FF0000")
    else:
        display_result(index, "#00FF00")

# Input label
input_label = tk.Label(root, text="Enter the number:", font=("Helvetica", 16), bg="#E5E5E5")
input_label.pack(pady=20)

# Input entry
input_entry = tk.Entry(root, font=("Helvetica", 16))
input_entry.pack(pady=10)

# Search button
search_button = tk.Button(root, text="Search", font=("Helvetica", 16), command=search)
search_button.pack(pady=10)

# Result label
result_label = tk.Label(root, font=("Helvetica", 16), bg="#E5E5E5")
result_label.pack(pady=20)

# Generate random numbers
numbers = random.sample(range(100), 15)

# Create a list of rectangles to represent the numbers
boxes = []
for i in range(15):
    box = tk.Label(root, width=5, height=2, bg="#FFFFFF", font=("Helvetica", 16), text=str(numbers[i]), relief="solid")
    box.pack(side="left", padx=10)
    boxes.append(box)

# Display the main window
root.mainloop()
