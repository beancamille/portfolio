from markov import Markov
import numpy as np
import operator

# create starting weather for each of 7 major cities
city_weather = {
    'New York': 'rainy',
    'Chicago': 'snowy',
    'Seattle': 'rainy',
    'Boston': 'hailing',
    'Miami': 'windy',
    'Los Angeles': 'cloudy',
    'San Francisco': 'windy'
}

# load probabilities from weather.csv
weather = np.genfromtxt('weather.csv', delimiter=",") 

# for NY, run 100 simulations to find weather for day 7, given that day 0 is rainy. save predictions as dictionary.
NY_weather = Markov('rainy')
NY_weather.load_data(weather)    
NY_sims = NY_weather.get_weather_for_day(7,100)
NY_predictions = {
    'sunny': NY_sims.count('sunny'),
    'cloudy': NY_sims.count('cloudy'),
    'windy': NY_sims.count('windy'),
    'rainy': NY_sims.count('rainy'),
    'hailing': NY_sims.count('hailing'),
    'snowy': NY_sims.count('snowy')
}

# for Chicago, run 100 simulations to find weather for day 7, given that day 0 is snowy. save predictions as dictionary.
Chi_weather = Markov('snowy')
Chi_weather.load_data(weather)    
Chi_sims = Chi_weather.get_weather_for_day(7,100)
Chi_predictions = {
    'sunny': Chi_sims.count('sunny'),
    'cloudy': Chi_sims.count('cloudy'),
    'windy': Chi_sims.count('windy'),
    'rainy': Chi_sims.count('rainy'),
    'hailing': Chi_sims.count('hailing'),
    'snowy': Chi_sims.count('snowy')
}

# for Seattle, run 100 simulations to find weather for day 7, given that day 0 is rainy. save predictions as dictionary.
Se_weather = Markov('rainy')
Se_weather.load_data(weather)    
Se_sims = Se_weather.get_weather_for_day(7,100)
Se_predictions = {
    'sunny': Se_sims.count('sunny'),
    'cloudy': Se_sims.count('cloudy'),
    'windy': Se_sims.count('windy'),
    'rainy': Se_sims.count('rainy'),
    'hailing': Se_sims.count('hailing'),
    'snowy': Se_sims.count('snowy')
}

# for Boston, run 100 simulations to find weather for day 7, given that day 0 is hailing. save predictions as dictionary.
Bo_weather = Markov('hailing')
Bo_weather.load_data(weather)    
Bo_sims = Bo_weather.get_weather_for_day(7,100)
Bo_predictions = {
    'sunny': Bo_sims.count('sunny'),
    'cloudy': Bo_sims.count('cloudy'),
    'windy': Bo_sims.count('windy'),
    'rainy': Bo_sims.count('rainy'),
    'hailing': Bo_sims.count('hailing'),
    'snowy': Bo_sims.count('snowy')
}

# for Maimi, run 100 simulations to find weather for day 7, given that day 0 is windy. save predictions as dictionary.
Mi_weather = Markov('windy')
Mi_weather.load_data(weather)    
Mi_sims = Mi_weather.get_weather_for_day(7,100)
Mi_predictions = {
    'sunny': Mi_sims.count('sunny'),
    'cloudy': Mi_sims.count('cloudy'),
    'windy': Mi_sims.count('windy'),
    'rainy': Mi_sims.count('rainy'),
    'hailing': Mi_sims.count('hailing'),
    'snowy': Mi_sims.count('snowy')
}

# for LA, run 100 simulations to find weather for day 7, given that day 0 is cloudy. save predictions as dictionary.
LA_weather = Markov('cloudy')
LA_weather.load_data(weather)    
LA_sims = LA_weather.get_weather_for_day(7,100)
LA_predictions = {
    'sunny': LA_sims.count('sunny'),
    'cloudy': LA_sims.count('cloudy'),
    'windy': LA_sims.count('windy'),
    'rainy': LA_sims.count('rainy'),
    'hailing': LA_sims.count('hailing'),
    'snowy': LA_sims.count('snowy')
}

# for SF, run 100 simulations to find weather for day 7, given that day 0 is windy. save predictions as dictionary.
SF_weather = Markov('windy')
SF_weather.load_data(weather)    
SF_sims = SF_weather.get_weather_for_day(7,100)
SF_predictions = {
    'sunny': SF_sims.count('sunny'),
    'cloudy':SF_sims.count('cloudy'),
    'windy': SF_sims.count('windy'),
    'rainy': SF_sims.count('rainy'),
    'hailing': SF_sims.count('hailing'),
    'snowy': SF_sims.count('snowy')
}

#print counts of weather predicted for each city
print('New York:', NY_predictions)
print('Chicago:', Chi_predictions)
print('Seattle:', Se_predictions)
print('Boston:', Bo_predictions)
print('Miami:', Mi_predictions)
print('Los Angeles:', LA_predictions)
print('San Francisco:', SF_predictions)

print('Most likey weather in seven days:')
print('----------------------------------')

#print most likely weather for each city
print('New York:', max(NY_predictions.items(), key=operator.itemgetter(1))[0])
print('Chicago:', max(Chi_predictions.items(), key=operator.itemgetter(1))[0])
print('Seattle:', max(Se_predictions.items(), key=operator.itemgetter(1))[0])
print('Boston:', max(Bo_predictions.items(), key=operator.itemgetter(1))[0])
print('Miami:', max(Mi_predictions.items(), key=operator.itemgetter(1))[0])
print('Los Angeles:', max(LA_predictions.items(), key=operator.itemgetter(1))[0])
print('San Francisco:', max(SF_predictions.items(), key=operator.itemgetter(1))[0])