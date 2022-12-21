import errors

def run(self):
        while True:
            self.print_commands()
            command = input("Enter command number: ")
            try:
                command = int(command)
                if command == 1:
                    self.create_character()
                elif command == 2:
                    self.create_weapon()
                elif command == 3:
                    self.create_item()
                elif command == 4:
                    self.print_characters()
                elif command == 5:
                    self.delete_character()
                elif command == 6:
                    break
                else:
                    raise errors.InvalidCommand("Invalid command number")
            except errors.GameError as e:
                print(f"Error: {e}")

