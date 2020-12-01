on = True
while on:
    user_choice = int(input("Haluatko 1: Muuttaa numeron roomalaiseksi vai 2: Muuttaa roomalaisen numeroksi? (1/2)\n"))
    if user_choice == 1:
        user_int_input = int(input("Anna jokin luku 1-4000 välillä:\n"))
        # Luodaan listat ja apumuuttujat
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        roman_num = ''
        i = 0
        # Vertaillaan listoja keskenään ja jos syötteen ja alkion jakojäännös on 0
        # vähennetään käyttäjän antamasta syötteestä
        while user_int_input > 0:
            for _ in range(user_int_input // val[i]):
                roman_num += syb[i]
                user_int_input -= val[i]
            i += 1
        print(roman_num)
        another = input("Haluatko jatkaa? (k/e)\n")
        if another == 'e':
            on = False
            break

    elif user_choice == 2:
        user_roman_input = input("Anna jokin luku I-MMMM välillä:\n")
        user_roman_input = user_roman_input.upper()
        # luodaan dictionary nums, jossa keynä Roomalaiset numerot ja valuena niitä vastaavat luvut
        nums = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        sum = 0
        # Käydään läpi silmukassa käyttäjän syötä paloittain
        for i in range(len(user_roman_input)):
            # Aloitetaan try silmukka virheenkäsittelyä varten.
            try:
                value = nums[user_roman_input[i]]
                # Jos seuraavassa alkiossa on suurempi numero, tämä luku on negatiivinen
                if i + 1 < len(user_roman_input) and nums[user_roman_input[i + 1]] > value:
                    sum -= value
                else:
                    sum += value
            except KeyError:
                raise ValueError('input is not a valid Roman numeral: %s' % user_roman_input)
        # Lopuksi printataan yhteenlaskettu summa
        print(sum)
        another = input("Haluatko jatkaa? (k/e)\n")
        if another == 'e':
            on = False
            break






