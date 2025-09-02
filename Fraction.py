
"""
lcm =0
left_frac = input("Fraction. eg; 3/4:  ")
operator = input("Operator (+) (-) ")
right_frac = input("Fraction. eg; 3/4  ")

#Getting the denominator and numerator from the left fraction

      

left_deno = int(left_frac.split("/")[1])
left_numera = int(left_frac.split("/")[0])

#Getting the right denominator from tge right fraction
right_deno = int(right_frac.split("/")[1])
right_numera = int(right_frac.split("/")[0])


left_deno_by_lcm = 0
right_deno_by_lcm = 0
numera =0

lcms =[1,2,3,4,5,6,7,8,9,10,11,12]


   

def find_LCM(left_denominator,right_denominator):
    
    for i in lcms:
                     is_lcm = False
                     for j in lcms:
                         #print(f"left:{left_deno * i} , right:{right_deno * j}")
                         if left_deno * i == right_deno * j:
                             lcm_deno = left_deno * i
                             is_lcm = True
                             print(f"lcm: {lcm_deno}")
                             
                             break
                      
                         
                     if is_lcm:
                         break
                     
    
    return lcm_deno
    
lcm = find_LCM(left_deno,right_deno)
            
left_deno_by_lcm = lcm / left_deno
right_deno_by_lcm = lcm / right_deno

if operator =="+":
        
        
        
        left_numera =left_deno_by_lcm   *left_numera
        right_numera =right_deno_by_lcm * right_numera
        numera = int(left_numera + right_numera)
        print(f"{numera}/{lcm}")
        
        pass
        
        

    
"""
