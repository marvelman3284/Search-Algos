package shah.jeevan;

import java.util.ArrayList;
import java.util.Random;

public class QuickSort {
    public static ArrayList<Integer> quickSort(ArrayList<Integer> arr) {
        Random rand = new Random();

        if (arr.size() < 2) { return arr; }

        ArrayList<Integer> low = new ArrayList<>();
        ArrayList<Integer> same = new ArrayList<>();
        ArrayList<Integer> high = new ArrayList<>();

        int pivot = rand.nextInt(arr.size() - 1);

        for (int i : arr) {
            if (i < pivot) {
                low.add(i);
            } else if (i == pivot) {
                same.add(i);
            } else if (i > pivot) {
                high.add(i);
            }
        }
        ArrayList<Integer> res = new ArrayList<>(quickSort(low));
        res.addAll(same);
        res.addAll(quickSort(high));

        return res;
    }
}
