import os
import re

def patch_all():
    # 1. Manifest-тің бинарлық пішінін бұзбау үшін тек тиісті тегті қосу
    manifest = "apk_extracted/AndroidManifest.xml"
    if os.path.exists(manifest):
        with open(manifest, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Manifest-те <manifest ... > жабылуына дейін рұқсатты кірістіру
        # Бұл жерде xmlns:android бар ма, соны тексереміз
        if 'android.permission.SYSTEM_ALERT_WINDOW' not in content:
            content = content.replace('>', ' xmlns:android="http://schemas.android.com/apk/res/android">\n    <uses-permission android:name="android.permission.SYSTEM_ALERT_WINDOW"/>', 1)
            with open(manifest, "w", encoding="utf-8") as f:
                f.write(content)
            print("[+] Manifest-ке рұқсат сәтті қосылды.")

    # 2. Activity инекциясы
    for r, d, f in os.walk("apk_extracted/smali"):
        for file in f:
            if "MainActivity.smali" in file or "UnityPlayerActivity.smali" in file:
                path = os.path.join(r, file)
                with open(path, "r", encoding="utf-8") as f:
                    lines = f.readlines()
                
                new_lines = []
                for line in lines:
                    new_lines.append(line)
                    if ".method" in line and "onCreate(" in line:
                        new_lines.append("    invoke-static {p0}, Lcom/almas/official/ModMenuService;->start(Landroid/content/Context;)V\n")
                
                with open(path, "w", encoding="utf-8") as f:
                    f.writelines(new_lines)
                print(f"[+] MainActivity инекциясы орындалды: {path}")

if __name__ == "__main__":
    patch_all()
