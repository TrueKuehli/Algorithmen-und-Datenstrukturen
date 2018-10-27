function kaprekar(n) {
  let num = n;
  if (num > 9999) return false;
  while (num != 6174) {
    let digits = num.toString().padStart(4, '0').split('');
    let sorted = digits.sort();
    let nUp = parseInt(sorted.join(''));
    let nDown = parseInt(sorted.reverse().join(''));

    num = nDown - nUp;

    if (num == 0) {
      // Sollte 0 erreicht werden, soll der Algorithmus beendet werden, da
      //   dieser sonst nicht terminiert
      console.log('Breaks for:', n);
      return false;
    }

    // console.log(nDown, nUp, num);
  }

  return true;
}

for (let i = 0; i < 10000; i++) {
  kaprekar(i);
}
