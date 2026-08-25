"""Render the mapping table in README.md from mapping.csv.

The CSV is the source. The README table is generated from it and lives
between two markers, so the two cannot drift: `--check` reproduces the
table and compares, and the pipeline runs that. Any edit belongs in the
CSV, and running this without a flag rewrites the README section.
"""

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = ROOT / "mapping.csv"
README = ROOT / "README.md"
BEGIN = "<!-- BEGIN MAPPING TABLE: generated from mapping.csv -->"
END = "<!-- END MAPPING TABLE -->"


def read_rows() -> tuple[list[str], list[list[str]]]:
    with CSV_PATH.open(newline="") as handle:
        rows = list(csv.reader(handle))
    header, body = rows[0], rows[1:]
    body.sort(key=lambda row: row[0].lower())
    return header, body


def escape(cell: str) -> str:
    # A pipe inside a cell would end the column early in Markdown.
    return cell.replace("|", "\\|")


def render() -> str:
    header, body = read_rows()
    lines = [
        "| " + " | ".join(header) + " |",
        "|" + "|".join(["---"] * len(header)) + "|",
    ]
    for row in body:
        lines.append("| " + " | ".join(escape(cell) for cell in row) + " |")
    return "\n".join(lines)


def splice(text: str, table: str) -> str:
    start = text.index(BEGIN) + len(BEGIN)
    stop = text.index(END)
    return text[:start] + "\n\n" + table + "\n\n" + text[stop:]


def main() -> int:
    text = README.read_text()
    if BEGIN not in text or END not in text:
        print("README is missing the table markers", file=sys.stderr)
        return 1
    updated = splice(text, render())
    if "--check" in sys.argv:
        if updated != text:
            print(
                "README table does not match mapping.csv; "
                "run scripts/render_table.py to regenerate it",
                file=sys.stderr,
            )
            return 1
        _, body = read_rows()
        print(f"table matches mapping.csv, {len(body)} entries")
        return 0
    README.write_text(updated)
    _, body = read_rows()
    print(f"README table written, {len(body)} entries")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
