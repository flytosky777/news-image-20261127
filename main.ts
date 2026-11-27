// Entry program for the make.fun news-image-20261127 bounty.
// It ships the finished front page (entry.png, drawn by
// build_frontpage.py) to the grader's output directory, unchanged.
// The copy is byte for byte, so repeated runs agree exactly.
//
// Node 22, standard library only. Try it locally with:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
import { copyFile, mkdir, readFile, stat } from "node:fs/promises";
import { createHash } from "node:crypto";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const MAX_BYTES = 1048576;
const MAX_SIDE = 1024;

const PNG_SIG = Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]);
const JPEG_SIG = Buffer.from([0xff, 0xd8, 0xff]);

function fail(message) {
  throw new Error(message);
}

async function main() {
  const here = dirname(fileURLToPath(import.meta.url));
  const src = join(here, "entry.png");
  const dir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
  const dest = join(dir, "entry.png");

  const meta = await stat(src);
  if (meta.size > MAX_BYTES) {
    fail(`entry.png is ${meta.size} bytes, above the ${MAX_BYTES} byte limit`);
  }
  const data = await readFile(src);
  const png = data.subarray(0, 8).equals(PNG_SIG);
  const jpeg = data.subarray(0, 3).equals(JPEG_SIG);
  if (!png && !jpeg) {
    fail("entry.png is neither a PNG nor a JPEG");
  }
  if (png) {
    // In a PNG the IHDR chunk stores width and height as big-endian
    // uint32 values at offsets 16 and 20.
    const width = data.readUInt32BE(16);
    const height = data.readUInt32BE(20);
    if (width > MAX_SIDE || height > MAX_SIDE) {
      fail(`entry.png is ${width}x${height}, above the ${MAX_SIDE}x${MAX_SIDE} cap`);
    }
  }
  await mkdir(dir, { recursive: true });
  await copyFile(src, dest);
  const copied = await readFile(dest);
  if (copied.length !== meta.size) {
    fail(`copied ${copied.length} bytes, expected ${meta.size}`);
  }
  const sha = createHash("sha256").update(copied).digest("hex");
  console.log(`wrote ${dest} (${meta.size} bytes) sha256 ${sha}`);
}

await main();
