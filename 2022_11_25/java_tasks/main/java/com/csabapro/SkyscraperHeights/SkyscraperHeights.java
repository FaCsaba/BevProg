package SkyscraperHeights;

import java.util.ArrayList;
import java.util.stream.Collectors;

public class SkyscraperHeights {

    static int getSkyscraperHeight(int[] skyscraperHeights) {
        ArrayList<Integer> heightDiffs = new ArrayList<Integer>();
        for (int i = 1; i < skyscraperHeights.length; i++) {
            heightDiffs.add(Math.abs(skyscraperHeights[i] - skyscraperHeights[i - 1]));
        }

        return heightDiffs.stream().collect(Collectors.summingInt(Integer::intValue));

    }

    // unfortunately I had to put 2 to the power of 1024 into a string because java
    // just thought it was infinity while python happily just went with it
    static String hugeNum = "179769313486231590772930519078902473361797697894230657273430081157732675805500963132708477322407536021120113879871393357658789768814416622492847430639474124377767893424865485276302219601246094119453082952085005768838150682342462881473913110540827237163350510684586298239947245938479716304835356329624224137216";

    public static void main(String[] args) {
        // int[] a = {2, 4, 8, 3, 9, 7, 1};
        // System.out.println(getSkyscraperHeight(a));

        int[] b = hugeNum.chars().map(e -> Integer.parseInt("" + e)).toArray();

        System.out.println(getSkyscraperHeight(b));
    }
}