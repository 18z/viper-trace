### [Viper](https://github.com/viper-framework/viper) 追 code 經驗紀錄

#### 化繁為簡 (一)

通常發展一段時日之專案，其規模與複雜度會隨之增加。因此，若直接從最近的版本下手，則較難以掌握精髓。為降低專案複雜度，首先建議使用 git checkout，將專案回溯到早期相對簡易之版本。

#### 將程式間的關聯找出

回到早期版本後，接下來的任務就是建立程式間關聯表格。以下面表格為例，程式由最左邊 viper.py 開始，該程式會呼叫、使用 console.py，而 console.py 又會呼叫、使用到 colors.py、session.py、plugins.py、commands.py。其中 colors.py 並無呼叫或使用其他程式，因此它後面就接上 end 表示結束。依上面方法，將所有程式之間的關聯表建立出來後，將有助於對專案架構的理解與程式的使用。

| 1                    | 2                                | 3                                  | 4                                   | 5                                | 6   |
|----------------------|----------------------------------|------------------------------------|-------------------------------------|----------------------------------|-----|
| [viper.py](viper.py) | [console.py](konsole/console.py) | [colors.py](konsole/colors.py)     | end                                 |                                  |     |
|                      |                                  | [session.py](konsole/session.py)   | [objects.py](konsole/objects.py)    | end                              |     |
|                      |                                  |                                    | [geoip.py](konsole/geoip/geoip.py)  | end                              |     |
|                      |                                  | [plugins.py](konsole/plugins.py)   | [out.py](konsole/out.py)            | [colors.py](konsole/colors.py)   | end |
|                      |                                  |                                    | [abstracts.py](konsole/abstract.py) | [colors.py](konsole/colors.py)   | end |
|                      |                                  | [commands.py](konsole/commands.py) | [out.py](konsole/abstract.py)       | [colors.py](konsole/colors.py)   | end |
|                      |                                  |                                    | [colors.py](konsole/colors.py)      | end                              |     |
|                      |                                  |                                    | [session.py](konsole/session.py)    | [objects.py](konsole/objects.py) | end |

#### 化繁為簡 (二)

回到早期版本後，專案複雜度雖降低許多，但或許還是不易閱讀。此時便可搭配上一階段所建立的關聯表，依循脈絡，切割功能模組並過濾雜質。舉例來說，colors.py 已經是程式關聯脈絡的最底層了。因此，我們就從 colors.py 開始，反方向追 code 回去。

以 viper 專案來說，colors.py 本身提供 console 字元顏色變換之功能。因此，閱讀完 colors.py 後，我們撰寫一[測試範例](color-example.py)，試圖呼叫 colors.py 裡面定義的功能來實現字元顏色變換。若能成功使用 colors.py 所定義的功能，則字元顏色控制這塊「功能模組切割」就成功了。

功能模組切割成功後，為了對專案細節透徹了解。因此，閱讀 colors.py 的細節是必要的。在閱讀過程中，程式碼可能還是很複雜。在此階段，我們就可開始「過濾雜質」。所謂過濾雜質就是刪除「不影響主要功能」的程式碼區塊，並在刪除後執行測試範例。 若能成功執行，則表示我們「過濾雜質」成功。如此，程式碼將更簡潔易懂，對於專案的精隨，掌握度也更高。



將上述過程重複執行，便可逐漸掌握專案輪廓與細節。
