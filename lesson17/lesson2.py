goods = [["яблоки", 50], ["апельсины", 190], ["груши", 100], ["нектарины", 200], ["бананы", 77]]
print('Текущий ассортимент: ', goods)

new_fruit = input('Новый фрукт: ')
price = int(input('Цена:'))
goods.append([new_fruit, price])
print('Новый ассортимент:', goods)

i_list = 0
for fruits in goods:
    goods[i_list][1] *= 1.08
    goods[i_list][1] = round(goods[i_list][1], 2)
    i_list += 1

print('Новый ассортимент с увел. ценой:', goods)