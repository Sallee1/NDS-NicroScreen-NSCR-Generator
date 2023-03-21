
import Utils.regex as regex
from customException.ex import FileTypeError


def checkFileType(type:str):
  """
  @checkFileType(type)
  该装饰器将比较输入的文件格式是否与参数一致，否则raise FileTypeError\n
  该装饰器只能用做类的成员函数\n
  文件名需要作为函数的第一个参数\n
  """
  def decorator(fun):
    def wrapper(self,fileName,*args,**kwargs):
      extType = regex.getExtName(fileName).lower()
      if(extType != type):
        raise FileTypeError(f"所需要的格式为{type},但实际打开的是{extType}")
      return fun(self,fileName,*args,**kwargs)
    return wrapper
  return decorator