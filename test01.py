input_value = int(input("성적 입력: "))
score = ""
#90점 이상이면 A
#80점 이상이면 B
#70점 이상이면 C
#60점 이상이면 D
#60점 미만이면 F

if input_value >= 90:
    score = "A"
elif input_value >= 80:
    score = "B"
elif input_value >= 70:
    score = "C"
elif input_value >= 60:
    score = "D"
else:
    score = "F"
    
print(score)