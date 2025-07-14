# A code that gives recommendations based on the weather

#Take User's weather input
weather = input("What's the weather like today? (sunny/rainy/cold): ")

# Recommendations based on User's choice of weather
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")

elif weather == "rainy":
    print(" Don't forget your umbrella and a raincoat.")

elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")

else :
    print("Sorry, I don't have recommendations for this weather.")
