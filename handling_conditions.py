#price = float(input('Enter The Price: '))  # int() to convert the inputs into float so we can compare it with tax

#if price >= 2.0:
    #tax = 0.07
#else:
   # tax = 0.00
#print(f'The Tax for this price is: ', {tax}, '\n \n') # note that the print statements without indentations so it will wait the if and else tesults to print the final tax


#country = 'CANADA'
#if country.lower() == 'canada':   # we add .lower() cause python is case senstive, so when working with string becarful 
    #print('You Are Canadian')
#else:
    #print('You Are Not Canadian \n \n')

#province = input('What is your province : ')
#if province.capitalize() == 'Alberta':
    #tax_1 = 0.05
#elif province.capitalize() == 'Nunavut':
    #tax_1 = 0.05
#elif province.capitalize() == 'Ontario':
   # tax_1 = 0.13
#else:
   # tax_1 = 0.15
#print(f'The Tax for Your province is: {tax_1} \n \n ')

# capitalizing the user input so we can compare the results
# how to use or/ and 
#province = input('What is your province : ')
#if province.capitalize() == 'Alberta'\
    #or province.capitalize() == 'Nunavut':
      # tax_2 = 0.05
#elif province.capitalize() == 'Ontario':
  #  tax_2 = 0.13
#else:
  #  tax_2 = 0.15
#print(f'The Tax for Your province is: {tax_2} \n \n ')

# instead of using or/ and python provide IN so we can use it to compare the user input with a list:
province = input('What is your province : ')
if province in ('Alberta', 'Nunavut', 'Ontario'):
    tax_3 = 0.05
elif province == 'Ontario':
    tax_3 = 0.13
else:
    tax_3 = 0.15
print(f'The Tax for your province is : {tax_3} \n \n')


# as well as you can use nest if statements : 
# for example we have combination of conditions so we need to check the country firt and then to check the province

country = input('Your Country is : ')

if country.capitalize() == 'Canada':
    province = input('Your province is : ')
    if province in ('Alberta', 'Nunavut', 'Yukon'):
        tax_4 = 0.05
    elif province == 'Ontario':
        tax_4 = 0.13
    else:
        tax_4 =0.15
else:
    tax_4 = 0.00
print(f'The tax in Your Case is : {tax_4} \n \n')


# if the cinditions are complicated and needed lots of if statements then you can use boolean flag :
gpa = float(input('What is your GPA : '))
lowest_grade = float(input('WHat is you lowest grade among the whole grades : '))
#if gpa >= 0.85:
    #if lowest_grade >= 0.70:
        #print('Well Done You are in the honour roll')
if gpa >= 0.85 and lowest_grade>= 0.70:
    honour_roll: True # we created this var and we assigned a True value to it
else:
    honour_roll: False
# somewhere later in your code :
if honour_roll:
    print('Well Done \n \n ')

