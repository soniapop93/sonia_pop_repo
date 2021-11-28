# declară o listă care conține elementele 7, 8, 9, 2, 3, 1, 4, 10, 5, 6 (în această ordine)
my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

# afișează lista inițială ordonată ascendent (lista inițială trebuie păstrată în aceeași formă)
my_list.sort()
print(my_list)

#afișează lista inițială ordonată descendent (lista inițială trebuie păstrată în aceeași formă)
my_list.sort(reverse=True)
print(my_list)

#afișează o listă ce conține numerele pare din lista ordonată (folosind slice)
new_list_even = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(new_list_even[1::2])

#afișează o listă ce conține numerele impare din lista ordonată (folosind slice)
new_list_odd = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(new_list_odd[0::2])

# afisează o listă ce conține numerele ce sunt multipli ai numărului 3 (folosind slice)
list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list3[2::3])