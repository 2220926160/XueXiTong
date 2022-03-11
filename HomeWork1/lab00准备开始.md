# lab0 准备开始

> **练习完成方式：独立完成**

[TOC]

## 概述

### 提供的材料

下载 [hw01.zip](./hw00.zip) ，解压到某个文件夹下面，你会发现这次实验的问题，以及Ok程序。

## 介绍

这个实验解释了如何使用你的计算机来完成课程作业并介绍了一些Python的基础知识。实验说明虽然看上去比较长，但主要是学会如何使用基础工具，这些现在看起来可能有点困难，但随着课程的开展很快就会变得习惯。

## 安装

### 安装一个终端

程序的终端允许你通过输入命令和你的计算机互动。不论你使用的是什么操作系统（Windows, macOS, Linux），终端将是本课程的一个重要工具。

#### macOS/Linux

如果你的是苹果电脑或者使用的是Linux（比如 Ubuntu）,那么你已经有了一个称为终端（`Terminal`）的程序，打开就可以开始了。

#### Windows

在Windows上获得终端的最简单的方法是使用 **WSL**（Windows Subsystem for Linux），并安装一个在你的Windows计算机上模拟 Ubuntu 操作系统的终端程序 `Ubuntu` ，这样本课程的任务都可以比较舒心的在你的设备上进行。

要在Windows上安装 `Ubuntu` ，打开 Powershell，右键单击以管理员身份运行，然后键入 `wsl --install` 并回车，注意命令的顺序。这样应该会自动完成安装过程（按照屏幕上给你的指示做）

下一步，在 Windows 应用商店（Windows store）中下载  ubuntu。 一旦安装完成，你就可以搜索到 Ubuntu 了，第一次运行可能需要花几分钟，以后的启动会很快。

### 安装 Python3

Python3是本课程使用的编程语言，使用下面的指令安装Python 3（指令里面可能包括的是旧版本的Python 3，但是按照步骤类似。）

**注意**：如果已经有个旧版本的Python，请确保下载和安装Python 3.9 及以上的版本，使用  `python3 --version` 查看你的 Python 版本。

#### macOS

