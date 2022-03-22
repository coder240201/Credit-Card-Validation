import datetime

class CreditCardValidator:
    def __init__(self, cardNum, name, validity_date, cvv) -> None:
        self.card_num = cardNum
        self.card_holder_name = name
        self.card_validity = validity_date
        self.cvv = cvv

    def validate_card_num(self):

        def checkLuhn(cardNo):

            nDigits = len(cardNo)
            nSum = 0
            isSecond = False
            
            for i in range(nDigits - 1, -1, -1):
                d = ord(cardNo[i]) - ord('0')

                if (isSecond == True):
                    d = d * 2
                
                nSum += d // 10
                nSum += d % 10
                isSecond = not isSecond

            if (nSum % 10 == 0):
                return True
            else:
                return False

        return checkLuhn(self.card_num)


    def validate_card_holder_name(self):
        
        #Name should not startwith or ends with space.
        if self.card_holder_name.endswith(" ") or self.card_holder_name.startswith(" "):
            return False
        
        #Name should not contain special character or number.
        for char in self.card_holder_name:
            if not char.isalpha() and not char.isspace():
                return False
        
        return True


    def validate_card_validity(self):

        #Validity date must be less than the today date.

        today = datetime.datetime.now()

        mon = int(self.card_validity[:2])
        year = int("20" + self.card_validity[-2:])

        if today.year > year:
            return False
        if today.year == year and today.month > mon:
            return False
        return True

    def validate_card_cvv(self):

        #CVV num should be of length 3 or 4.
        #Should contain only numbers.
        if not self.cvv.isdecimal():
            return False
        
        if len(self.cvv) != 3 and len(self.cvv) != 4:
            return False
        
        return True


    def validate(self):

        #Card is valid card if all above validations are true.
        if not self.validate_card_num() or not self.validate_card_holder_name() or not self.validate_card_validity() or not self.validate_card_cvv():
            return False
        
        return True

    def card_cvv_length(self):
        return len(self.cvv)

    def card_num_length(self):
        return len(self.card_num)

    def is_visa_card(self):

        #VISA Card:
        # Card num length = 13 or 16
        # Begins with '4'
        # Length of CVV = 3
        if self.card_num_length() != 13 and self.card_num_length() != 16:
            return False

        if not self.card_num.startswith("4"):
            return False
        
        if self.card_cvv_length() != 3:
            return False
        
        return True

    def is_master_card(self):

        #Master Card
        # Card Num length = 16
        # Begins with '5'
        # Length of CVV = 3
        if self.card_num_length() != 16:
            return False

        if not self.card_num.startswith("5"):
            return False
        
        if self.card_cvv_length() != 3:
            return False
        
        return True

    def is_amex_card(self):

        #American Express Card
        # Card Num length = 15
        # Begins with '34' or '37'
        # Length of CVV = 4
        if self.card_num_length() != 15:
            return False

        if not self.card_num.startswith("34") and not self.card_num.startswith("37"):
            return False
        
        if self.card_cvv_length() != 4:
            return False
        
        return True

    def check_card_brand(self):

        if not self.validate():
            return "Not a Valid Credit Card"

        if self.is_visa_card():
            return "Visa Card"

        if self.is_master_card():
            return "Master Card"

        if self.is_amex_card():
            return "AMEX Card"

        return "Other Card"