#!/usr/bin/env python3

import sys
from collections import Counter


def main() -> int:
    if len(sys.argv) != 3:
        sys.stderr.write("Usage: analyse.py <LEVEL> <path-to-log-file>\n")
        return 1

    level, path = sys.argv[1], sys.argv[2]

    counts: Counter = Counter()

    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.rstrip("\n")

                if not line.strip():
                    continue

                parts = line.split(" ", 3)

                if len(parts) < 4:
                    continue

                _timestamp, service, lvl, _message = parts

                if lvl != level:
                    continue

                counts[service] += 1
    except OSError as e:
        sys.stderr.write(f"Error reading file '{path}': {e}\n")
        return 1

    for service, count in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])):
        print(f"{service}: {count}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
