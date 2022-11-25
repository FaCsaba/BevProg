package MysteriousMessage;

import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Arrays;

public class MysteriousMessage {
    static String[] ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".split("");
    static String[] abc = "abcdefghijklmnopqrstuvwxyz".split("");

    static String caesarChange(String toExchangeChar, int changeBy, String[] list) {
        return list[(list.length + Arrays.asList(list).indexOf(toExchangeChar) - changeBy) % list.length];
    }

    static String change(String stringToExchange) {
        String ret = "";
        for (String ch : stringToExchange.split("")) {
            if (Arrays.stream(ABC).anyMatch(ch::equals)) {
                ret += caesarChange(ch, -2, ABC);
            } else if (Arrays.asList(abc).contains(ch)) {
                ret += caesarChange(ch, -2, abc);
            } else {
                ret += ch;
            }
        }
        return ret;
    }
    
    public static void main(String[] args) {
        Path path = Paths.get("2022_11_25/message");
        System.out.println(Paths.get(".").toAbsolutePath().normalize().toString());
        try {
            String message = Files.readString(path);
            System.out.println(change(message));
        } catch (Exception e) {
            e.printStackTrace();
        }
        
        
    }
}
