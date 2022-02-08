from main import CreditCard

class PredatoryCreditCard(CreditCard):
    """
    An extension of CreditCard that compunds interest and fee

            blance is zero at the start

            cutomer:    the name if the cutomer (ex: 'john anderson')
            bank :      the name of the bank (ex: 'people b<sda></sda>ack')
            account:    account number (ex: "4121 1233 1234 1314")
            limit:      credit card limit (in dollars)
            apr:        annual percentage rate (ex: 0.0825 for 8.25% APR)
    """

    def __init__(self,customer,bank,account,limit,apr):
        super().__init__(customer,bank,account,limit)
        self.__balance = 0
        self.__apr = apr


    def charge(self,price):
        """Charge given price to tehnd of the card , assuming sufficient credit limit
            Return  True if charge was processed successfully
            Return False and assess $5 fee if charge is denied


        """
        success = super().charge(price)
        if not success:
            self.__balance += 5

        return success


    def process_monthly(self):
        """Assess monthly interest on outstanding balance"""
        if self.__balance > 0:
            # if balce is greater than 0 that we add APR to interest
            monthly = pow( 1 + self.__apr, 1/12)
            self.__balance *= monthly


p = PredatoryCreditCard('Ehsan Rahimi' , "bank1",'1234 12312113123123 1232 1234',1000,0.2)


p.get_account()
p.get_balance()

p.charge(1)
p.charge(995)
p.charge(5000)
