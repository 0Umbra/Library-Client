from pathlib import Path

# Setting the file paths
file_p = Path('LibraryClients.txt')
book_p = Path('ClientsBooks.txt')

while True:
    print('\n1. Register')
    print('2. Check the books you have taken')
    print('3. Take more books')
    print('4. Exit')
    choice = int(input('Type the option you want: '))

    if choice == 1:
        # Generating card number based on the number of lines in the client file
        try:
            with file_p.open() as file:
                line = file.readlines()
                card_num = len(line) + 1
        except FileNotFoundError:
            card_num = 1

        # Requesting client data
        name = str(input('Type your name: '))
        num = int(input('Type your phone number: '))

        # Opening the file in a mode(append)
        with file_p.open(mode='a') as file:
            # Writing client data on file
            file.write(f'{name}, {num}, {card_num}\n')

        print(f'Client successfully registered! Your card code is: {card_num} ')

    elif choice == 3:
        # Requesting card number
        card_num = int(input('Type your card number: '))
        books = str(input('type the name of the book you wish to take (separated by coma): '))

        # Opening file in a mode(append)
        with book_p.open(mode='a') as file:
            file.write(f'{card_num}, {books}\n')

        print('Books successfully added!')

    elif choice == 2:
        # Requesting card number
        card_num = int(input('Type your card number: '))

        # Reading file and verifying the books took by the client
        try:
            with book_p.open() as file:
                lines = file.readlines()
                found = False
                for line in lines:
                    card_num2, books = line.strip().split(',', 1)
                    if int(card_num2) == card_num:
                        print(f'Books taken: {books}')
                        found = True
                if not found:
                    print('0 books found for this card number')
        except FileNotFoundError:
            print('No register found')

    elif choice == 4:
        break
