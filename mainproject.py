import tkinter as tk
from tkinter import messagebox, OptionMenu
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import json

# Function to load employee data from EMP JSON file
def load_employee_data(file_path):
    with open(file_path, 'r') as file:
        employee_data = json.load(file)
    return employee_data

# Function to load events data from EVENT JSON file
def load_events_data(file_path):
    with open(file_path, 'r') as file:
        events_data = json.load(file)
    return events_data

# Function to display employee data GUI window
def show_employee_data_window(employee_data):
    employee_window = tk.Toplevel()
    employee_window.title("Employee Data")
    employee_window.configure(background="light blue")
    
    logo_img = Image.open("IWlogoleast.png")
    logo_photo = ImageTk.PhotoImage(logo_img)
    logo_label = tk.Label(employee_window, image=logo_photo)
    logo_label.image = logo_photo
    logo_label.pack()
    
    emp_id_label = tk.Label(employee_window, text="Enter Employee ID:")
    emp_id_label.pack()
    
    emp_id_entry = tk.Entry(employee_window)
    emp_id_entry.pack()

    options = ["Name", "Email", "Department", "Joining Date", "Year", "All Data"]
    selected_option = tk.StringVar(value=options[0])

    def search_employee():
        emp_id = emp_id_entry.get()
        for emp in employee_data:
            if emp["id"] == emp_id:
                selected_value = selected_option.get()
                if selected_value == "All Data":
                    info = ""
                    for key, value in emp.items():
                        info += f"{key}: {value}\n"
                    messagebox.showinfo("Employee Data", info)
                else:
                    info = emp[selected_value.lower()]
                    messagebox.showinfo("Employee Data", f"{selected_value}: {info}")
                break
        else:
            messagebox.showerror("Error", "Employee ID not found")

    for option in options:
        tk.Radiobutton(employee_window, text=option, variable=selected_option, value=option).pack(anchor=tk.W)
    
    search_button = tk.Button(employee_window, text="Search", command=search_employee)
    search_button.pack()

# Function to display joining month graph GUI window
def show_joining_month_graph_window(employee_data):
    graph_window = tk.Toplevel()
    graph_window.title("Joining Month Graph")
    graph_window.configure(background="light green")
    
    logo_img = Image.open("IWlogoleast.png")
    logo_photo = ImageTk.PhotoImage(logo_img)
    logo_label = tk.Label(graph_window, image=logo_photo)
    logo_label.image = logo_photo
    logo_label.pack()
    
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    department_counts = {dep: [0] * len(months) for dep in set(emp['department'] for emp in employee_data)}
    
    for emp in employee_data:
        month = int(emp['joining_date'].split('/')[0]) - 1
        department_counts[emp['department']][month] += 1
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    for i, (dep, counts) in enumerate(department_counts.items()):
        ax.plot(months, counts, label=dep)
    
    ax.set_xlabel('Months')
    ax.set_ylabel('Employee Count')
    ax.set_title('Joining Month Graph')
    ax.legend()
    
    plt.show()

# Function to display events information GUI window
def show_events_information_window(events_data):
    events_window = tk.Toplevel()
    events_window.title("Events Information")
    events_window.configure(background="light pink")
    
    logo_img = Image.open("IWlogoleast.png")
    logo_photo = ImageTk.PhotoImage(logo_img)
    logo_label = tk.Label(events_window, image=logo_photo)
    logo_label.image = logo_photo
    logo_label.pack()
    
    event_names = [event['name'] for event in events_data]
    
    selected_event = tk.StringVar(value=event_names[0])
    event_label = tk.Label(events_window, text="Enter Event Name:")
    event_label.pack()

    event_entry = tk.Entry(events_window, textvariable=selected_event)
    event_entry.pack()

    def show_event_details():
        event_name = selected_event.get()
        for event in events_data:
            if event['name'] == event_name:
                details = f"Event Name: {event['name']}\nDate: {event['date']}\nTime: {event['time']}\nParticipation Fee: {event['participation_fee']}"
                messagebox.showinfo("Event Details", details)
                break
        else:
            messagebox.showerror("Error", "Event not found")

    show_button = tk.Button(events_window, text="Show Details", command=show_event_details)
    show_button.pack()

    events_window.mainloop()

# Main function to create the main menu GUI window
def main():
    # Load employee data
    employee_data = load_employee_data("data.json")
    
    # Load events data
    events_data = load_events_data("event.json")
    
    # Create main menu GUI window
    main_window = tk.Tk()
    main_window.title("Menu")
    main_window.configure(background="light grey")
    
    
    # Add college image as background
    college_img = Image.open("collegenew.png")
    college_photo = ImageTk.PhotoImage(college_img)
    college_label = tk.Label(main_window, image=college_photo)
    college_label.image = college_photo
    college_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    logo_img = Image.open("IWlogoleast.png")
    logo_photo = ImageTk.PhotoImage(logo_img)
    logo_label = tk.Label(main_window, image=logo_photo)
    logo_label.image = logo_photo
    logo_label.pack()
    
    def option1():
        show_employee_data_window(employee_data)
    
    def option2():
        show_joining_month_graph_window(employee_data)
    
    def option4():
        show_events_information_window(events_data)
    
    button1 = tk.Button(main_window, text="Employee Data", command=option1, bg="light blue")
    button1.pack()
    
    button2 = tk.Button(main_window, text="Joining Month Graph", command=option2, bg="light green")
    button2.pack()
    
    button4 = tk.Button(main_window, text="Events Information", command=option4, bg="light pink")
    button4.pack()
    
    main_window.mainloop()

if __name__ == "__main__":
    main()
#hello papa ye mera code 