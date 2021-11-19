#include <ctime>
#include <iostream>
#include <cstdlib>

using namespace std;

void swap(int &a, int &b) {
  int temp;
  temp = a;
  a = b;
  b = temp;
}

int sort(int *lst, int len) {

  for (int i = 0; i < len-1; i++) {
    int swaps = 0;
    for (int j = 0; j < len-i-1; j++) {

      if (lst[j] > lst[j+1]) {
        swap(lst[j], lst[j+1]);
        swaps = 1;
      }
    }
    if (!swaps) break;
  }
  cout << "Sorted list:" << endl;
  for (int i = 0; i < len; i++) {
    cout << "" << lst[i] << endl;
  }
  return 0;
}

int main() {
  srand(time(0));
  int n;

  cout << "Enter the amount of elements: " << endl;
  cin >> n;

  int arr[n];

  for(int i = 0; i < n; i++) {
    arr[i] = rand() % 100;
  }

  sort(arr, n);
}
