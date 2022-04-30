[TOC]



# exam（spring2022）

## midterm 1

### Q1(7'). Python 解释器显示什么？（WWPD）

```python
def dipping(dots):
    if print("you dip"):
        return print("i dip")
    else:
        return print(dots) or dots or print("we dip")
```

(a)  （2‘）

| >>> dipping(0) |
| -------------- |
|                |

(b) （2’）

| \>>> dipping(555) |
| ----------------- |
|                   |

（c）（1‘）

dipping(0) 的返回值是？

```

```

（d）（1’）

dipping(-666) 的返回值是？

```

```

（e）（1‘）

重写 dipping 函数的函数体，用一行代码实现。

```
def dipping(dots):
	____________________
```

### Q2. Ring My Bell Tower

代码如下：

```python
floor = 30

def bell(tower, ring):
    ring += tower(ring)(floor)
    def tower(steps):
        return lambda steps: floor + steps
    return tower(ring+1)

my = bell(lambda x: lambda y: x * y, floor)
my(38)
```

最终状态的环境图如下：

![image-20220429111738877](https://cnchen2000.oss-cn-shanghai.aliyuncs.com/img/image-20220429111738877.png)

（a）（1’）填空（a）

```

```

（b）（1’）填空（b）

```

```

（c）（1’）填空（c）

```

```

（d）（1’）填空（d）

```

```

（e）（1’）填空（e）

```

```

（f）（1’）填空（f）

```

```

（g）（1’）填空（g）

```

```

（h）（1’）填空（h）

```

```

Q3.  （6`）Doctor Octalpus, Reborn

数字转换：八进制 ---> 十进制

例如： 八进制的 123，可以展开为 (1 * 64) + (2 * 8) + (3 * 1)，结果为十进制的 83。如下图所示：

![image-20220429112356246](https://cnchen2000.oss-cn-shanghai.aliyuncs.com/img/image-20220429112356246.png)

实现函数 `convert_to_decimal`，该函数接受一个八进制数，返回其对应的十进制，八进制数总是以非零数位开头，并且总是正的。

```
def convert_to_decimal(octal):
	"""
	>>> convert_to_decimal(3) # (8^0 * 3)
	3
	>>> convert_to_decimal(23) # (8^1 * 2) + (8^0 * 3)
	19
	>>> convert_to_decimal(123) # (8^2 * 1) + (8^1 * 2) + (8^0 * 3)
	83
	"""
	decimal = 0
	curr_place = ___(a)______
	____(b)_____:     
		curr_digit = ____(c)_____
		decimal = ____(d)_____
		curr_place = ____(e)_____
		octal = ____(f)_____
	return decimal
```

（a）（1’）填空（a）

```

```

（b）（1’）填空（b）

```

```

（c）（1’）填空（c）

```

```

（d）（1’）填空（d）

```

```

（e）（1’）填空（e）

```

```

（f）（1’）填空（f）

```

```

（g）（1’）填空（g）

```

```

（h）（1’）填空（h）

```

```

### Q4. （6‘）Forbidden Digits

实现高阶函数 `forbid_digit`，该函数接受2个参数：一个函数 `f` 和 一个数位 forbidden，返回另一个函数。如果返回的函数所传递的数中的个位等于 数位 `forbidden` ，则返回去掉个位的数所调用给定函数的结果，否则，返回这个数所调用给定函数的结果。

```python
def forbid_digit(f, forbidden):
	"""
	>>> g = forbid_digit(lambda y: 200 // (y % 10), 0)
	>>> g(11)
	200
	>>> g(10)
	200
	>>> g = forbid_digit(lambda x: f'{x}a', 6)
	>>> g(61)
	'61a'
	>>> g(66)
	'6a'
	>>> g = forbid_digit(g, 3)
	>>> g(43)
	'4a'
	>>> g(63)
	'0a'
	>>> g(44)
	'44a'
	"""
	def forbid_wrapper(n):
		if ___(a)_____:
			____(b)____
		else:
			___(c)_____
	___(d)_____
```

（a）（1’）填空（a）

```

```

（b）（1’）填空（b）

```

```

（c）（1’）填空（c）

```

```

（d）（1’）填空（d）

```

```

（e）（2’）重写 forbid_digit 函数用一行代码实现

```python
def forbid_digit(f, forbidden):
	____________________
```