下载和安装 [Python 3（64-bit)](https://www.python.org/ftp/python/3.9.6/python-3.9.6-macosx10.9.pkg) 。你可能需要右键单击下载图标并选择 “打开” 。安装后，关闭并重新打开 Terminal。

如果你安装了 Homebrew，也可以运行 `brew install python3` 来安装 Python3。

#### Windows

在Ubuntu中键入 `sudo apt install python3` 并敲击 `enter` 来安装Python。一旦完成安装，就可以敲入`python3 --version` 来测试是否正确安装，你应该可以看到响应的一个显示版本的信息 `Python 3.9.6`

#### Linux

运行 `sudo apt install python3` （Ubuntu）， `sudo pacman -S python3` （Arch），或者你的Linux发行版的命令。

#### 其他

从[Python下载页](https://www.python.org/downloads/)下载安装。

### 安装文本编辑器

刚刚安装的 **Python 解释器** 让你可以运行 python 代码，你也需要一个文本编辑器来编写Python 代码。

[Visual Studio Code（VS Code）](https://code.visualstudio.com/)  是最流行的选择之一。如果你使用的是 Windows，并安装上面的过程安装了Python， VS Code 会最适合你（由于WSL的支持）。安装了 VS Code 后， 安装 [Remote Development extension pack](https://aka.ms/vscode-remote/download/extension) 插件包。然后，你可以使用 VS Code 文档中 [这一节](https://code.visualstudio.com/docs/remote/wsl#_open-a-remote-folder-or-workspace) 来在VS Code 中打开 WSL 文件夹。

 **本课程高度推荐使用 VS Code**。

更多的使用指南请参考：

- [Visual Studio Code](https://cs61a.org/articles/vscode)
- [PyCharm](https://www.jetbrains.com/pycharm/)

### 结对编程

在本课程，你可能需要和其他人合作完成实验和项目，可以使用  [VS Code](https://cs61a.org/articles/vscode#pair-programming) 的结对编程插件。

测试一个特定的问题 `python3 ok --local -q ### Q1` 测试所有问题 `python3 ok --local`  显示所有测试 `python3 ok --local -v` 

## 使用终端

让我们检查一切是否安装就绪！

首先，打开一个终端（terminal）窗口

![image-20220308211542353](https://cnchen2000.oss-cn-shanghai.aliyuncs.com/img/image-20220308211542353.png)

当你第一次打开终端时，你会从"home directory"开始。**home directory** 用符号 `~` 表示，可能你在提示符上看到了。

> 不要担心你的终端窗口看上去不太一样，重要的是提示符显示 `$`（指示 Bash）或者 `% `（指示 zsh）

试着运行 `echo "$HOME"` 命令应该会显示你的home directory的完整路径 PATH，看上去像这样 `/Users/OskiBear`  PATH就像地址一样，高速你一个文件夹的完整路径。

访问文件和目录（文件夹）有两种方式，浏览技术不同，文件是一样的：

- 使用终端（**c**ommand **l**ine **i**nterface， CLI）
- 使用访达（Mac）/资源管理器（Windows）（**g**raphics **u**ser **i**nterface， GUI)）

![GUI folder example](https://cs61a.org/lab/lab00/assets/finder-path-example.png)

![CLI folder exmaple](https://cs61a.org/lab/lab00/assets/terminal-path-example.png)

注意黄色方框显示的是路径，紫色椭圆显示的是 ‘labs’ 文件夹

### Python解释器

可以使用终端来检查 Python 3 解释器是否正确安装，试试下面的命令：

```
python3
```

如果安装成功，应该可以看到一些关于解释器的文本，后面会有单独一行的 `>>>` ，这里你可以敲入 Python 代码，试着敲入课程中讲的一些表达式或者其他内容。你可以敲入 `exit()` 或者 `Ctrl-D` 来返回命令行。

终端 vs Python 解释器

思考一下终端和Python 解释器的区别

![image-20220308224601283](https://cnchen2000.oss-cn-shanghai.aliyuncs.com/img/image-20220308224601283.png)



1. A，B，C，D中哪些是终端？
2. 哪个是Python解释器？
3. 哪个是代码编辑器？

A 和 D 是终端，你可以运行 bash 命令，如 `cd` 和 `ls` 。D是VS Code 内置的终端。

B是Python解释器，因为 >>> 提示符表示你已经开始了一个Python解释器。也是因为可以看到你使用了 `python3` 命令，该命令会运行一个 python解释器。如果你在python解释器中敲入bash命令，可能会得到一个语法错误。

![interpreter syntax error](https://cs61a.org/lab/lab00/assets/interpreter-syntax-error.png)

如果你要退出python解释器，敲入 `exit()` 或者 `Ctrl-D`

C是文本编辑器，在这里编写代码，然后通过终端执行。

## 组织你的文件

这一小节讲学习如何通过终端命令管理你的文件

> 确保你的提示符是 `$`，而不是 `>>>` 。如果是 `>>>` 说明你还处在Python shell 中，你需要退出。

终端中常用的基础命令：

- `ls`: **l**i**s**ts all files in the current directory 列出当前目录下的所有文件
- `cd <path to directory>`: **c**hange into the specified **d**irectory 改变到某个目录
- `mkdir <directory name>`: **m**a**k**e a new **dir**ectory with the given name 创建一个给定名的新目录
- `mv <source path> <destination path>`: **m**o**v**e the file at the given source to the given destination 将文件从source 移动到 destination

## Python基础

### 表达式和语句

程序由表达式和语句构成。 表达式（expression）是一小片代码，计算出某些值。语句是一行或者多行代码使程序中发生点什么。

当你在Python解释器交互地输入一个表达式时，会显示其值。

现在让我们看看这个实验中你需要完成的内容

### Primitive expressions

primitive expressions只需要一步就算出来，这包括数字，布尔，计算就是它们自身：

```python
>>> 3
3
>>> 12.5
12.5
>>> True
True
```

### 算术表达式

数字可能结合数学运算符来构成复合表达式，除了 加 ，减，乘，乘方 `+ - * **` 外，还有：带小数除 `/`，整数除 `//` ，取模`%` 求余数。可以使用小括号分组不同的子表达式。

### 字符串

字符串可以包括一个或者多个字符，使用单引号 `''` 或者双引号 `""` 括起来。字符串和  Primitive expression 还是有点区别的，不过在作业中一样的看待，后面的课程会继续字符串

```
>>> "hello"       # Both single and double quotes work!
'hello'
>>> 'world!'
'world'
```

### 赋值语句

赋值语句由 名（name）和 表达式（expression）组成。它通过计算符号 `=` 右侧的表达式并将其值*绑定*到左侧的名称来更改程序的状态。

```
>>> a = (100 + 50) // 2
```

现在，如果我们计算 `a` ，解释器将显示值 75

```
>>> a
75
```

## 做实验

> 当做作业或者实验时，请确保你的终端的工作目录时正确的（应该是你解压的开始代码目录）
>
> 推荐使用**VS Code**打开解压文件夹

### 1. What Would Python Do? (WWPD) 

实验和作业的一部分练习是预测Python解释器的行为（WWPD， Python会怎么做）。

> 在终端输入下面命令来开始这个环节：
>
> ```
> python3 ok -q python-basics -u
> ```
>
> 你将被提示输入各种语句/表达式的输出，必须正确输入它们才能继续，不正确的答案不会受到惩罚。

```python
>>> 10 + 2
______

>>> 7 / 2
______

>>> 7 // 2
______

>>> 7 % 2  # 7 modulo 2, the remainder when dividing 7 by 2.
______
```

```python
>>> x = 20
>>> x + 2
______

>>> x
______

>>> y = 5
>>> y = y + 3
>>> y * 2
______

>>> y = y // 4
>>> y + x
______
```



### 2. Parson 问题

实验和作业的一部分练习是Parson问题。Parson问题由一组部分完整的代码行组成。若要完成该问题，必须在有效表达式的代码行空白处填空，包括重新排列代码行，来构造有效的程序。

在解压的文件夹目录下，应该可以看到Parsons问题相关的文件夹：

`parsons` : parsons网页程序文件

`parsons_probs` ：parson问题文件，每个问题应该包括一个源文件（ `.py` ）和一个配置文件( `.yaml` )

> **因服务器配置未完成，这个环节作业无法在网页上完成，大家可以在 parsons_probs文件夹下找到问题文件，完成相关问题，并在终端测试。**

例如，此次Parson问题是： `ilove61a`

```python
def ilove61a():
    """
    Write a function that returns the string "I love CS 61A!".
    >>> ilove61a() # .Case 1
    'I love CS 61A!'
    """
    "*** YOUR CODE HERE ***"
```

完成代码，并在解释器中输入函数调用表达式 `ilove61a()` ，查看输出是否为 I love CS 61A!

### 3. 编程问题

在打开的解压后的文件夹中，应该可以看到本次实验的编程问题文件（例如，lab00.py）

三引号（`"""`）中的行称为 **docstring** ，对函数会做什么的描述。在本课程中编写代码时，总应该阅读 docstring！

`>>>` 开头的行称为 **doctests**。回想一下，在使用Python解释器时，您在 `>>>` 后面编写Python表达式，输出将打印在该行下方。doctests 通过展示实际的Python代码来解释该函数的作用。它回答了这个问题："如果我们输入这个Python代码，预期的输出应该是什么？

![image-20220309155625866](https://cnchen2000.oss-cn-shanghai.aliyuncs.com/img/image-20220309155625866.png)

在 `twenty_twenty_two` 中，

- docstring 告诉你要“使用最有创造性的表达式来计算2022”，智能使用数字和算术运算符 `+ * -` 。
- doctest 检查函数调用 `twenty_twenty_two()` ，应该返回数字 2022。


> 请不要修改 docstring，除非你要添加自己的测试，如无特殊说明，你只需要编写代码即可

### 编写代码

一旦你理解了所问的问题，你就可以开始写代码了！，用计算得到2022的表达式替换掉 `return ______` 中的下划线。最有创造性的表达式会是什么样的？

> 不要忘了编辑后保存你的工作，请使用 `Ctrl+ S` 保存
>
> 推荐在 VS Code 中将 文件菜单中自动保存勾选
>
> 配合gitlab使用会更加方便

### 运行测试

使用 `ok` 来测试代码，每个作业或者实验都会包括 `ok`

回到终端，请确保你在 `lab00` 目录下，敲入 `ls` 会发现下面三个文件：

- `lab00.py`:  你刚编辑的开始文件
- `ok`: 测试程序
- `lab00.ok`: OK的配置文件

现在，让我们测试代码来确保它正常工作，你可以使用 `ok` 命令：

```
python3 ok --local
```

> `--local` 表示在本地运行测试

如果测试成功，会显示：

```
=====================================================================
Assignment: Lab 0
Ok, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running tests

---------------------------------------------------------------------
Test summary
    3 test cases passed! No cases failed.
```

测试失败：

```
---------------------------------------------------------------------
Doctests for twenty_twenty_two

>>> from lab00 import *
>>> twenty_twenty_two()
2013

# Error: expected
#     2022
# but got
#     2013

---------------------------------------------------------------------
Test summary
    0 test cases passed before encountering first failed test case
```

修复你的代码直到通过测试。

> 在 doctests 中可以添加自己编写的测试，然后使用 `-m doctest` 选项来测试它们
>
> 在Parson 问题中，你也可以使用 下面的命令验证
>
> ```
> python3 ok --local -q ilove61
> ```



## Tips





## 附

### 有用的python命令行可选项

在运行python文件时，可以使用命令行可选项来进一步检查代码，这里介绍了几个有用的可选项，如果你想了解有关其他 Python 命令行选项的更多信息，请查看[文档](https://docs.python.org/3.9/using/cmdline.html)。

- 不使用命令行可选项将运行你提供的文件中的代码，并返回到命令行。例如，如果我们想以这种方式运行 `lab00.py`，将在终端中输入：

  ```
  python3 lab00.py
  ```

- **`-i`**：该可选项 `-i` 运行你的 Python 脚本，然后打开一个交互式会话。在交互式会话中，你可以逐行运行 Python 代码并获得即时反馈，而不是一次运行整个文件。要退出交互，请在解释器提示符中键入`exit()`。还可以使用键盘快捷键,  Linux/Mac 计算机上是 `Ctrl-D` ， Windows 上是`Ctrl-Z Enter`

  如果在以交互方式运行 Python 文件时对其进行编辑，则需要退出并重新启动解释器，以使这些更改生效。

  下面是如何以交互方式运行：`lab00.py`

  ```
  python3 -i lab00.py
  ```

- **`-m doctest`**：在特定文件中运行 doctests。doctests 在函数内由三重引号 （`"""`） 括起来。

  文件中的每个测试都包含`>>>` 及随后的一些 Python 代码，和预期的输出（尽管在 doctest 命令的输出中看不到这些 `>>>` 代码）。

  要运行 `lab00.py` 的doctests，可以运行：

  ```
  python3 -m doctest lab00.py
  ```

### VS Code

#### 介绍

 Visual Studio Code（VS Code）是由Microsoft开发的开源文本编辑器，可以免费使用。它以相对轻量级而闻名，同时还结合了现代IDE中的关键功能，例如Git集成和广泛的调试器。这使得VS Code非常适合从简单的Python脚本到更密集的软件工程项目的任何事物。

#### 获取 VS Code

访问 [VS Code 的网站](https://code.visualstudio.com/)，然后按照说明将其安装到你的计算机上

#### 举例： welcome.py

首先在终端输入命令来创建一个目录 `example` ：

```
mkdir ~/Desktop/example
cd ~/Desktop/example
```

#### 打开文件

安装好 VS Code 后，你可以找到这个应用打开，或者在终端打开它。在当前工作目录打开的命令是：

```
code .
```

![blank vscode](https://cs61a.org/articles/vscode/assets/vscode-blank.png)

VS Code 会打开一个欢迎界面，点击资源管理器（左上角的页面图标），然后点击 `EXAMPLE` ，点击角上的页面带加号的图标新建一个文件，命名为 `welcome.py` , 会提示你安装Python插件。插件随后会介绍，现在只安装 Python插件，并忽略掉其他的弹出框，可以开始编程了。

#### 编写文件

现在可以开始编写第一个Python文件，编写一个短程序执行时会打印欢迎信息，现在如果不明白Python代码没关系，照着敲代码即可：

```
def welcome(name):
    print(f'Welcome to CS61A, {name}')
```

`Ctrl-s` 保存文件，文件名后面的白色圆点会消失。

#### 运行Python

回到终端，现在在 `example` 目录下面。在终端敲入：

```
python3 -i welcome.py
```

目录会执行如下操作：

1.  `python3` 命令会开始Python
2.  `-i` 标记告诉Python开始**交互模式**，允许你在终端敲入Python命令
3.  `welcome.py` 是要运行的文件名 

注意Python解释器提示 `>>>` ，表示Python准备好接受一个命令

我们定义了函数 `welcome` ，敲入：

```
>>> welcome('Laryn')
```

Python会打印出

```
Welcome to CS61A, Laryn!
```

代码起作用了！试试其他的名字，关闭 Python 请敲入：

```
>>> exit()
```

或者使用 `Ctrl+d` 快捷键

恭喜你，你已经在VS Code中编写完成了第一个文件。

#### 键盘快捷键

VS Code 有许多的键盘快捷键，下面是其中常用的一些

- \- Ctrl+  `  ：在VS Code中打开集成终端
- \- `Ctrl+s`：保存当前文件
- \- `Ctrl+x`：剪切光标所在的整行
- \- `Ctrl+v`：将剪切的整行粘贴到光标上方的行中，或将所选文本就地粘贴
- \- `Ctrl+z`：撤消
- \- `Ctrl+shift-z`：重做
- \- `tab`：缩进一行或一组行
- \- `shift-tab`：删除一行或一组行
- \- `Ctrl+d`：突出显示当前单词。对于你在第一个单词之后键入的每个内容，它将突出显示该单词的每个下一个实例。这使你可以轻松地使用多个游标重命名变量！（玩玩这个，它很有趣，非常实用！）
- \- `Ctrl+tab`：移动到下一个选项卡
- \- `Ctrl+shift-tab`：移动到上一个选项卡（
- \- `Ctrl+f`：搜索单词
- \- `Ctrl+shift-f`：搜索所有选项卡

#### 扩展插件

扩展允许你定制文本编辑器。扩展可以做任何事情，从更改配色方案，到允许你在编码时控制音乐播放器，再到让你与朋友实时共享你的工作区（❌不要在作业上使用❌）！[这里](https://code.visualstudio.com/docs/editor/extension-gallery#:~:text=You can browse and install,on the VS Code Marketplace.) 是有关扩展的文档，请点击 `Ctrl+shift+x` 自行浏览 。

本指南仅触及 VS Code 的基础功能。请记住，如果你希望VS Code可以做什么，可能它就会，只需搜索一下。

### 结对编程

你可以使用实时共享扩展在 VSCode 中结对编程。

[在此下载](https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare&ssr=false)

一旦你和你的合作伙伴都安装了扩展，你将需要启动一个新的实时共享会话，然后彼此显式共享你的代码和终端。有关共享和加入会话的更多详细信息，请参阅下载页面上的说明。
