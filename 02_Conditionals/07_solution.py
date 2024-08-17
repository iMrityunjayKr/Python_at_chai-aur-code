#Coffee Cutomization
#Problem: Customize a coffee order: "Small","Medium", or "Large" with the option for "Extra shot" expresso.
order_size = input("Tell me your order size : ")
extra_shot = input("Need Extra Shot, say True or False : ")
if extra_shot=="True":
    coffee = order_size + " coffee with an extra shot"
elif extra_shot=="False":
    coffee = order_size + " coffee"
print("Order : ",coffee)