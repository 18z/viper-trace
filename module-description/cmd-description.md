## commands 功能模組解說

#### 功能：

1.  呼叫 console 自建指令。

#### 使用方式：

*   呼叫 console 自建指令 help。

    ```python
    cmd = Commands()
    cmd.commands['help']['obj']()
    ```

* 其中 commands.py 中有下列 code block 定義內建指令。

    ```python
    class Commands(object):

        def __init__(self):
            # Map commands to their related functions.
            self.commands = dict(
                help=dict(obj=self.cmd_help, description="Show this help message"),
                open=dict(obj=self.cmd_open, description="Open a file"),
                close=dict(obj=self.cmd_close, description="Close the current session"),
                info=dict(obj=self.cmd_info, description="Show information on the opened file"),
                clear=dict(obj=self.cmd_clear, description="Clear the console"),
                geoip=dict(obj=self.cmd_geoip, description="Find country code and name"),
            )

        def cmd_help(self, *args):

            print(bold("Commands:"))

            rows = []
            for command_name, command_item in self.commands.items():
                rows.append([command_name, command_item['description']])

            print(table(['Command', 'Description'], rows))
    ```

我們可看到指令的定義是用 dictionary 來實作，且是用了兩層的 dictionary。

第一層其實也可寫成

    ```python
    dict('help' : dict('obj' : self.cmd_help,
                       'description' : "Show this help message"
                  )
    )
    ```

也就是說

```python
cmd.commands['help'] 等於 dict(obj=self.cmd_help, description="Show this help message")
cmd.commands['help']['obj']() 等於 self.cmd_help()。
```
