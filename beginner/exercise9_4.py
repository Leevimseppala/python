from functions import show_numbered_list

people = input("Syötä tapahtuman osallistujat pilkulla eroteltuna:")

show_numbered_list("Ilmoittautumisjärjestys:", people)
print("\n")
show_numbered_list("Aakkosjärjestys etunimen perusteella:", people)
print("\n")
show_numbered_list("Aakkosjärjestys sukunimen perusteella:", people)