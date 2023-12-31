# PokerBankingScripter
Input a donkhouse autogenerated .csv ledger file and receive a generated "payment.txt" file with a script that minimizes the number of transactions needed to settle a game. 

Ensure that your csv file is in the same directory as the script, then on line 3, change "ledger.csv" to the same of your .csv file.

Then, manually add two columns in the csv file called "Zelle" and "Exc_Zelle", which are binary indicators. The former represents if a user has Zelle and the latter represents
if a user exclusively uses Zelle.

Then, run:
```bash
python3 ledger.py
```
and if it is indeed possible to settle the game without any undesirable pairings, a file called "payments.txt" will be autogenerated in the working directory.

![image](https://github.com/neilshah12/PokerBankingScripter/assets/90114248/d9b7a0e8-e13d-4d51-a2e9-afdf751592f1)
