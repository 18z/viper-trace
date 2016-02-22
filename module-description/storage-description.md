## storage 功能模組解說

#### 功能：

```python
將所分析的檔案以 sha256 hash value 為檔名儲存。
儲存位置位於
binary /依序以前四個 hash value 字元建立之巢狀資料夾中。

例如：檔案 6a59f51d13ae0ea87fa503c1ce13300177a684798f8e7c1fed8392ad46eff56b
前四個字元為 6a59，則存放位置就會在
binaries/6/a/5/9/
```

#### 使用方式：

*   儲存檔案

    ```python
    f = File("/home/deanboole/Documents/ProjectGithub/check_lists.md")

    new_path = store_sample(f)
    ```

*   找尋檔案儲存位置

    ```python
    f = File("/home/deanboole/Documents/ProjectGithub/check_lists.md")
    print get_sample_path(f.sha256)
    ```
