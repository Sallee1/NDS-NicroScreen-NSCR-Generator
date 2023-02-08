# NDS游戏命名表生成器

针对CrystalTile2的命名表编辑器导入图片（特别是4bpp的图片）经常出现BUG，这里打算自己写一个命名表编辑器

## 实现原理

1. 将图像分为8x8小块
2. 根据选择的评估指标，使用合适的色板优化图像
3. 检查散列表里是否存在相同的小块或者小块的镜像
4. 排序散列表生成NCGR，根据NCGR的顺序生成NSCR