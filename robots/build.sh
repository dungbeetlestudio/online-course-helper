cp *.py pack/
cd pack
pyinstaller gathercontrol.py -y 
#pyinstaller taskcontrol.py -i favicon_old.ico -y
cd dist
cp gathercontrol/gathercontrol.exe ./