import json

class Configurator:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.settings = self.load_config()

    def load_config(self):
        """Load configuration from a JSON file."""
        try:
            with open(self.config_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Configuration file {self.config_file} not found. Loading default settings.")
            return self.default_config()

    def default_config(self):
        """Return default configuration settings."""
        return {
            'theme': 'light',
            'language': 'en',
            'notifications': True,
            'volume': 50
        }

    def save_config(self):
        """Save current settings to a JSON file."""
        with open(self.config_file, 'w') as file:
            json.dump(self.settings, file, indent=4)
        print(f"Settings saved to {self.config_file}")

    def update_setting(self, key, value):
        """Update a specific setting."""
        if key in self.settings:
            self.settings[key] = value
            print(f"Setting '{key}' updated to '{value}'.")
        else:
            print(f"Setting '{key}' does not exist.")

    def display_settings(self):
        """Display current configuration settings."""
        print("Current settings:")
        for key, value in self.settings.items():
            print(f"{key}: {value}")

def main():
    config = Configurator()

    while True:
        print("\n1. Display Settings")
        print("2. Update Setting")
        print("3. Save Settings")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            config.display_settings()
        elif choice == '2':
            key = input("Enter the setting key to update: ")
            value = input("Enter the new value: ")
            config.update_setting(key, value)
        elif choice == '3':
            config.save_config()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
