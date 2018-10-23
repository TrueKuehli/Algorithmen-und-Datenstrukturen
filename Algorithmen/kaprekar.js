function kaprekar(n) {
  if (n > 9999) return false;
  while (n != 6174) {
    let digits = n.toString().padStart(4, '0').split('');
    let sorted = digits.sort();
    let nUp = parseInt(sorted.join(''));
    let nDown = parseInt(sorted.reverse().join(''));

    n = nDown - nUp;

    console.log(nDown, nUp);
  }

  return true;
}

kaprekar(90);
