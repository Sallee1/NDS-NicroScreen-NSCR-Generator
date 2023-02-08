from copy import deepcopy

def returnCopy(fun):
  """
  @returnCopy
  该装饰器强制使函数返回对象的副本
  """
  def wrapper(*args,**kwargs):
    ret = fun(*args,**kwargs)
    if(type(ret) in [int,str,tuple]):   # 基本类型，不处理
      return ret
    return deepcopy(ret)        # 其他类型，返回副本
  
  return wrapper