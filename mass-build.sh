echo "\033[1mDiPS CodeJam 2022 - Mass Build Files[0m"
echo "\033[1m-------------------------------------------------\033[0m"
for d in */ ; do
     echo "\033[1mBuilding $d\033[0m"
     cd "$d"
     sh build.sh
     cd ..
done
echo "\033[1m-------------------------------------------------\033[0m"
echo "\033[1mFinished building files.\033[0m"