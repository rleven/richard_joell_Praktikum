all: build/main.pdf

# hier Python-Skripte:
build/plot.pdf: plot.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python plot.py

build/80Cplot.pdf: tabellen3.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python tabellen3.py

build/plot1.pdf, build/plot2.pdf, build/plot3.pdf: tabellen1.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python tabellen1.py

build/plot4.pdf, build/plot5.pdf: tabellen2.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python tabellen2.py
# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: build/plot.pdf build/80Cplot.pdf build/plot1.pdf build/plot2.pdf build/plot3.pdf build/plot4.pdf build/plot5.pdf

build/main.pdf: FORCE | build
	  TEXINPUTS=build: \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	main.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
