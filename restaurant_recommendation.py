
types = ['german', 'japanese', 'vegetarian', 'french', 'african', 'american', 'barbecue', 'czech', 'chinese', 'thai',
         'mexican', 'indian', 'cafe', 'pizza', 'italian']


restaurant_data = [['german', "Esther's German Saloon", '3', '3', '22 Teutonic Ave.'],
                   ['japanese', 'Robatayaki Hachi','4', '5', '8 Hawthorne Ln.'],
                   ['vegetarian', 'BBQ Tofu Paradise', '2', '1', '22A King West'],
                   ['french', 'Le Bateau Rouge', '5', '4', '2 South Park Dr.'],
                   ['african', 'Khartoum Khartoum', '3', '2', '1566 Maple Rd.'],
                   ['american', "Sally's Diner", '4', '3', '96 College Blvd.'],
                   ['barbecue', 'Saucy Piggy', '3', '2', '623 Industrial Rd.'],
                   ['czech', 'Czech Point', '1', '4', '5567 Queen-Mary Rd'],
                   ['german', 'Der Speisewagen', '3', '5', '402 College Blvd.'],
                   ['chinese', 'Beijing Express', '2', '4', '38 Teutonic Ave.'],
                   ['thai', 'Satay Village', '4', '2', '12 High St.'],
                   ['mexican', 'Cancun', '3', '3', '2030 Maple Rd.'],
                   ['indian', 'Curry Up', '4', '5', '455 University'],
                   ['african', 'Carthage', '2', '1', '59 Court Terrace'],
                   ['american', 'Burgerama', '5', '4', '456 University'],
                   ['barbecue', 'Three Little Pigs', '3', '2', '12 Summer Court'],
                   ['czech', 'Little Prague', '4', '3', '44 Park Ave'],
                   ['german', 'Kohl Haus', '3', '2', '3421 Queen-Mary Rd'],
                   ['chinese', "Dragon's Tail", '1', '4', '8 Jasmine Rd.'],
                   ['thai', 'Hit Me Baby One More Thai', '3', '5', '12 Jasmine Rd.'],
                   ['mexican', 'The Whole Tamale', '2', '4', '401 University'],
                   ['indian', 'Birmingham Bhangra', '4', '2', '992 Riddick St.'],
                   ['mexican', 'Taqueria', '3', '3', '12 North Circle Dr.'],
                   ['mexican', "Pedro's", '4', '5', '5521 Alameda'],
                   ['chinese', 'Super Wonton Express', '2', '1', '223 Milliways Ave'],
                   ['indian', 'Naan Sequitur', '5', '4', '"Unit 12'],
                   ['japanese', 'Sakura', '3', '2', '"Unit 18'],
                   ['chinese', 'Shandong Lu', '4', '3', '335 University'],
                   ['indian', 'Curry Galore', '3', '2', '56 Park Ave'],
                   ['cafe', 'North by Northwest', '1', '4', '201 University'],
                   ['cafe', 'Full of Beans', '3', '5', '498 College Ave.'],
                   ['cafe', "Tropical Jeeve's Cafe", '2', '4', '550 Milliways Ave'],
                   ['cafe', 'Zardoz Cafe', '4', '2', '6202 Alameda'],
                   ['pizza', 'Angular Pizza', '1', '5', '2232 King St.'],
                   ['pizza', 'Flavia', '4', '5', '401 Riddick St.'],
                   ['pizza', "Luigi's House of Pies", '2', '1', '5 Garcia Ave.'],
                   ['pizza', 'Thick and Thin', '5', '4', '832 Dominican Ave.'],
                   ['pizza', 'When in Rome', '3', '2', '234 Valencia St.'],
                   ['pizza', 'Pizza 76', '4', '3', '76 Market St.'],
                   ['italian', 'Party Pasta', '5', '2', '70 E Main St']]


def prompt_food():
    ''' Prompt the User for their Choice '''

    print("What type of food would you like to eat?")
    print("Type the beginning of that food type and press enter to see if it's here.")
    char_input = input("").strip()
    return char_input 



def choices(char):
    ''' Create a trie from their input Choice '''
    types_trie =[]
    for choice in types:
        if char == choice[0]:
            types_trie.append(choice)
    return types_trie



def longest_common_subsequence(letter,food_list): 
    ''' Find the longest_common_subsequence and return what users expected it to be'''
    max_char=float("-inf")
    current_min = float('-inf')

    for food in food_list:
        current_min = lcs(letter,food)
        if current_min > max_char and food.startswith(letter):
            max_char = current_min
            looking_for = food
    return looking_for 


def lcs(string_a, string_b):
    ''' Dynamic Programming Logic to solve the Longest Common String between two strings'''
    # initialize the matrix 
    lookup_table = [[0 for x in range(len(string_b) + 1)] for x in range(len(string_a) + 1)]

    for i, char_a in enumerate(string_a):
        for j, char_b in enumerate(string_b):
             # If there is a match, 
            # fill that grid cell with the value to the top-left of that cell plus one
            if char_a == char_b:
                lookup_table[i + 1][j + 1] = lookup_table[i][j] + 1
            
            # If there is not a match, 
            # take the maximum value from either directly to the left or the top cell
            else:
                lookup_table[i + 1][j + 1] = max(
                    lookup_table[i][j + 1],
                    lookup_table[i + 1][j])

    # the bottom-right cell will hold the non-normalized LCS length value.
    return lookup_table[-1][-1]


def print_list(search): 
    ''' Display the result in the proper Format'''
    rating ='5'
    result = []
    for data in restaurant_data:
        if data[0] == search:
            json = {
                "Name": f"{data[1]}", 
                "Price": f"{data[2]}/{rating}", 
                "Rating": f"{data[3]}/{rating}", 
                "Address": f"{data[4]}" 
            }
            result.append(json)
    # Print the Result
    for item in result:
        for i in item:
            print(f"{i}: {item[i]}")
        print("--------------------------------\n")



if __name__ == '__main__':
    ''' The Main Logic Behind the Game'''
    print("--------------------------------\n")
    print("   Welcome to Nerd's Restaurant   \n")
    print("--------------------------------\n")
    yes_no_prompt=''
    while yes_no_prompt!='q':
        # Prompt For Food Type 
        char_input = prompt_food()
        print("\n")
        store_tries = choices(char_input) 


        while len(store_tries) !=1:
            print(f"With those beginning letters, your choices are: {store_tries}") 
            char_input = prompt_food()
            store_tries = choices(char_input)
    

        print(f"The only option with those beginning letters is {store_tries}. Do you want to look at {store_tries} restaurants?")
      
        user_input = prompt_food()
        print("\n")
        available_choice = longest_common_subsequence(user_input,store_tries) 
        print(f"The only option with those beginning letters is {available_choice}. Do you want to look at {available_choice} restaurants?")
        yes_no_prompt = input("Enter 'y' for yes and 'n' for no:").lower().strip()

        if yes_no_prompt =='y':
            print("\n")
            print_list(available_choice)
      







