import random
import string

def password_generator_app():
    """
    Generates a strong, random password based on user-specified length
    and displays it on the screen.
    """
    print("====================================")
    print("  🔒 Simple Password Generator App   ")
    print("====================================")
    
    while True:
        try:
            length = int(input("Enter the desired password length (e.g., 12): "))
            if length > 0:
                break
            else:
                print("❌ Length must be a positive number.")
        except ValueError:
            print("❌ Invalid input. Please enter a whole number.")

    characters = string.ascii_letters + string.digits + string.punctuation
    password_list = random.choices(characters, k=length)
    generated_password = "".join(password_list)

    print("\n------------------------------------")
    print("✨ Your Generated Password:")
    print(f"👉 {generated_password}")
    print(f"Length: {length}")
    print("------------------------------------")


if __name__ == "__main__":
    password_generator_app()