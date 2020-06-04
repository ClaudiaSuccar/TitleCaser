# TitleCaser
Converts a string to a formalized title, avoiding capitalization of words such as 'and' or 'the' in the right context.

1. According to ALA format, the following words should not be capitalized if they are not the first or last words of the title. The list of words to be left lowercase, given the right context, are stored in the array, noCap.

```python
noCap = ["and", "as", "but", "for", "nor", "or", "yet", "a", "an", "the", "at",
         "in", "by", "of", "on", "to"]
```

2. A function tc (title case) takes in two parameters, x being the user's input, and the list of exceptions.
```python
def tc(x, excpt):
```

3. x is modified into lowercase, then split at each space, resulting in an array of the lowercase words.
```python
x = x.lower().split(' ')
```

4. The array new_arr is initialized with the requirement that the first word must be capitalized.
```python
new_arr = [x[0].capitalize()]
```

5. The for loop iterates from the second word and stops at, but does not include, the last word.
```python
for word in x[1:-1]:
```

6. If the word is found in the excpt array, the word is appended to new_arr as is (lowercase).
```python
if word in excpt:
  new_arr.append(word)
```

8. Else if it is not found in excpt, the capitalized version is appended to new_arr.
```python
else:
  new_arr.append(word.capitalize())
```

9. Lastly, the final word is appended to new_arr, with the requirement that the last word must be capitalized.
```python
new_arr.append(x[-1].capitalize())
```

10. The function tc returns joined new_arr, with words separated by an empty space.
```python
return ' '.join(new_arr)
```
