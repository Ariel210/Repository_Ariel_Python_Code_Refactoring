def exercise_countrys():
    enter_country = str(input("Enter one country: "))
    list_country_America = ['Argentine', 'Brasil']
    list_country_Europe = ['Spanish', 'French']
    list_country_Asia = ['Chine', 'Japan']
    list_country_Africa = ['Nigeria', 'Senegal']
    list_country_Oceania = ['New Zeland', 'Australia']
    
    
    if enter_country in list_country_America:
        print(f"This country, {enter_country} is the America continent")
    elif enter_country in list_country_Europe:
        print(f"This country, {enter_country} is the Europe Continent")
    elif enter_country in list_country_Asia:
        print(f"This country, {enter_country} is the Asia continent")
    elif enter_country in list_country_Africa:
        print(f"This country, {enter_country} is the Africa continent")
    elif enter_country in list_country_Oceania:
        print(f"This country, {enter_country} is the Oceania continent")
    else:
        print("Other Country from other continent !")
exercise_countrys()