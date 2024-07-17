class Menu:
    def menu(self):
        print('''\t\tWELCOME TO DABANG LIBRARY
              \nPress One Of The Following To Pick Your Option
              1. Check available books
              2. Rent a book
              3. Buy a book 
              4. Return a book
              5. Client info
              6. Exit''')
        self.a=input("Enter your choice\n")
    def store_data(self,filename, data):
        try:
            with open(filename, 'a') as file:  
                file.write(data + '\n')
            print(f"Data successfully written to {filename}")
        except Exception as e:
            print(f"An error occurred: {e}") 
    def overwrite_data(self, filename, data):
        try:
            with open(filename, 'w') as file:
                file.write(data)
            print(f"Data successfully written to {filename}")
        except Exception as e:
            print(f"An error occurred: {e}")        
    def read_data(self, filename):
        try:
            with open(filename, 'r') as file:
                data = file.read()
            #print(f"Data read from {filename}:\n{data}")
            return data.split('\n') if data else []
        except FileNotFoundError:
            print(f"The file {filename} does not exist.")
            return []
        except Exception as e:
            print(f"An error occurred: {e}")
            return []          
    def available(self):
        available_books = self.read_data("Available_books.txt")
        if not available_books:
            ab=["Harry potter","Lotr","Hobbit","Alchemist","The big short","Wolf of wall street"]
            data = '\n'.join(ab)
            self.overwrite_data("Available_books.txt",data)
            for i, book in enumerate(ab, start=1):
                    print(f"{i}. {book}")
            back_to_menu = input("Do you want to go back to the menu? (yes/no): ").lower()
            if back_to_menu == 'yes':
                self.interface()        
        else:
            for i, book in enumerate(available_books, start=1):
                    print(f"{i}. {book}")
            back_to_menu = input("Do you want to go back to the menu? (yes/no): ").lower()
            if back_to_menu == 'yes':
                self.interface()         
                               
    def rental(self):
        available_books = self.read_data("Available_books.txt")
        rental_price = 1000  
        if not available_books:
            print("No books available for rental.")
            return
        else:
            print("Available books for rental:")
            for i, book in enumerate(available_books, start=1):
                print(f"{i}. {book} price is {rental_price}Rs")
            book_choice = int(input("Enter the number of the book you want to rent: ")) - 1
        
            if 0 <= book_choice < len(available_books):
                chosen_book = available_books[book_choice]
            else:
                print("Invalid choice.")
                return
        
        
            user_name = input("Enter your name: ")
        
        
            rental_info = f"User: {user_name}, Book: {chosen_book}, Total Price: ${rental_price}"
            self.store_data("Rental_records.txt", rental_info)
            print(f"You have rented '{chosen_book}'. Total price is ${rental_price}.")
        
        
            available_books.pop(book_choice)
            self.ab = available_books
        
        # Update the available books file
            data = '\n'.join(available_books)
            self.overwrite_data("Available_books.txt", data)
            back_to_menu = input("Do you want to go back to the menu? (yes/no): ").lower()
            if back_to_menu == 'yes':
                self.interface()
            
    def buy(self):
        available_books = self.read_data("Available_books.txt")
        book_prices = {
            "Harry potter": 5000,
            "Lotr": 6000,
            "Hobbit": 4500,
            "Alchemist": 3500,
            "The big short": 4000,
            "Wolf of wall street": 5500
        }
        
        if not available_books:
            print("No books available for purchase.")
            return
        
        print("Available books for purchase:")
        for i, book in enumerate(available_books, start=1):
            print(f"{i}. {book} price is {book_prices[book]} Rs")
        
        try:
            book_choice = int(input("Enter the number of the book you want to buy: ")) - 1
            if 0 <= book_choice < len(available_books):
                chosen_book = available_books[book_choice]
                book_price = book_prices[chosen_book]
            else:
                print("Invalid choice.")
                return
        except ValueError:
            print("Invalid input. Please enter a number.")
            return
        
        user_name = input("Enter your name: ")
        buyer_info = f"Buyer: {user_name}, Book: {chosen_book}, Total Price: {book_price} Rs"
        self.store_data("Purchase_records.txt", buyer_info)
        print(f"You have bought '{chosen_book}'. Total price is {book_price} Rs.")
        
        available_books.pop(book_choice)
        data = '\n'.join(available_books)
        self.overwrite_data("Available_books.txt", data)
        
        back_to_menu = input("Do you want to go back to the menu? (yes/no): ").lower()
        if back_to_menu == 'yes':
            self.interface()
    def return_book(self):
        rental_records = self.read_data("Rental_records.txt")
        print(rental_records)
        if not rental_records:
            print("No rental records found.")
            back_to_menu = input("Do you want to go back to the menu? (yes/no): ").lower()
            if back_to_menu == 'yes':
                self.interface()
            return
        
        else:
        
            user_name = input("Enter your name: ")
            book_name = input("Enter the name of the book you want to return: ")
            found = False
            updated_rental_records = []
        
            for record in rental_records:
                if record and user_name in record and book_name in record:
                    found = True
                else:
                    updated_rental_records.append(record)
        
            if found:
                available_books = self.read_data("Available_books.txt")
                available_books.append(book_name)
                data = '\n'.join(available_books)
                self.overwrite_data("Available_books.txt", data)
            
                rental_data = '\n'.join(updated_rental_records)
                self.overwrite_data("Rental_records.txt", rental_data)
            
                print(f"Book '{book_name}' returned successfully.")
            else:
                print(f"No record found for '{book_name}' rented by '{user_name}'.")
        
            back_to_menu = input("Do you want to go back to the menu? (yes/no): ").lower()
            if back_to_menu == 'yes':
                self.interface() 
    def clients(self):
        rclient = self.read_data("Rental_records.txt")
        bclient = self.read_data("Purchase_records.txt")
        data="\n".join(rclient)
        data1="\n".join(bclient)
        print(f"\t\tRental clients\n{data}\n\n\t\tBuyers\n{data1}")                                   
class User(Menu):
    def interface(self):
        self.menu()
        if self.a=="1":
            self.available()
            #self.read_data("Available_books.txt")
        elif self.a=="2":
            self.rental()
        elif self.a=="3":
            self.buy()
        elif self.a=="4":
            self.return_book()
        elif self.a=="5":
            self.clients()
        elif self.a=="6":
            print("Thank You For Using Debang Rental")  
        else:
            self.interface()
                      
user=User()
user.interface()        
