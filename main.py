class CreditCard():
    """Custom credit card"""
    def __init__(self,cutomer,bank,account,limit):
        """
        blance is zero at the start
        cutomer:  the name if the cutomer (ex: 'john anderson')
        bank : the name of the bank (ex: 'people back')
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




help(CreditCard)
