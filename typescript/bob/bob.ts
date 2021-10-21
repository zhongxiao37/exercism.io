export function hey(message: string): string {
  const responseList: string[] = [
    "Whoa, chill out!",
    "Sure.",
    "Fine. Be that way!",
    "Whatever.",
    "Calm down, I know what I'm doing!",
  ];
  message = message.trim().split("\n").join(" ");
  const characters = message.match(/[a-zA-Z]+/);
  const numbers = message.match(/\d/);
  if (
    (characters === null && numbers === null) ||
    (message && message.length === 0)
  ) {
    return responseList[2];
  } else if (
    characters &&
    characters.length !== 0 &&
    characters.every((x) => isNaN(parseInt(x)) && x === x.toLocaleUpperCase())
  ) {
    if (message.match(/.*\?$/m)) {
      return responseList[4];
    } else {
      return responseList[0];
    }
  } else if (message.match(/.*\?$/m)) {
    return responseList[1];
  }
  return responseList[3];
}
