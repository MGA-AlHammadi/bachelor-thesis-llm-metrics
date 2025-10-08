/**
 * Merge Sort Algorithm
 * https://github.com/trekhleb/javascript-algorithms/blob/master/src/algorithms/sorting/merge-sort/mergeSort.js
 * @param {number[]} originalArray - Array to be sorted
 * @return {number[]} - Sorted array
 */
export default function mergeSort(originalArray) {
  // Base case – array with one element
  if (originalArray.length <= 1) {
    return originalArray;
  }

  // Split array into two halves
  const middleIndex = Math.floor(originalArray.length / 2);
  const leftArray = originalArray.slice(0, middleIndex);
  const rightArray = originalArray.slice(middleIndex);

  // Recursively sort both halves
  const leftSortedArray = mergeSort(leftArray);
  const rightSortedArray = mergeSort(rightArray);

  // Merge sorted halves
  return mergeSortedArrays(leftSortedArray, rightSortedArray);
}

/**
 * Merge two sorted arrays into one sorted array.
 * @param {number[]} leftArray
 * @param {number[]} rightArray
 * @return {number[]}
 */
function mergeSortedArrays(leftArray, rightArray) {
  const sortedArray = [];

  // Merge elements from both arrays in order
  while (leftArray.length && rightArray.length) {
    const minElement =
      leftArray[0] <= rightArray[0] ? leftArray.shift() : rightArray.shift();
    sortedArray.push(minElement);
  }

  // If any elements remain, add them
  return sortedArray.concat(leftArray).concat(rightArray);
}

// Example usage:
// console.log(mergeSort([3, 6, 8, 10, 1, 2, 1]));
