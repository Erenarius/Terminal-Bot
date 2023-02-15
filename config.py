import os
import re

id_pattern = re.compile(r'^.\d+$')


token = os.environ.get("61129922919191Ğ919911Ğ1Ğ1Ğ1Ğ:LSWİPFROFKSLDKSÖARKviFHSJt7fN8r8jyHTsjIIh3ViiY")
app_id = int(os.environ.get("284848347447383929100195736"))
app_hash = os.environ.get("3888283f63bkdkdk48b463f292929fşfşd01cc90c5a469e9")
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
