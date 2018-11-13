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

  hamPathUtil(path, pos) {
    if (pos == this.v) {
      return true;
    }

    for (let v = 0; v < this.v; v++) {
      if (this.isSafe(v, pos, path)) {
        path[pos] = v;

        if (this.hamPathUtil(path, pos + 1)) return true;

        path[pos] = null;
      }
    }

    return false;
  }

  hamPath() {
    for (let i = 0; i < this.v; i++) {
      let path = (new Array(this.v)).fill(null);
      path[0] = i;

      if (this.hamPathUtil(path, 1)) {
        let solution = '';
        // solution = 'Solution found: \n';
        // for (let vertex of path) {
        //   solution += vertex + ', ';
        // }

        // solution += '\nfor Graph: \n';
        // for (let row of this.g) {
        //   solution += row.join(' ') + '\n';
        // }
        return solution;
      }
    }
    let solution = 'Solution does not exist for Graph: \n';

    for (let row of this.g) {
      solution += row.join(' ') + '\n';
    }

    return solution;
  }
}

let numOfNodes = 5;

for (let num = 1; num <= numOfNodes; num++) {
  // Generate a whole f*ckton of graphs

  let adjazenz = [];

  for (let i = 0; i < num; i++) {
    adjazenz.push(new Array(num));
  }

  let triangle = num * (num - 1) / 2;
  outer:
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

    // Remove graphs with nodes of even degree => These have a euler cycle
    // Remove graphs with some number other than two nodes of uneven degree => These don't have a euler path
    let numUneven = 0;
    for (row of adjazenz) {
      let vertex = row.reduce((acc, elt) => acc + ((elt == '1') ? 1 : 0), 0);
      if (vertex == 0) continue outer;
      if (vertex & 1) numUneven++;
    }

    if (numUneven == 0) continue;
    if (numUneven != 2) continue;



    // Find hamiltonian paths

    let ham = new Hamilton(adjazenz);
    let result = ham.hamPath();
    if (result != '') console.log(result);


    // Output of the brutes:

    // let str = '';
    // for (let row of adjazenz) {
    //   str += row.join(' ') + '\n';
    // }

    // console.log(str);

  }

}
