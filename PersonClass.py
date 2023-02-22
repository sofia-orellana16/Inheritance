class Person:
    def __init__(self, n, a, t):
        self.name = n
        self.address = a
        self.telephone = t
    
    def get_name(self):
        return self.name
    def get_address(self):
        return self.address
    def get_tel(self):
        return self.telephone
    
    def print_person(self):
        print('Name:', self.name )
        print('Address:', self.address )
        print('Telephone number:', self.telephone )

class Customer(Person):
    def __init__(self, n, a, t, cn, ml):
        Person.__init__(self, n, a, t)

        self.custnum = cn
        self.maillist = ml

    def get_custnum(self):
        return self.custnum
    def get_mail(self):
        return self.maillist
    
    
    def print_person(self):
        print('Name:', self.name)
        print('Address:', self.address)
        print('Telephone number:', self.telephone )
        print('Customer number:', self.custnum )
        if self.maillist:
            print('Mailing list: YES' )
        else:
            print('Mailing list: NO')

