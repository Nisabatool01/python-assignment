# 1 condition - if statement
# 1 condition, 2 outputs - if-else statement
# 2 conditions, 3 outputs - if-elif-else statement

# Topic 1: Conditional Statements 
# Program 1: Smart Canteen Discount System
# Topic: if, elif, else, comparison operators, and logical thinking.

print("===== SMART CANTEEN =====")
bill_amount = float(input("Enter your total bill amount (Rs.): "))

if bill_amount <= 0:
    print("Invalid bill amount!")
else:
    if bill_amount >= 3000:
        discount_rate = 20
    elif bill_amount >= 2000:
        discount_rate = 10
    elif bill_amount >= 1000:
        discount_rate = 5
    else:
        discount_rate = 0

# Membership discount
    membership = input("Do you have a membership card? (yes/no): ").lower()

    if membership == "yes":
        discount_rate += 5
    
discount_amount = bill_amount * discount_rate / 100
final_amount = bill_amount - discount_amount

print("\n===== BILL SUMMARY =====")
print(f"Original Bill: Rs. {bill_amount:.2f}")
print(f"Discount Rate: {discount_rate}%")
print(f"Discount Amount: Rs. {discount_amount:.2f}")
print(f"Final Payable: Rs. {final_amount:.2f}")

# Display savings message
if discount_amount > 0:
    print(f"Congratulations! You saved Rs. {discount_amount:.2f}")




