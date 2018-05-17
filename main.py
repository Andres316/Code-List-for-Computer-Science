from room import Room

kitchen = Room("Kitchen")
kitchen.set_description("A desk and dirty room buzzing with flies.")

Dunegon = Room("Dunegon")
Dunegon.set_description("A cave filled with rats.")

LavaPit = Room("Lava Pit")
LavaPit.set_description("A desk and dirty room buzzing with flies.")

Bathroom = Room("Bathroom")
Bathroom.set_description("Pure Crap.")

kitchen.link_room(Dunegon, "west")
LavaPit.link_room(kitchen, "north")
Dunegon.link_room(Bathroom, "west")
Bathroom.link_room(Dunegon, "east")

current_room = kitchen
while True:
    print('>')
    current_room.print_details()
    command = input('>')
    current_room = current_room.move(command)
