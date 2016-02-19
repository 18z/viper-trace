## object 功能模組解說

#### 功能：
負責計算與提供檔案基本資訊，例如：檔案類型，sha256 hash value 等。

#### 使用方式：

*   檔案類型查詢

    ```python
    f = File("viper.py")

    print f.get_type()
    ```
