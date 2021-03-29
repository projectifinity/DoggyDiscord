import requests, json

######## refreshes data
"""
def refresh_data():
    #grab data
    res = requests.get('https://www.thecocktaildb.com/api/json/v1/1/random.php')

    # converts response data to dict (like an array)
    info = json.loads(res.text)
    return info

data = refresh_data()
"""

def drink_grab (argu):

    ############ name of drink
    drinkName = data['drinks'][0]['strDrink']


    ########### ingredients

    igArr = []
    i = 0

    while True:
        iStr = str(i+1)
        strIgx = "strIngredient" + iStr

        # check ingredients key and value
        if (not strIgx in data['drinks'][0]):
            break
        if (bool(data['drinks'][0][strIgx]) == False):
            break
        
        else:
            ing = data['drinks'][0][strIgx]

            igArr.append(ing)
            i += 1

    ############ measurement amount

    meaArr = []
    i= 0

    while (True):
        iStr = str(i+1)
        strMeax = "strMeasure" + iStr

        # check if measurement value amount exists
        if (bool(data['drinks'][0][strMeax]) == False):
            break
        else:
            mea = data['drinks'][0][strMeax]
            meaArr.append(mea)
            i += 1

    ############ measure + ingredients

    # find length of ing array
    igLen = len(igArr)

    #match with measure, check to see if measure exists first
    meaLen = len(meaArr)

    # array with everything
    fullIg = []

    i = 0



    while (i < igLen):
        #checks if measurement value exists
        if (meaArr[i] == False):
            fullIg.append(igArr[i] + "\n")
            break
        else:
            fullIg.append(meaArr[i] + " " + igArr[i] + "\n" )
        i += 1

    print (''.join(fullIg))
    pfull = (''.join(fullIg))

    ########### directions

    direc = data['drinks'][0]['strInstructions']


    ########### image url

    imgLink = data['drinks'][0]['strDrinkThumb']

