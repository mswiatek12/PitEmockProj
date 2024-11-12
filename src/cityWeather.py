class cityWeather:
    def __init__(self, city_name, time, temperature, description, feels_like, humidity, pressure, wind_speed):
        self.city_name = city_name
        self.time = time
        self.temperature = temperature
        self.description = description
        self.feels_like = feels_like
        self.humidity = humidity
        self.pressure = pressure
        self.wind_speed = wind_speed

    def __str__(self):
        return (f"Weather in {self.city_name} at {self.time}:\n"
                f"Temperature: {self.temperature}°C, Feels like: {self.feels_like}°C\n"
                f"Description: {self.description}\n"
                f"Humidity: {self.humidity}%\n"
                f"Pressure: {self.pressure} hPa\n"
                f"Wind: {self.wind_speed} m/s")