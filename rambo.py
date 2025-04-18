class Pet:
    def __init__(self, name):
        """Initialize a new pet with default values"""
        self.name = name
        self.hunger = 5  # Default starting value
        self.energy = 5  # Default starting value
        self.happiness = 5  # Default starting value
        self.tricks = []  # List to store learned tricks
    
    def eat(self):
        """Feed the pet to reduce hunger and increase happiness"""
        self.hunger = max(0, self.hunger - 3)  # Reduce hunger by 3 but not below 0
        self.happiness = mrain(10, self.happiness + 1)  # Increase happiness by 1 but not above 10
        return f"{self.name} has eaten and is now less hungry!"
    
    def sleep(self):
        """Let the pet sleep to increase energy"""
        self.energy = min(10, self.energy + 5)  # Increase energy by 5 but not above 10
        return f"{self.name} has taken a nap and is now more energetic!"
    
    def play(self):
        """Play with the pet to increase happiness but decrease energy and increase hunger"""
        if self.energy < 2:
            return f"{self.name} is too tired to play right now!"
        
        self.energy = max(0, self.energy - 2)  # Decrease energy by 2 but not below 0
        self.happiness = min(10, self.happiness + 2)  # Increase happiness by 2 but not above 10
        self.hunger = min(10, self.hunger + 1)  # Increase hunger by 1 but not above 10
        return f"{self.name} had fun playing with you!"
    
    def get_status(self):
        """Print the current state of the pet"""
        status_mapping = {
            'hunger': ['Full', 'Satisfied', 'Peckish', 'Hungry', 'Starving'],
            'energy': ['Exhausted', 'Tired', 'Resting', 'Energetic', 'Hyperactive'],
            'happiness': ['Miserable', 'Sad', 'Content', 'Happy', 'Ecstatic']
        }
        
        # Convert numeric values to descriptive text
        hunger_status = status_mapping['hunger'][min(4, self.hunger // 3)]
        energy_status = status_mapping['energy'][min(4, self.energy // 3)]
        happiness_status = status_mapping['happiness'][min(4, self.happiness // 3)]
        
        status = f"Status of {self.name}:\n"
        status += f"Hunger: {self.hunger}/10 ({hunger_status})\n"
        status += f"Energy: {self.energy}/10 ({energy_status})\n"
        status += f"Happiness: {self.happiness}/10 ({happiness_status})"
        
        return status
    
    def train(self, trick):
        """Teach the pet a new trick"""
        if self.energy < 3:
            return f"{self.name} is too tired to learn a new trick right now!"
        
        if trick in self.tricks:
            return f"{self.name} already knows how to {trick}!"
        
        self.tricks.append(trick)
        self.energy = max(0, self.energy - 3)  # Training is tiring
        self.happiness = min(10, self.happiness + 1)  # Learning is fun
        return f"{self.name} has learned how to {trick}!"
    
    def show_tricks(self):
        """Show all tricks the pet has learned"""
        if not self.tricks:
            return f"{self.name} doesn't know any tricks yet!"
        
        tricks_text = f"{self.name} knows the following tricks:"
        for trick in self.tricks:
            tricks_text += f"\n- {trick}"
        
        return tricks_text


# Example usage
if __name__ == "__main__":
    # Create a new pet
    pet_name = input("Enter your pet's name: ")
    my_pet = Pet(pet_name)
    print(f"Congratulations! You are now the proud owner of {pet_name}!")
    
    # Main interaction loop
    while True:
        print("\nWhat would you like to do with your pet?")
        print("1. Feed")
        print("2. Let sleep")
        print("3. Play")
        print("4. Check status")
        print("5. Train a trick")
        print("6. Show tricks")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == "1":
            print(my_pet.eat())
        elif choice == "2":
            print(my_pet.sleep())
        elif choice == "3":
            print(my_pet.play())
        elif choice == "4":
            print(my_pet.get_status())
        elif choice == "5":
            trick = input("What trick would you like to teach? ")
            print(my_pet.train(trick))
        elif choice == "6":
            print(my_pet.show_tricks())
        elif choice == "7":
            print(f"Goodbye! Take care of {pet_name}!")
            break
        else:
            print("Invalid choice. Please try again.")