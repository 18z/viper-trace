## commands 功能模組解說

#### 功能：
了解 getopt 使用方法。

#### 使用方式：

*   以 split() 將參數以空格區分開

    ```python
    args = '-a -b -cfoo -d bar a1 a2 z5'.split()
    print args

    結果：
    ['-a', '-b', '-cfoo', '-d', 'bar', 'a1', 'a2', 'z5']
    ```

*   使用 getopt 區分參數及參數值

    ```python
    optlist, args = getopt.getopt(args, 'abc:d:')
    c 與 d 後面有 : 表示後面會接參數值。


    optlist 表示
    [('-a', ''), ('-b', ''), ('-c', 'foo'), ('-d', 'bar')]
    有定義的參數及參數值

    args 表示其餘沒有被定義到的參數值
    ['a1', 'a2', 'z5']
    ```

