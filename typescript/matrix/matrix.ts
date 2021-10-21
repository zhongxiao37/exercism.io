export class Matrix {
  matrix: number[][];
  constructor(message: string) {
    this.matrix = message
      .split("\n")
      .map((x) => x.split(" ").map((y) => parseInt(y)));
  }

  get rows(): number[][] {
    return this.matrix;
  }

  get columns(): number[][] {
    let columns: number[][] = [];

    if (this.matrix.length > 0) {
      for (let i = 0; i < this.matrix.length; i++) {
        for (let j = 0; j < this.matrix[i].length; j++) {
          if (i === 0) {
            columns[j] = [];
          }
          columns[j].push(this.matrix[i][j]);
        }
      }
    }
    return columns;
  }
}
