import requests

def pull_weather_data(url, api_key):
  """
  This function takes the url with query and api key and pull the data using
  python's request module.
  """
  ## if the code in try block gives error then we will return False
  try:
    res = requests.get(url)
    data = res.json()
  except:
    return False
  # if response was successful then data will be returned
  return data

def print_report(data):
  """
  This function Parse the json file received from api response and print out all 
  the relevant information in more descriptive way.
  """
  # getting the name of city/state
  name = data['name']

  # looping through the main in data to get all relevant temperature information
  print(f'----------- Weather Report for {name} ------------')
  print('Overall Description:', data['weather'][0]['description'])
  for key in data['main']:
    if key not in ['humidity', 'pressure']:
      print(key,':', data['main'][key], 'C')
    else:
      print(key,':', data['main'][key])

  # same process for the wind report
  print('----- Wind Report -----')
  for key in data['wind']:
    print(key,':', data['wind'][key])
  print()

def main():
  """
  Main function that keep asking the user for their search and
  using all the relevant functions, it shows the weather report to the user.
  """
  # api key for authentication
  api_key = '8ec5615b2d4a21d1399634ba20734cf5'

  # running loop to make sure it works unitil user wants
  while True:

    ## asking the user for name or code of city
    city_info = input('Please enter the city name or zip code:')

    ## validating user input and creating api_url
    if city_info.isnumeric():
        api_url = f'http://api.openweathermap.org/data/2.5/weather?zip={city_info},us&appid={api_key}&units=metric'

    else:
        api_url = f'http://api.openweathermap.org/data/2.5/weather?q={city_info}&appid={api_key}&units=metric'

    ## pulling the data from web server
    data = pull_weather_data(api_url, api_key)
    
    ## data validation and report printing
    if data != False and data['cod'] != '404':
      print_report(data)

    else:
      print('[Error] The given information about city name or zip code was not found. Please try again.')
      continue
    # asking the user to search again
    search_again = input('Do you want to search again?: (y/n)')
    if search_again.lower() == 'y':
      continue
    else:
      print('Good Bye!')
      break

if __name__ == '__main__':
  main()    
