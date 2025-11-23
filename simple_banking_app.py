balance = 0.0
kyc_documents = {}


def check_balance():
  print(f"Your current balance is: {balance}")
  print("============================================")




def deposit(amount):
  global balance
  if amount > 0:
    balance += amount
  else:
    print("Cannot deposit a negative or zero amount.")
    print("============================================")
  


def withdraw(amount):
  global balance
  if amount < 0:
    print("Cannot withdraw a negative or zero amount.")
    print("============================================")
  elif amount > balance:
    print("Insufficient balance.")
    print("============================================")
  else:
    balance -= amount
  




def update_kyc(docs):
  global kyc_documents
  kyc_documents.update(docs)





def check_kyc():
  if len(kyc_documents) == 0:
    print("No KYC documents found.")
    print("============================================")
    print("KYC Documents:")
  else:
     for doc in kyc_documents:
      print(f"{doc}: {kyc_documents[doc]}")
      print("============================================")

 


  




if __name__ == "__main__":
    print("============================================")
    print("Welcome to the Simple Banking App!")
    print("============================================")

while True:
    print("1. Check Balance")
    print("2. Deposit an amount")
    print("3. Withdraw an amount")
    print("4. Check KYC Document")
    print("5. Update KYC Document")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")
    print("============================================")

    if choice == "1":
      check_balance()
    elif choice == "2":
      amt = float(input("Enter the amount to deposit: "))
      deposit(amt)
      print(f"Amount {amt} deposited successfully.")
      print("============================================")
    elif choice == "3":
      amt = float(input("Enter the amount to withdraw: "))
      withdraw(amt)
      print(f"Amount {amt} withdrawn successfully.")
      print("============================================")
    elif choice == "4":
      if len(kyc_documents) == 0:
        print("No KYC documents found.")
        print("============================================")
      else:
        check_kyc()
    elif choice == "5":
      kyc_docs= {}
      n_documents = int(input("Enter the number of documents to update: "))
      for i in range(n_documents):
        key = input("Enter the document type:")
        value = input("Enter the document number:")
        kyc_docs[key] = value
      update_kyc(kyc_docs)
      print("KYC document updated successfully.")
      print("============================================")
    elif choice == "6":
      print("Thank you for using the Simple Banking App!")
      print("============================================")
      break
    else:
      print("Invalid choice. Please try again.")
      print("============================================")








