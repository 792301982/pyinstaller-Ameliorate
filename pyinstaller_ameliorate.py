import  os,sys
import shutil
import time

pyFilename=sys.argv[1]
pyFileBasename=os.path.basename(pyFilename)
exeFilename=sys.argv[2]
r=os.popen("pyinstaller -F %s"%pyFilename)
if(r.close()!=None):
    input("pyinstaller出错")
    sys.exit()
versionTime=time.strftime('%y%m%d%H%M%S',time.localtime(time.time()))
shutil.move("./dist/%s.exe"%(pyFileBasename.split('.')[0]),"./%sv%s.exe"%(exeFilename,versionTime))
shutil.rmtree("./build")
shutil.rmtree("./dist")
os.remove("%s.spec"%pyFileBasename.split('.')[0])