class Recipe():
    def __init__(self, dish_name, ingredient, instructions):
        self.dish_name = dish_name
        self.ingredient = ingredient
        self.instructions = instructions
        
    def icerik(self):
        return {
            "dishname": self.dish_name,
            "ingredient": self.ingredient,
            "instructions": self.instructions
        }

class Recipe_book():
    def __init__(self):
        self.all_dish = []
        self.results = []
    
    def icerige_ekle(self, recipe):
        self.all_dish.append(recipe.icerik())
    
    def liste_yazdir(self):
        return self.all_dish

    def arama_yap(self, keyword):
        self.results = []  # Her aramadan önce sonuç listesini sıfırla
        for recipe in self.all_dish:
            if keyword.lower() in recipe["dishname"].lower():
                self.results.append(recipe)

        if self.results:
            # Arama sonucunda sadece ilk bulunan tarifin detaylarını yazdır
            first_result = self.results[0]  # İlk tarif her seferinde sıfırlanıyor
            print(f"Dish Name: {first_result['dishname']}")
            print(f"Ingredients: {', '.join(first_result['ingredient'])}")
            print(f"Instructions: {first_result['instructions']}\n")
            
        else:
            return "Not found"  # Eğer tarif bulunmadıysa "Not found" döndür








Recipebook = Recipe_book()
recipe1 = Recipe("Pasta", ["Noodles", "Tomato Sauce"], "Boil and mix.")

Recipebook.icerige_ekle(recipe1)

print(Recipebook.arama_yap("Pasta"))



