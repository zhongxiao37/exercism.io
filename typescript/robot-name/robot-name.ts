export class Robot {
  name: string;
  static availableNames: string[];

  constructor() {
    this.name = Robot.generateName();
  }

  public resetName(): void {
    this.name = Robot.generateName();
  }

  public static releaseNames(): void {
    Robot.availableNames = [];
  }

  public static generateName(): string {
    if (
      Robot.availableNames === undefined ||
      Robot.availableNames.length === 0
    ) {
      Robot.availableNames = [];
      let letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".split("");
      let numbers = "0123456789".split("");
      for (const a of letters) {
        for (const b of letters) {
          for (const x of numbers) {
            for (const y of numbers) {
              for (const z of numbers) {
                Robot.availableNames.push([a, b, x, y, z].join(""));
              }
            }
          }
        }
      }
      // shuffle the array list
      for (let i = Robot.availableNames.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [Robot.availableNames[i], Robot.availableNames[j]] = [
          Robot.availableNames[j],
          Robot.availableNames[i],
        ];
      }
    }

    return Robot.availableNames.pop() as string;
  }
}
