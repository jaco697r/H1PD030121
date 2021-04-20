using System;


namespace bankacount
{
   
    class Program
    {
        static void Main(string[] args)
        {
            while(true)
            { 
            Console.WriteLine("Hello!");
            Console.Write("Enter your pin: ");
            int pin = Int32.Parse(Console.ReadLine());

                if (pin == 1234)
                {
                    var my_account = new BankAccount();
                    int menu_choice = Menu();
                    if (menu_choice == 1)
                    {
                        Console.WriteLine(my_account.balance());
                        Console.WriteLine("Do you want to exit? y/n");
                        Exit_app();
                    }
                    if (menu_choice == 2)
                    {
                        Console.WriteLine(my_account.withdraw());
                        Console.WriteLine("Do you want to exit? y/n");
                        Exit_app();

                    }
                    if (menu_choice == 3)
                    {
                        double amount = my_account.deposit();
                        Console.WriteLine("You made a deposit for: ");
                        Console.WriteLine(amount);
                        Console.WriteLine("New Balance:");
                        Console.WriteLine(my_account.balance());
                        Exit_app();
                    }
                    else
                    {
                        Console.WriteLine("Invalid input. Try again");
                    }
                }
            }

        }

        static int Menu()
        {
            Console.WriteLine("What do you want to do?");
            Console.WriteLine("1. See Balance");
            Console.WriteLine("2. Withdraw");
            Console.WriteLine("3. Deposit Money");
            int user_input = Int32.Parse(Console.ReadLine());
            return user_input;
        }

        static void Exit_app()
        {
            Console.WriteLine("Do you want to exit? y/n");
            char input = Console.ReadKey().KeyChar;
            if (input == 'y' || input == 'Y')
            {
                Environment.Exit(0);
            }

        }
    }

    public class BankAccount

    {
        private double account_balance;

        public BankAccount()
        { 
         account_balance = 1500;
        }

        public double withdraw()
        {
            int amount;
            
            while (true) 
            { 
            Console.Write("How much do you want to withdraw");
            amount = Int32.Parse(Console.ReadLine());
                if (amount > account_balance || amount < 0)
                {
                    Console.WriteLine("You do not have enough money on the account, or you tried to withdraw less than 0. \n Choose a different amount and try again \n Press any key to continue");
                    Console.ReadLine();
                }
                else
                {
                    account_balance -= amount;                    

                    Console.WriteLine();
                    break;
                }
            }
            return account_balance;     
        }

        public double deposit()
        {
            Console.Write("How much do you want to deposit");
            int amount = Int32.Parse(Console.ReadLine());
            if (amount <= 0)
            {
                Console.WriteLine("You can not deposit nothing or less than nothing. Choose withdraw if you want money from your account. \n Press any key to continue");
                Console.ReadLine();
                withdraw();
            }
            account_balance += amount;
            return amount;
        }

        public double balance()
        {
            return account_balance;
        }
    }
}


//Lave en klasse BankAccount, som har en instance variable balance og to metoder withdraw og deposit
//Lav en print metode, som udskriver balencen
//Gør balance privat, så den kun kan tilgåes via metoder
//Lav withdraw modstandsdygtig overfor overtræk
//Lav en "brugergrænseflade" til bank systemet i en separat fil

