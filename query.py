"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# Get the brand with the **id** of 8.

brand_id_8 = Brand.query.get(8)
brand_id_8.name


# Get all models with the **name** Corvette and the **brand_name** Chevrolet.

Model.query.filter_by(name='Corvette', brand_name='Chevrolet').all()

# Get all models that are older than 1960.

Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.

Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".

Model.query.filter(Model.name.like('%Cor%')).all() 

# Get all brands that were founded in 1903 and that are not yet discontinued.

Brand.query.filter(Brand.founded == 1903, Brand.discontinued.is_(None)).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.

Brand.query.filter( db.or_(Brand.discontinued !=None, Brand.founded < 1950)).all()

# Get all models whose brand_name is not Chevrolet.

Model.query.filter(Model.brand_name != 'Chevrolet').all()

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    return db.session.query(Model.year, 
							Model.name, 
							Model.brand_name, 
							Brand.headquarters).filter(Model.year == year).join(Brand).all()

def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

brands_summary = db.session.query(Brand.name, Model.name).join(Model).order_by(Brand.name).all()

for brand, model in brands_summary:
	print brand

# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of
# ``Brand.query.filter_by(name='Ford')``?
#<flask_sqlalchemy.BaseQuery object at 0x7f1e5116fa90>
#type is flask_sqlalchemy.BaseQuery object

# 2. In your own words, what is an association table, and what *type* of
# relationship does an association table manage?

#An association table is an object used to refer to additional information, it is used in 
#many to many relationships.

# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):

	return Brand.query.filter(Brand.name.like('%'+mystr+'%')).all()


def get_models_between(start_year, end_year):

	years = []
	all_models_between = []

	initialize = 0 #initialize i

	for i in range(end_year-start_year): #difference between endyr and startyr
		years.append(start_year+i)

# Run a query for each of the years in the years list and append the
# results to the all_models_between list.
	for n in years:
		all_models_between.append(db.session.query(Model).filter_by(year=n).order_by(Model.year).all())
	return all_models_between

