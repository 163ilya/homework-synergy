# задание 1
eq = input()

a = eq.split(" ")[:-1]

variables = []
for e in a:
    print(e)
    while e[0].isdigit():
        e = e[1:]
    print(e)
    variables.append(e)
print(variables)

# задание 2
s = input()
sentences = s.split('.')

final_sentences = []

for sentence in sentences:
  sentence = sentence.strip()

  if not sentence:
    continue
  sentence = sentence.capitalize()

  final_sentences.append(sentence)

final_text = '. '.join(final_sentences)

final_text = final_text  + '.'


print(final_text)

# задание 3
str1 = input()
str2 = input()

str1 = str1.lower()
str2 = str2.lower()

if(len(str1) == len(str2)):
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    if(sorted_str1 == sorted_str2):
        print(str1 + " и " + str2 + " Являются анаграмой.")
    else:
        print(str1 + " и " + str2 + " не являются анаграмой.")
else:
    print(str1 + " и " + str2 + " не являются анаграмой")

# задание 4
algebra = input().split() 
geometry = input().split() 
trigonometry = input().split() 

solved_all = set(algebra) & set(geometry) & set(trigonometry) 

if solved_all: 
    print(' '.join(sorted(solved_all)))
else: 
    print('Никто не решил все три задачи')
