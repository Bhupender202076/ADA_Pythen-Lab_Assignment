#include <iostream>
#include <algorithm>
using namespace std;

void swap(int arr[],int i,int j){   // for swaping two elements
    int temp=arr[i];
    arr[i]=arr[j];
    arr[j]=temp;
}

// for partition into left part(smaller elements) and right part(larger elements)
int partition(int arr[],int l,int r){  
    int pivot = arr[r];       // setting last elements as pivot
    int i=l-1;               // for keeping check on index of last element which is small than pivot
    for(int j=l;j<r;j++){   // loop for separating small and large elements
        if(arr[j]<pivot){
            i++;
            swap(arr,i,j);}
    }
    swap(arr,i+1,r);
    return i+1;
}

void quickSort(int arr[],int l,int r){ 
    if(l<r){
        int pi=partition(arr, l, r); // partition function
        quickSort(arr,l,pi-1);      //  again calling quickSort function for left part sorting
        quickSort(arr,pi+1,r);     //   calling quickSort function for right part sorting
    }
}

int main(){
    
    int arr[6]={23,30,64,11,7,91};  // unsorted array
    
    quickSort(arr,0,5);                // calling function for sorting
 
    for(int i=0;i<6;i++){             // printing sorted array
        cout<<arr[i]<<" ";
    }cout<<endl;

    return 0;
}
