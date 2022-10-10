from model import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db?check_same_thread=False')
Base.metadata.create_all(engine)
# session = scoped_session(sessionmaker(bind=engine))
DBSession = sessionmaker(bind=engine)
session = DBSession()

#add_place takes 4 variables and it creates an Place Object and then it adds it to the database so it can be accessed later on..
def add_res(reserve_name,full_name,reserve_time,reserve_day,num_people,location,phone_num,waiter_name,is_coming,is_food,closed_menu,notes):
	reserve_obj = Reservation(
		reserve_name = reserve_name,
		full_name = full_name,
		reserve_time=reserve_time,
		reserve_day = reserve_day,
		num_people = num_people,
		location = location,
		phone_num = phone_num,
		waiter_name = waiter_name,
		is_coming = is_coming,
		is_food = is_food,
		closed_menu = closed_menu,
		notes = notes)

	session.add(reserve_obj)
	session.commit()


#query_all gets all of the Place objects in the database and it returns them as a list which is called Places
def query_all():
	Reservations = session.query(Reservation).all()
	return Reservations

def query_res():
	Reservations1 = session.query(Reservation).order_by(Reservation.reserve_day).order_by(Reservation.reserve_time).all()
	return Reservations1

