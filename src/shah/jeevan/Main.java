package shah.jeevan;

import java.util.*;

public class Main {

    public static Random rand = new Random();
    public static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        System.out.println("Would you like a sorting(1) or searching(2) algorithm?[1, 2]: ");
        int which = sc.nextInt();
        switch (which){
            case 1: {
                sorting();
            }
            case 2: {
                searching();
            }
        }
    }

    public static void searching() {
        System.out.println("Which searching algorithm do you want? Binary(1), Linear(2): [1,2] ");
        int which = sc.nextInt();

        switch (which) {
            case 1: {
                ArrayList<Integer> l = genRandomList(2000,10000);
                Collections.sort(l);
                int find = l.get(rand.nextInt(l.size()));
                BinarySearch.search(l, find);
            }
            case 2: {
                ArrayList<Integer> l = genRandomList(2000,10000);
                int find = l.get(rand.nextInt(l.size()));
                LinearSearch.search(l, find);
            }
        }
    }

    public static void sorting() {
        System.out.println("Which sorting algorithm do you want? Selection(1), Bubble(2), Quick(3): [1, 2, 3] ");
        int which = sc.nextInt();

        switch (which) {
            case 1 -> SelectionSort.sort(genRandomArr(200, 10000));
            case 2 -> BubbleSort.bubbleSort(genRandomArr(200, 10000));
            case 3 -> QuickSort.quickSort(genRandomList(200, 10000));
        }
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
