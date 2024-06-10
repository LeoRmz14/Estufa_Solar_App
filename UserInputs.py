import customtkinter as tk
from geopy.geocoders import Nominatim
import requests
from datetime import datetime
import numpy as np


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

def get_geolocation(topFrame, entry_location, currentRow, littles, subtittles2, font_color):
    #global location
     # Retrieve the number entered by the user
    entry_text = entry_location.get()
    geolocator = Nominatim(user_agent='MyFirstApp')    
    location = geolocator.geocode(str(entry_text))
    label = tk.CTkLabel(topFrame, text='Geolocación', font = subtittles2, text_color=font_color, padx=10)
    label.grid(row = currentRow, column = 0, sticky="new", columnspan = 3)
    currentRow +=1
    if location:
        label = tk.CTkLabel(topFrame, text=f'Dirección: {location.address}', font = littles, text_color=font_color, padx=10)
        label.grid(row = currentRow, column = 0, sticky="new", columnspan = 3)
        currentRow +=1
        label1 = tk.CTkLabel(topFrame, text=f'Latitud: {location.latitude}', font = littles, text_color=font_color, padx=10)
        label1.grid(row = currentRow, column = 0, sticky="new")
        label2 = tk.CTkLabel(topFrame, text=f'Longitud: {location.longitude}', font = littles, text_color=font_color, padx=10)
        label2.grid(row = currentRow, column = 2, sticky="new")
        currentRow +=1 
    else:
        label = tk.CTkLabel(topFrame, text='No es una geolocación válida', font = littles, text_color=font_color, padx=10)
        label.grid(row = currentRow, column = 0, sticky="new", columnspan = 3)
        currentRow +=1
    return currentRow

# ------------------ NASA API -----------------------------------------#
def get_solar_radiation(location):
    # Obtener la fecha actual
    start_date = '20240401'
    end_date = datetime.now().strftime('%Y%m%d')
    lon = location.longitude
    lat = location.latitude
    # Construir la URL de la API con los parámetros necesarios
    url = f"https://power.larc.nasa.gov/api/temporal/daily/point?parameters=ALLSKY_SFC_SW_DWN&community=RE&longitude={lon}&latitude={lat}&format=JSON&start={start_date}&end={end_date}"
    
    # Realizar la solicitud a la API
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        # Extraer la radiación solar promedio diaria
        solar_radiation = data['properties']['parameter']['ALLSKY_SFC_SW_DWN']
        # Filtrar los valores -999.0
        filtered_data = {k: v for k, v in solar_radiation.items() if v != -999.0}
        sorted_data = sorted(filtered_data.items())
        # Obtener las últimas 15 mediciones
        last_15_measurements = sorted_data[-15:]

        last_15_values = [value for date, value in last_15_measurements]
        # Calcular el promedio
        average = sum(last_15_values) / len(last_15_values)
        print(f"El promedio de las últimas 15 mediciones es: {average:.2f}")
        return average
    else:
        print("Error fetching data from NASA POWER API")
        return None


### FUNCIONES DE TEMPERATURA --------------------------------------------------------------------------

# Función para simular la radiación solar
def solar_radiation(t, G_max):
    T = 86400  # Periodo de un día en segundos
    return G_max * np.sin(np.pi * t / T)

# Función para simular la temperatura
def simulate_temperature(T_agua_inicial, T_cobre_inicial, A_colector,
                          time_seconds, G_max, efficiency, A_contacto, 
                          d_cobre, m_agua, c_agua, m_cobre, c_cobre, T_ambiental, time_step, h, h_ambiental):
    T_agua = T_agua_inicial
    T_cobre = T_cobre_inicial
    temperatures_agua = []
    temperatures_cobre = []
    G_tf = []
    
    for t in time_seconds:
        # Radiación solar en el tiempo t
        G_t = solar_radiation(t, G_max)
    
        # Incremento de temperatura del agua por radiación solar
        delta_T_agua_solar = (G_t * A_colector * efficiency * time_step) / (m_agua * c_agua)

        # Transferencia de calor del agua al cobre 
        Q_agua_cobre = (h * A_contacto * (T_agua - T_cobre) * time_step) # Convección
        # Ecuación de Fourier
        #Q_agua_cobre = (k_cobre * A_contacto * (T_agua - T_cobre) * time_step)/ d_cobre # Conducción

        # Pérdida de calor al ambiente (para agua y cobre)
        Q_agua_ambiental = h_ambiental * A_contacto * (T_agua - T_ambiental) * time_step
        Q_cobre_ambiental = h_ambiental * A_contacto * (T_cobre - T_ambiental) * time_step

        # Actualización de la temperatura del agua y del cobre
        delta_T_agua_conduccion = Q_agua_cobre / (m_agua * c_agua)
        delta_T_cobre_conduccion = Q_agua_cobre / (m_cobre * c_cobre)

        delta_T_agua_enfriamiento = Q_agua_ambiental / (m_agua * c_agua)
        delta_T_cobre_enfriamiento = Q_cobre_ambiental / (m_cobre * c_cobre)

        T_agua -= delta_T_agua_conduccion + delta_T_agua_enfriamiento
        T_cobre += delta_T_cobre_conduccion - delta_T_cobre_enfriamiento

        # Incrementar la temperatura del agua por radiación solar
        T_agua += delta_T_agua_solar

        # Almacenar temperaturas
        temperatures_agua.append(T_agua)
        temperatures_cobre.append(T_cobre)
        G_tf.append(G_t)

    return temperatures_agua, temperatures_cobre, G_tf


# Se puede hacer un approach utilizando un histórico de datos de la API (para el modelo) 
# El otro approach es hacerlo utilizando únicamente un día (NO FUNCIONA para fech actual, tiene wque ser un año o mes anterior)
# Se puede usar un promedio del mes, sin incluir los valores -999.0

