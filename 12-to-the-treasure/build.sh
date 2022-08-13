echo "\033[1mStarting pdfLaTeX...\033[0m"
pdflatex --file-line-error --synctex=1 "problem.tex"

echo
echo "\033[1mRemoving AUX files...\033[0m"
rm problem.aux
rm problem.log
rm problem.synctex.gz

echo
echo "\033[1mDone.\033[0m"