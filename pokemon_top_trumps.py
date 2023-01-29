import random
import requests
def random_pokemon():
    pokemon_number = random.randint(1, 151)  #took a random number between 1 and 151
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_number}/"
    response = requests.get(url)
    pokemon = response.json()
    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
    }
def run(c=0,d=0): #added two parameters c and d as counters
    my_pokemon = random_pokemon()
    print(f"You were given {my_pokemon['name']}")
    stat_choice = input('Which stat do you want to use? (id, height, weight) ') #player chooses the stat their pokemon would compete with
    opponent_pokemon = random_pokemon()
    print(f"The opponent chose {opponent_pokemon['name']}")
    my_stat = my_pokemon[stat_choice]
    opponent_stat = opponent_pokemon[stat_choice]
    if my_stat > opponent_stat:
        print('You Win!')
        c+=1
    elif my_stat < opponent_stat:
        print('You Lose!')
        d+=1
    else:
        print('Draw!')
    if c>d: #verifies if the player won more rounds
        print("You won more rounds. Congratulations!")
    elif c<d: #verifies if the computer won more rounds
        print("Your opponent won more rounds. Keeping training to be the very best.")
    else: #verifies if c=d
        print("It is evenly matched.")
while True:
    run()
    play_again = input("Would you like to play again? (y/n)")
    if play_again.lower() == 'n':
        break
print("Thanks for playing! Come back to battle everyday with your pokemon team.") 
