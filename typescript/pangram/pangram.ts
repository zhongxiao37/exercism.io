export function isPangram(setence: string): boolean {
  const regex = /[a-zA-Z]/g;
  const matched_chars = setence.match(regex);
  if (matched_chars) {
    return (
      Array.from(
        matched_chars
          .reduce(
            (acc, e) =>
              acc.set(
                e.toLocaleLowerCase(),
                (acc.get(e.toLocaleLowerCase()) || 0) + 1
              ),
            new Map()
          )
          .keys()
      ).length === 26
    );
  }
  return false;
}
