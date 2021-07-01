record=["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
result=["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
diverge = [log.split() for log in record]
user = {}
answer=[]
for log in diverge:
    if log[0]=="Enter":
        user[log[1]]=log[2]
    elif log[0]=="Leave":
        continue
    else:
        user[log[1]]=log[2]

for log in diverge:
        if log[0]=="Enter":
            answer.append(user[log[1]]+"님이 들어왔습니다.")
        elif log[0]=="Leave":
            answer.append(user[log[1]]+"님이 나갔습니다.")
        else:
            continue
print(answer)
print(result)