import unittest
from CreditCardValidation import CreditCardValidator

class CreditCardValidatorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.card_validator1 = CreditCardValidator(
            "4263982640269299",
            "John_Wick",
            "01/22",
            "234$"
        )

        self.card_validator2 = CreditCardValidator(
            "4917484589197107",
            " Hemanth",
            "03/22",
            "06789"
        )

        self.card_validator3 = CreditCardValidator(
            "4263982640269299",
            "Kavya",
            "06/29",
            "435"
        )

        self.card_validator4 = CreditCardValidator(
            "5425233430109903",
            "Amit",
            "11/23",
            "865"
        )

        self.card_validator5 = CreditCardValidator(
            "374245455400126",
            "Gagan",
            "10/25",
            "9078"
        )

        self.card_validator6 = CreditCardValidator(
            "6011000991300009",
            "Darshan",
            "01/26",
            "723"
        )



    def test_card_num(self):
        res = self.card_validator1.validate_card_num()
        self.assertEqual(res, True)

        res = self.card_validator2.validate_card_num()
        self.assertEqual(res, False)

    def test_card_holder_name(self):
        res = self.card_validator1.validate_card_holder_name()
        self.assertEqual(res, False)

        res = self.card_validator2.validate_card_holder_name()
        self.assertEqual(res, False)

    def test_card_validity(self):
        res = self.card_validator1.validate_card_validity()
        self.assertEqual(res, False)

        res = self.card_validator2.validate_card_validity()
        self.assertEqual(res, True)
    
    def test_card_cvv(self):
        res = self.card_validator1.validate_card_cvv()
        self.assertEqual(res, False)

        res = self.card_validator2.validate_card_cvv()
        self.assertEqual(res, False)


    def test_card_brand(self):
        res = self.card_validator1.check_card_brand()
        self.assertEqual(res, "Not a Valid Credit Card")

        res = self.card_validator3.check_card_brand()
        self.assertEqual(res, "Visa Card")

        res = self.card_validator4.check_card_brand()
        self.assertEqual(res, "Master Card")

        res = self.card_validator5.check_card_brand()
        self.assertEqual(res, "AMEX Card")

        res = self.card_validator6.check_card_brand()
        self.assertEqual(res, "Other Card")
      

    
if __name__ == "__main__":
    unittest.main()