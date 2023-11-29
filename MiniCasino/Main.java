import java.util.Scanner;


class Main {
    static Scanner input = new Scanner(System.in);

    public static final String ANSI_YELLOW = "\u001B[33m";
    public static final String ANSI_RESET = "\033[0m";
    public static final String ANSI_RED = "\033[0;31m";
    public static final String ANSI_BLACK = "\033[0;30m";
    public static final String ANSI_GREEN = "\033[0;32m";



    public static void main(String[] args) {
        double coins;
        boolean run = true;
        System.out.println(ANSI_YELLOW + " __      __   _                    _         _   _           ___   _   ___ ___ _  _  ___  _\n" +
                " \\ \\    / /__| |__ ___ _ __  ___  | |_ ___  | |_| |_  ___   / __| /_\\ / __|_ _| \\| |/ _ \\| |\n" +
                "  \\ \\/\\/ / -_) / _/ _ \\ '  \\/ -_) |  _/ _ \\ |  _| ' \\/ -_) | (__ / _ \\\\__ \\| || .` | (_) |_|\n" +
                "   \\_/\\_/\\___|_\\__\\___/_|_|_\\___|  \\__\\___/  \\__|_||_\\___|  \\___/_/ \\_\\___/___|_|\\_|\\___/(_)\n" +
                "                                                                                            " + ANSI_RESET);
        while (run) {
            System.out.println("Insert amount of coins (Minimum insert of 30 coins and maximum of 3000 coins):  ");
            coins = input.nextDouble();
            while (coins >= 30 && coins <= 3000) {
                coins = menu(coins);
                if (coins == 0) {
                    System.out.println("You lost all of your coins :(");
                } else {
                    System.out.println("You ended with a total of " + Math.round(coins * 100) /100.0 + " coins.");
                }
                run = false;
                break;
            }
        }
    }

    public static double menu(double coins) { // Allows the user to select a game
        boolean play = true;
        int gameChoice;
        while (play) {
            System.out.println("Which game would you like to play? \n 1 - Roulette \n 2 - Mines \n 3 - Quit");
            gameChoice = input.nextInt();
            switch (gameChoice) {
                case 1: coins = roulette(coins); break;
                case 2: coins = mines(coins); break;
                case 3: play = false; break;
            }
            if (coins == 0) {
                play = false;
            }
        }
        return coins;
    }

