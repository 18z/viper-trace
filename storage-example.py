from konsole.objects import *
from konsole.storage import store_sample, get_sample_path

f = File("/home/deanboole/Documents/ProjectGithub/check_lists.md")

new_path = store_sample(f)
#print new_path

print get_sample_path(f.sha256)
