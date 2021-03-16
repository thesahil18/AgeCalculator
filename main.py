'''
There will be 1 year differnce in this program.
If you cross check check yor age in real or through the program.
If You check your age from present age input then there also 1 year differnce in present input or abirth input.
'''
'''
If you run this program from choice 2 this will assume that you have Birthday on 1st January.
'''
print('''----------------AGE CALCULATOR----------------\n\n''')

present_year = int(input("Enter Present Year : "))
future_year = int(input("Enter Year to check your future Age : "))
    
print('''1. Enter Your Age\n2. Enter Your Birth year\n''')

choice = int(input("Enter Your Choice : "))
    
if choice == 1:
    age_year = int(input("Enter Your Present Age : "))
        
    if age_year == 0 and len(str(age_year)) == 1:
        print(f'Your age in {future_year} is : {future_year - present_year}')

    elif age_year > 0 and len(str(age_year))>=1 and len(str(age_year))<=3:
        print(f'Your age in {future_year} is : {future_year-present_year+age_year}')
            
    else:
        print("<<<Invalid Age>>>")
elif choice == 2:
    age_year = int(input("Enter Your Birth Year : "))
    if age_year > present_year:
        print("<<<Invalid Input>>>")
    else:
        if future_year < present_year:
            print("<<<Invalid Input>>>")
        else:
            print(f'Your age in {future_year} is : {(present_year-age_year)+(future_year-present_year)}')            
else:
    print("<<<Invalid Input>>>")
