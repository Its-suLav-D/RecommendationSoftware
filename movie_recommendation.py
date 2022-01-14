import json

 
CATEGORIES = set()
MOVIES_DATA=[]


def read_file():
    '''Read the File'''
    try:
        file = open("Names.json", "r")
        board_text = file.read()
        board_json = json.loads(board_text)
        MOVIES_DATA.append(board_json)

    except:
        print("Error Reading Board")
        return



def create_category():
    ''' Create A Category for the json '''
    lists =[]
    for item in MOVIES_DATA:
        for val in item:
            values = val['Genre'].replace(" ", "")
            lists.append(values.split(','))

    for val in lists:
        for item in val:
            if item not in CATEGORIES:
                CATEGORIES.add(item.lower())


def prompt_movie():
    ''' Prompt the User for their Choice '''

    print("What type of Movie would you like to watch?")
    print("Type the beginning of the Genre and press enter to see if it's here.")
    char_input = input("").strip()
    return char_input 


def longest_common_subsequence(letter,movie_list): 
    ''' Find the longest_common_subsequence and return what users expected it to be'''
    looking_for=[]

    for val in movie_list:
        valid = starts_with(letter,val)
        if valid:
            looking_for.append(val)
    

    return looking_for 

def starts_with(letter, genre):
    ''' Check to see if that's they are looking for or not '''
    for i in range(len(letter)):
        if letter[i] != genre[i]:
            return False 

    

    return True 

def find_movie_with_genre(genre):
    ''' Find movie with that Genre '''
    movies =[]
    for item in MOVIES_DATA:
        for val in item:
            if genre in val['Genre']:
                movies.append(val)

    return movies 


def pretty_print(movies):
    ''' Pretty Print the Movie Name'''
    for item in movies:
        item.pop("Genre", None)
        for key in item:
            print(f'{key}: {item[key]}')
        print("\n***********************************************\n")




if __name__ == '__main__':
    # Read the File 
    read_file()
    # Create Category From the Genres 
    create_category()
    # Welcome the User 
    print("Welcome to Nerd's Search Lab")
    valid_input = ''
    while valid_input!='q':
        genre_choice = prompt_movie() 

        available = longest_common_subsequence(genre_choice, CATEGORIES)

        while len(available) !=1 :
            print(f"We found few genres that fits your criteria {available}, give us more information so we can narrow it for you!!\n")
            genre_choice = prompt_movie() 
            available = longest_common_subsequence(genre_choice, CATEGORIES)

        print(f"The Genre with that Beginning is: {available}")  
    
        valid_input =  input("Enter 'y' for yes, 'n' for No, 'Q' to Quit Search ").lower().strip()


        if valid_input == "y":
            genre = available[0].capitalize()
            movies = find_movie_with_genre(genre)
            pretty_print(movies)
        print("\n")

    
  
    




