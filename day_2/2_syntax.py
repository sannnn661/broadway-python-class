# Like any other language Python has also its det of Keywords. There are around 35 keywords.
# Keywords are the reserved words of the language which cannot be used as variables or identifiers

help("keywords")

# Rules for naming identifiers

# 1. Identifiers are case sensitive i.e A = 1 and  a = 1 , "A" and "a" are two different identifiers
# 2. Identifiers cannot be the keywords
# 3. Identifiers  can't start with numbers
# 4. Identifiers can include from A-Z , a- z, 0-9 (but can't start with numbers) and underscore (_)
# 5. Identifiers can't include special characters like (/,$,@,*,%)



################# PYTHON STATEMENT ################

# Each line in a program is a python statements
# But sometimes multiple statements can be written in a same line
# and also one statement can occurs in multiple lines

m1 = "hello" ; m2 = "world"  # two statement in a single line

message = ("Hello i'm learning python ." \
           " It is a high level langauge")

print (message)


############### INDENTATIONS IN PYTHON ###############

# Indentations in python are very important. They are the part of syntax
# Indentations helps to define a block of code in python

a = 1

if a>2:
    print ("Hello world")


############## COMMENTS IN PYTHON ###############
# (hash) (#) in python is used as a single line comment
# triple-quoted string ("""   """)in python can be used as a multiline comment
 """ 
 these are multi line comments using triple-quoted string
 """
