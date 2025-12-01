import "dotenv/config";
async function getInput(dayNumber: number): Promise<string[]> {
  const request = await fetch(
    `https://adventofcode.com/2025/day/${dayNumber}/input`,
    {
      headers: {
        cookie: `session=${process.env.SESSION_ID}`,
        "Content-Type": "text/plain",
      },
    },
  );
  const data = await request.text();
  console.log(data);
  return [];
}

export default getInput();
