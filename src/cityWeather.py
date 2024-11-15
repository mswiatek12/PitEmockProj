import datetime

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
        self.timestamp = time

    def __str__(self):
        minute = datetime.datetime.fromtimestamp(self.timestamp).minute
        hour = datetime.datetime.fromtimestamp(self.timestamp).hour
        temp1 = "%.0f"%(self.temperature - 272.5)
        temp2 = "%.0f"%(self.feels_like - 272.5)

        return (f"Weather in {self.city_name} at {hour}:{minute}:\n"
                f"Temperature: {temp1}°C, Feels like: {temp2}°C\n"
                f"Description: {self.description}\n"
                f"Humidity: {self.humidity}%\n"
                f"Pressure: {self.pressure} hPa\n"
                f"Wind: {self.wind_speed} m/s")