from flask import Flask, render_template, request
import json
import requests
import datetime
import geocoder

app = Flask(__name__)


@app.route('/')
def index():
    g = geocoder.ip('me')
    lat = str(g.latlng[0])
    long = str(g.latlng[1])
    time = datetime.datetime.now()
    api_key = "b41cca6b4f5592308fa8b579b37903ac"
    url = "http://api.openweathermap.org/data/2.5/weather?lat=" + lat + "&" + "lon=" + long + "&appid="+api_key
    response = requests.get(url)
    json_data = response.content
    data = json.loads(json_data)
    print(data)

    main = data['main']
    city = data['name']
    print(city)
    tempk = (main['temp'])
    weat = data['weather']
    weat = dict(weat[0])
    sky = weat['main']
    skydesc = weat['description']
    skydesc = skydesc.capitalize()
    garbage = ""
    if skydesc == sky:
        skydesc = garbage
    else:
        skydesc = "(" + skydesc + ")"
    time = datetime.datetime.now()

    temp = int(tempk) - 273
    degree = "o"
    celsi = "C"
    clouds = data['clouds']
    clouds = clouds['all']
    percep = str(clouds) + "%"
    wind = data['wind']
    windspeed = wind['speed']
    windspeed = int(windspeed) * 3.6
    windmsg = str(windspeed) + " km/h"
    windangle = wind['deg']
    windangle = int(windangle)

    if sky == 'Haze':
        icon = "./static/images/icons/icon-7.svg"
    elif sky == 'Clear':
        icon = "./static/images/icons/icon-1.svg"
    elif sky == 'Clouds':
        icon = "./static/images/icons/icon-6.svg"
    elif sky == 'Rain' and skydesc == '(Light rain)':
        icon = "./static/images/icons/icon-9.svg"
    elif sky == 'Rain' and skydesc == '(Heavy rain)':
        icon = "./static/images/icons/icon-10.svg"
    elif sky == 'Snow':
        icon = "./static/images/icons/icon-14.svg"

    if windangle == 0 or windangle == 360:
        winddir = "North"
    elif 90 > windangle > 0:
        winddir = "North-East"
    elif windangle == 90:
        winddir = "East"
    elif 90 < windangle < 180:
        winddir = "South-East"
    elif windangle == 180:
        winddir = "South"
    elif 180 < windangle < 270:
        winddir = "South-West"
    elif 270 < windangle < 360:
        winddir = "North-West"

    return render_template('index.html', **locals())


@app.route('/', methods=["POST"])
def weather():
    api_key = "b41cca6b4f5592308fa8b579b37903ac"
    city = request.form["city"]
    url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + api_key
    response = requests.get(url)
    json_data = response.content
    data = json.loads(json_data)
    print(type(data))
    main = data['main']
    tempk = (main['temp'])
    weat = data['weather']
    weat = dict(weat[0])
    sky = weat['main']
    skydesc = weat['description']
    skydesc = skydesc.capitalize()
    garbage = ""
    if skydesc == sky:
        skydesc = garbage
    else:
        skydesc = "(" + skydesc + ")"

    print(sky)
    print(weat)
    time = datetime.datetime.now()

    temp = int(tempk) - 273
    city = city.capitalize()
    degree = "o"
    celsi = "C"

    temp_max = int(main['temp_max']) - 273
    temp_min = int(main['temp_min']) - 273
    pressure = main['pressure']
    humidity = main['humidity']
    humidity = str(humidity) + "%"
    pressure = str(pressure) + " hPa"
    print(pressure)
    print(temp_max)
    print(temp_min)
    print(humidity)

    clouds = data['clouds']
    clouds = clouds['all']
    percep = str(clouds) + "%"
    wind = data['wind']
    windspeed = wind['speed']
    windspeed = int(windspeed) * 3.6
    windmsg = str(windspeed) + " km/h"
    windangle = wind['deg']
    windangle = int(windangle)
    print(skydesc)
    if sky == 'Haze':
        icon = "./static/images/icons/icon-7.svg"
    elif sky == 'Clear':
        icon = "./static/images/icons/icon-1.svg"
    elif sky == 'Clouds':
        icon = "./static/images/icons/icon-6.svg"
    elif sky == 'Rain' and skydesc == '(Light rain)':
        icon = "./static/images/icons/icon-9.svg"
    elif sky == 'Rain' and skydesc == '(Heavy rain)':
        icon = "./static/images/icons/icon-10.svg"
    elif sky == 'Snow':
        icon = "./static/images/icons/icon-14.svg"

    if windangle == 0 or windangle == 360:
        winddir = "North"
    elif 90 > windangle > 0:
        winddir = "North-East"
    elif windangle == 90:
        winddir = "East"
    elif 90 < windangle < 180:
        winddir = "South-East"
    elif windangle == 180:
        winddir = "South"
    elif 180 < windangle < 270:
        winddir = "South-West"
    elif 270 < windangle < 360:
        winddir = "North-West"

    return render_template('index.html', **locals())


if __name__ == '__main__':
    app.run()
