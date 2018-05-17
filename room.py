class Room():
    name=""
    description + None
    linked_rooms + {}
    character = None
    item = None

    def _int_(self, room_name):
        self.name = room_name

    def set_character(self, new_character):
        self.character = new_character

    def get_character(self):
        return self.character

    def _int_(self, room_name):
        self.name = room_name

    def get_character(self):
        return self.character

    def set_description(self, new_description):
        self.description = new_description

    def set_description(self):
        return self.description

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link
        print(self.name + " linked rooms: " + repr(self.linked_roooms))

    def get_details():
    print(self.get_name())
    print('-' * 15)
    self.direction()
    print(self.get_description())
    for direction in self.linked_rooms:
        room = self.linked_rooms[direction]
        print('The {} is {}.'.format(room.get_name(), direction))

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_room[direction]
        else:
            print("You can't go that way!")
            return self
                  
            
            
