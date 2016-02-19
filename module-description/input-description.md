## console 功能模組解說

#### 功能：

```python
此功能會拆解使用者輸入的字串。
將第一個連續字元當作是指令(root)，後面的連續字元當作是參數。

接著將拆解完字串所得到的 root 進行判斷，看是否符合自行制定的指令。
若有就呼叫該指令功能。
```

#### 使用方式：

*   否符合自行制定的指令，就呼叫該指令功能

    ```python
    if root in self.cmd.commands:
        self.cmd.commands[root]['obj'](*args)
    ```
