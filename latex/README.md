# Overleaf Setup

This folder contains an Overleaf-ready LaTeX manuscript generated from:

- `papers/the-critical-line-perfect-closure.md`

## Files

- `main.tex` — manuscript source
- `references.bib` — bibliography database

## Upload Instructions (Overleaf)

1. Create a new Overleaf project.
2. Upload `main.tex` and `references.bib` from this `latex/` folder.
3. Set the compiler to **pdfLaTeX** or **LuaLaTeX**.
4. Build the project.

## Bibliography Notes

This manuscript uses `biblatex` with `biber`.

- If references do not appear, make sure Overleaf is running **Biber** in project settings.
- If your environment does not support `biber`, switch to a BibTeX-based template as needed.
