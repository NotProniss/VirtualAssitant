import json
import python_weather
import asyncio
from urllib.request import urlopen

# Get IP and Location data from json
url = 'http://ip-api.com/json'
response = urlopen(url)
data = json.load(response)

city = data['city']
country = data['country']

async def getWeather():
  async with python_weather.Client(unit=python_weather.METRIC) as client:
    # Get weather from location
    weather = await client.get(city)
    
    loc = weather.location
    region = weather.region
    country = weather.country

    # Usefull values for current weather
    now_temp = f'{weather.temperature} °C'
    now_dateTime = weather.datetime
    now_desc = f'{weather.description}, and with {weather.kind} skies'
    now_feelsLike = f'Feels like {weather.feels_like} °C'
    now_humd = f'{weather.humidity}% humidity'
    now_precip = weather.precipitation
    now_press = f'{weather.pressure / 10} kPa'
    now_uv = f'{weather.ultraviolet} UV Index'
    now_vis = f'{weather.visibility} Km of visibility'
    now_wind = f'Wind is blowing {weather.wind_direction} at {weather.wind_speed} Km'

# Printing stuff for debugging/info
    '''
    print(loc)
    print(region)
    print(country)

    print(now_temp)
    print(weather.daily_forecasts)
    print(now_dateTime)
    print(now_desc)
    print(now_feelsLike)
    print(now_humd)
    print(now_precip)
    print(now_press)
    print(now_uv)
    print(now_vis)
    print(now_wind)
    '''

    # get the weather forecast for a few days
    for daily in weather.daily_forecasts:

      # Usefull values for daily weather
      daily_high = f' with a high of {daily.highest_temperature} °C'
      daily_low = f' with a low of {daily.lowest_temperature} °C'
      daily_date = daily.date

      # More printing
      '''
      print(daily_date)
      print(daily_high)
      print(daily_low)
      '''
      
      # hourly forecasts
      for hourly in daily.hourly_forecasts:

        # Usefull hourly values
        hour_overcast = f'Chance of overcast {hourly.chances_of_overcast}%'
        hour_rain = f'Chance of rain {hourly.chances_of_rain}%'
        hour_snow = f'Chance of snow {hourly.chances_of_snow}%'
        hour_sun = f'Chance of sunshine {hourly.chances_of_sunshine}%'
        hour_thunder = f'Chance of thunder {hourly.chances_of_thunder}%'
        hour_wind = f'Chance of being windy {hourly.chances_of_windy}%'
        hour_cloud = f'Cloud cover {hourly.cloud_cover}%'
        hour_desc = f'{hourly.description} and {hourly.kind} skies'
        hour_dew = f'Dew point of {hourly.dew_point}°C'
        hour_feelsLike = f' Feels like {hourly.feels_like}°C'
        hour_hum = f' Humidity of {hourly.humidity}%'
        hour_precipitation = f'{hourly.precipitation}mm of precipitation'
        hour_temp = f' Temperature {hourly.temperature}°C'
        hour_time = f' At {hourly.time}'
        hour_uv = f'{hourly.ultraviolet} UV index'
        hour_vis = f'{hourly.visibility} Km of visibility'
        hour_windChill = f'Wind chill of {hourly.wind_chill}°C'
        hour_windDir = f'{hourly.wind_direction} wind'
        hour_windGust = f'Gusting up to {hourly.wind_gust} Km per hour'
        hour_windSpeed = f'Wind speed of {hourly.wind_speed} Km per hour'

        #print(hour_time)

        # Remove empty values
        if hourly.chances_of_overcast == 0:
          hour_overcast = None
        else:
          #print(hour_overcast)
          continue
          
        if hourly.chances_of_rain == 0:
          hour_rain = None
        else:
          #print(hour_rain)
          continue
        
        if hourly.chances_of_snow == 0:
          hour_snow = None
        else:
          #print(hour_snow)
          continue
        
        if hourly.chances_of_sunshine == 0:
          hour_sun = None
        else:
          #print(hour_sun)
          continue
        
        if hourly.chances_of_thunder == 0:
          hour_thunder = None
        else:
          #print(hour_thunder)
          continue
        
        if hourly.chances_of_windy == 0:
          hour_wind = None
        else:
          #print(hour_wind)
          continue
        
        if hourly.cloud_cover == 0:
          hour_cloud = None
        else:
          #print(hour_cloud)
          continue

        if hourly.precipitation == 0:
          hour_precipitation = None
        else:
          #print(hour_precipitation)
          continue
        
        # Moar printing!!!
        '''
        print(f' --> {hour_desc}')
        print(f' --> {hour_dew}')
        print(f' --> {hour_feelsLike}')
        print(f' --> {hour_hum}')
        print(f' --> {hour_temp}')
        print(f' --> {hour_uv}')
        print(f' --> {hour_vis}')
        print(f' --> {hour_windChill}')
        print(f' --> {hour_windDir}')
        print(f' --> {hour_windGust}')
        print(f' --> {hour_windSpeed}')
        '''
  return now_temp, now_dateTime, now_desc, now_feelsLike, now_humd,\
      now_precip, now_press, loc, region, country, now_uv, now_vis,\
      now_wind, daily_date, daily_high, daily_low, hour_desc, hour_dew,\
      hour_feelsLike, hour_hum, hour_overcast, hour_precipitation,\
      hour_rain, hour_snow, hour_sun, hour_temp, hour_thunder, hour_uv,\
      hour_vis, hour_wind, hour_windChill, hour_windDir, hour_windGust,\
      hour_windSpeed, hour_cloud, hour_time
#asyncio.run(getWeather())