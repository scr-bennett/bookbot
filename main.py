def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        letters = list(file_contents.lower())
        alphabet = []
        for character in letters:
            if character.isalpha() == True:
                alphabet.append(character)
        
        count_dict = {}
        wordcount = len(words)
        for letter in alphabet:
            if letter in count_dict:
                count_dict[letter] += 1
            else:
                count_dict[letter] = 1

        new_list = []
        for key, value in count_dict.items():
            new_list.append({"key": key, "value":value})
        
        new_list.sort(key=lambda d: d["value"], reverse=True)
        
        
        print("--- Begin report of books/frankenstein.txt ---")
        print(wordcount, "words found in the document")
        print()
        for k in new_list:
            print (f"The '{k["key"]}' character was found, {k["value"]}, times")
        print("--- End report ---")
        


        
main()