from classes import *

if __name__ == '__main__':
    bus = Bus()
    tour = Tour()
    # tour.add_in_table()
    # tour.remove_from_table('tours', 'tour_id>0')
    bus.find_all_peoples()
    tour.find_many_to_many()
