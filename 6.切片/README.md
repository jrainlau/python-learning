# 1、对List进行切片
类比于js的`.slice()`方法

在python中要对List进行切片，使用`[begin:end:interval]`即可。
- `begin`：起始下标，为0时可省略
- `end`：终止下标，省略时为为末尾下标（切片时不包括该下标）
- `interval`：间隔，即为隔多少个元素切片一个

```
L = range(1, 101)

print L[:10]  # 前10个数
print L[2::3]  # 3的倍数
print L[4:50:5]  # 不大于50的5的倍数
```