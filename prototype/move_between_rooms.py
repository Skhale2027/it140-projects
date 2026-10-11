# A dictionary for the simplified dragon text game. 
# The dictionary links a room to other rooms. rooms = { Great Hall: {south: Bedroom}, Bedroom: {north: Great Hall, east: Cellar}, Cellar: {west: Bedroom} 
} 
# Set the players starting room for the simplified prototype. current_room = Great Hall 
# Display introductory welcome message print(Welcome to the Dragon Text Game!) print(Commands: go [direction] (e.g., go south, go east) or exit) print(- * 50) 
# Main gameplay loop while current_room != exit: 
    # Display the current room location print(f\nYou are in the {current_room}.) 
    # Prompt user for input and normalize (strip spaces and convert to lower case) user_input = input(Enter your move: ).strip().lower() 
    # Handle the exit command if user_input == exit: current_room = exit print(\nThank you for playing! Goodbye.) break 
    # Parse go [direction] command format command_parts = user_input.split() 
    if len(command_parts) == 2 and command_parts[0] == go: direction = command_parts[1] 
        # Validate if direction exists as a valid move from current_room if direction in rooms[current_room]: 
            # Update current room to the destination room current_room = rooms[current_room][direction] 
else:
    # Output message for invalid directions print(fYou cant go {direction} from here!) else: # Output message for invalid or unrecognized command formatting print(Invalid command! Please enter go [direction] (e.g., go south) or exit.)
