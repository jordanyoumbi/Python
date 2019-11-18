# function qui prend 2 arguments en parametres

def clean_string(string, change_string):
    replacement_string = ""
    cleaned_string = string.replace(change_string, replacement_string)
    return(cleaned_string)

goal = clean_string("Goal!!!!!!!", "!")
print(goal)

# function qui prend 3 arguments en parametres

def jordan(string_text, a_changer, le_nouveau):
    nouveau_text = string_text.replace(a_changer, le_nouveau)
    return(nouveau_text)

goal2 = jordan("je suis peut-etre !!!!la et !!!!vous?", "!", "")
print(goal2)
