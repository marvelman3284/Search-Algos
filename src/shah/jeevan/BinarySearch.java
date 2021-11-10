package shah.jeevan;

import java.util.ArrayList;

public class BinarySearch {
    public static void search (ArrayList<Integer> lst, int findVal) {
        float min = 0;
        float max = lst.size();
        for (int i = 0; i < lst.size(); i++) {
            int mid = (int) Math.floor(((min+max)/2));
            if (lst.get(mid) == findVal) {
                System.out.println("Value " + findVal + " found at index " + lst.indexOf(lst.get(mid)));
                break;
            } else if (lst.get(mid) > findVal) {
                max = mid - 1;
            } else if (lst.get(mid) < findVal) {
                min = mid + 1;
            }
        }
    }
}
