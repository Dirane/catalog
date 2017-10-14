from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from catalogdb_setup import *

#specify app engine 12/10/2017
engine = create_engine('sqlite:///catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

#session object
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit() but if you change your mind, you can call
# session.rollback() to revert the changes
session = DBSession()

# Remove Categories if it exists.
session.query(Category).delete()
# Remove Items if it exists.
session.query(Items).delete()
# Delete Users if exisitng.
session.query(User).delete()

# Create fake users to populate the database
User1 = User(name="John Doe",
              email="johndoe@skype.com")
session.add(User1)
session.commit()

User2 = User(name="James Allen",
              email="jamesallen@whatsapp.co")
session.add(User2)
session.commit()

# Create fake categories
Category1 = Category(name="Computers",
                      user_id=1)
session.add(Category1)
session.commit()

Category2 = Category(name="Musical Instruments",
                      user_id=2)
session.add(Category2)
session.commit

Category3 = Category(name="Snacks",
                      user_id=1)
session.add(Category3)
session.commit()

Category4 = Category(name="Sports",
                      user_id=1)
session.add(Category4)
session.commit()

Category5 = Category(name="Food",
                      user_id=1)
session.add(Category5)
session.commit()

Category5 = Category(name="Electronics",
                      user_id=1)
session.add(Category5)
session.commit()

# Populate a category with items for testing
# Using different users for items also
Item1 = Items(name="Lenovo Laptop",
               date=datetime.datetime.now(),
               description="A powerful laptop and remarkable gadget",
               category_id=1,
               user_id=1)
session.add(Item1)
session.commit()

Item2 = Items(name="Dell Laptop",
               date=datetime.datetime.now(),
               description="Strong and reliable laptops",
               category_id=1,
               user_id=1)
session.add(Item2)
session.commit()

Item3 = Items(name="Android Phones",
               date=datetime.datetime.now(),
               description="Modern computers",
               category_id=1,
               user_id=1)
session.add(Item3)
session.commit()

print "Databse populated!"