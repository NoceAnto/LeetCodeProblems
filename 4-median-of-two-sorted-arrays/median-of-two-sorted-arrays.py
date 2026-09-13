class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        sorted_array = []
        i = j = 0

        # Merge elements from both halves in sorted order
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                sorted_array.append(nums1[i])
                i += 1
            else:
                sorted_array.append(nums2[j])
                j += 1

        # Append remaining elements from either half
        sorted_array.extend(nums1[i:])
        sorted_array.extend(nums2[j:])     
        
        print(sorted_array)
        if len(sorted_array)%2==0:
            midindex = floor(len(sorted_array)/2);

            return (sorted_array[midindex]+sorted_array[midindex-1])/2
        else: 
            midindex = floor(len(sorted_array)/2);
            return sorted_array[midindex]