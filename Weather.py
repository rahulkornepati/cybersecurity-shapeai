import requests
from datetime import datetime

text_file = open('Weatherreport.txt',"w+")
api_key = 'b1f90acf1c00fda813354758abc4404a'
location = input("Name of the city: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temperature = ((api_data['main']['temp']) - 273.15)
weather_descp = api_data['weather'][0]['description']
humidity = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

def text_write():
    text_file.write("-------------------------------------------------------------\n")
    text_file.write(("Weather Stats for - {}  || {}\n".format(location.upper(), date_time)))
    text_file.write("-------------------------------------------------------------\n")
    text_file.write(("Current temperature is: {:.2f} deg C \n".format(temperature)))
    text_file.write(("Current weather desc  :"+weather_descp+'\n'))
    text_file.write(("Current Humidity      :"+str(humidity)+ '%\n'))
    text_file.write(("Current wind speed    :"+str(wind_spd) +'kmph\n'))
text_write()

print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")

print ("Current temperature is: {:.2f} deg C".format(temperature))
print ("Current weather desc  :",weather_descp)
print ("Current Humidity      :",humidity, '%')
print ("Current wind speed    :",wind_spd ,'kmph')
