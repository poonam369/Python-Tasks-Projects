# Calculate electronics bill with 18% GST 
def calculateElectronicsGST(a, b): 
    
    # Add both electronics item amounts 
    
    amount = a + b 
    
    # Calculate 18% GST on the combined amount 
    
    gst = amount * 18 / 100 
    
    # Return amount including GST 
    
    return amount + gst 
 
 
# Calculate fashion bill with 13% GST 

def calculateFashionGST(c, d): 
    
    # Add both fashion item amounts 
    
    amount = c + d 
    
    # Calculate 13% GST on the combined amount 
    
    gst = amount * 13 / 100 
    
    # Return amount including GST 
    
    return amount + gst 
 
 
# Calculate food bill with 7% GST 

def calculateFoodGST(e): 
    
    # Calculate 7% GST on the food amount 
    
    gst = e * 7 / 100 
    
    # Return food amount including GST 
    
    return e + gst 
 
 
 
 
# Calculate total bill after GST 

def totalBill(a, b, c, d, e): 
    
    # Call the three GST calculation functions 
    
    electronics = calculateElectronicsGST(a, b)
     
    fashion = calculateFashionGST(c, d) 
    
    food = calculateFoodGST(e) 
    
    # Add all amounts after GST 
    
    return electronics + fashion + food 
 
# Calculate, print, and return the final bill 

def calculateDiscountedBill(a, b, c, d, e): 
    
    # Get the total bill after GST 
    
    total = totalBill(a, b, c, d, e) 
    
    # Calculate 20% discount on the total 
    
    discount = total * 20 / 100 
    
    # Subtract discount from total 
    
    payable = total - discount 
    
    # Print results inside this function 
    
    print(f"Total after GST = {total:.2f}") 
    print(f"Discount = {discount:.2f}") 
    print(f"Final payable amount = {payable:.2f}") 
    
    # Return final payable amount 
    return payable 
 
# Pass sample values directly; no input() required 
calculateDiscountedBill(100, 100, 100, 100, 100) 