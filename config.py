import os
import re

id_pattern = re.compile(r'^.\d+$')


token = 6114960309:AAEeP4RKviFHSJt7fN8r8jyHTsjIIh3ViiY
app_id = int(os.environ.get("APP_ID"))
app_hash = os.environ.get("API_HASH")
allowed = [int(user) if id_pattern.search(user) else user for user in os.environ.get('Erenarius', '').split()]

help_text = """
Merhabaaa Ben @Erenarius abimin botuyum :)

Terminal'i bu botla kullanıcakmıs o.

**Sahibim olmadığın için beni kullanamazsın. @Erenarius
TELEGRAM APK ARSIVI ==> [URL](t.me/mooveapk)**

**erenarius abime özel komutlar:**

🔹 /st - speed test
🔹 /ip - ip details
🔹 /stats - disk space
🔹 /cd - change working dir
🔹 /my_files - file manager
🔹 And All System Commands...

"""
