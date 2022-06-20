def family_hide(family):
    return(f"{family[0].capitalize()}{'*' * (len(family) - 1)}")
    
print(family_hide(input('Введите фамилию: ')))
