"""
This program will take a string and translate the sting into pig latin.

"""

def find_vowel(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    ##find vowel and give index
    for i in range(len(word)):
        if word[i] in vowels:
            return i
    return -1    
#
def translate(words):
    ##strips punctuation with the english function
    text_lowered = english_text(words)
    
    ##new list for the translated words
    new = []
    
    ##splits string into list
    new_text = text_lowered.split(" ")
           
    for word in new_text:
        vowel = find_vowel(word)
       
        ##no vowel
        if(vowel == -1):
            new.append(word)

        ##vowel or y as first letter
        elif vowel == 0:
            word = word + "way"
            new.append(word)
  
        else:
            ##vowel elsewhere within word
            word = word[vowel:] + word[:vowel] + "ay"
            new.append(word)

    ##joins together list as new string        
    new = " ".join(new)
    return new

def english_text(text):
    
    ##removes all punctuation
    text = text.replace("\n", "")
    text = text.replace(",", "")
    text = text.replace(".", "")
    text = text.replace("!", "")
    text = text.replace("?", "")
    
    ##lowers text
    new = text.lower()
    
    ##returns string
    return new


def main():
    print("Pig Latin Translator\n\n")
    choice = "y"
    while choice == "y":
        text = input("Enter text: ")
        
        ##lower case/removed punctuation
        english = english_text(text)
        print("English: ", english)
        
        ##translated text
        pig_latin = translate(text)
        print("Pig Latin: ", pig_latin)
        
        choice = input("Continue y/n: ")
    print("Bye")
              

if __name__=="__main__":
    main()