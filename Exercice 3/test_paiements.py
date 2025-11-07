import unittest
from paiements import CarteBancaire, PayPal, Crypto

class TestPaiements(unittest.TestCase):
    def test_cartebancaire(self):
        cb = CarteBancaire(100, "1234567812345678", "123")
        self.assertIn("100.00", cb.payer())
        self.assertIn("Carte Bancaire", cb.payer())

    def test_paypal(self):
        pp = PayPal(50, "test@example.com", "token")
        self.assertIn("50.00", pp.payer())
        self.assertIn("PayPal", pp.payer())

    def test_crypto(self):
        cr = Crypto(200, "wallet123", "BTC")
        self.assertIn("200.00", cr.payer())
        self.assertIn("BTC", cr.payer())

if __name__ == "__main__":
    unittest.main()
