#converts string to "search format"


def drama_search():

    dramaInput = "example here and here"

    dramaInput = dramaInput.split()
    dramaInput = 'https://mydramalist.com/search?q=' + '+'.join(dramaInput)

    return(dramaInput)