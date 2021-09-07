class Atm(object):
      def __init__(self,CashWithDrawl,BalanceEnquiry,Loan):
          self.CashWithDrawl = CashWithDrawl
          self.BalanceEnquiry = BalanceEnquiry
          self.Loan = Loan
          
      def setCashWithDrawl(self):
          print("setCashWithDrawl Time")
         
      def setBalanceEnquiry(self):
          print("setBalanceEnquiry")
      def setLoan(self):
          print("setLoan")
hdfc = Atm("No Money in your account","Today at 5pm","we can give you 70,000 loan.")
print(hdfc.setCashWithDrawl())
print(hdfc.CashWithDrawl)
print(hdfc.setBalanceEnquiry())
print(hdfc.BalanceEnquiry)
print(hdfc.setLoan())
print(hdfc.Loan)