    public static double roulette(double coins) { // Plays roulette
        double bet = 0;
        int choice;
        String chosenColour, chosenEvenOrOdd;
        while (bet < 1 || bet > coins) {
            System.out.println("You currently have " + coins + " coins");
            System.out.println("How much would you like to bet? ");
            bet = input.nextDouble();
            if (bet == 0) {
                System.out.println("Not enough");
                menu(coins);
            }

        }
        coins = coins - bet;
        System.out.println("Your bet is " + bet + " coins.");

        System.out.println("\nWelcome to roulette! The objective of the game is to correctly bet on the characteristic of the pocket in which the ball lands, i.e., either its colour, whether it is odd or even, or its exact number.");

        System.out.println("      ____________________ \n"
                + "     |__________" + ANSI_GREEN + "0" + ANSI_RESET + "_________|\n"
                + "     |___" + ANSI_RED + "1" + ANSI_RESET + "__|___" + ANSI_BLACK + "2" + ANSI_RESET + "__|___" + ANSI_RED + "3" + ANSI_RESET + "__|\n"
                + "     |___" + ANSI_BLACK + "4" + ANSI_RESET + "__|___" + ANSI_RED + "5" + ANSI_RESET + "__|___" + ANSI_BLACK + "6" + ANSI_RESET + "__|\n"
                + "     |___" + ANSI_RED + "7" + ANSI_RESET + "__|___" + ANSI_BLACK + "8" + ANSI_RESET + "__|___" + ANSI_RED + "9" + ANSI_RESET + "__|\n"
                + "     |__" + ANSI_BLACK + "10" + ANSI_RESET + "__|__" + ANSI_BLACK + "11" + ANSI_RESET + "__|__" + ANSI_RED + "12" + ANSI_RESET + "__|\n"
                + "     |__" + ANSI_BLACK + "13" + ANSI_RESET + "__|__" + ANSI_RED + "14" + ANSI_RESET + "__|__" + ANSI_BLACK + "15" + ANSI_RESET + "__|\n"
                + "     |__" + ANSI_RED + "16" + ANSI_RESET + "__|__" + ANSI_BLACK + "17" + ANSI_RESET + "__|__" + ANSI_RED + "18" + ANSI_RESET + "__|\n"
                + "     |__" + ANSI_RED + "19" + ANSI_RESET + "__|__" + ANSI_BLACK + "20" + ANSI_RESET + "__|__" + ANSI_RED + "21" + ANSI_RESET + "__|\n"
                + "     |__" + ANSI_BLACK + "22" + ANSI_RESET + "__|__" + ANSI_RED + "23" + ANSI_RESET + "__|__" + ANSI_BLACK + "24" + ANSI_RESET + "__|\n"
                + "     |__" + ANSI_RED + "25" + ANSI_RESET + "__|__" + ANSI_BLACK + "26" + ANSI_RESET + "__|__" + ANSI_RED + "27" + ANSI_RESET + "__|\n"
                + "     |__" + ANSI_BLACK + "28" + ANSI_RESET + "__|__" + ANSI_BLACK + "29" + ANSI_RESET + "__|__" + ANSI_RED + "30" + ANSI_RESET + "__|\n"
                + "     |__" + ANSI_BLACK + "31" + ANSI_RESET + "__|__" + ANSI_RED + "32" + ANSI_RESET + "__|__" + ANSI_BLACK + "33" + ANSI_RESET + "__|\n"
                + "     |__" + ANSI_RED + "34" + ANSI_RESET + "__|__" + ANSI_BLACK + "35" + ANSI_RESET + "__|__" + ANSI_RED + "36" + ANSI_RESET + "__|\n");


        System.out.println("What would you like to bet on? \n 1 - Colour \n 2 - Odd or even (0 is not an odd or even number) \n 3 - Specific number");
        choice = input.nextInt();
        if (choice == 1) {
            int randomNum = (int) (Math.random() * (37) + 1);
            if (randomNum == 37) {
                randomNum = 0;
            }
            System.out.println("Which colour would you like to bet on? \n 'Black' (2x payout) \n 'Red' (2x payout) \n 'Green' (35x payout)");
            chosenColour = input.next();
            System.out.println("The ball landed on " + randomNum);
            if (chosenColour.equalsIgnoreCase("black")) {
                if (randomNum == 2 || randomNum == 4 || randomNum == 6 || randomNum == 8 || randomNum == 10 || randomNum == 11 || randomNum == 13 || randomNum == 15 || randomNum == 17 || randomNum == 20 || randomNum == 22 || randomNum == 24 || randomNum == 26 || randomNum == 28 || randomNum == 29 || randomNum == 31 || randomNum == 33 || randomNum == 35) {
                    coins = coins + bet * 2;
                    System.out.println("You won " + bet * 2 + " coins.");
                    System.out.println("Your total is " + coins + " coins. ");
                } else {
                    System.out.println("You lost " + bet + " coins.");
                    System.out.println("Your total is " + coins + " coins. ");
                }
            } else if (chosenColour.equalsIgnoreCase("red")) {
                if (randomNum == 1 || randomNum == 3 || randomNum == 5 || randomNum == 7 || randomNum == 9 || randomNum == 12 || randomNum == 14 || randomNum == 16 || randomNum == 18 || randomNum == 19 || randomNum == 21 || randomNum == 23 || randomNum == 25 || randomNum == 27 || randomNum == 30 || randomNum == 32 || randomNum == 34 || randomNum == 36) {
                    coins = coins + bet * 2;
                    System.out.println("You won " + bet * 2 + " coins. ");
                    System.out.println("Your total is " + coins + " coins. ");
                } else {
                    System.out.println("You lost " + bet + " coins.");
                    System.out.println("Your total is " + coins + " coins. ");
                }
            } else if (chosenColour.equalsIgnoreCase("green")) {
                if (randomNum == 0) {
                    coins = coins + bet * 35;
                    System.out.println("You won " + bet * 35 + " coins. ");
                    System.out.println("Your total is " + coins + " coins. ");
                } else {
                    System.out.println("You lost " + bet + " coins.");
                    System.out.println("Your total is " + coins + " coins. ");
                }
            }
        } else if (choice == 2) {
            int randomNum = (int) (Math.random() * (36) + 1);
            System.out.println("What would you like to bet on? \n 'Odd' for odd numbers (2x payout) \n 'Even' for even numbers (2x payout)");
            chosenEvenOrOdd = input.next();
            System.out.println("The ball landed on " + randomNum);
            if (chosenEvenOrOdd.equalsIgnoreCase("even")) {
                if (randomNum % 2 == 0) {
                    coins = coins + bet * 2;
                    System.out.println("You won " + bet * 2 + " coins. ");
                    System.out.println("Your total is " + coins + " coins. ");
                } else {
                    System.out.println("You lost " + bet + " coins. ");
                    System.out.println("Your total is " + coins + " coins. ");
                }
            } else if (chosenEvenOrOdd.equalsIgnoreCase("odd")) {
                if (randomNum % 2 == 1) {
                    coins = coins + bet * 2;
                    System.out.println("You won " + bet * 2 + " coins. ");
                    System.out.println("Your total is " + coins + " coins. ");
                } else {
                    System.out.println("You lost " + bet + " coins. ");
                    System.out.println("Your total is " + coins + " coins. ");
                }
            }
        } else if (choice == 3) {
            int specificNum;
            int randomNum = (int) (Math.random() * (37) + 1);
            if (randomNum == 37){
                randomNum = 0;
            }
            System.out.println("What specific number would you like to pick that is on the board? (35x payout)");
            specificNum = input.nextInt();
            System.out.println("The ball landed on " + randomNum);
            if (randomNum == specificNum){
                coins = coins + bet * 35;
                System.out.println("You won " + bet * 35 + " coins. ");
                System.out.println("Your total is " + coins + " coins. ");
            }
            else {
                System.out.println("You lost " + bet + " coins. ");
                System.out.println("Your total is " + coins + " coins. ");
            }

        }
        return coins;
    }
    public static double mines(double coins) { // Plays mines
        double bet = 0;
        String cashOut;
        int numMines, col, row, totalCells = 25, nonMineCells, counter = 0;
        char[][] grid = new char[5][5];
        int[][] grid2 = new int[5][5];
        boolean play = true;
        double multiplier = 1;

        while (bet < 1 || bet > coins) {
            System.out.println("You currently have " + coins + " coins");
            System.out.println("How much would you like to bet? ");
            bet = input.nextDouble();
            if (bet == 0) {
                System.out.println("Not enough");
                menu(coins);
            }
        }
      
        System.out.println("Your bet is " + bet + " coins.");
        coins = coins - bet;
        System.out.println("\nWelcome to mines! The objective of the game is to select cells that do not have mines under them. Once you choose a cell with a mine, you lose.");
        do {
            System.out.print("Enter the number of mines you would like to play with: (less than 25; discovering all the cells without mines = 50x payout) \n");
            numMines = input.nextInt();

            while (numMines <= 0 || numMines >= 25) {
                System.out.println("Invalid number. Please enter a number between 1 and 24.");
                numMines = input.nextInt();
            }
            
            nonMineCells = totalCells - numMines;  
            multiplier = 1 + (numMines / 5.0);

            while (numMines > 0) {
                int randomNumX = (int) (Math.random() * (5));
                int randomNumY = (int) (Math.random() * (5));

                if (grid2[randomNumX][randomNumY] != 1) {
                    grid2[randomNumX][randomNumY] = 1;
                    numMines--;
                }
            }
          // CHEAT CODE
           // gridder(grid2);
            System.out.println();
            declareGrid(grid);

            while (play) {
                displayGrid(grid);
                System.out.println("You have a total of " + coins + " coins, and your bet is/was " + bet + " coins. " + "Would you like to cash out? Y - Yes or N - No");
                input.nextLine();
                cashOut = input.nextLine();

                if (cashOut.equalsIgnoreCase("y")) {
                    if (coins == 0) {
                        coins = bet;
                    }
                    play = false;
                } 
                else {
                    System.out.print("Enter column: ");
                    col = input.nextInt();
                    System.out.print("Enter row: ");
                    row = input.nextInt();

                    if (row < 0 || col < 0 || row >= 5 || col >= 5) {
                        System.out.println("Out of bounds");
                    } else {
                        if (grid2[row][col] == 1) {
                            System.out.println("You discovered a mine. You lost your bet of " + bet + " coins.");
                          if (counter == 1){
                            coins = coins - bet * multiplier;
                          }
                          else {
                            coins = coins - bet * (multiplier * counter);
                          }
                            play = false;
                        } else if (grid[row][col] == '?') {
                            counter ++;
                            System.out.println("\nMultiplier of " + multiplier + "x\n");
                            coins = coins + bet * multiplier;
                            if (nonMineCells == counter){
                              System.out.println("You won without hitting a mine! (50x Payout)");
                              coins = coins * 50;
                              play = false;
                            }
                        }
                        grid[row][col] = '*';
                    }
                }
            }

            revealGrid(grid, grid2);
        } while (play);
        return coins;
    }
        public static void displayGrid(char[][] grid) {
            System.out.println("    0   1   2   3   4");
            for (int row = 0; row < grid.length; row++) {
                System.out.print((row + row) / 2 + " ");
                for (int col = 0; col < grid[row].length; col++) {
                    if (grid[row][col] == '?' || grid[row][col] == 'o') {
                        System.out.print("| ? ");
                    } else {
                        System.out.print("| " + grid[row][col] + " ");
                    }
                }
                System.out.println("|");
            }
        }

        public static void declareGrid(char[][] grid) {
            for (int row = 0; row < grid.length; row++) {
                for (int col = 0; col < grid[row].length; col++) {
                    grid[row][col] = '?';
                }
            }
        }

        // CHEAT CODE
     public static void gridder(int[][] grid2) {
            for (int row = 0; row < grid2.length; row++) {
                for (int col = 0; col < grid2[row].length; col++) {
                    System.out.print(grid2[row][col] + " ");
                }
                System.out.println("");
            }
        }

        public static void revealGrid(char[][] grid, int[][] grid2) {
            System.out.println("GRID REVEALED (o - mine, ? - not a mine, * - already discovered):");
            System.out.println("    0   1   2   3   4");
            for (int row = 0; row < grid.length; row++) {
                System.out.print((row + row) / 2 + " ");
                for (int col = 0; col < grid[row].length; col++) {
                    if (grid2[row][col] == 1) {
                        System.out.print("|" + ANSI_RED + " o " + ANSI_RESET);
                    } else {
                        System.out.print("| " + grid[row][col] + " ");
                    }
                }
                System.out.println("|");
            }
        }
}
