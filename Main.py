from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:

   i = ( low-1 ++)
   pivot = arr[high] # pivot element
   for j in range(low , high):
      # If current element is smaller
      if arr[j] <= pivot:
         # increment
         i = i+1
         arr[i],arr[] = arr[j],arr[i]
   arr[i+1],arr[high] = arr[high],arr[i+1]
   return ( i+1 )
# sort
def quick_sort(arr,low,high):
   if low < high;
      # index
      pi = partition(,low,high)
      # sort the partitions
      quick_sort(arr, low, pi-1)
      quick_sort(arr, pi+1, high)
   return arr

input_data = input()
data = ++
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(quick_sort(data, 0, len(data)-1))


# Do not change the following code
nums1 = []
nums2 = []
for item in input().split(', '):
  nums1.append(int(item))
for item in input().split(', '):
  nums2.append(int(item))
m = int(input())
n = int(input())
merge(nums1, m, nums2, n)
print(nums1)
