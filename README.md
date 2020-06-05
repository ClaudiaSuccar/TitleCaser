# TitleCaser
Converts a string to a formalized title, avoiding capitalization of words such as 'and' or 'the' in the right context.

1. According to ALA format, these words should not be capitalized if they are not the first or last words of the title.
```python
nocap = ["and", "as", "but", "for", "nor", "or", "yet", "a", "an", "the", "at",
         "in", "by", "of", "on", "to"]
```

2. A function tc (title case) takes in two parameters, x being the user's input, and the list of exceptions.
```python
def tc(x, excpt):
```

3. x is modified into lowercase, then split at each space, resulting in a list of the lowercase words.
```python
x = x.lower().split(' ')
```

4. The list newlist is initialized with the requirement that the first word must be capitalized.
```python
newlist = [x[0].capitalize()]
```

5. The for loop iterates from the second word and stops at, but does not include, the last word. Its function is to capitalize all
words, with the exception of the words contained in nocap.
```python
    for word in x[1:-1]:
        # If the word is found in the excpt list...
        if word in excpt:
            # The word is appended to newlist as is (lowercase).
            newlist.append(word)
        else:
            # Else if it is not found in excpt, the capitalized version is appended to newlist.
            newlist.append(word.capitalize())
```

6. Lastly, the final word is appended to newlist, with the requirement that the last word must be capitalized.
```python
newlist.append(x[-1].capitalize())
```

7. The function tc returns joined newlist, with words separated by an empty space.
```python
return ' '.join(newlist)
```

## Output Examples
```
Input:
whAt HAvE wE cOme tO

Output:
What Have We Come To
```
```
Input:
tHe boY Of the NiLe In tHe wESt

Output:
The Boy of the Nile in the West
```

# What I Learned
- String methods, such as .lower(), .split(), and .capitalize()
- List methods, such as .append() and .join()
- List slicing
- The 'in' keyword
