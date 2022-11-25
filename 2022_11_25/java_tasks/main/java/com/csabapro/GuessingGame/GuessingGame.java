package GuessingGame;
import java.util.Random;
import java.util.Scanner;

public class GuessingGame {
    static int min = 1;
    static int max = 100;
    

    public static void main(String[] args) {
        Random rand = new Random();
        int num = rand.ints(1, min, max).findFirst().getAsInt();
        Scanner scanner = new Scanner(System.in);
        System.out.println("Guessing game");
        while (true) {
            int guess;
            while (true) {
                try {
                    System.out.print("Guess: ");
                    String guess_str = scanner.next();
                    guess = Integer.parseInt(guess_str);
                    break;
                } catch (NumberFormatException e) {
                    System.out.println("That's not a number");
                }
            }
            if (guess > num) {
                System.out.println("Your guess is bigger than my number");
            } else if (guess < num) {
                System.out.println("Your guess is smaller than my number");
            } else {
                break;
            }
        }
        scanner.close();
        System.out.println("Congrats the number was: " + num);

    }
}