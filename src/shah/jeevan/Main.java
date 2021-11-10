package shah.jeevan;

import java.util.*;

public class Main {

    public static Random rand = new Random();

    public static void main(String[] args) {
	// write your code here
        ArrayList<Integer> l = genRandomArr(2000, 100);
        int find = l.get(rand.nextInt(l.size()));
        Collections.sort(l);
//        LinearSearch.search(l, find);
        BinarySearch.search(l, find);
    }

    public static ArrayList<Integer> genRandomArr(int length, int max) {
        ArrayList<Integer> l = new ArrayList<>();
        Random rand = new Random();
        for (int i = 0; i < length; i++) {
            l.add(rand.nextInt(max));
        }
        return l;
    }
}
