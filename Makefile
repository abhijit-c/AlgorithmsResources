name=texResult
PLatFlags= -jobname=$(name) --shell-escape

default:
	make build
	make build
	make clean

build:
	pdflatex $(PLatFlags) main.tex

clean:
	rm $(name).log $(name).aux
	rm -rf _minted-*
