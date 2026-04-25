# 1. Lista
meat = ["Ham", 3.99, 50, "Sliced"]
cheese = ["Cheddar", 5.49, 100, "Sharp"]
condiment = ["Mustard", 1.99, 75, "Spicy"]
# 2. Lista Principal
deli_dept = [meat, cheese, condiment]
print("Initial Deli list:", deli_dept)
# 3. Reabastecer Item 
if meat [0] == "Ham" and meat [2] < 100:
    meat [2] = 100
# 4. Adc Carne sazonal
seasonal_meat = ["Turkey", 4.50, 100, "Sliced"]
deli_dept.append(seasonal_meat)
# 5. Remover condimento
deli_dept.remove(condiment)
# 6. Ordenar lista
deli_dept.sort()
print("Updated Deli list:", deli_dept)


