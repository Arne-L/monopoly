from enum import Enum

class Card(Enum):
    GET_OUT_OF_JAIL_FREE = "Get Out of Jail Free"
    ADVANCE_TO_GO = "Advance to Go"
    BANK_ERROR_IN_YOUR_FAVOR = "Bank Error in Your Favor"
    DOCTORS_FEES = "Doctor's Fees"
    HOLIDAY_FUND_MATURITY = "Holiday Fund Maturity"
    INCOME_TAX_REFUND = "Income Tax Refund"
    LIFE_INSURANCE_MATURITY = "Life Insurance Maturity"
    PAY_HOSPITAL_FEES = "Pay Hospital Fees"
    RECEIVE_CONSULTANCY_FEE = "Receive $25 Consultancy Fee"
    ASSESSED_FOR_STREET_REPAIRS = "You are Assessed for Street Repairs"
    SECOND_PRIZE_BEAUTY_CONTEST = "You Have Won Second Prize in a Beauty Contest"
    WONT_BELIEVE_IT = "You Won't Believe It!"
    ADVANCE_TO_ILLINOIS_AVE = "Advance to Illinois Ave"

class StackOfCards:
    def __init__(self):
        pass