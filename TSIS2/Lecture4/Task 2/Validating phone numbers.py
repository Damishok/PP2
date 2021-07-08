import re
for i in range(int(input())):
    print("YES") if re.match("^[789][0-9]{9}$",input()) else print("NO")