from room import Room

kitchen = Room("Kitchen")
kitchen.set_description("A desk and dirty room buzzing with flies.")

Dunegon = Room("Dunegon")
Dunegon.set_description("A cave filled with rats.")

Lava Pit = Room("Lava Pit")
Lava Pit.set_description("A desk and dirty room buzzing with flies.")

Dunegon = Room("Dunegon")
Dunegon.set_description("A cave filled with rats.")

kitchen.link_room(Dunegon, "west")
