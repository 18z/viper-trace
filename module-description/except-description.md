## plugins 功能模組解說

#### 功能：
了解 python 例外處理使用方法。

#### 使用方式：

*   以簡單範例說明

    ```python
    try:
        f = open('myfile.txt')
        s = f.readline()
        i = int(s.strip())
    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)
    except ValueError:
        print "Could not convert data to an integer."
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise

    """
    *   First, the try clause (the statement(s) between the try and except
        keywords) is executed.
    *   If no exception occurs, the except clause is skipped and execution of the try
        statement is finished.
    *   If an exception occurs during execution of the try clause, the rest of the
        clause is skipped. Then if its type matches the exception named after the
        except keyword, the except clause is executed, and then execution continues
        after the try statement.
    *   If an exception occurs which does not match the exception named in the except
        clause, it is passed on to outer try statements; if no handler is found, it is
        an unhandled exception and execution stops with a message as shown above.

    *   首先，執行 try 裡面的程式。
    *   若都沒出錯，則 except 部分就跳過。
    *   若執行 try 裡的程式時出錯，假設是 s = f.readline() 出錯，則 i = int(s.strip())
        就不會再執行。出錯的類型若符合 except 中的其中一個，就會跳該 except 中的訊息。
    *   若出錯，但無符合 except 類型，則使用最後一個 except。
    """
    ```
