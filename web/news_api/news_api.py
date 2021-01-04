import requests
import datetime
from colorama import Fore, Style

find_news = 'y'

categories = ['business', 'entertainment', 'general', 'health', 'science', 'sports', 'technology']

while True:

    # User-set conditions for keeping the game going. Checks for valid response.
    if find_news == 'y' or find_news == 'yes':
            pass
    elif find_news == 'n' or find_news == 'no':
        break
    else:
        print('Not a valid option - please enter yes (y) or no (n) in lowercase.')
        find_news = input("Would you like to find more news articles? [y/n] >> ")
        continue
    
    # opening prompt
    print('Welcome to Command Line News!\n\nPlease make a choice: [1] Top headlines [2] Search\n')
    choice = input('>> ')
    print("")

    # make sure the choice is an integer
    try:
        int(choice)
    # error message if not an integer
    except ValueError:
        print("Please enter one of the whole numbers 1 and 2, not other types of characters. Enter 1 or 2 and try again.\n")
        continue
    # headlines option
    if int(choice) == 1:
        print('\nSelect which category you would like to get headlines for:\n')
        # print the options to the user
        for i in range(0, len(categories)):
            print('[{}]'.format(i+1)+categories[i])
        print('')
        # get the user's choice.
        category_choice = input('>> ')
        # make sure the choice is a number
        try:
            category_choice = int(category_choice)
        except ValueError:
            print("Please enter a valid number 1 through 7. Non-integer characters are invalid. Re-run the program to try again.\n")
            break
        # category choice should be between numbers 1 through 7 inclusive
        if not (1<=int(category_choice)<=7):
            print("Please enter one of the listed integer options from 1 to 7. Re-run the program to try again.\n")
            break
        # get the category from the list of options
        category_choice = categories[category_choice-1]
        # plug into URL string
        url = ('http://newsapi.org/v2/top-headlines?'
            'country=us&'
            'category={}&'
            'apiKey=d1ea35c04826459f939e51a46a0ad70c').format(category_choice)
        # get response object
        response = requests.get(url)
        # we want the response text in JSON for parsing
        payload = response.json()
        # restrict to 10 headlines
        headlines = 10
        # the 'articles' JSON object is a list of dicts in python. Loop through the dicts.
        for dictnry in payload['articles']:
            # only ten headlines
            if headlines > 0:
                # get the datetime
                publish_dt = dictnry['publishedAt']
                publish_date = datetime.date(int(publish_dt[:4]),int(publish_dt[5:7]),int(publish_dt[8:10]))
                # print the title and formatted date
                print(Fore.GREEN + Style.BRIGHT + "* "+dictnry['title']+' - '+publish_date.strftime("%B %d, %Y"))
                # print the description if it exists, else just print a blank line
                if dictnry['description']:
                    print(Fore.CYAN + "\t> "+dictnry['description']+'\n')
                else:
                    print("")
                # decrement headline count
                headlines -= 1
            # break once we reach ten
            else:
                break
        # ask if user wants more
        find_news = input(Style.RESET_ALL + "Would you like to find more news articles? [y/n] >> ")
            
    # search option
    elif int(choice) == 2:
        # prompt
        print('Enter your search term:')
        search_term = input(">> ").lower()
        print("")
        # same code as headlines option with slight difference in URL
        url = ('http://newsapi.org/v2/top-headlines?'
            'q={}&'
            'apiKey=d1ea35c04826459f939e51a46a0ad70c').format(search_term)

        response = requests.get(url)

        payload = response.json()

        headlines = 10

        # make sure there are search results
        if payload['totalResults'] == 0:
            print("No results found for "+search_term+".\n")
        
        # we can print the same way as the first option
        else:
            for dictnry in payload['articles']:
                if headlines > 0:

                    publish_dt = dictnry['publishedAt']
                    publish_date = datetime.date(int(publish_dt[:4]),int(publish_dt[5:7]),int(publish_dt[8:10]))

                    print(Fore.GREEN + "* "+dictnry['title']+' - '+publish_date.strftime("%B %d, %Y"))

                    if dictnry['description']:
                        print(Fore.CYAN + "\t> "+dictnry['description']+'\n')
                    else:
                        print("")
                    headlines -= 1
                else:
                    break
        
        # while loop keeps going if response is yes
        find_news = input(Style.RESET_ALL + "Would you like to find more news articles? [y/n] >> ")

    else:
        print('Only numbers 1 and 2 are options. Please re-run and enter one of the valid options.')