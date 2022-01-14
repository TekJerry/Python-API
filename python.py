from flask import Flask  
from flask import request  
from flask import jsonify   

from peewee import *        
from playhouse.shortcuts import model_to_dict   

db = PostgresqlDatabase('cocktails', user='postgres', password='pass123', host='localhost', port=5432)

class BaseModel(Model):
    class Meta:
        database = db

class Drink(BaseModel):
    name = CharField()
    instructions= CharField()
    glass = CharField()
    ingredients = CharField()
    thumbnail = CharField()
    alcoholic = CharField()

db.connect()
db.drop_tables([Drink])
db.create_tables([Drink])

paloma = Drink(name='Paloma',instructions='Stir together and serve over ice.',glass='Collins glass',ingredients='Grapefruit Soda, Tequila',thumbnail='https://www.thecocktaildb.com/images/media/drink/samm5j1513706393.jpg',alcoholic='Alcoholic Beverage')
pink_gin = Drink(name='Pink Gin',instructions='Pour the bitters into a wine glass. Swirl the glass to coat the inside with the bitters, shake out the excess. Pour the gin into the glass. Do not add ice.',glass='White wine glass',ingredients='Bitters, Gin',thumbnail='https://www.thecocktaildb.com/images/media/drink/qyr51e1504888618.jpg',alcoholic='Alcoholic Beverage')
radler = Drink(name='Radler',instructions='Pour beer into large mug, slowly add the 7-up (or Sprite).',glass='Highball Glass',ingredients='Beer, 7-up',thumbnail='https://www.thecocktaildb.com/images/media/drink/xz8igv1504888995.jpg',alcoholic='Alcohlic Bevarage')
rum_sour = Drink(name='Rum Sour',instructions='In a shaker half-filled with ice cubes, combine the rum, lemon juice, and sugar. Shake well. Strain into a sour glass and garnish with the orange slice and the cherry.',glass='',ingredients='Light Rum, Lemon Juice, Sugar, Orange, Maraschino Cherry',thumbnail='https://www.thecocktaildb.com/images/media/drink/bylfi21504886323.jpg',alcoholic='Alcoholic Beverage')
rum_punch = Drink(name='Rum Punch',instructions='Mix all ingredients in a punch bowl and serve.',glass='Punch Bowl',ingredients='Rum, Ginger Ale, Fruit Punch, Orange Juice, Ice',thumbnail='https://www.thecocktaildb.com/images/media/drink/wyrsxu1441554538.jpg',alcoholic='Alcoholic Beverage')
dragonfly = Drink(name='Dragonfly',instructions='In a highball glass almost filled with ice cubes, combine the gin and ginger ale. Stir well. Garnish with the lime wedge.',glass='Highball Glass',ingredients='Gin, Ginger Ale, Lime',thumbnail='https://www.thecocktaildb.com/images/media/drink/uc63bh1582483589.jpg',alcoholic='Alcoholic Beverage')
dry_martini = Drink(name='Dry Martini',instructions='Straight: Pour all ingredients into mixing glass with ice cubes. Stir well. Strain in chilled martini cocktail glass. Squeeze oil from lemon peel onto the drink, or garnish with olive.',glass='Cocktail Glass',ingredients='Gin, Dry Vermouth, Olive',thumbnail='https://www.thecocktaildb.com/images/media/drink/6ck9yi1589574317.jpg',alcoholic='Alcoholic Beverage')
dark_and_stormy = Drink(name='Dark and Stormy',instructions='In a highball glass filled with ice add 6cl dark rum and top with ginger beer. Garnish with lime wedge.',glass='Highball Glass',ingredients='Dark Rum, Ginger Beer',thumbnail='https://www.thecocktaildb.com/images/media/drink/t1tn0s1504374905.jpg',alcoholic='Alcoholic Beverage')
ice_pick = Drink(name='Ice Pick',instructions='Put Vodka in glass fill with iced tea. Stir in lemon to taste.',glass='Collins Glass',ingredients='Vodka, Iced Tea, Lemon Juice',thumbnail='https://www.thecocktaildb.com/images/media/drink/ypsrqp1469091726.jpg',alcoholic='Alcoholic Beverage')
imperial_cocktail= Drink(name='Imperial Cocktail',instructions='Shake with ice and strain into cocktail glass.',glass='Cocktail Glass',ingredients='Lime Juice, Gin, Aperol',thumbnail='https://www.thecocktaildb.com/images/media/drink/bcsj2e1487603625.jpg',alcoholic='Alcoholic Beverage')
yellow_bird= Drink(name='Yellow Bird',instructions='Shake and strain into a chilled cocktail glass',glass='Cocktail Glass',ingredients='White Rum, Galliano, Triple Sec, Lime Juice',thumbnail='https://www.thecocktaildb.com/images/media/drink/2t9r6w1504374811.jpg',alcoholic='Alcoholic Beverage')
smut= Drink(name='Smut',instructions='Throw it all together and serve real cold.',glass='Beer Mug',ingredients='Red Wine , Peach schnapps, Pepsi Cola, Orange Juice',thumbnail='https://www.thecocktaildb.com/images/media/drink/rx8k8e1504365812.jpg',alcoholic='Alcoholic')
spritz= Drink(name='Spritz',instructions='Build into glass over ice, garnish and serve.',glass='Old-Fashioned Glass',ingredients='Prosecco, Campari, Soda Water',thumbnail='https://www.thecocktaildb.com/images/media/drink/j9evx11504373665.jpg',alcoholic='Alcoholic Beverage')
shot_gun= Drink(name='Shot-Gun',instructions='Pour one part Jack Daneils and one part Jim Beam into shot glass then float Wild Turkey on top.',glass='Shot Glass',ingredients='Jim Beam, Jack Daniels, Wild Turkey',thumbnail='https://www.thecocktaildb.com/images/media/drink/2j1m881503563583.jpg',alcoholic='Alcoholic Beverage')
sea_breeze= Drink(name='Sea Breeze',instructions='Build all ingredients in a highball glass filled with ice. Garnish with lime wedge.',glass='Highball Glass',ingredients='Vodka, Cranberry Juice, Grape',thumbnail='https://www.thecocktaildb.com/images/media/drink/7rfuks1504371562.jpg',alcoholic='Alcoholic Beverage')
screwdriver= Drink(name='Screwdriver',instructions='Mix in a highball glass with ice. Garnish and serve.',glass='Highball Glass',ingredients='Vodka, Orange Juice',thumbnail='https://www.thecocktaildb.com/images/media/drink/8xnyke1504352207.jpg',alcoholic='Alcoholic Beverage')
b_53= Drink(name='B-53',instructions='Layer the Kahlua, Sambucca and Grand Marnier into a shot glas in that order. Better than B-52',glass='Shot Glass',ingredients='Kahlua, Sambuca, Grand Marnier',thumbnail='https://www.thecocktaildb.com/images/media/drink/rwqxrv1461866023.jpg',alcoholic='Alcoholic Beverage')
b_52= Drink(name='B-52',instructions='Layer ingredients into a shot glass. Serve with a stirrer.',glass='Shot Glass',ingredients='Bileys Irish Cream, Grand Marnier, Kahlua',thumbnail='https://www.thecocktaildb.com/images/media/drink/5a3vg61504372070.jpg',alcoholic='Alcoholic Beverage')
sherry_eggnog= Drink(name='Sherry Eggnog',instructions='Shake sherry, powdered sugar, and egg with ice and strain into a collins glass. Fill with milk and stir. Sprinkle nutmeg on top and serve.',glass='Collins Glass',ingredients='Sherry, Powdered Sugar, Egg, Milk, Nutmeg',thumbnail='https://www.thecocktaildb.com/images/media/drink/xwrpsv1478820541.jpg',alcoholic='Alcoholic Beverage')


paloma.save()
pink_gin.save()
radler.save()
rum_sour.save()
rum_punch.save()
dragonfly.save()
dry_martini.save()
dark_and_stormy.save()
ice_pick.save()
imperial_cocktail.save()
yellow_bird.save()
smut.save()
spritz.save()
shot_gun.save()
sea_breeze.save()
screwdriver.save()
b_52.save()
b_53.save()
sherry_eggnog.save()


app = Flask(__name__)


@app.route('/cocktails', methods= ['GET'])
def cocktail(id=None):
  if id:
    cocktail = Drink.get(Drink.id == id)
    cocktail = model_to_dict(cocktail)
    return jsonify(cocktail)
  else:
    cocktails = []
    for cocktail in Drink.select():
      cocktails.append(model_to_dict(cocktail))
    return jsonify(cocktails)

app.run(port=9000, debug=True)