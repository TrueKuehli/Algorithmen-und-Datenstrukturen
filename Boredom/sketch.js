var width = 800;
var height = 600;
let graph;
let zsg;
let vNum = 10;
let chance = 0.25;
let borders = 50;
let frame = 0;

function setup() {
  width = document.documentElement.clientWidth;
  height = document.documentElement.clientHeight;
  vNum = parseInt(prompt('Wie viele Knoten?', '10')) || 10;
  chance = parseFloat(prompt('Wahrscheinlichkeit für Verbindung?', '0.25')) || 0.25;
  console.log(chance);
  createCanvas(width, height);
  graph = new Graph();
  graph.genRandom(vNum);
  zsg = new Zusammenhang(graph, 0);
  background(0);
  zsg.draw();
}

function draw() {
  frame++;
  if (frame == 90) {
    background(0);
    zsg.doStep();
    frame = 0;
  }
}

class Vertex {
  constructor(x, y) {
    this.x = x;
    this.y = y;
    this.edges = [];
  }

  addEdge(edge) {
    this.edges.push(edge);
  }

  draw() {
    stroke(255);
    strokeWeight(5);
    point(this.x, this.y);
  }
}

class Edge {
  constructor(v1, v2) {
    this.vertices = [v1, v2];
    v1.addEdge(this);
    v2.addEdge(this);
  }

  draw() {
    stroke(255);
    strokeWeight(1);
    line(this.vertices[0].x, this.vertices[0].y,
         this.vertices[1].x, this.vertices[1].y);
  }
}

class Zusammenhang {
  constructor(graph, beginAt) {
    this.g = graph;
    this.yellow = [this.g.vertices[beginAt]];
    this.red = [this.g.vertices[beginAt]];
    this.edges = [];
    this.gZsg = new Graph();
  }

  doStep() {
    let current = this.red[0];
    if (current !== undefined) {
      let didSomething = false;
      outer:
      for (let edge of current.edges) {
        for (let vertex of edge.vertices) {
          if (vertex == current) continue;

          if (!this.yellow.includes(vertex)) {
            didSomething = true;
            this.edges.push(edge);
            this.yellow.push(vertex);
            this.red.push(vertex);
            break outer;
          }
        }
      }
      if (!didSomething) this.red.splice(0, 1);
    }

    this.draw();
  }

  draw() {
    this.g.draw();
    for (let v of this.red) {
      stroke(255, 0, 0);
      strokeWeight(30);
      point(v.x, v.y);
    }

    for (let v of this.yellow) {
      stroke(255, 255, 0);
      strokeWeight(15);
      point(v.x, v.y)
    }

    for (let e of this.edges) {
      let v = e.vertices[0];
      let v2 = e.vertices[1];
      stroke(255, 255, 0);
      strokeWeight(4);
      line(v2.x, v2.y, v.x, v.y);
    }
  }
}

class Graph {
  constructor() {
    this.vertices = [];
    this.edges = [];
  }

  example() {
    this.vertices.push(new Vertex(200, 100));
    this.vertices.push(new Vertex(250, 150));
    this.vertices.push(new Vertex(50, 300));

    this.edges.push(new Edge(this.vertices[0], this.vertices[1]));
    this.edges.push(new Edge(this.vertices[0], this.vertices[2]));
  }

  genRandom(n) {
    for (let i = 0; i < n; i++) {
      this.vertices.push(new Vertex(borders + Math.random() * (width - borders*2), borders + Math.random() * (height - borders*2)));
    }

    for (let i = 0; i < this.vertices.length; i++) {
      for (let j = i + 1; j < this.vertices.length; j++) {
        if (Math.random() < chance) {
          this.edges.push(new Edge(this.vertices[i], this.vertices[j]));
        }
      }
    }
  }

  draw() {
    for (let v of this.vertices) {
      v.draw();
    }

    for (let e of this.edges) {
      e.draw();
    }
  }
}
