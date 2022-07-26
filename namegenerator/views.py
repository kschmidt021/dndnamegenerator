from django.shortcuts import render
import numpy as np
import pandas as pd

# Create your views here.


def createname(request):
    #Read in database
    name_db = pd.read_csv(
        r"C:\Users\schmi\Desktop\FunProjects\dndnamegen\dndnamedb.csv")
# Determine Race
    race = request.GET['race']
    raceval = 0
    if race == "dragonborn":
        raceval = 0
    elif race == "dwarf":
        raceval = 3
    elif race == "elf":
        raceval = 6
    elif race == "gnome":
        raceval = 9
    elif race == "halfling":
        raceval = 12
    elif race == "half-orc":
        raceval = 15
    elif race == "tiefling":
        raceval = 17
    elif race == "human":
        nation = request.GET['nation']
        if nation == 'arabic':
            raceval = 20
        elif nation == 'celtic':
            raceval = 22
        elif nation == 'chinese':
            raceval = 24
        elif nation == 'egyptian':
            raceval = 26
        elif nation == 'english':
            raceval = 28
        elif nation == 'french':
            raceval = 30
        elif nation == 'greek':
            raceval = 32
        elif nation == 'german':
            raceval = 34
        elif nation == 'indian':
            raceval = 36
        elif nation == 'japanese':
            raceval = 38
        elif nation == 'mesoamerican':
            raceval = 40
        elif nation == 'african':
            raceval = 42
        elif nation == 'norse':
            raceval = 44
        elif nation == 'polynesian':
            raceval = 46
        elif nation == 'roman':
            raceval = 48
        elif nation == 'slavic':
            raceval = 50
        elif nation == 'spanish':
            raceval = 52
# Determine Gender
    gender = request.GET['gender']
    genval = 0
    if gender == "male":
        genval = 0
    elif gender == "female":
        genval = 1
    elif gender == "nonbinary":
        genval = np.random.randint(0, 2)
# Parses Database for Rows based on Gender and Race
    fnameval = genval + raceval
    lnameval = raceval + 2
# Creates a random number for the first name the length of the selected first name list
    fnum = np.random.randint(len(name_db))
# Creates a random number for the last name of the length of the selected last name list
    lnum = np.random.randint(len(name_db))
# Slice off first name
    slicedfname = name_db.iat[fnum, fnameval]
# Slice off last name
    slicedlname = name_db.iat[lnum, lnameval]
# Create the name
    if raceval == 15 or raceval >= 20:
        name = str(slicedfname).upper()
        nation = str(nation).capitalize()
    else:
        name = str(slicedfname).upper()+" "+str(slicedlname).upper()
        nation = ""
# Turn other components uppercase
    gender = str(gender).capitalize()
    race = str(race).capitalize()
    return render(request, 'namegenerator/index.html', {"created_name": name, "race": race, "gender": gender, "nation": nation})


def namegen(request):
    return render(request, 'namegenerator/index.html')
