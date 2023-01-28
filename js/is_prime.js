const is_prime = (n) => {
  if (n <= 3) {
    return n > 1;
  }
  if (n % 2 === 0 || n % 3 === 0) {
    return false;
  }
  let i = 5;
  while (i ** 2 <= n) {
    if (n % i === 0 || n % (i + 2) === 0) {
      return false;
    }
    i += 6;
  }
  return true;
};
//--------------------main----------------------------------------------------------------------
// findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]);
for (let i = 0; i < 100; i++) {
  if (is_prime(i)) {
    console.log(i, is_prime(i));
  }
}
