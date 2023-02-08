import re

extName = re.compile(r"\.(?=[^\.]+$).+$")

def getExtName(s:str):
  return re.search(extName,s).group()