import customtkinter as tk
import os 
from PIL import Image
from UserInputs import *
import matplotlib.pyplot as plt 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from geopy.geocoders import Nominatim
import time 
from datetime import datetime

#INPUTS
#El usuario meterá: Latitud.
# El usuario meterá la ubicación donde está y una API mostrará la información geográfica (GEOPY). El usuario meterá su ubicación aproximada.
#Hora (Checa cómo se puede dar)
#Día del año (checa )

#time sirve para medir el tiempo y obtener la fecha

ScreenSize = [1024,768]
color_theme = {
    'black': '#000000',
    'darkgray': '#2E2E2E',
    'lightgray': '#A9A9A9',
    'white': '#FFFFFF',
    'darkwhite': '#D3D3D3'
}
mainframe_color = color_theme['white']
frames_colors = color_theme['darkwhite']
font_color = color_theme['black']

tk.set_appearance_mode("light")
tk.set_default_color_theme('blue')

# Configuración de la ventana principal
root = tk.CTk()
root.title("Proyecto")
root.geometry(f"{ScreenSize[0]}x{ScreenSize[1]}")
root.protocol("WM_DELETE_WINDOW", lambda: quit_wndw)  # Bind the window close event to the function that correctly destroys the root window


## -------------------------- Main frame set ----------------------------- ##
main_frame = tk.CTkFrame(root, width=ScreenSize[0], height=ScreenSize[1])
main_frame.pack(fill="both", expand=True)
main_frame.configure(fg_color=mainframe_color)
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_columnconfigure(1, weight=1)
main_frame.grid_columnconfigure(2, weight=1)
main_frame.grid_columnconfigure(3, weight=1)

## ------------------------- Images --------------------------------------- ##
image_path = os.path.join(os.path.dirname(__file__), 'Images/Sol.png')

## -------------------------- Typography ----------------------------------- ##
Titles = tk.CTkFont(family = "Poppins SemiBold", size = 40, weight = "bold")#), slant = "italic")
littles = tk.CTkFont(family = "Poppins Regular", size = 12)
subtittles = tk.CTkFont(family = "Poppins SemiBold", size = 16, weight = "bold")
subtittles2 = tk.CTkFont(family = "Poppins SemiBold", size = 14, weight = "bold")

## -------------------------- Frames ----------------------------------- ##
currentRow = 0
topFrame = tk.CTkFrame(master=main_frame)
topFrame.grid(row=currentRow, column=0, sticky="new", columnspan=4, padx=10, pady=10)
topFrame.configure(fg_color=frames_colors)
#main_frame.grid_rowconfigure(0, weight=1)
topFrame.grid_columnconfigure(0, weight=1)
topFrame.grid_columnconfigure(1, weight=1)
topFrame.grid_columnconfigure(2, weight=1)

currentRow +=1
LeftFrame = tk.CTkFrame(main_frame, fg_color=frames_colors)
LeftFrame.grid(row=currentRow, column=0, sticky="new", padx=10, pady=10)

# currentRow +=1
# LeftFrame2 = tk.CTkFrame(main_frame, fg_color=frames_colors)
# LeftFrame2.grid(row=currentRow, column=0, sticky="new", padx=10, pady=10)


RightFrame1 = tk.CTkFrame(main_frame, fg_color=frames_colors) # height=100 to control dimensions (width)
RightFrame1.grid(row=currentRow, column=1, sticky="new", columnspan=3, padx=10, pady=10)
RightFrame1.grid_columnconfigure(0, weight=1)
RightFrame1.grid_columnconfigure(1, weight=1)
RightFrame1.grid_columnconfigure(2, weight=1)
currentRow +=1

RightFrame2 = tk.CTkFrame(main_frame, fg_color=frames_colors) # height=100 to control dimensions (width)
RightFrame2.grid(row=currentRow, column=1, sticky="new", columnspan=3, padx=10, pady=10)
RightFrame2.grid_columnconfigure(0, weight=1)
RightFrame2.grid_columnconfigure(1, weight=1)
RightFrame2.grid_columnconfigure(2, weight=1)



## -------------------------- Widgets ----------------------------------- ##
label = tk.CTkLabel(topFrame, text="iSolenum", font = Titles, text_color=font_color, padx=50)
label.grid(row=0, column=0, sticky='w')#, columnspan=1)
image = tk.CTkImage(light_image=Image.open(image_path), size=(120,90))
image_label = tk.CTkLabel(topFrame, image=image, text='')
image_label.grid(row=1, column=0, sticky='w', padx = 70)

