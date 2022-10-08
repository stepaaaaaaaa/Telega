n = int(input("Введите серию. Их 37: "))
for i in range(n, n+1):
    enote = (f"https://jut.su/bookofd/episode-{i}.html")
    if n > 37:
        print("Такой серии не существует")
    elif n < 1:
        print("Такой серии не существует")
    else: 
        print(enote)


