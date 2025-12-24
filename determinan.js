/**
 *
 * @param {[]} matrix
 * @param {number} n
 */
function iterative(matrix) {
  let left = 0,
    right = 0;
  for (let i = 0; i < 3; i++) {
    let k = i,
      total = 1;
    for (let j = 0; j < 3; j++) {
      if (k >= 3) k = 0;
      total *= matrix[j][k];
      k++;
    }
    left += total;
  }
  for (let i = 0; i < 3; i++) {
    let k = i,
      total = 1;
    for (let j = 0; j < 3; j++) {
      if (k < 0) k = 2;
      total *= matrix[j][k];
      k--;
    }
    right += total;
  }
  return left - right;
}

function innerRecursive(matrix, column = 0, row = 0, step) {
  if (column === 3) return 1;
  else {
    if ((step === 1 && row === 2) || (step === -1 && row === 0))
      return (
        matrix[column][row] *
        innerRecursive(matrix, column + 1, step === 1 ? 0 : 2, step)
      );
    else
      return (
        matrix[column][row] *
        innerRecursive(matrix, column + 1, step === 1 ? row + 1 : row - 1, step)
      );
  }
}

/**
 *
 * @param {[]} matrix
 * @param {number} n
 */
function recursive(matrix, row, step = null) {
  if (step != null) {
    if (row >= 2) return innerRecursive(matrix, 0, row, step);
    else
      return (
        innerRecursive(matrix, 0, row, step) + recursive(matrix, row + 1, step)
      );
  } else return recursive(matrix, 0, 1) - recursive(matrix, 0, -1);
}

let matrix = [
  [3, 2, 8],
  [20, 7, 10],
  [21, 10, 11],
];

console.log("Rekursif:", recursive(matrix));
console.log("Iteratif:", iterative(matrix));

/**
 *
 * (0 0) (0 1) (0 2)
 * (1 0) (1 1) (1 2)
 * (2 0) (2 1) (2 2)
 *
 */
