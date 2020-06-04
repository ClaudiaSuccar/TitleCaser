# According to ALA format, these words should not be capitalized if they are not the first or last words of the title.
# The list of words to be left lowercase, given the right context, are stored in the array, noCap.
noCap = ["and", "as", "but", "for", "nor", "or", "yet", "a", "an", "the", "at",
         "in", "by", "of", "on", "to"]

# A function tc (title case) takes in two parameters, x being the user's input, and the list of exceptions.
def tc(x, excpt):

    # x is modified into lowercase, then split at each space, resulting in an array of the lowercase words.
    x = x.lower().split(' ')
    # The array new_arr is initialized with the requirement that the first word must be capitalized.
    new_arr = [x[0].capitalize()]
    # The for loop iterates from the second word and stops at, but does not include, the last word.
    for word in x[1:-1]:
        # If the word is found in the excpt array...
        if word in excpt:
            # The word is appended to new_array as is (lowercase).
            new_arr.append(word)
        else:
            # Else if it is not found in excpt, the capitalized version is appended to new_arr.
            new_arr.append(word.capitalize())
    # Lastly, the final word is appended to new_arr, with the requirement that the last word must be capitalized.
    new_arr.append(x[-1].capitalize())
    # The function tc returns joined new_arr, with words separated by an empty space.
    return ' '.join(new_arr)

# The user is prompted to enter their string of words.
strInput = input("Enter the words you would like to title case:\n")
# The result of function tc, with arguments strInput and noCap, are printed to the console.
print(tc(strInput, noCap))
