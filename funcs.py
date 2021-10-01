
def rectangle_pixel(lista,indice):
    try:
        value_i = lista[indice]
        new_indice = indice + 1
        new_list = []
        counter = 1
        while value_i == lista[new_indice] and new_indice < len(lista)-1:
            # if new_indice < len(lista)-1:
            counter+=1
            new_indice+= 1
            # else:
            #     cola = new_list.append(value_i,counter)
            #     return cola
        new_list.append([value_i,counter])
    except IndexError:
        return None
    return new_list

xd = [1,2,2,2,3,3,3]
print(rectangle_pixel(xd,0))
print(rectangle_pixel(xd,1))
print(rectangle_pixel(xd,7))