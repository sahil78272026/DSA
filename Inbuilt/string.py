# encoding schemes : Unicode, ASCII, UTF-8, UTF-16, UTF-32, ISO/IEC 8859-1, URL encoding, EBCDIC, Base64, Character encoding in HTML, Windows-1252, Windows-1254

# question: difference between isdecimal(), isdigit() and isnumeric()
# question: difference between index() and find()

s = 'python is Popular prOgramming is language pr'
print('Original String : ', s)

news = s.capitalize() # does not take any argument, capitalize first character and returns a new string
print("s.capitalize() :", news)

news = news.casefold() # does not take any argument, convert uppercase to lowercase, almost same as .lower() and returns a new string
print('news.casefold() :', news)

newsCenter = news.center(50, '*') # The center() method returns a new centered string after padding it with the specified character.
# first arg: width - length of the string with padded characters
# second arg: fillchar (optional) - padding charactert
# first arg number should be greater than the length of the string, otherwise characher paddhing will not be done
# character will start padding from right then left one by one
print('news.center(50, "*") :', newsCenter)

print('news.count("pr") :',news.count('pr')) #4 # The count() method returns the number of occurrences of a substring in the given string.


newsEncode = news.encode() # converts the unicode string into utf-8
"""By default, the encode() method doesn't require any parameters.
It returns an utf-8 encoded version of the string. In case of failure, it raises a UnicodeDecodeError exception.
However, it takes two parameters:
encoding - the encoding type a string has to be encoded to
errors - response when encoding fails. There are six types of error response
strict - default response which raises a UnicodeDecodeError exception on failure
ignore - ignores the unencodable unicode from the result
replace - replaces the unencodable unicode to a question mark ?
xmlcharrefreplace - inserts XML character reference instead of unencodable unicode
backslashreplace - inserts a \\uNNNN escape sequence instead of unencodable unicode
namereplace - inserts a \\N{...} escape sequence instead of unencodable unicode
"""
print('news.encode() :',newsEncode)

# expandtabs() ?

newsEndsWith = news.endswith('ge') # The endswith() method returns True if a string ends with the specified suffix. If not, it returns False.
print('news.endswith("ge") 1:',newsEndsWith)


#find
newsFind = news.find('pop') # The find() method returns the index of first occurrence of the substring (if found). If not found, it returns -1.
print('news.find("pop") :', newsFind)
#rfind
# rfind() method returns an integer value.
# If substring exists inside the string, it returns the highest index where substring is found.
# If substring doesn't exist inside the string, it returns -1.
quote = 'Let it be, let it be, let it be'
result = quote.rfind('let it')
print("Substring 'let it':", result) #22
result = quote.rfind('small')
print("Substring 'small ':", result)# -1
result = quote.rfind('be,')
if  (result != -1):
  print("Highest index where 'be,' occurs:", result) #18
else:
  print("Doesn't contain substring")



# format() ?
# format_map() ?

#index
newIndex = news.index('is') # The index() method returns the index of a substring inside the string (if found). If the substring is not found, it raises an exception.
# If substring doesn't exist inside the string, it raises a ValueError exception.
# The only difference is that find() method returns -1 if the substring is not found, whereas index() throws an exception.
print('news.index("is") :', newIndex) # 7

#rindex
# If substring exists inside the string, it returns the highest index in the string where the substring is found.
# If substring doesn't exist inside the string, it raises a ValueError exception.
print('news.rindex("is") :',news.rindex("is")) # 30





print('news.isalnum() : ',news.isalnum()) # The isalnum() method returns True if all characters in the string are alphanumeric (either alphabets or numbers). If not, it returns False.

print('news.isalpha() : ',news.isalpha()) # True if all characters in the string are alphabets (can be both lowercase and uppercase).
    # False if at least one character is not alphabet.

print('news.isascii() : ',news.isascii()) # The isascii() method returns True if the string is empty or all characters in the string are ASCII.

print('news.isdecimal() : ',news.isdecimal()) # The isdecimal() returns:
# True if all characters in the string are decimal characters.
# False if at least one character is not decimal character.

print('news.isdigit() : ',news.isdigit()) # The isdigit() method returns True if all characters in a string are digits. If not, it returns False.

print('news.islower() : ',news.islower()) # return true if all the characters of the string are in lowercase, esle false

print('news.isnumeric() : ',news.isnumeric()) # The isnumeric() method checks if all the characters in the string are numeric.


text1 = 'python programming' # The isprintable() method returns True if all characters in the string are printable. If not, it returns False.
print('text1.isprintable() : ', text1.isprintable()) # True
text1 = 'python programming\n'
print('text1.isprintable() : ',text1.isprintable()) # False

print('news.istitle() : ', news.istitle()) # returns true if first character of every word is Uppercase

print('news.isupper() : ',news.isupper()) # return true if all the characters of the string are in uppercase, esle false


# The string join() method returns a string by joining all the elements of an iterable (list, string, tuple), separated by the given separator.
text = ['Python', 'is', 'a', 'fun', 'programming', 'language']
text1 = 'python'
str1 = '88'.join(text)
str2 = '99'.join(text1)
print(str1) # Python88is88a88fun88programming88language
print(str2) # p99y99t99h99o99n

# ljust, rjust
# width - width of the given string. If width is less than or equal to the length of the string, the original string is returned.
# fillchar (Optional) - character to fill the remaining space of the width
text1 = 'python'
text1_ljust = text1.ljust(8)
print('text1.ljust(8) :',text1_ljust) # python     , with 2 spaces on the right of the string

text1_rjust = text1.rjust(8)
print('text1.rjust(8) :',text1_rjust) #   python     , with 2 spaces on the left of the string

str_lower = news.lower() # converts all characters to lower and returns a new string
print('news.lower() : ' , str_lower)

str_upper = news.upper() # converts all characters to upper and returns a new string
print('news.upper() : ' , str_upper)


# strip
text = '---hello----'
print(text.lstrip('-')) # hello----
print(text.rstrip('-')) # ---hello
print(text.strip('-')) # hello


# partition
# The partition method returns a 3-tuple containing:
# the part before the separator, separator parameter, and the part after the separator if the separator parameter is found in the string
# the string itself and two empty strings if the separator parameter is not found
text = 'python is fun'
print(text.partition('is')) # ('python ', 'is', ' fun')
print(text.partition('not')) # ('python is fun', '', '')
text = 'python is fun, isn''t it'
print(text.partition('is')) # ('python ', 'is', ' fun, isnt it'), # splits at first occurence of 'is'

#rpartition
text = 'python is fun, isn''t it'
print('text.rpartition("is")' , text.rpartition('is')) # ('python ', 'is', ' fun, isnt it'), # splits at last occurence of 'is'
print('text.rpartition("not") :', text.rpartition('not')) # ('', '', 'python is fun, isnt it')


# #replace
# The replace() method can take a maximum of three arguments:
# old - the old substring we want to replace
# new - new substring which will replace the old substring
# count (optional) - the number of times you want to replace the old substring with the new string
# Note: If count is not specified, the replace() method replaces all occurrences of the old substring with the new string.
text = 'python is fun, not fun, fun not fun'
print(text.replace('fun','horror')) # python is horror, not horror, horror not horror
print(text.replace('fun','horror',1)) # python is horror, not horror, horror not horror


#split



