package shah.jeevan;

import java.util.*;

public class Main {

    public static Random rand = new Random();

    public static void main(String[] args) {
	// write your code here
        ArrayList<Integer> l = genRandomList(2000, 100);
        int find = l.get(rand.nextInt(l.size()));
        int[] arr = genRandomArr(200, 1000);
        LinearSearch.search(l, find);
        BubbleSort.bubbleSort(arr);
        Collections.sort(l);
        BinarySearch.search(l, find);
    }

    public static ArrayList<Integer> genRandomList(int length, int max) {
        ArrayList<Integer> l = new ArrayList<>();
        Random rand = new Random();
        for (int i = 0; i < length; i++) {
            l.add(rand.nextInt(max));
        }
        return l;
    }

    public static int[] genRandomArr(int length, int max) {
        int[] arr = new int[length];
        Random rand = new Random();
        for (int i = 0; i < length; i++) {
            arr[i] = rand.nextInt(max);
        }
        return arr;
    }
}
