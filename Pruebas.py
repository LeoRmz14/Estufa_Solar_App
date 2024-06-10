import requests
from datetime import datetime
import numpy as np

def fetch_solar_radiation(lat, lon):
    # Obtener la fecha actual
    end_date = datetime.now().strftime('%Y%m%d')
    
    # Construir la URL de la API con los parámetros necesarios
    url = f"https://power.larc.nasa.gov/api/temporal/daily/point?parameters=ALLSKY_SFC_SW_DWN&community=RE&longitude={lon}&latitude={lat}&format=JSON&start=20220101&end={end_date}"
    
    # Realizar la solicitud a la API
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        # Extraer la radiación solar promedio diaria
        solar_radiation = data['properties']['parameter']['ALLSKY_SFC_SW_DWN']
        return solar_radiation
    else:
        print("Error fetching data from NASA POWER API")
        return None

def calculate_average_solar_radiation(solar_radiation):
    total_radiation = sum(solar_radiation.values())
    number_of_days = len(solar_radiation)
    average_radiation = total_radiation / number_of_days
    return average_radiation

def simulate_temperature(solar_radiation, time_hours):
    efficiency = 0.7  # Eficiencia del colector solar
    heat_capacity = 500  # Capacidad térmica del sistema (J/°C)
    initial_temperature = 20  # Temperatura inicial (°C)
    temperature = initial_temperature + (solar_radiation * efficiency / heat_capacity) * time_hours
    return temperature

def update_plot(lat, lon):
    solar_radiation_data = fetch_solar_radiation(lat, lon)
    if solar_radiation_data:
        average_radiation = calculate_average_solar_radiation(solar_radiation_data)
        time_hours = np.arange(0, 24, 1)
        temperature = simulate_temperature(average_radiation, time_hours)
        
        ax1.clear()
        ax1.plot(time_hours, temperature, 'orange', marker='o', linewidth=2)
        ax1.set_xlabel('Tiempo (horas)', color='white', family='Cambria', size=15)
        ax1.set_ylabel('Temperatura (°C)', color='white', family='Cambria', size=15)
        ax1.tick_params(color='white', labelcolor='white', length=6, width=2)
        ax1.spines['bottom'].set_color('white')
        ax1.spines['left'].set_color('white')
        canvas.draw()

# Ejemplo de uso
latitude = 37.7749  # Latitud de ejemplo
longitude = -122.4194  # Longitud de ejemplo
solar_radiation_data = fetch_solar_radiation(latitude, longitude)
if solar_radiation_data:
    average_radiation = calculate_average_solar_radiation(solar_radiation_data)
    print(f"Radiación solar promedio diaria: {average_radiation} kWh/m²")
