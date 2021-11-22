package shah.jeevan;

import java.util.Arrays;

public class SelectionSort {
    public static void sort(int[] arr) {
        int min;
        int temp;

        for (int i = 0; i < arr.length; i++) {
            min = i;
            for (int j=i+1; j < arr.length; j++) {
                if (arr[j] < arr[min]) {
                    min = j;
                }
            }
            temp = arr[min];
            arr[min] = arr[i];
            arr[i] = temp;
        }
        System.out.println(Arrays.toString(arr));
    }
}
