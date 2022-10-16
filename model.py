class Reservation:
	def __init__(self,reserve_name,full_name,reserve_time,reserve_day,num_people,location,phone_num,waiter_name,is_coming,is_food,closed_menu,notes):
		self.reserve_name = reserve_name
		self.full_name = full_name
		self.reserve_time=reserve_time
		self.reserve_day = reserve_day
		self.num_people = num_people
		self.location = location
		self.phone_num = phone_num
		self.waiter_name = waiter_name
		self.is_coming = is_coming
		self.is_food = is_food
		self.closed_menu = closed_menu
		self.notes = notes


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
	return reserve_obj