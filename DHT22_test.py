import board
import adafruit_dht

# Initialize the DHT22 sensor connected to pin D17
dhtDevice = adafruit_dht.DHT22(board.D17)

# Get the temperature in Celsius from the DHT22 sensor
temperature_c = dhtDevice.temperature

# Convert the temperature from Celsius to Fahrenheit
temperature_f = temperature_c * (9 / 5) + 32

# Get the humidity percentage from the DHT22 sensor
humidity = dhtDevice.humidity

# Print the temperatures in both Fahrenheit and Celsius, and the humidity percentage
print("Temp: {:.1f} F / {:.1f} C Humidity: {}% ".format(temperature_f, temperature_c, humidity))

