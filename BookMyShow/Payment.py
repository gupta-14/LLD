class Payment:
    def __init__(self) -> None:
        self.paymentId = None

    def getPaymentId(self):
        return self.paymentId
    
    def setPaymentId(self, paymentId):
        self.paymentId = paymentId