import tkinter as tk
from tkinter import messagebox

# Sample in-memory data structure to hold registration information
registration_data = []

def submit_form():
    full_name = entry_full_name.get()
    course = entry_course.get()
    matric_number = entry_matric_number.get()
    email = entry_email.get()
    activity = activity_var.get()
    gender = gender_var.get()  # Retrieve selected gender
    additional_info = text_additional_info.get("1.0", "end-1c")

    # Validation (you can add more validation as needed)
    if not full_name or not course or not matric_number or not email or not activity or not gender:
        messagebox.showerror("Error", "Please fill in all required fields.")
    else:
        registration_data.append({
            "Full Name": full_name,
            "Course": course,
            "Matric Number": matric_number,
            "Email": email,
            "Activity": activity,
            "Gender": gender,  # Add gender to the registration data
            "Additional Info": additional_info
        })
        messagebox.showinfo("Success", "Form submitted successfully!")
        clear_fields()

def delete_data():
    selected_index = listbox.curselection()
    if selected_index:
        index = selected_index[0]
        del registration_data[index]
        messagebox.showinfo("Deleted", "Selected data has been deleted.")
        show_registered_data()

def update_data():
    selected_index = listbox.curselection()
    if selected_index:
        index = selected_index[0]
        full_name = entry_full_name.get()
        course = entry_course.get()
        matric_number = entry_matric_number.get()
        email = entry_email.get()
        activity = activity_var.get()
        gender = gender_var.get()  # Retrieve selected gender
        additional_info = text_additional_info.get("1.0", "end-1c")

        # Validation
        if not full_name or not email or not activity or not gender:
            messagebox.showerror("Error", "Please fill in all required fields.")
        else:
            registration_data[index] = {
                "Full Name": full_name,
                "Course": course,
                "Matric Number": matric_number,
                "Email": email,
                "Activity": activity,
                "Gender": gender,  # Update gender in the registration data
                "Additional Info": additional_info
            }
            messagebox.showinfo("Updated", "Selected data has been updated.")
            show_registered_data()

def show_registered_data():
    listbox.delete(0, tk.END)
    for data in registration_data:
        listbox.insert(tk.END, f"{data['Full Name']} - {data['Course']} - {data['Matric Number']} - {data['Email']} - {data['Activity']} - {data['Gender']}")

def clear_fields():
    entry_full_name.delete(0, tk.END)
    entry_course.delete(0, tk.END)
    entry_matric_number.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    activity_var.set(activities[0])
    gender_var.set(genders[0])  # Set default gender value
    text_additional_info.delete("1.0", tk.END)

# Create main window
root = tk.Tk()
root.title("Co-curricular Registration Form")

# Load pattern image
pattern_image = tk.PhotoImage(file="c:\\Users\\Asus\\Desktop\\PYTHON\\sport.png") 

# Create a label with the pattern as the background
background_label = tk.Label(root, image=pattern_image)
background_label.place(x=0, y=0, relwidth=1.5, relheight=1.5)

# Create form elements
label_full_name = tk.Label (root, text="Full Name:", fg="purple", font=("Times", 14, "bold"))
label_full_name.pack()  # Adjust padding
entry_full_name = tk.Entry(root)
entry_full_name.pack()

label_course = tk.Label(root, text="Course:", fg="cyan", font=("Times", 14, "bold"))  
label_course.pack()
entry_course = tk.Entry(root)
entry_course.pack()

label_matric_number = tk.Label(root, text="Matric Number:",  fg="brown", font=("Times", 14, "bold"))  
label_matric_number.pack()
entry_matric_number = tk.Entry(root)
entry_matric_number.pack()

label_email = tk.Label(root, text="Email:", fg= "green", font=("Times", 14, "bold"))  
label_email.pack()
entry_email = tk.Entry(root)
entry_email.pack()

label_activity = tk.Label(root, text="Select Co-curricular Activity:", font=("Arial", 12))  
label_activity.pack()

activities = ["BADMINTON CLUB", "BASKETBALL CLUB", "FOOTBALL CLUB", "VOLLEYBALL CLUB", "TENNIS CLUB"]  
activity_var = tk.StringVar(root)
activity_var.set(activities[0])  # Default value
activity_dropdown = tk.OptionMenu(root, activity_var, *activities)
activity_dropdown.pack()

label_gender = tk.Label(root, text="Select Gender:", font=("Arial", 12))  
label_gender.pack()

genders = ["Male", "Female", "Other"]  # List of genders
gender_var = tk.StringVar(root)
gender_var.set(genders[0])  # Default value
gender_dropdown = tk.OptionMenu(root, gender_var, *genders)
gender_dropdown.pack()

label_additional_info = tk.Label(root, text="Additional Information:", font=("Arial", 12)) 
label_additional_info.pack()

text_additional_info = tk.Text(root, height=2, width=20) 
text_additional_info.pack()

submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.pack()

def open_view_window():
    view_window = tk.Toplevel(root)
    view_window.title("View Data")
    label = tk.Label(view_window, text="Registered Data:")
    label.pack()

    listbox_view = tk.Listbox(view_window, height=10, width=100)
    listbox_view.pack()

    for data in registration_data:
        listbox_view.insert(tk.END, f"{data['Full Name']} - {data['Course']} - {data['Matric Number']} - {data['Email']} - {data['Activity']} - {data['Gender']}")

# Listbox to display registered data
listbox = tk.Listbox(root, height=2, width=100)
listbox.pack()

# Buttons for delete, update, and view all data
delete_button = tk.Button(root, text="Delete", command=delete_data)
delete_button.pack()

update_button = tk.Button(root, text="Update", command=update_data)
update_button.pack()

view_all_button = tk.Button(root, text="View All Data", command=show_registered_data)
view_all_button.pack()

# Run the application
root.mainloop()
