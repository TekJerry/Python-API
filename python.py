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
 = Drink(name='',instructions='',glass='',ingredients='',thumbnail='',alcoholic='')
 = Drink(name='',instructions='',glass='',ingredients='',thumbnail='',alcoholic='')
 = Drink(name='',instructions='',glass='',ingredients='',thumbnail='',alcoholic='')
 = Drink(name='',instructions='',glass='',ingredients='',thumbnail='',alcoholic='')
 = Drink(name='',instructions='',glass='',ingredients='',thumbnail='',alcoholic='')
 = Drink(name='',instructions='',glass='',ingredients='',thumbnail='',alcoholic='')
 = Drink(name='',instructions='',glass='',ingredients='',thumbnail='',alcoholic='')
 = Drink(name='',instructions='',glass='',ingredients='',thumbnail='',alcoholic='')
 = Drink(name='',instructions='',glass='',ingredients='',thumbnail='',alcoholic='')
 = Drink(name='',instructions='',glass='',ingredients='',thumbnail='',alcoholic='')

 


