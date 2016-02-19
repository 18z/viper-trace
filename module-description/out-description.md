## out 功能模組解說

#### 功能：

1. 依據不同情況 (info, warning, error, success) 印出不同顏色之訊息。
2. 列印表格。

#### 使用方式：

1.  依據不同情況 (info, warning, error, success) 印出不同顏色之訊息。
    ```python    
    print_info("info message")
    print_warning("warning message")
    print_error("error message")
    print_success("success message")
    ```

2. 列印表格。
    ```python
    rows = [["cmd", "des"]]
    print table(設定欄位標題, 欄位內容)
    ```
