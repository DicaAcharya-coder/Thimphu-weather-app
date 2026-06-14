# Thimphu Weather App - FIXED VERSION
import requests

def get_thimphu_weather():
    print("\n" + "="*50)
    print("🌤️  THIMPHU WEATHER APP")
    print("="*50)
    
    # Thimphu coordinates
    latitude = 27.4728
    longitude = 89.6390
    
    # API URL - using correct parameters
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m,wind_direction_10m,weather_code"
    
    print(f"\n🔍 Connecting to Open-Meteo API...")
    
    try:
        response = requests.get(url, timeout=10)
        
        print(f"✅ Connected! Status: {response.status_code}")
        
        if response.status_code != 200:
            print(f"❌ API error: {response.status_code}")
            return
        
        data = response.json()
        
        # CORRECTED: Open-Meteo uses 'current' not 'current_weather'
        current = data['current']
        
        temperature = current['temperature_2m']
        wind_speed = current['wind_speed_10m']
        wind_direction = current['wind_direction_10m']
        weather_code = current['weather_code']
        
        # Convert weather code to description
        if weather_code == 0:
            weather = "Clear Sky ☀️"
        elif weather_code in [1, 2, 3]:
            weather = "Partly Cloudy ⛅"
        elif weather_code in [45, 48]:
            weather = "Foggy 🌫️"
        elif weather_code in [51, 53, 55, 56, 57]:
            weather = "Drizzle 🌦️"
        elif weather_code in [61, 63, 65, 66, 67]:
            weather = "Rain 🌧️"
        elif weather_code in [71, 73, 75, 77]:
            weather = "Snow ❄️"
        elif weather_code in [80, 81, 82]:
            weather = "Rain Showers 🌦️"
        elif weather_code in [85, 86]:
            weather = "Snow Showers ❄️"
        elif weather_code in [95, 96, 99]:
            weather = "Thunderstorm ⚡"
        else:
            weather = "Cloudy ☁️"
        
        # Show results
        print("\n" + "="*50)
        print(f"📍 Location: Thimphu, Bhutan")
        print("="*50)
        print(f"\n🌡️  Temperature:    {temperature}°C")
        print(f"\n💨 Wind Speed:      {wind_speed} km/h")
        print(f"\n🧭 Wind Direction:  {wind_direction}°")
        print(f"\n☁️  Weather:        {weather}")
        
        print("\n" + "="*50)
        if temperature < 10:
            print("💡 Tip: Very cold! Wear warm clothes and layers.")
        elif temperature < 15:
            print("💡 Tip: It's cool. Wear a sweater or light jacket.")
        elif temperature < 22:
            print("💡 Tip: Pleasant weather. Great for outdoor activities!")
        else:
            print("💡 Tip: It's warm. Stay hydrated and avoid direct sun.")
        print("="*50 + "\n")
        
    except requests.exceptions.Timeout:
        print("\n❌ Error: Connection timed out")
        print("   Try again or check your internet.")
    except requests.exceptions.ConnectionError:
        print("\n❌ Error: Can't connect to API")
        print("   Check internet or visit: https://open-meteo.com")
    except KeyError as e:
        print(f"\n❌ Error: Data format unexpected")
        print(f"   Missing key: {e}")
        print("   Full response: {data}")
    except Exception as e:
        print(f"\n❌ Unexpected error: {type(e).__name__}")
        print(f"   Details: {e}")

if __name__ == "__main__":
    get_thimphu_weather()