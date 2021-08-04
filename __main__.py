### 0 - IMPORTS AND CONNECTION TO DATABASE ###

from pymongo import MongoClient
from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np
from datetime import date, datetime

HOST = '15.236.51.148'
USER_NAME = 'rhobs'
PASSWORD = 'xeiPhie3Ip8IefooLeed0Up6'
AUTH_SOURCE = 'rhobs'

client = MongoClient(host = HOST, username = USER_NAME, password = PASSWORD, authSource = AUTH_SOURCE)
db = client.rhobs
collection = db.test


### 1 - NUMBER OF LISTENERS BY MUSIC ###


def getData(people,data):
    '''
    people: a document of the collection
    data: a key (city or job or iban or color or phone or phone or birthdate) of the dictionnary stored in the value of the name Object
    Returns the value (data) matching the key (people)
    '''
    return people[list(people.keys())[1]][data]

def numberOfListenersByMusic():
    '''
    Returns a dictionnary :
        -keys : type of music
        -values : number of listeners
    '''
    number_of_listeners_by_music = {}
    for people in collection.find({}):
        musics = getData(people,'music')
        for music in musics:
            if music in number_of_listeners_by_music:
                number_of_listeners_by_music[music]+=1
            else:
                number_of_listeners_by_music[music] = 1

    return number_of_listeners_by_music

#pprint(numberOfListenersByMusic())

def displayNumberOfListenersByMusic():
    '''
    Displays the output of the previous function

    WARNING : it is recommended to display the window in full screen
    '''
    number_of_listeners_by_music = numberOfListenersByMusic()
    type_of_music = list(number_of_listeners_by_music.keys())
    number_of_listeners = list(number_of_listeners_by_music.values())

    for index,value in enumerate(number_of_listeners):
        plt.text(x = index, y = value, s = str(value), ha = 'center')

    plt.title("Number of listeners by music")
    plt.xlabel("Type of music")
    plt.ylabel("Number of listeners")
    plt.bar(type_of_music,number_of_listeners)
    plt.show()

#displayNumberOfListenersByMusic()


### 2 - AVERAGE AGE BY MUSIC ###


current_date = date.today()

def getAge(people):
    '''
    people: a document of the collection
    Returns the age of this people

    WARNING : We assume here that 'age' means the common definition so that it is always a positive integer ; it is not the decimal age
    reflecting months, weeks or days (only years)
    '''
    birthdate = datetime.strptime(getData(people,'birthdate'),'%Y-%m-%d')
    age = current_date.year - birthdate.year - ((current_date.month,current_date.day)<(birthdate.month,birthdate.day))
    return age

def averageAgeByMusic():
    '''
    Returns a dictionnary :
        -keys : type of music
        -values : average age rounded to 1 decimal
    '''
    stats_by_music = {} #contains current number of listeners and sum of ages, while looping 
    for people in collection.find({}):
        musics = getData(people,'music')
        age = getAge(people)
        for music in musics:
            if music in stats_by_music :
                stats_by_music[music]['sum_ages']+=age
                stats_by_music[music]['listeners']+=1
            else:
                stats_by_music[music] = {'sum_ages':age,'listeners':1}
        
    average_age_by_music = {}
    for music in stats_by_music:
        average_age_by_music[music] = round(stats_by_music[music]['sum_ages']/stats_by_music[music]['listeners'],1)

    return average_age_by_music

#pprint(averageAgeByMusic())

def displayAverageAge():
    '''
    Displays the output of the previous function

    WARNING : it is recommended to display the window in full screen
    '''
    average_age_by_music = averageAgeByMusic()
    type_of_music = list(average_age_by_music.keys())
    average_age = list(average_age_by_music.values())

    for index,value in enumerate(average_age):
        plt.text(x = index, y = value, s = str(value), ha = 'center')

    plt.title("Average age of listeners by music")
    plt.xlabel("Type of music")
    plt.ylabel("Average age of listeners")
    plt.bar(type_of_music,average_age)
    plt.show()

#displayAverageAge()

### 3 - PYRAMID AGE ###


def pyramidAge(city,slice):
    '''
    city: a city of type str matching one of the city instances of the collection 
    slice: a positive integer between 1 and 100

    Returns a dictionnary :
        -keys : age slices
        -values : number of people in the city
    '''
    number_of_slices = int(np.floor(100/slice))
    number_of_people_by_slice_number = [0 for i in range(number_of_slices+1)]

    for people in collection.find({}):
        people_city = getData(people,'city')
        if people_city == city:
            age = getAge(people)
            if age>=100:
                slice_number = -1
            else:
                slice_number = int(np.floor(age/slice))
            number_of_people_by_slice_number[slice_number]+=1

    number_of_people_by_slice = {str(str(i*slice)+"-"+str((i+1)*slice-1)):number_of_people_by_slice_number[i] for i in range(number_of_slices)}
    number_of_people_by_slice[str('over '+str(slice*number_of_slices))] = number_of_people_by_slice_number[-1]

    return number_of_people_by_slice

#pprint(pyramidAge('Prevost',10))

def displayPyramidAge(city,slice):
    '''
    city: a city of type str found in the city instances of the database 
    slice: a positive integer between 1 and 100

    Displays a pyramid which represents the population of the city sliced by years (given by slice argument)
    '''
    number_of_people_by_slice = pyramidAge(city,slice)
    slices = list(number_of_people_by_slice.keys())
    number_of_people = list(number_of_people_by_slice.values())

    for index,value in enumerate(number_of_people):
        plt.text(x = index, y = value, s = str(value), ha = 'center')

    plt.title("Pyramid of ages in the city of {} sliced by {} years".format(city,slice))
    plt.ylabel("Population")
    plt.xlabel("Age (years)")
    plt.bar(slices, number_of_people)
    plt.show()

#displayPyramidAge("Prevost",13)