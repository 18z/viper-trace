## session 功能模組解說

#### 功能：

```python
在使用 open -f file 後，便會呼叫 session。
session 被呼叫後，使用 __session__.set("viper.py")
便會呼叫 object。

之後使用 __session__.file.type 即可得知檔案型態。
```

#### 使用方式：

*   幫開啟檔案建立 session。

    ```python
    __session__.set("viper.py")
    ```
