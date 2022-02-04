#include <iostream>

using namespace std;

int arr[10000];
int rrr[10000];

void merge(int start, int end) {
	int mid = (start + end) / 2;
	int i = start, j = mid + 1, k = start;
	
	while (i <= mid && j <= end) {
		if (arr[i] <= arr[j])
			rrr[k++] = arr[i++];
		else
			rrr[k++] = arr[j++];
	}

	while (i <= mid)
		rrr[k++] = arr[i++];
	while (j <= end)
		rrr[k++] = arr[j++];	

	for (int i = start; i <= end; i++)
	{
		arr[i] = rrr[i];
	}
}

void sort(int start, int end) {
	if (start < end) {
		int mid = (start + end) / 2;
		sort(start, mid);
		sort(mid + 1, end);
		merge(start, end);
	}
}

int binary_search(int n) {
	int flag = 0;

	return flag;
}

int main() {
	// 입력
	int c1, c2;

	cin >> c1;
	for (int i = 0; i < c1; i++)
	{
		cin >> arr[i];
	}
	// 정렬
	sort(0, c1 - 1);

	// find, 출력
	for (int i = 0; i < c1; i++)
	{
		cout << arr[i];
	}

	//cin >> c2;
	//int n;
	//for (int i = 0; i < c2; i++)
	//{
	//	cin >> n;
	//	cout << binary_search(n);
	//}
		
	return 0;
}