label1 = tk.CTkLabel(topFrame, text="App Version 1", font = littles, text_color=font_color, padx=10)
label1.grid(row = 2, column = 0, sticky="new", columnspan = 3) 

button = tk.CTkButton(topFrame, text="Quit", command=lambda: quit_wndw(root, plt), fg_color="#244984", corner_radius=32, hover_color='#C850C0')
button.grid(row=1, column=2, sticky='e', padx=10, pady=10)

## ----------------------------- Left Frame ------------------------------## 
currentRow = 0
label3 = tk.CTkLabel(LeftFrame, text="Parámetros iniciales", font = subtittles, text_color=font_color, padx=10)
label3.grid(row = currentRow, column = 0, sticky="new") 
currentRow +=1

label4 = tk.CTkLabel(LeftFrame, text="Geolocación:", font = subtittles2, text_color=font_color, padx=10)
label4.grid(row = currentRow, column = 0, sticky="w", columnspan = 3) 
currentRow +=1
entry_location, currentRow = write_geolocation(LeftFrame, currentRow, lambda: get_geolocation(RightFrame1, entry_location, currentRow, littles, subtittles2, font_color))

label5 = tk.CTkLabel(LeftFrame, text="Temperatura:", font = subtittles2, text_color=font_color, padx=10)
label5.grid(row = currentRow, column = 0, sticky="w", columnspan = 3) 
currentRow +=1
#To store the input
number_var = tk.StringVar(value=0)
value = tk.StringVar(value='Humedad')
entry1, currentRow = Entry_Button(LeftFrame, currentRow, number_var, lambda: submit_number(entry1, number_var))

# # ------------------------------------------- GRáfica ----------------------#
# # Parámetros
# G_max = 8  # Radiación solar máxima en W/m²
# T = 86400  # Periodo de un día en segundos

# # Función de radiación solar
# def solar_radiation(t, G_max):
#     return G_max * np.sin(np.pi * t / T)

# # Tiempo en segundos para un día completo
# time_seconds = np.arange(0, 24 * 60 * 60, 1)

# # Radiación solar a lo largo del día
# G_values = solar_radiation(time_seconds, G_max)

# # Convertir tiempo en segundos a horas para la gráfica
# time_hours = time_seconds / 3600

# # Crear la figura de Matplotlib
# fig, ax = plt.subplots(dpi=80, facecolor='#000000')
# ax.set_facecolor('#000000')

# # Graficar la radiación solar
# ax.plot(time_hours, G_values)
# ax.set_xlabel("Tiempo (horas)", fontdict={'family': 'serif', 'color': 'blue', 'size': 14})
# ax.set_ylabel("Radiación Solar (W/m²)", fontdict={'family': 'serif', 'color': 'blue', 'size': 14})
# ax.set_title("Radiación Solar a lo Largo del Día", fontdict={'family': 'serif', 'color': 'darkblue', 'weight': 'bold', 'size': 16})

# # Personalizar los ticks del eje x
# ax.set_xticks(np.arange(0, 25, 1))
# ax.set_xticklabels(np.arange(0, 25, 1), fontname='serif', fontsize=9, color='white')
# ax.set_yticklabels(ax.get_yticks(), fontname='serif', fontsize=12, color='white')

# # Mostrar la cuadrícula
# ax.grid(alpha=0.3)

# # Crear el widget de Matplotlib para CustomTKinter
# canvas = FigureCanvasTkAgg(fig, master=LeftFrame2)
# canvas.draw()
# canvas.get_tk_widget().grid(row=1, column=0, sticky="new", columnspan=3, padx=10, pady=10)





## --------------------------- Right Frame ------------------------------------------##
label4 = tk.CTkLabel(RightFrame1, text="Parámetros de salida", font = subtittles, text_color=font_color, padx=10)
label4.grid(row = 0, column = 0, sticky="new", columnspan = 3) 



#currentRow, location = get_geolocation(RightFrame1, entry_location, currentRow, littles, subtittles2)
# average = get_solar_radiation(location)
# print(average)
## --------------------------- Get time ---------------------------------------- ##

current_time_str = datetime.now().strftime('%d%m%Y')

label5 = tk.CTkLabel(RightFrame1, text="Hora de consulta", font = subtittles2, text_color=font_color, padx=10)
label5.grid(row = 1, column = 0, sticky="new", columnspan = 3) 
label6 = tk.CTkLabel(RightFrame1, text=f'{current_time_str}', font = littles, text_color=font_color, padx=10)
label6.grid(row = 2, column = 0, sticky="new", columnspan = 3) 

