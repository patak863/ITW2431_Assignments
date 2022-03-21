# Name: Jim Smith
# ITW 2431
# Lab 0 Prob 2
# File name: ITW2431_L0_P2_jsmith.py
# Last Update: 1/10/2022
# Purpose: To compute and display the area of a square or volume of a cube
# with a side length from 1 to 50 with the increment of 5 based on the user for choosing a or v

#Display a Welcome Screen

print(('Welcome to Our Area or Volume Computation App').center(75))
print('-'*75)

#print a blank line
print()

#print a blank line

print()

while True:
    #prompt the user to input a choice - pay attention the user of lower() function
    choice = (input('Enter a for areas of squares, v for volumes of Cubes, and q for quit: ')).lower()

    #add a blank line
    print()
    
    #if the user select a (areas of squares)
    if choice == 'a':
        
        #print the heading
        print(('The Areas of Squares').center(75))
        print('-'*75)

        #print a blank line
        print()

        #print the heading for the length of a side with 4 spaces right justistied,
        #two empty spaces for the middle column right justisfied, and 10 spaces
        #right justisfied for the areas of sqaures
       
        print(('Side').rjust(4), ('').rjust(2), ('Area').rjust(10))

        #print a dash line
        print(('-'*4).rjust(4), ('').rjust(2), ('-'*10).rjust(10))

        #Displaying the areas of square with a side of 1 to 50 with increment of 5
        for i in range(0, 51, 5):
            if i == 0:
                #if the length is 0, skip it
                continue
            else:
                print(str(i).rjust(4), ('').rjust(2), ((f'{(i * i):,.0f}').rjust(10)))

        #print a blank line
        print()
        
        #after displaying the price list, continue the program
        continue

    #if the user select v (volumes of cubes)
    elif choice == 'v':
        #print the heading
        print(('The Volumes of Cubes').center(75))
        print('-'*75)

        #print a blank line
        print()

        print(('Side').rjust(4), ('').rjust(2), ('Volumes').rjust(10))

        #print a dash line
        print(('-'*4).rjust(4), ('').rjust(2), ('-'*10).rjust(10))

        #Displaying the volumes of cubes with length of a side from 1 to 50 with increment of 5
        for i in range(0, 51, 5):
            if i == 0:
                #if the length is 0, skip it
                continue
            else:
                print(str(i).rjust(4), ('').rjust(2), ((f'{(i * i * i):,.0f}').rjust(10)))

        #print a blank line
        print()
        
        #after displaying the price list, continue 
        continue
    elif choice == 'q':
        #print a thank you message
        print('\nThank you for using to Our Area or Volume Computation App, please come again!\n')

        #exit the program
        break

    else:
        print('\nYou entered a wrong code, it should be a or c...\n')

        #after displaying the error message repeat the while loop
        continue
        
        
        






