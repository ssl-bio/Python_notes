# Notes on Python


## Description

Basic notes on Python


### Python crash course

Exercises from 'Python crash course: A hands-on, project-based introduction to programming' by <a href="#citeproc_bib_item_1">Matthes 2019</a>

Exercises are written in plain text (`*.py`) and in Emacs's org-mode (`*.org`). The latter include exercises' instructions and it is meant to be exported as `LaTeX` file (`*.tex`) which can then, be used to produce a `pdf` file.


### Exporting `tex` file and producing a `pdf` document

To convert the `*.org` file into `LaTeX` format it should be open in Emacs, where the following key-combination is entered, `C-c C-e l l`. The `C-<letter>` indicates that the `Ctrl` key should be pressed along with a letter; after that the options to export as a latex file are selected with the last two keys (`l` pressed twice).

Later, a pdf file is produced with `XeLaTex` with the `--shell-escape` option

```bash
# Example for Ch-3-ex.tex
xelatex --shell-escape Ch-3-ex.tex
```

To change the colors used to highlight the code change the following lines in the file `latex_conf.org`

```
#+LATEX_HEADER: \usemintedstyle{pastie} 
#+LATEX_HEADER: \setminted[python]{fontsize=\footnotesize, linenos, baselinestretch=1.2, framesep=2mm, frame=lines}
```

The first line changes the colors (other options can be found elsewhere, *e.g.* [Overleaf](https://www.overleaf.com/learn/latex/Code_Highlighting_with_minted#Colours_and_stylesheets)). On the second line the specification for the background color (`bgcolor=darkgray`) was removed resulting in a white color.


# References

  <div class="csl-entry"><a id="citeproc_bib_item_1"></a>Matthes, Eric. 2019. <i>Python Crash Course: A Hands-on, Project-Based Introduction to Programming</i>. 2nd edition. San Francisco, CA: No Starch Press.</div>
</div>
