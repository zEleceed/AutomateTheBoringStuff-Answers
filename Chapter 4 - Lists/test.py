import random
recorded_answers = []
for flip in range(1, 101):
    x = random.randint(0, 1)
    if x == 0:
        recorded_answers.append("T")
    elif x == 1:
        recorded_answers.append("H")

T = "TTTTTT"
H = "HHHHHH"
rawr = ''.join(recorded_answers)

print(rawr.count(H))
print(rawr.count(T))
print(rawr)
