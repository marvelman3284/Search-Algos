package shah.jeevan;

import java.util.ArrayList;

public class LinearSearch {
    public static void search(ArrayList<Integer> lst, Integer findVal) {
        for (int i : lst) {
            if (i == findVal) {
                System.out.println("Value " + findVal + " found at index " + lst.indexOf(i));
                break;
            }
        }
    }
}
