def likes(names):
    # your code here
    if len(names) <0:
        return "no one likes this"
    elif len(names)==1:
        return f"{str(names[0:1]) }likes this"
    elif len(names)==2:
        return f"{str(names[0:1])} and {names[1:2]} like it"
    elif len(names)==3:
        return f"{str(names[0:1])}, {names[1:2]} and {names[2:3]} like it"
    elif len(names)>3:
        return f"{str(names[0:1])}, {names[1:2]} and {len(names)} others like it"
arr=["james",'alex','ven']
print(likes(arr))