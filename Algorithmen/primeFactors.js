function prime(n) {
  for (let i = 2; i < Math.sqrt(n); i++) {
    if (n % i == 0) return prime(i).concat(prime(n / i));
  }
  return [n];
}

console.log(prime(4680));
