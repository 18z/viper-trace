## console 功能模組解說

#### 功能：

```python
console 環境中，若需要執行 bash 指令或其他系統工具。
viper 用的方法是在指令最前頭加上驚嘆號。
```

#### 使用方式：

*   若指令開頭有驚嘆號，則執行驚嘆號之後的指令(字串)。

    ```python
    cmd2 = "!date"

    if cmd2.startswith('!'):
        os.system(cmd2[1:])
    ```
