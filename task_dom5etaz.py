#В высотном доме 5 подьездов по 20 квартир каждый. 
#На каждом этаже по 4 квартиры.
#Нумерация квартир идет подряд.
#Вывести этаж и подьезд квартирые 

flat_number = 40

entrance_number = (flat_number - 1) // 20 + 1
floor_number = (flat_number - 1) % 20 // 4 + 1
print(entrance_number)
print(floor_number)
