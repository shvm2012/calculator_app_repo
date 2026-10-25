# Calculator App Blueprint --> MANAGER : Shivam

# Add Features Here . .

def add(a,b): # 1. add feature: Added by Shivam from main
    return a+b 

def sub(a,b): # 2. subtraction feature: Added by Shivam from main
    return a-b

def mul(a,b): # 3. multiplication feature: Added by Shivam from branch : feature_3_mul_shivam
    return a*b

if __name__ == "__main__" : #  prevent code from executing automatically when a file is imported as a module into another script
    a = int(input("Enter 1st Number: "))
    b = int(input("Enter 1st Number: "))

    # Print Features Action Here . . 
    print(f"Sum : {add(a,b)}")  # 1. print addtion : Line Added by Shivam from main
    print(f"Diff : {sub(a,b)}") # 2. print subtraction : Line Added by Shivam from main
    print(f"Mul : {mul(a,b)}")  # 3. print multiplication : Line Added by Shivam branch : feature_3_mul_shivam