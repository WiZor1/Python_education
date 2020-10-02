words = input('Введите... что-нибудь:\n')

world_l = words.split()
for i, word in enumerate(world_l):
    print(i, word[:10])
