import tkinter as tk
from tkinter import ttk
import random

# GUI window setup
root = tk.Tk()
root.title("Binary Search Visualization")
root.geometry("800x600")
root.configure(bg='lightblue')

# Function for binary search algorithm
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        # Check if x is greater, move to right half subarray
        if arr[mid] < x:
            low = mid + 1

        # Check if x is smaller, move to left half subarray
        elif arr[mid] > x:
            high = mid - 1

        # X is present at mid
        else:
            return mid

    # Element is not present in array
    return -1

#heading
heading = tk.Label(root, text="Binary Search Visualization", font=("Helvetica", 35, "bold"), foreground="Blue", background="Light Blue")
heading.grid(row=0, column=0, columnspan=8, pady=10)

# Function to update color of searched box
def update_color(index, color):
    boxes[index].configure(bg=color)

# Function to reset color of boxes
def reset_colors():
    for box in boxes:
        box.configure(bg="orange")

# Function to search for a number in the array
def search():
    # Get the value to search
    search_value = int(search_entry.get())

    # Get the array to search in
    arr = [int(box.get()) for box in boxes]

    # Run binary search on the array
    result = binary_search(arr, search_value)

    # Reset the colors of all boxes
    reset_colors()

    # If the number was found, update color of box
    if result != -1:
        update_color(result, "green")
        result_label.config(text="Index: {}".format(result))
    else:
        result_label.config(text="Number not found.")

# User input boxes for array
boxes = []
for i in range(8):
    box = tk.Entry(root, width=10)
    box.grid(row=2, column=i%8, padx=10, pady=10)
    boxes.append(box)
for i in range(7):
    box2 = tk.Entry(root, width=10)
    box2.grid(row=3, column=i%7, padx=10, pady=12)
    boxes.append(box2)

# Search entry
search_entry = tk.Entry(root, width=20, font=(18))
search_entry.grid(row=4, column=0, columnspan=8, pady=10)
search_entry.configure(bg='yellow')

# Search button
search_button = ttk.Button(root, text="Search", command=search, width=20)
search_button.grid(row=5, column=0, columnspan=8, pady=10)

# Result label
result_label = tk.Label(root, text="", background="light blue")
result_label.grid(row=8, column=0, columnspan=8, pady=10)

# Start GUI event loop
root.mainloop()
