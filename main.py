from pyscript import document

def verify_account(event):
    # Get values from input boxes
    u = document.querySelector("#user").value
    p = document.querySelector("#pass").value
    out = document.querySelector("#output")
    
    # Requirement: Username at least 7 characters
    if len(u) < 7:
        out.style.color = "#ff8a80"
        out.innerHTML = "Username must contain at least 7 characters.<br>Try again"
        return

    # Requirement: Password at least 10 characters long
    if len(p) < 10:
        diff = 10 - len(p)
        out.style.color = "#ff8a80"
        out.innerHTML = f"Your password is too short. Add at least {diff} more character/s to proceed.<br>Try again"
        return

    # Requirement: Password must have letter and number
    has_letter = any(c.isalpha() for c in p)
    has_number = any(c.isdigit() for c in p)

    if not has_letter or not has_number:
        out.style.color = "#ff8a80"
        out.innerHTML = "Password must contain at least one letter and one number.<br>Try again"
    else:
        # Success message
        out.style.color = "#2d6a4f"
        out.innerHTML = "<b>✨ Success! Welcome to the Games! ✨</b>"
