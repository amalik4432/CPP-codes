// Program to find min, max number in array

#include <iostream>
#include <climits>
using  namespace std;
int main() {

  int n;
  cout << "Enter Length of array: ";
  cin >> n;
  int arr[n];
  for (int i = 0; i < n; i++)
  {
      cin>> arr[i];
  }

  int minNo = INT_MAX;
  for (int i = 0; i < n; i++)
  {
      minNo = max(arr[i], minNo);
  }
  cout<<"Greater Number in array is: "<<minNo<<endl;
  return 0;
}