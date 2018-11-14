class Hamilton {
  constructor(adjazenz) {
    this.g = adjazenz;
    this.v = adjazenz.length;
  }

  isSafe(v, pos, path) {
    if (this.g[path[pos - 1]][v] == 0) return false;
    if (path.includes(v)) return false;

    return true;
  }

  hamCycleUtil(path, pos) {
    if (pos == this.v) {
      if (this.g[path[pos-1]][path[0]] == 1) return true;
      else return false;
    }

    for (let v = 1; v < this.v; v++) {
      if (this.isSafe(v, pos, path)) {
        path[pos] = v;

        if (this.hamCycleUtil(path, pos + 1)) return true;

        path[pos] = null;
      }
    }

    return false;
  }

  hamCycle() {
    let path = (new Array(this.v)).fill(null);
    path[0] = 0;

    let solution = '';
    if (!this.hamCycleUtil(path, 1)) {
      solution = 'Solution does not exist for Graph: \n';

      for (let row of this.g) {
        solution += row.join(' ') + '\n';
      }
    } else {
      // solution = 'Solution found: \n';
      // for (let vertex of path) {
      //   solution += vertex + ', ';
      // }

      // solution += '\nfor Graph: \n';
      // for (let row of this.g) {
      //   solution += row.join(' ') + '\n';
      // }
    }

    return solution;
  }
}

let numOfNodes = 8;

for (let num = 1; num <= numOfNodes; num++) {
  // Generate a whole f*ckton of graphs

  let adjazenz = [];

  for (let i = 0; i < num; i++) {
    adjazenz.push(new Array(num));
  }

  let triangle = num * (num - 1) / 2;
  for (let bin = 0; bin < Math.pow(2, triangle); bin++) {
    let val = bin.toString(2).padStart(triangle, '0');
    let index = 0;

    for (let i = 0; i < num; i++) {

      adjazenz[i][i] = '-';

      for (let j = 0; j < i; j++) {

        adjazenz[i][j] = val[index];
        adjazenz[j][i] = val[index++];

      }

    }

    // Remove graphs with nodes of degree != 3

    if (adjazenz.some((row) => row.reduce((acc, elt) => acc + ((elt == '1') ? 1 : 0), 0) != 3)) {
      continue;
    }

    // Find hamiltonian clycles

    let ham = new Hamilton(adjazenz);
    let result = ham.hamCycle()
    if (result != '') console.log(result);


    // Output of the brutes:

    // let str = '';
    // for (let row of adjazenz) {
    //   str += row.join(' ') + '\n';
    // }

    // console.log(str);

  }

}
