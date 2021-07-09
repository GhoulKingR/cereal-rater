import joblib

# cereal rating model
model = joblib.load("cereal_rater.mdl")

# user input
print("Input the specifications of your cereal.")

calories = int( input("Calories: ") )
protein = int( input("Protein: ") )
fat = int( input("Fat: ") )
sodium = int( input("Sodium: ") )
fiber = float( input("Fiber: ") )
carbo = float( input("Carbo: ") )
sugars = int( input("Sugars: ") )
potass = int( input("Potass: ") )
vitamins = int( input("Vitamins: ") )
shelf = int( input("Shelf: ") )
weight = float( input("Weight: ") )
cups = float( input("Cups: ") )

combined = [calories, protein, fat, sodium, fiber, carbo, sugars, potass, vitamins, shelf, cups]

# model processing
rating = model.predict([combined])

# output
print("I'll rate your cereal: ", str(int(rating[0]+17)), "/ 100")