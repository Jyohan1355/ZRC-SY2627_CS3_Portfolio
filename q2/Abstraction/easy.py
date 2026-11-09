from abc import ABC, abstractmethod

# 1. Define the Abstract Class
class PaymentGateway(ABC):
    
    @abstractmethod
    def process_payment(self, amount):
        """Child classes must implement this method"""
        pass

# 2. Define a Child Class for Credit Cards
class StripePayment(PaymentGateway):
    
    # Implementing the strict contract
    def process_payment(self, amount):
        print(f"Processing ${amount:.2f} securely via Stripe...")

# 3. Define another Child Class for PayPal
class PayPalPayment(PaymentGateway):
    
    # Implementing the strict contract
    def process_payment(self, amount):
        print(f"Redirecting to PayPal to authorize ${amount:.2f}...")

# 4. Usage in your checkout system
# gateway = PaymentGateway()  <-- ERROR: Cannot instantiate abstract class

stripe_gateway = StripePayment()      # <-- SUCCESS
paypal_gateway = PayPalPayment()      # <-- SUCCESS

stripe_gateway.process_payment(50.00)
paypal_gateway.process_payment(25.50)