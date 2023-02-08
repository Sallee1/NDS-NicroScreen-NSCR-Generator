class FileTypeError(TypeError):
  def __init__(self, needType, realType) -> None:
    print(f"文件类型错误，所需的类型为\"{needType}\",实际是\"{realType}\"")