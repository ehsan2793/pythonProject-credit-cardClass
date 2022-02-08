class CreditCard():
    """Custom credit card"""
    def __init__(self,cutomer,bank,account,limit): # __init__ is constructor

        """
        blance is zero at the start
        cutomer:  the name if the cutomer (ex: 'john anderson')
        bank : the name of the bank (ex: 'people b<sda></sda>ack')
        account : account number (ex: "4121 1233 1234 1314")
        limit :credit card limit (in dollars)
        """
        self._balance = 0
        self._cutomer  = cutomer
        self._bank = bank
        self._account = account
        self._limit = limit

    def get_customer(self):
        """ Return the name fo the customer """
        return self._cutomer

    def get_bank(self):
        """Return the name of the bank"""

        return self._bank

    def get_account(self):
        """Return account number """
        return self._account

    def get_limit(self):
        """Return the credit card limit"""
        return self._limit

    def get_balance(self):
        """Return the credit card balance"""
        return self._balance

    def charge(self,amount):
        """
        Charge the credit card the amount when credit card limit is suffient
        Return True when charge was successful and False otherwise
        """
        if amount + self._balance > self._limit:  #if charge would exceed the limit
            return False   #charge is denied

        else:
            self._balance += amount
            return True


    def make_payment(self,amount):
        """Process the payment that reduce the balance of the credit card"""
        self._balance -= amount




#
# help(CreditCard)


cc = CreditCard('Ehsan Rahimi' , "bank1",'1234 1234 1234 1234',1000) # instance of CreditCard has 5 instance variables
cc.get_balance()
cc.get_limit()
cc.make_payment(100)
cc.get_balance()
