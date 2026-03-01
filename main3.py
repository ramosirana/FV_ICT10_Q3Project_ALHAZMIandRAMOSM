from pyscript import document

def sub(event):
    # Get form elements
    reg_yes = document.getElementById("yes").checked
    med_yes = document.getElementById("yes2").checked
    grade = document.getElementById("grade").value
    section = document.getElementById("section").value
    output = document.getElementById("out")

    # Check eligibility conditions
    if not reg_yes:
        output.innerHTML = "Please complete your online registration first."
        return
    elif not med_yes:
        output.innerHTML = "Please secure your medical clearance first."
        return

    # Assign team
    teams = {
        "Blue Bears": [(7, "Sapphire"), (8, "Topaz"), (9, "Ruby"), (10, "Topaz")],
        "Green Hornets": [(7, "Emerald"), (8, "Ruby"), (9, "Emerald"), (9, "Jade"), (10, "Ruby")],
        "Yellow Tigers": [(7, "Ruby"), (8, "Emerald"), (9, "Sapphire"), (10, "Sapphire")],
        "Red Bulldogs": [(7, "Topaz"), (8, "Jade"), (8, "Sapphire"), (9, "Topaz"), (10, "Emerald")]
    }

    assigned_team = None

    for team_name, combinations in teams.items():
        if (int(grade), section) in combinations:
            assigned_team = team_name
            break

    if assigned_team:
        output.innerHTML = f"""Congratulations! You are eligible to join the Intramurals.<br>
        Your team is: {assigned_team}"""
    else:
        output.innerHTML = "Error assigning team. Please check your information."
