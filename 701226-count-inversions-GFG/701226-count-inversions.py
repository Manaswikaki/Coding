class Solution:
    def inversionCount(self, arr):
        n = len(arr)
        temp_arr = [0] * n
        return self._merge_sort(arr, temp_arr, 0, n - 1)

    def _merge_sort(self, arr, temp_arr, left, right):
        inv_count = 0
        if left < right:
            mid = (left + right) // 2

            # Recursive calls for left and right halves
            inv_count += self._merge_sort(arr, temp_arr, left, mid)
            inv_count += self._merge_sort(arr, temp_arr, mid + 1, right)

            # Merge the two halves and count inversions
            inv_count += self._merge(arr, temp_arr, left, mid, right)
        return inv_count

    def _merge(self, arr, temp_arr, left, mid, right):
        i = left    # Starting index for left subarray
        j = mid + 1 # Starting index for right subarray
        k = left    # Starting index to be sorted
        inv_count = 0

        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp_arr[k] = arr[i]
                i += 1
            else:
                # Inversion found: arr[i] > arr[j]
                # All elements from arr[i] to arr[mid] are > arr[j]
                temp_arr[k] = arr[j]
                inv_count += (mid - i + 1)
                j += 1
            k += 1

        # Copy remaining elements
        while i <= mid:
            temp_arr[k] = arr[i]
            i += 1
            k += 1
        while j <= right:
            temp_arr[k] = arr[j]
            j += 1
            k += 1

        # Copy back to original array
        for loop_var in range(left, right + 1):
            arr[loop_var] = temp_arr[loop_var]
            
        return inv_count


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna