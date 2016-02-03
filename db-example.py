from konsole.objects import *
from konsole.database import Database

f = File("/home/deanboole/Documents/ProjectGithub/check_lists.md")
v = File("/home/deanboole/Documents/ProjectGithub/console-test/viper.py")

db = Database()

# add file to db
status = db.add(f)
db.add(f)
db.add(v)

# find from db
rows = db.find('sha256', v.sha256)
print rows

# delete from db
malware_id = rows[0].id
db.delete(malware_id)
