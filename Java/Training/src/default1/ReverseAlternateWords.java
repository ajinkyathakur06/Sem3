package default1;

import java.util.Scanner;

public class ReverseAlternateWords {

    public static void main(String[] args) {
        // Create a Scanner object for user input
        Scanner scanner = new Scanner(System.in);

        // Input a sentence
        System.out.println("Enter a sentence:");
        String sentence = scanner.nextLine();

        // Process and print the result
        String result = reverseAlternateWords(sentence);
        System.out.println("Output: " + result);
        scanner.close();
    }

    // Method to reverse alternate words in a sentence
    public static String reverseAlternateWords(String sentence) {
        // Split the sentence into words
        String[] words = sentence.split("\\s+");
        
        // Loop through the words
        for (int i = 0; i < words.length; i++) {
            // Reverse every alternate word (1st, 3rd, 5th, etc.)
            if (i % 2 == 1) {
                words[i] = new StringBuilder(words[i]).reverse().toString();
            }
        }

        // Join the words back into a sentence
        return String.join(" ", words);
    }
}
