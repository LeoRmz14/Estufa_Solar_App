import customtkinter as tk
import os 
from PIL import Image
from UserInputs import *
import matplotlib.pyplot as plt 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from geopy.geocoders import Nominatim
import time 

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
    'lightgray': '#A9A9A9'
}
mainframe_color = color_theme['darkgray']
frames_colors = color_theme['black']

tk.set_appearance_mode("dark")
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
label = tk.CTkLabel(topFrame, text="iSolenum", font = Titles, text_color="#FFFFFF", padx=50)
label.grid(row=0, column=0, sticky='w')#, columnspan=1)
image = tk.CTkImage(light_image=Image.open(image_path), size=(120,90))
image_label = tk.CTkLabel(topFrame, image=image, text='')
image_label.grid(row=1, column=0, sticky='w', padx = 70)

label1 = tk.CTkLabel(topFrame, text="App Version 1", font = littles, text_color="#FFFFFF", padx=10)
label1.grid(row = 2, column = 0, sticky="new", columnspan = 3) 

button = tk.CTkButton(topFrame, text="Quit", command=lambda: quit_wndw(root, plt), fg_color="#244984", corner_radius=32, hover_color='#C850C0')
button.grid(row=1, column=2, sticky='e', padx=10, pady=10)

## ----------------------------- Left Frame ------------------------------## 
currentRow = 0
label3 = tk.CTkLabel(LeftFrame, text="Parámetros iniciales", font = subtittles, text_color="#FFFFFF", padx=10)
label3.grid(row = currentRow, column = 0, sticky="new") 
currentRow +=1

label4 = tk.CTkLabel(LeftFrame, text="Geolocación:", font = subtittles2, text_color="#FFFFFF", padx=10)
label4.grid(row = currentRow, column = 0, sticky="w", columnspan = 3) 
currentRow +=1
entry_location, currentRow = write_geolocation(LeftFrame, currentRow, lambda: get_geolocation(RightFrame1, entry_location, currentRow, littles, subtittles2))

label5 = tk.CTkLabel(LeftFrame, text="Temperatura:", font = subtittles2, text_color="#FFFFFF", padx=10)
label5.grid(row = currentRow, column = 0, sticky="w", columnspan = 3) 
currentRow +=1
#To store the input
number_var = tk.StringVar(value=0)
value = tk.StringVar(value='Humedad')
entry1, currentRow = Entry_Button(LeftFrame, currentRow, number_var, lambda: submit_number(entry1, number_var))



## --------------------------- Right Frame ------------------------------------------##
label4 = tk.CTkLabel(RightFrame1, text="Parámetros de salida", font = subtittles, text_color="#FFFFFF", padx=10)
label4.grid(row = 0, column = 0, sticky="new", columnspan = 3) 
## --------------------------- Get time ---------------------------------------- ##
local_time = time.localtime()
current_time_str = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
label5 = tk.CTkLabel(RightFrame1, text="Hora de consulta", font = subtittles2, text_color="#FFFFFF", padx=10)
label5.grid(row = 1, column = 0, sticky="new", columnspan = 3) 
label6 = tk.CTkLabel(RightFrame1, text=f'{current_time_str}', font = littles, text_color="#FFFFFF", padx=10)
label6.grid(row = 2, column = 0, sticky="new", columnspan = 3) 

## --------------------------- Plots ------------------------------------------##
label2 = tk.CTkLabel(RightFrame2, text="Evolución Temperatura", font = littles, text_color="#FFFFFF", padx=10)
label2.grid(row = 0, column = 0, sticky="new", columnspan = 3) 

x = np.linspace(0,1,35)
y = np.cos(2*np.pi*x)

fig1, ax1 = plt.subplots(dpi=80,facecolor='#000000') #dpi=80
ax1.set_facecolor('#000000') 


line, = ax1.plot(x,y, 'orange', marker='o', linewidth=2)
ax1.grid(alpha=0.2)
ax1.set_xlabel('Eje X', color='white', family='Cambria', size=15)
ax1.set_ylabel('Eje Y', color='white', family='Cambria', size=15)
ax1.tick_params(color='white', labelcolor='white', length=6, width=2)
ax1.spines['bottom'].set_color('white')
ax1.spines['left'].set_color('white')
FigureCanvasTkAgg(fig1, master= RightFrame2).get_tk_widget().grid(row = 1, column = 0,sticky="new", columnspan=3, padx=10, pady=10)


root.mainloop()
