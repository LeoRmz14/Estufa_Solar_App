import customtkinter as tk
import os 
from PIL import Image

#INPUTS
#El usuario meterá: Latitud.
# El usuario meterá la ubicación donde está y una API mostrará la información geográfica (GEOPY). El usuario meterá su ubicación aproximada.
#Hora (Checa cómo se puede dar)
#Día del año (checa )

ScreenSize = [1024,768]

tk.set_appearance_mode("dark")
tk.set_default_color_theme('blue')

# Configuración de la ventana principal
root = tk.CTk()
root.title("Proyecto")
root.geometry(f"{ScreenSize[0]}x{ScreenSize[1]}")

## -------------------------- Main frame set ----------------------------- ##
main_frame = tk.CTkFrame(root, width=ScreenSize[0], height=ScreenSize[1])
main_frame.pack(fill="both", expand=True)
main_frame.configure(fg_color="#A9A9A9")

## ------------------------- Images --------------------------------------- ##
image_path = os.path.join(os.path.dirname(__file__), )

## -------------------------- Typography ----------------------------------- ##
Titles = tk.CTkFont(family = "Poppins SemiBold", size = 40, weight = "bold")#), slant = "italic")
littles = tk.CTkFont(family = "Poppins Regular", size = 12)

topFrame = tk.CTkFrame(master=main_frame, fg_color="#FFFFFF")
topFrame.grid(row=0, column=0, sticky="new", columnspan=2, padx=10, pady=10)

topFrame.grid_columnconfigure((0,1), weight=1)
topFrame.configure(fg_color="#A9A9A9")

label = tk.CTkLabel(topFrame, text="iSolenum", font = Titles, text_color="#FFFFFF", padx=10)
label.grid(row=0, column=0)#, columnspan=1)


# Iniciar el loop de la aplicación
root.mainloop()