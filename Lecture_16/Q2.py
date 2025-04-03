# What will the following code print when the input is 'incomprellion'?

spell = 'incomprehensibilities'
#       'incomprellion'
score = 0

answer = input('21-letter word meaning impossible to comprehend: ')

# print(len(spell))
# print(len(answer))
for i in range(len(spell)):
    if answer[i] == spell[i]:
        score += 1

print(score)
