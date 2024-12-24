from factorial.factorial import fact
from exp_root.exponentiation import exp2, exp3
from exp_root.root import root2, root3
from logarithm.logarithm import log, ln, lg

def main():
    while True:
        print("\nMenu:")
        print("1. Factorial")
        print("2. Square/Third Power")
        print("3. Square/Third Root")
        print("4. Logarithms")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        try:
            if choice == '1':
                n = int(input("Enter a natural number: "))
                print(f"Factorial of {n}: {fact(n)}")
            
            elif choice == '2':
                x = float(input("Enter a number: "))
                print(f"{x} squared: {exp2(x)}")
                print(f"{x} cubed: {exp3(x)}")
            
            elif choice == '3':
                x = float(input("Enter a positive number: "))
                print(f"Square root of {x}: {root2(x)}")
                print(f"Cube root of {x}: {root3(x)}")
            
            elif choice == '4':
                print("1. Logarithm with custom base")
                print("2. Natural Logarithm (ln)")
                print("3. Common Logarithm (lg)")
                log_choice = input("Choose an option (1-3): ")
                
                if log_choice == '1':
                    a = float(input("Enter base (a > 0, a != 1): "))
                    b = float(input("Enter number (b > 0): "))
                    print(f"log_{a}({b}) = {log(a, b)}")
                elif log_choice == '2':
                    b = float(input("Enter number (b > 0): "))
                    print(f"ln({b}) = {ln(b)}")
                elif log_choice == '3':
                    b = float(input("Enter number (b > 0): "))
                    print(f"lg({b}) = {lg(b)}")
                else:
                    print("Invalid option")
            
            elif choice == '5':
                print("Exiting program.")
                break
            else:
                print("Invalid option. Please choose 1-5.")
        
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
