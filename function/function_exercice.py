def clean_text(text_string, special_characters, replacement_string):
    cleaned_string = text_string

    for string in special_characters: # special caractere est une liste
        cleaned_string = cleaned_string.replace(string, replacement_string)
        cleaned_string = cleaned_string.lower()
    return(cleaned_string)

clean_characters = [".", ",", "'", "\n"]
replacement = ""
clean_text = clean_text(text_string, clean_characters, replacement)
print(cleaned_text)
