def pig_it(text):
    print(text)

    if text[-4:] == " !ay" or text[-4:] == " ?ay":
        return text[:-2]
    
    new_string = ""

    for x in text.split(" "):
        new_string += x[1:] + x[0] + "ay" + " "


    if new_string[-5:] == " !ay " or new_string[-5:] == " ?ay ":
        return new_string[:-3]

    new_string = new_string[0:-1]
    
    return new_string


#pig_it('Pig latin is cool')#'igPay atinlay siay oolcay'
#pig_it('This is my string')#'hisTay siay ymay tringsay'
pig_it('O tempora o mores !')

"""
Move the first letter of each word to the end of it, then add "ay" 
to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""