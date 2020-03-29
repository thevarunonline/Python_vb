ur_weight=int(input('Please enter your weight:'))
unit=input('For Kgs(K)and for Pound(L)')
if unit.upper()=='K':
    weight_in_p= ur_weight*2
    print(weight_in_p)
elif unit.upper()=='L':
    weight_in_kg=ur_weight*0.45
    print(weight_in_kg)

