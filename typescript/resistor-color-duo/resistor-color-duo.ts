const mapping: {
  [index: string]: number;
} = {
  black: 0,
  brown: 1,
  red: 2,
  orange: 3,
  yellow: 4,
  green: 5,
  blue: 6,
  violet: 7,
  grey: 8,
  white: 9,
};

export function decodedValue(colors: string[]) {
  return Number(
    colors
      .slice(0, 2)
      .map((x) => mapping[x])
      .join("")
  );
}
