import requests

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data["cod"] == "404":
        print("City not found. Please check the spelling and try again.")
    else:
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]
        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description}")

def main():
    api_key = "YOUR_API_KEY"
    city = input("Enter a city name: ")
    get_weather(api_key, city)

if __name__ == "__main__":
    main()
#Weather Forecast App in Python using the OpenWeatherMap API. Before running the code, make sure you have signed up for an API key on the OpenWeatherMap website.
#Make sure to replace "YOUR_API_KEY" with your actual API key from OpenWeatherMap. When you run the script, it will prompt you to enter a city name. It will then fetch the weather information for that city using the API and display the temperature, humidity, and weather description.
#Remember to have the requests library installed (pip install requests) before running the code.
