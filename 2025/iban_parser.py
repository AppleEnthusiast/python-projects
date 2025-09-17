# IBAN parser using slice()

iban = "DE12345678901234567890"  

country_slice = slice(0, 2)   
check_slice   = slice(2, 4)   
bank_slice    = slice(4, 12) 
account_slice = slice(12, 22)

country = iban[country_slice]
check   = iban[check_slice]
bank    = iban[bank_slice]
account = iban[account_slice]

print(f"IBAN:        {iban}")
print(f"Country Code: {country}")
print(f"Check Digits: {check}")
print(f"Bank Code:    {bank}")
print(f"Account No.:  {account}")

