def calculate_love_score(name1, name2):
    true = ['t', 'r', 'u', 'e']
    love = ['l', 'o', 'v', 'e']
    list_of_names = [name1.lower(), name2.lower()]
    true_count = 0
    love_count = 0
    for names in list_of_names:
        for letter in names:
            if letter in true:
                true_count += 1
            if letter in love:
                love_count += 1


    print(f"{true_count}{love_count}")

calculate_love_score("Angela Yu", "Jack Bauer")

calculate_love_score("Kanye West", "Kim Kardashian")