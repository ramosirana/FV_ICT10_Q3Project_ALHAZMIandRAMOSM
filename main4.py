from pyscript import document
import random

# sample player list
teammates = [
"Gonzales", "Ramos", "Funtanilla", "Paz", "Tiongson", "Mendoza", "Santos", "Cruz",
"San Juan", "De La Cruz", "Bandong", "Fabro", "Taguiga", "Datu", "Esguerra",
"Francisco", "Ibarra", "Clara", "Reyes", "Lilagan", "Belsa", "Mateo",
"Smith", "Mallari", "Natividad", "Naldoza", "Escarda",
"Deray", "Damaso", "Salvi", "Irene", "Pelaez",
"Tiago", "Tan", "Del Prado", "Ferrer", "Ligas"
]

def show_players(event=None):
    selected_team = document.getElementById("grade").value
    
    # pick 15 random players
    chosen_players = random.sample(teammates, 15)

    output = document.getElementById("output")

    # create HTML list
    html_list = "<h4>" + selected_team.upper() + " players:</h4><ul>"
    for player in chosen_players:
        html_list += f"<li>{player}</li>"
    html_list += "</ul>"

    output.innerHTML = html_list


# run when dropdown changes
document.getElementById("grade").addEventListener("change", show_players)
