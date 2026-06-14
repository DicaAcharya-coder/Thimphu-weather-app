# Thimphu Weather App - Desktop App WITH WINDOWS
import tkinter as tk
from tkinter import ttk
import requests
from datetime import datetime

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🌤️ Thimphu Weather App")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        
        # Set background color
        self.root.configure(bg="#f0f8ff")
        
        # Title
        title_label = tk.Label(
            root, 
            text="🌤️ THIMPHU WEATHER",
            font=("Arial", 20, "bold"),
            bg="#f0f8ff",
            fg="#2c3e50"
        )
        title_label.pack(pady=20)
        
        # Location
        location_label = tk.Label(
            root,
            text="📍 Thimphu, Bhutan",
            font=("Arial", 12),
            bg="#f0f8ff",
            fg="#555"
        )
        location_label.pack()
        
        # Temperature display
        self.temp_label = tk.Label(
            root,
            text="🌡️ Loading...",
            font=("Arial", 28, "bold"),
            bg="#f0f8ff",
            fg="#e74c3c"
        )
        self.temp_label.pack(pady=20)
        
        # Weather details
        self.details_frame = tk.Frame(root, bg="#f0f8ff")
        self.details_frame.pack(pady=10)
        
        self.wind_label = tk.Label(
            self.details_frame,
            text="💨 Wind: -- km/h",
            font=("Arial", 12),
            bg="#f0f8ff",
            fg="#555"
        )
        self.wind_label.pack(pady=5)
        
        self.weather_label = tk.Label(
            self.details_frame,
            text="☁️ Weather: --",
            font=("Arial", 12),
            bg="#f0f8ff",
            fg="#555"
        )
        self.weather_label.pack(pady=5)
        
        # Get button
        self.get_btn = tk.Button(
            root,
            text="🔄 Get Current Weather",
            command=self.get_weather,
            font=("Arial", 12, "bold"),
            bg="#3498db",
            fg="white",
            width=20,
            height=2,
            cursor="hand2"
        )
        self.get_btn.pack(pady=20)
        
        # Save button
        self.save_btn = tk.Button(
            root,
            text="💾 Save to Log File",
            command=self.save_weather,
            font=("Arial", 10),
            bg="#2ecc40",
            fg="white",
            width=20,
            height=1,
            cursor="hand2"
        )
        self.save_btn.pack(pady=5)
        
        # Status
        self.status_label = tk.Label(
            root,
            text="",
            font=("Arial", 9),
            bg="#f0f8ff",
            fg="#777"
        )
        self.status_label.pack(pady=10)
        
        # Auto-get weather on start
        self.get_weather()
    
    def get_weather(self):
        """Fetch weather from API"""
        url = "https://api.open-meteo.com/v1/forecast?latitude=27.4728&longitude=89.6390&current=temperature_2m,wind_speed_10m,weather_code"
        
        try:
            response = requests.get(url, timeout=10)
            data = response.json()
            
            current = data['current']
            temp = current['temperature_2m']
            wind = current['wind_speed_10m']
            code = current['weather_code']
            
            # Weather description
            if code == 0:
                weather = "Clear Sky ☀️"
            elif code in [1, 2, 3]:
                weather = "Partly Cloudy ⛅"
            elif code in [61, 63, 65]:
                weather = "Rain 🌧️"
            elif code in [71, 73, 75]:
                weather = "Snow ❄️"
            else:
                weather = "Cloudy ☁️"
            
            # Update display
            self.temp_label.config(text=f"🌡️ {temp}°C")
            self.wind_label.config(text=f"💨 Wind: {wind} km/h")
            self.weather_label.config(text=f"☁️ Weather: {weather}")
            self.status_label.config(text=f"✅ Updated: {datetime.now().strftime('%H:%M')}")
            
        except Exception as e:
            self.temp_label.config(text="🌡️ Error")
            self.status_label.config(text=f"❌ {str(e)}")
    
    def save_weather(self):
        """Save weather to log file"""
        try:
            with open("thimphu_weather_log.txt", "a") as f:
                time = datetime.now().strftime("%Y-%m-%d %H:%M")
                temp_text = self.temp_label.text
                f.write(f"{time} | {temp_text}\n")
            self.status_label.config(text="✅ Saved to log file!")
        except:
            self.status_label.config(text="❌ Save failed")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()