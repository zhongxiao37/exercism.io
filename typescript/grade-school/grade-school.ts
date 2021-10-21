export class GradeSchool {
  _roster: {
    [index: number]: string[];
  };

  constructor() {
    this._roster = {};
  }

  roster() {
    let roster: { [index: number]: string[] } = {};
    for (const i in this._roster) {
      roster[i] = [...this._roster[i]];
    }
    return roster;
  }

  add(name: string, grade: number): void {
    if (!this._roster[grade]) this._roster[grade] = [];
    for (const i in this._roster) {
      let idx = this._roster[i].indexOf(name);
      if (idx !== -1) this._roster[i].splice(idx, 1);
    }
    this._roster[grade].push(name);
    this._roster[grade].sort();
  }

  grade(grade: number) {
    if (this._roster[grade]) {
      return [...this._roster[grade]];
    } else {
      return [];
    }
  }
}
