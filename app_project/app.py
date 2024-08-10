import os
import sys

restaurants = [{'name': 'The Pancake House'.upper(), 'category': 'breakfast'.upper(), 'status': True},
               {'name': 'Sushi Central'.upper(), 'category': 'japanese'.upper(), 'status': False},
               {'name': 'Taco Haven'.upper(), 'category': 'mexican'.upper(), 'status': True}]

def show_app_name():
    '''Displays the name and introduction of the app with decorative formatting.'''
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def invalid_option():
    '''Handles invalid options by displaying an error message and returning to the main menu.'''
    print('Invalid option\n')
    input('Press any button to go back to the main menu')
    main()

def show_app_options():
    '''Displays the available options in the application menu.'''
    print('''
    1. Register restaurant
    2. List restaurants
    3. Switch restaurant status
    4. Exit
    ''')

def select_option():
    '''Prompts the user to select an option and executes the corresponding function.'''
    while True:
        try:
            option_selected = int(input('Select an option: '))
            match option_selected:
                case 1:
                    register_restaurant()
                case 2:
                    registered_restaurants()
                case 3:
                    restaurant_status()
                case 4:
                    exit_app()
                case _:
                    invalid_option()
            break
        except ValueError:
            print('Please enter a valid number.')
        except Exception as e:
            print(f'An unexpected error occurred: {e}')

def register_restaurant():
    '''Registers a new restaurant by prompting the user for details and adding it to the list.'''
    show_sub_titles('Register new restaurants\n')
    restaurant_name = input("What is the restaurant's name: ").upper().strip()
    category = input(f'What is the {restaurant_name} restaurant category: ').upper().strip()

    if not restaurant_name or not category:
        print('Both name and category are required.')
        back_to_the_main_menu()
        return

    if any(restaurant['name'] == restaurant_name for restaurant in restaurants):
        print('It looks like a restaurant with that name is already registered. How about trying a different name?')
        back_to_the_main_menu()
        return

    restaurant_data = {'name': restaurant_name, 'category': category, 'status': False}
    restaurants.append(restaurant_data)
    print(f'The restaurant {restaurant_name} has been successfully registered\n')
    back_to_the_main_menu()

def registered_restaurants():
    '''Lists all registered restaurants with their name, category, and status.'''
    show_sub_titles('List of registered restaurants')
    print(f'{"Restaurant".ljust(25)} | {"Category".ljust(20)} | {"Status"}')
    for restaurant in restaurants:
        restaurant_name = restaurant['name']
        category = restaurant['category']
        status = 'ACTIVE' if restaurant['status'] else 'INACTIVE'
        print(f'- {restaurant_name.ljust(25)} | {category.ljust(20)} | {status}')
    back_to_the_main_menu()

def restaurant_status():
    '''Switches the status of a restaurant from active to inactive or vice versa.'''
    show_sub_titles('Switching restaurant status')
    restaurant_name = input("Enter the restaurant's name to change its status: ").upper().strip()
    restaurant_found = False
    for restaurant in restaurants:
        if restaurant_name == restaurant['name']:
            restaurant_found = True
            restaurant['status'] = not restaurant['status']
            status = 'activated' if restaurant['status'] else 'deactivated'
            print(f'The restaurant {restaurant_name} has been successfully {status}')
            break
    if not restaurant_found:
        print(f"The restaurant {restaurant_name} wasn't found")
    back_to_the_main_menu()

def exit_app():
    '''Exits the application and prints a message.'''
    show_sub_titles('Exiting app...\n')
    sys.exit()

def back_to_the_main_menu():
    '''Returns to the main menu after the user presses a button.'''
    input('Press any button to go back to the main menu')
    main()

def show_sub_titles(text):
    '''Clears the screen and prints the given text with decorative lines.'''
    clear_screen()
    line = '*' * len(text)
    print(line)
    print(text)
    print(line)
    print()

def clear_screen():
    '''Clears the console screen.'''
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    '''Main function to initialize and run the application.'''
    clear_screen()
    show_app_name()
    show_app_options()
    select_option()

if __name__ == '__main__':
    main()
