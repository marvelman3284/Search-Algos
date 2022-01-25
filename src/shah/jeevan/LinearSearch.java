package shah.jeevan;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class LinearSearch {

    public static void main(String[] args)
    {
        System.out.print("\f");
        ArrayList<Integer> array = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5, 6));
        Scanner input=new Scanner(System.in);
        System.out.println("What number would you like to search for?");
        int search=input.nextInt();
        search(array,search);
        search(array, 0);
    }

    public static void search(ArrayList<Integer> lst, Integer findVal) {
        boolean found = false;
        for (int i : lst) {
            if (i == findVal) {
                System.out.println("Value " + findVal + " found at index " + lst.indexOf(i));
                found = true;
                break;
            }
        }
        if (!found) {
            System.out.println("Value " + findVal + " not found in list.");
        }
    }
}
