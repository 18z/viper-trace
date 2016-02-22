## database 功能模組解說

#### 功能：

```python
示範如何在資料庫中儲存、尋找及刪除檔案。
```

#### 使用方式：

*   儲存檔案

    ```python
    f = File("inspect-example.py")
    v = File("viper.py")

    db = Database()

    # add file to db
    db.add(f)
    db.add(v)
    ```

    ```sql
    sqlite> select * from malware;
    1|inspect-example.py|763|ASCII Java program text|ba41a0572ad44a0c1c1862758b8599f0|3B16151C|8920c9292d5760a7e10dd1b8d77f7c30c837f8ef|450bc8ce8e3748f98aed03516079ec25604066a14775fe609d0054d2e5852d31|dbec056e7930542c27126b4b472dbb7430b7c2f8f28ac4c4bace08c2f3730d3c78415ff412ceba382d37a573f1524e77bf3f3160554a523f2a1d108afc1721a7||2016-02-22 10:10:40.778191
    2|viper.py|83|a python script text executable|79a3cca8475be134a5897697c6038f8d|4FFA009D|6dba40f678bcc1cbcf9e80bcb7cced05e7ead028|6a59f51d13ae0ea87fa503c1ce13300177a684798f8e7c1fed8392ad46eff56b|f8d80d4e1aafea7c02b4a4fedbd6701ba1c1297b4b05acf315fe9a45f4271ce075a98153fffa535bccec7ac163a2525d7adc8da1208451a92d97dc9de60fedc0||2016-02-22 10:10:40.778191
    ```

*   找尋檔案

    ```python
    # find from db
    rows = db.find('sha256', v.sha256)
    print rows

    # 其中 db.find('sha256', v.sha256) 也可以用其他種雜湊值來查詢
    # 例如：db.find('md5', v.md5)。
    # 註：rows 是 list。
    ```

*   刪除檔案

    ```python
    # delete from db
    malware_id = rows[0].id
    db.delete(malware_id)
    ```
