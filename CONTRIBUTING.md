# Contributing

Corrections are the contribution this repository wants most, especially to
the rows marked rough or with no clean equivalent. Open an issue naming
the row and what the boundary difference actually is, or send a pull
request that edits `mapping.csv` only: the README table is generated from
it, and the check refuses a change where the two disagree.

```bash
python3 scripts/render_table.py --check
```

Run that before pushing; the pipeline runs it again. Keep the Azure column
to the closest comparable rather than an equivalent, and say "rough" when
the shape matches but the boundary does not.

By contributing you agree your work is licensed under CC BY 4.0.
