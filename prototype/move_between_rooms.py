rooms = {
    'Great Hall': {'south': 'Bedroom'},
    'Bedroom': {'north': 'Great Hall', 'east': 'Cellar'},
    'Cellar': {'west': 'Bedroom'}
}
current_room = 'Great Hall'

while current_room != 'exit':
    print(f"\nYou are in the {current_room}.")
    user_input = input("Enter your move: ").strip().lower()
    if user_input == 'exit':
        current_room = 'exit'
        print("Goodbye!")
        break
    command_parts = user_input.split()
    if len(command_parts) == 2 and command_parts[0] == 'go':
        direction = command_parts[1]
        if direction in rooms[current_room]:
            current_room = rooms[current_room][direction]
        else:
            print(f"You can't go {direction} from here!")
    else:
        print("Invalid command!")
