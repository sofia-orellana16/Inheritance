import PersonClass as pc

name = 'John'
address = '123 Main St'
telephone = '254-114-123'
cust_num = '111'
mail_list = True

person1 = pc.Person(name, address, telephone)

customer1 = pc.Customer(name, address, telephone, cust_num, mail_list)
 
person1.print_person()

print()
print()

customer1.print_person()