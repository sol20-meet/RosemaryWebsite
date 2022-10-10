from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
Base = declarative_base()

class Reservation(Base):
	__tablename__ ="Reservations"
	id = Column(Integer,primary_key=True)
	reserve_name = Column(String)
	full_name = Column(String)
	reserve_time = Column(String)
	reserve_day = Column(String)
	num_people = Column(String)
	location = Column(String)
	phone_num = Column(String)
	waiter_name = Column(String)
	is_coming = Column(String)
	is_food = Column(String)
	closed_menu = Column(String)
	notes = Column(String)
	def __repr__(self):
		return("Reserve Name: {}\n"
				"Full Name: {}\n"
				"Reserve Time: {}\n"
				"Reserve Day: {}\n"
				"Number of People: {}\n"
				"Location: {}\n"
				"Phone Number: {}\n"
				"Waiter Name: {}\n"
				"Is Coming?: {}\n"
				"Is eating food?: {}\n"
				"Closed Menu?: {}\n"
				"Notes:").format(
				self.reserve_name,
				self.full_name,
				self.reserve_time,
				self.reserve_day,
				self.num_people,
				self.location,
				self.phone_num,
				self.waiter_name,
				self.is_coming,
				self.is_food,
				self.closed_menu,
				self.notes)
			