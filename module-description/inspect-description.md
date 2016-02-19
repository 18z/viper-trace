## plugins 功能模組解說

#### 功能：
檢查工具包，例如檢查 module 中 member_object 是否為 class。

#### 使用方式：

*   檢查範例說明

    ```python
    import 想檢查之模組

    接著會找該模組是否有子模組
    若有，則用 __import__ 載入

    接著用inspect.isclass(member_object)
    一一檢查 member_object 是否為 class
    ```
