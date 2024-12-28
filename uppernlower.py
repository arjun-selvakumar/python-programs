sen = "Boku no nawa Monkey.D.Luffy"
for i in range(0,len(sen)):
    if i<=len(sen)//2:
        let=sen[i]
        print(let.lower(),end='')
    else:
        let=sen[i]
        print(let.upper(),end='')
