function prime(n, i=2) {
  for (i; i < Math.sqrt(n); i++) {
    if (n % i == 0) return prime(i).concat(prime(n / i, i));
  }
  return [n];
}

function prime2(n) {
  let a = 2;
  let primes = [];
  while (n > 1) {
    if (n % a) {
      primes.push(a);
      n = n / a;
    } else a++;
  }
  return primes;
}

console.time('1');
for (let i = 1; i < 1000000; i++) {
  prime(i);
}
console.timeEnd('1');

console.time('2');
for (let i = 1; i < 1000000; i++) {
  prime2(i);
}
console.timeEnd('2');