## --------------------------- Plots ------------------------------------------##
label2 = tk.CTkLabel(RightFrame2, text="Evolución Temperatura", font = littles, text_color=font_color, padx=10)
label2.grid(row = 0, column = 0, sticky="new", columnspan = 3) 

# Propiedades del agua y del cobre en unidades SI
c_agua = 4180  # J/(kg·K)
c_cobre = 385  # J/(kg·K)
k_cobre = 385  # W/(m·K)  # Conductividad térmica del cobre
h = 500  # W/(m²·K) -> Depende de las condiciones del fluido
h_ambiental = 50  # Coeficiente de transferencia de calor al ambiente (W/(m²·K))

# Parámetros geométricos y condiciones iniciales en unidades SI
r_cobre = 0.006  # Radio del cobre en m
l_cobre = 1.4  # Longitud total del cobre en m
A_contacto = 2 * np.pi * r_cobre * l_cobre  # Área de contacto en m²
d_cobre = 0.05  # Espesor del cobre en m
m_agua = 5  # Masa del agua en kg
m_cobre = 1  # Masa del cobre en kg
T_agua_inicial = 293.15  # Temperatura inicial del agua en K (20 °C)
T_cobre_inicial = 288.15  # Temperatura inicial del cobre en K (15 °C)
T_ambiental = 293.15  # Temperatura ambiental en K (20 °C)
G_max = 7000  # Radiación solar máxima en W/m² (valor realista)
efficiency = 0.05  # Eficiencia del colector solar
A_colector = 0.5  # Área del colector en m²
time_seconds = np.arange(0, 24 * 60 * 60, 1)  # Simulación de 24 horas con intervalos de 1 segundo
time_step = 1  # Intervalo de tiempo en segundos (1 segundo)

# Función para simular la radiación solar
def solar_radiation(t, G_max):
    T = 86400  # Periodo de un día en segundos
    return G_max * np.sin(np.pi * t / T)

# Función para simular la temperatura
def simulate_temperature(time_seconds, G_max, efficiency, A_contacto, d_cobre, m_agua, c_agua, m_cobre, c_cobre, T_ambiental):
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
        #Q_agua_cobre = (k_cobre * A_contacto * (T_agua - T_cobre) * time_step)/ d_cobre # Convección

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

# Simulación de 24 horas con intervalos de 1 segundo
temperatures_agua, temperatures_cobre, G_tf = simulate_temperature(time_seconds, G_max, efficiency, A_contacto, d_cobre, m_agua, c_agua, m_cobre, c_cobre, T_ambiental)
temperaturas_agua_C = [temp - 273.15 for temp in temperatures_agua]
temperaturas_cobre_C = [temp - 273.15 for temp in temperatures_cobre]
# Convertir tiempo en segundos a horas para la gráfica
time_hours = time_seconds / 3600
#

# Crear la figura de Matplotlib
fig1, ax1 = plt.subplots(dpi=80, facecolor='#FFFFFF')
ax1.set_facecolor('#FFFFFF')

# Graficar los resultados de la temperatura del agua y del cobre
ax1.plot(time_hours, temperaturas_agua_C, label="Temperatura del Agua (C)")
ax1.plot(time_hours, temperaturas_cobre_C, label="Temperatura del Cobre (C)", linestyle="--")
ax1.set_xlabel("Tiempo (horas)", fontdict={'family': 'serif', 'color': 'black', 'size': 14})
ax1.set_ylabel("Temperatura (C)", fontdict={'family': 'serif', 'color': 'black', 'size': 14})
ax1.set_title("Evolución de la Temperatura del Agua y Cobre", fontdict={'family': 'serif', 'color': 'black', 'weight': 'bold', 'size': 16})
ax1.legend(prop={'family': 'serif', 'style': 'italic', 'size': 10})
ax1.grid(alpha=0.3)
ax1.tick_params(color='black', labelcolor='black', length=6, width=2)
ax1.spines['bottom'].set_color('black')
ax1.spines['left'].set_color('black')
ax1.spines['top'].set_color('black')
ax1.spines['right'].set_color('black')
ax1.set_xticks(np.arange(0, 25, 1))
ax1.set_xticklabels(np.arange(0, 25, 1), fontname='serif', fontsize=9, color='black')
ax1.set_yticklabels(ax1.get_yticks(), fontname='serif', fontsize=12, color='black')

# Crear el widget de Matplotlib para CustomTKinter
canvas = FigureCanvasTkAgg(fig1, master=RightFrame2)
canvas.draw()
canvas.get_tk_widget().grid(row=1, column=0, sticky="new", columnspan=3, padx=10, pady=10)


root.mainloop()
