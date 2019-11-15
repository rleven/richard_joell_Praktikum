all: build/Ausgleichsgerade.pdf build/hook.pdf

build/Ausgleichsgerade.pdf: hook.py | build
	python hook.py

build/hook.pdf: hook.tex | build
	lualatex --output-directory=build --interaction=batchmode --halt-on-error hook.tex
	lualatex --output-directory=build --interaction=batchmode --halt-on-error hook.tex

build:
	mkdir -p build

clean:
	rm -rf build

.PHONY: all clean