import numpy as np

class Markov:
    # initialize class Markov
    def __init__(self, day_zero_weather = None):
        self.data = [] #create array for data
        
        #set day to zero, and weather to day zero weather
        if day_zero_weather == None: 
            raise Exception('Must enter day zero weather')
        else:
            self.day_zero_weather = day_zero_weather
        self._current_day_weather = self.day_zero_weather
        self._current_day = 0

    # load array into data
    def load_data(self, array):
        self.data = array

    # convert weather types to numeric codes
    def get_prob(self, cdw, ndw):
        def numtrans(a):
            if a == 'sunny':
                return 0
            elif a == 'cloudy':
                return 1
            elif a == 'rainy':
                return 2
            elif a == 'snowy':
                return 3
            elif a == 'windy':
                return 4
            elif a == 'hailing':
                return 5
            else: 
                raise Exception('Not a valid weather name')
        return self.data[numtrans(cdw), numtrans(ndw)]
    
    # define iteration
    def __iter__(self):
        return self

    # define next weather
    def __next__(self):
        # convert from code to weather names
        def wordtrans(a):
            if a == 0:
                return 'sunny'
            elif a == 1:
                return 'cloudy'
            elif a == 2:
                return 'rainy'
            elif a == 3:
                return 'snowy'
            elif a == 4:
                return 'windy'
            elif a == 5:
                return 'hailing'

        # list all weathers
        weathers = ['sunny','cloudy','rainy','snowy','windy','hailing']

        # find probability of next weather based on current weather
        prob = self.data[weathers.index(self._current_day_weather)]
        
        # increase days passed
        self._current_day += 1

        # choose next weather
        a = np.random.choice(6, 1, p = prob)

        # return weather as word
        return (wordtrans(a))

    def _simulate_weather_for_day(self, day):
        # set simulation to zero
        dex = 0
        self._current_day = 0 
        self._current_day_weather = self.day_zero_weather

        # predict weather by calling next 
        while dex < day:
            self._current_day_weather = next(self)
            
            dex += 1
        return self._current_day_weather

    # run a number of trials of the same simulation, by calling _simulate_weather_for_day
    def get_weather_for_day(self, day, trials = 5):
        sims = []
        
        trialindex = 0 
        while trialindex < trials:
            sims.append(self._simulate_weather_for_day(day))
            trialindex += 1
        return sims 