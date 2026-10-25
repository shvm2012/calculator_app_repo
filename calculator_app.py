# Calculator App Blueprint --> MANAGER : Shivam

# Add Features Here . .

def add(a,b): # 1. add feature: Added by Shivam from main
    return a+b 

def sub(a,b): # 2. subtraction feature: Added by Shivam from main
    return a-b

def mul(a,b): # 3. multiplication feature: Added by Shivam from branch : feature_3_mul_shivam
    return a*b
  
def div(a, b): # 4. division feature: Added by Pavan from branch : feature_4_division_pavan
  if b==0:
      return "operation not defined"
  else:
      return a/b

def sqr_and_sum(a,b): # 5. squared sum feature: Added by Chaya from branch : feature_5_squared_sum_chaya
    return a**2 + b**2


    
if __name__ == "__main__" : #  prevent code from executing automatically when a file is imported as a module into another script
    a = int(input("Enter 1st Number: "))
    b = int(input("Enter 1st Number: "))

    # Print Features Action Here . . 
    print(f"Sum : {add(a,b)}")  # 1. print addtion : Line Added by Shivam from main
    print(f"Diff : {sub(a,b)}") # 2. print subtraction : Line Added by Shivam from main
    print(f"Mul : {mul(a,b)}")  # 3. print multiplication : Line Added by Shivam branch : feature_3_mul_shivam
    print(f"Div : {div(a,b)}")  # 4. print division : Line Added by Pavan from branch : feature_4_division_pavan
    print(f"Sq_Sum : {sqr_and_sum(a,b)}")  # 5. print squared sum : Line Added by Chaya from branch : feature_5_squared_sum_chaya
  