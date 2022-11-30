s="John Doe, Peter Parker, Mary Jane Watson-Parker, James Doe, John Elvis Doe, Jane Doe, Penny Parker"
C="Example"
arr=s.split(", ")
ans=[i.split(" ") for i in arr]
# print(arr)
# print(ans)

# k="Watson-Parker"
# p=list(k)
# print(p)
# p.remove("-")
# print("".join(p))

sol = []
for name in ans:
    if len(name) == 3:
        
        last_name = name[2]
        
        if "-" in last_name:
            l_n = list(last_name)
            l_n.remove("-")
            last_name = "".join(l_n)
        
        id = (name[0][0]+name[1][0]+last_name[:8]).lower()
    else:
        id = (name[0][0]+name[1][:8]).lower()
    num = sol.count(id)
    if num == 0:
        sol.append(id)
    else:
        sol.append(id+str(num+1))

answer = [arr[i]+" <"+sol[i]+"@"+C.lower()+".com>" for i in range(len(ans))]
print(", ".join(answer))
print(", ".join(answer) == "John Doe <jdoe@example.com>, Peter Parker <pparker@example.com>, Mary Jane Watson-Parker <mjwatsonpa@example.com>, James Doe <jdoe2@example.com>, John Elvis Doe <jedoe@example.com>, Jane Doe <jdoe3@example.com>, Penny Parker <pparker2@example.com>")