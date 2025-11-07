from abc import ABC, abstractmethod
import re


class Paiement(ABC):
    def __init__(self, montant):
        if montant <= 0:
            raise ValueError("Le montant doit être positif")
        self._montant = montant

    @abstractmethod
    def payer(self):
        pass

class CarteBancaire(Paiement):
    def __init__(self, montant, numero, cvv):
        super().__init__(montant)
        if not self._verifier_numero(numero):
            raise ValueError("Numéro de carte invalide")
        if not re.fullmatch(r"\d{3,4}", str(cvv)):
            raise ValueError("CVV invalide")
        self._numero = numero
        self._cvv = cvv

    def _verifier_numero(self, numero):
        return re.fullmatch(r"\d{16}", str(numero)) is not None

    def payer(self):
        return f"Paiement de {self._montant:.2f}€ effectué par Carte Bancaire ({self._numero[-4:]}...)"

class PayPal(Paiement):
    def __init__(self, montant, email, token):
        super().__init__(montant)
        if not re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Email invalide")
        self._email = email
        self._token = token

    def payer(self):
        return f"Paiement de {self._montant:.2f}€ effectué via PayPal ({self._email})"

class Crypto(Paiement):
    def __init__(self, montant, wallet_id, reseau):
        super().__init__(montant)
        self._wallet_id = wallet_id
        self._reseau = reseau.upper()

    def payer(self):
        return f"Paiement de {self._montant:.2f}€ effectué en crypto {self._reseau} (Wallet {self._wallet_id})"

def traiter_paiements(liste_paiements):
    for paiement in liste_paiements:
        print(paiement.payer())

if __name__ == "__main__":
    paiements = [
        CarteBancaire(100, "1234567812345678", "123"),
        CarteBancaire(50, "8765432187654321", "987"),
        PayPal(75, "user1@example.com", "token123"),
        PayPal(200, "user2@test.com", "token456"),
        Crypto(150, "wallet123", "BTC"),
        Crypto(300, "wallet456", "ETH")
    ]

    traiter_paiements(paiements)
