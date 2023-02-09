import Exception.Exceptions as ex
import Utils.regex as regex


def checkNoneReturn(fun):
  """
  @checkFileType
  该装饰器强制要求函数需要有返回值，否则raise None Return Error\n
  适用于以None代表异常的模块（如OpenCV）
  """
  def wrapper(*args,**kwargs):
    ret = fun(*args,**kwargs)
    if(ret is None): raise ex.NoneReturnError()
    return ret
  return wrapper