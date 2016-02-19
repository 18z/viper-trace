## console 功能模組解說

#### 功能：

```python
在程式 at exit 狀態時才會執行的功能

這裡主要是用來將每一次使用者在 console 中輸入的字串寫入 history 中。
```

#### 使用方式：

*   程式執行完畢後，螢幕會印出 the end。

    ```python
    def bye() :
        print "the end"
    atexit.register(bye)
    ```
