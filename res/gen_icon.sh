#!/bin/bash
set -euo pipefail

SRC="icon.png"
if [ ! -f "$SRC" ]; then
  echo "Missing $SRC in $(pwd)"
  exit 1
fi

for size in 16 32 48 64 128 256 512 1024; do
    convert "$SRC" -resize "${size}x${size}" "${size}.png"
done

# Windows icon bundle
convert 16.png 32.png 48.png 64.png 128.png 256.png -colors 256 icon.ico

# Common named assets used by packaging
cp -f 32.png 32x32.png
cp -f 64.png 64x64.png
cp -f 128.png 128x128.png
cp -f 256.png 128x128@2x.png
