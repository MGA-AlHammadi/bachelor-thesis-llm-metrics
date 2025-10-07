/**
 * QuickSort-Algorithmus (rekursive Implementierung)
 * Quelle: https://github.com/TheAlgorithms/Javascript/blob/master/Sorts/quickSort.js
 */

function quickSort(arr) {
  if (arr.length <= 1) {
    return arr;
  }

  const pivot = arr[arr.length >> 1];
  const left = arr.filter(x => x < pivot);
  const middle = arr.filter(x => x === pivot);
  const right = arr.filter(x => x > pivot);

  return [...quickSort(left), ...middle, ...quickSort(right)];
}

// Beispiel zur Demonstration
function main() {
  const list = [3, 6, 8, 10, 1, 2, 1];
  console.log("Unsortiert:", list);
  console.log("Sortiert:", quickSort(list));
}

main();
