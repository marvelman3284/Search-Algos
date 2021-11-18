#include <iostream>
#include <cstdlib>

using namespace std;
// todo gen random lists
int sort(const int (&arr)[10], int find_val) {
  for (int i = 0; i < (sizeof(arr) / sizeof(arr[0])); i++) {
    if (arr[i] == find_val) {
      cout << "Value " << find_val << " found at index " << i << endl;
      return 0;
    }
  } 
  return 1;
}


int main() {
  srand(time(0));
  int arr[10];

  int max = 10;

  for (int i = 0; i < max; i++) {
    arr[i] = rand() % 100;
  }
  int find = arr[rand() % 10];
  cout << find << endl;
  cout << sort(arr, find) << endl;
}
