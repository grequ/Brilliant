from gettext import find


print(7)
print (6+3+5)

print ("ver bad \"cod\" in progress")
print ('test diffrent print')


sentence = "I like waffles"
spacer = "because"

print(sentence+ " " + spacer)

str1 = "random"
str2 = "an"

val = str1.find(str2)
print(val)

str1 = "Spam spam spam spam. Lovely spam! Wonderful spam! Spam spa-a-a-a-a-am..."
str2 = str1[18:24]
print(str2)


word = "andom" #word is our input. Assume it is entirely lower-case.
vowels = "aeoui"
#j = 0 
j = -1
#i = word.find(vowels)
#i = word.find(vowels[0])
#i = vowels.find(word)
i = vowels.find(word[0])
if (i > j):
    print("This word begins with a vowel!")


hairs = "brown/red/gray/black/blonde"
hair_list = hairs.split("/")
print(hair_list)


nb_miles_string = '3, 2, 5, 2, 6, 1, 2'
nb_miles_list = nb_miles_string.split(', ')

miles = 0

for i in range(len(nb_miles_list)):
    miles +=int(nb_miles_list[i])
    print(nb_miles_list[i])

for i in range(5, 50, 5):
    print(i)

for i in range(20):
    print(i, i**2)