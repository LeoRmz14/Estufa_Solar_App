import customtkinter as tk
from geopy.geocoders import Nominatim


def submit_number(entry, number_var):
    # Retrieve the number entered by the user
    entered_number = entry.get()
    # Convert to integer if necessary
    try:
        entered_number = float(entered_number)
        number_var.set(entered_number)
        print(f"Number entered: {entered_number}")
    except ValueError:
        print("Please enter a valid number")

def Entry_Button(topFrame, currentRow, number_var, command_type):
    # Entry widget for number input
    entry = tk.CTkEntry(topFrame, placeholder_text='Ingresa la temperatura')
    entry.grid(row=currentRow, column=0, sticky='w', padx=10, pady=10)

    # Button to submit the entered number
    button = tk.CTkButton(topFrame, text="Listo", command=command_type, fg_color="#244984", corner_radius=32, hover_color='#C850C0')
    button.grid(row=currentRow, column=1, sticky='e', padx=10, pady=10)
    currentRow +=1
#     months = [
#     "Enero", "Febrero", "Marzo", "Abril",
#     "Mayo", "Junio", "Julio", "Agosto",
#     "Septiembre", "Octubre", "Noviembre", "Diciembre"
# ]
#     monthsSelect = tk.CTkComboBox(topFrame, values = months)
#     monthsSelect.grid(row=currentRow, columnspan = 2, sticky = 'new')
    return entry, currentRow

#This function destroys the root window, ensuring no error appear when using the close Windows button.
def quit_wndw(root, plt):
    cancel_all_after_events(root)
    plt.close()
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate


# track of after ids
after_ids = []
# Function to cancel all pending after events. It must be used to avoid any after callback error. The module matplotlib is internally calling after events (that is why is a must)
def cancel_all_after_events(root):
    for after_id in after_ids:
        try:
            root.after_cancel(after_id)
        except Exception as e:
            print(f"Error cancelling after event: {e}")

def write_geolocation(topFrame, currentRow, command_type):
    # Entry widget for number input
    entry_location = tk.CTkEntry(topFrame, placeholder_text='Ingresa tu ubicación')
    entry_location.grid(row=currentRow, column=0, sticky='new', padx=10, pady=10)

    # Button to submit the entered number
    button = tk.CTkButton(topFrame, text="Listo", command=command_type, fg_color="#244984", corner_radius=32, hover_color='#C850C0')
    button.grid(row=currentRow, column=1, sticky='new', padx=10, pady=10)
    currentRow +=1
    return entry_location, currentRow

def get_geolocation(topFrame, entry_location, currentRow, littles, subtittles2):
     # Retrieve the number entered by the user
    entry_text = entry_location.get()
    geolocator = Nominatim(user_agent='MyFirstApp')    
    location = geolocator.geocode(str(entry_text))
    label = tk.CTkLabel(topFrame, text='Geolocación', font = subtittles2, text_color="#FFFFFF", padx=10)
    label.grid(row = currentRow, column = 0, sticky="new", columnspan = 3)
    currentRow +=1
    if location:
        label = tk.CTkLabel(topFrame, text=f'Dirección: {location.address}', font = littles, text_color="#FFFFFF", padx=10)
        label.grid(row = currentRow, column = 0, sticky="new", columnspan = 3)
        currentRow +=1
        label1 = tk.CTkLabel(topFrame, text=f'Latitud: {location.latitude}', font = littles, text_color="#FFFFFF", padx=10)
        label1.grid(row = currentRow, column = 0, sticky="new")
        label2 = tk.CTkLabel(topFrame, text=f'Longitud: {location.longitude}', font = littles, text_color="#FFFFFF", padx=10)
        label2.grid(row = currentRow, column = 2, sticky="new")
        currentRow +=1 
    else:
        label = tk.CTkLabel(topFrame, text='No es una geolocación válida', font = littles, text_color="#FFFFFF", padx=10)
        label.grid(row = currentRow, column = 0, sticky="new", columnspan = 3)
        currentRow +=1
    return currentRow



