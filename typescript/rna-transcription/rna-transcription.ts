export const MAPPING: { [index: string]: string } = {
  A: "U",
  T: "A",
  C: "G",
  G: "C",
};

export function toRna(input: string) {
  const inputList = [...input];
  const keys = Object.keys(MAPPING);
  const valid = inputList.every((x) => {
    return keys.includes(x);
  });
  if (valid) {
    return inputList.map((x) => MAPPING[x]).join("");
  } else {
    throw new Error("Invalid input DNA.");
  }
}
