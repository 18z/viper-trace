## commands 功能模組解說

#### 功能：

```python
了解 def print_everything(*args): 中 * args
如何使用。
```

#### 使用方式：

1. 定義函式可以一次接收多個參數

    ```python
    def print_everything(*args):
        for count, thing in enumerate(args):
            print '{0}. {1}'.format(count, thing)

    print_everything('apple', 'banana', 'cabbage')
    ```
