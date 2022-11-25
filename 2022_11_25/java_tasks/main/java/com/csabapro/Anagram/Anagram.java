package Anagram;

import java.util.stream.Collectors;

public class Anagram {
    static String normalizeString(String s) {
        String normalized = "";
        for (int ch : s.chars().toArray()) {
            if (Character.isLetterOrDigit((char) ch)) {
                normalized += (char) ch;
            }
        }
        
        return normalized;
    }
    
    static Boolean isAnagram(String a, String b) {
        String sorted_a = Anagram.normalizeString(a).chars().sorted().mapToObj(c -> Character.toString(c)).collect(Collectors.joining());
        String sorted_b = Anagram.normalizeString(b).chars().sorted().mapToObj(c -> Character.toString(c)).collect(Collectors.joining());

        System.out.println(sorted_a + " " + sorted_b);
        return sorted_a.equals(sorted_b);
    }

    public static void main(String[] args) {
        System.out.println(Anagram.isAnagram("listen", "silent"));
        System.out.println(Anagram.isAnagram("dormitory", "dirty room"));
        
    }
}
