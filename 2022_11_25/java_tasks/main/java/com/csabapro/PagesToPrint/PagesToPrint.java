package PagesToPrint;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class PagesToPrint {
    public static ArrayList<Integer> getPagesToPrint(String toBePrintedInput) {
        ArrayList<Integer> toBePrinted = new ArrayList<>();
        for (String numOrRange : toBePrintedInput.split(",")) {
            try {
                if (numOrRange.length() == 1) {
                    toBePrinted.add(Integer.parseInt(numOrRange));
                } else {
                    String[] range = numOrRange.split("-");
                    toBePrinted.addAll(IntStream
                            .range(Integer.parseInt(range[0]),
                                    Integer.parseInt(range[1])+1)
                            .boxed()
                            .collect(Collectors.toList()));
                }
            } catch (Exception e) {
                System.out.println(e.getMessage());
            }
        }
        toBePrinted.sort(Comparator.naturalOrder());
        return toBePrinted;
    }

    public static void main(String[] args) {
        String pagesToPrintExample = "1-4,9,7,11-15";
        System.out.println(getPagesToPrint(pagesToPrintExample));
    }
}
