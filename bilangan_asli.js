function iterative(n) {
  let total = 0;
  for (let i = 1; i <= n; i++) {
    total += i;
  }
  return total;
}

function recursive(n) {
  if (n === 1) return n;
  else return n + recursive1(n - 1);
}

console.log("Iteratif:", iterative(10));
console.log("Rekursif:", recursive(10));
