import os

def patch_all():
    # 1. Manifest-ке рұқсатты sed арқылы қосамыз
    os.system("sed -i '/<uses-permission android:name=\"android.permission.SYSTEM_ALERT_WINDOW\"/d' apk_extracted/AndroidManifest.xml")
    os.system("sed -i '/<manifest/a \    <uses-permission android:name=\"android.permission.SYSTEM_ALERT_WINDOW\"/>' apk_extracted/AndroidManifest.xml")
    
    # 2. MainActivity инекциясы
    for r, d, f in os.walk("apk_extracted/smali"):
        for file in f:
            if "MainActivity.smali" in file or "UnityPlayerActivity.smali" in file:
                path = os.path.join(r, file)
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                # Сервисті қайталап қоспау үшін тексеру
                if "ModMenuService" not in content:
                    new_content = content.replace("    invoke-super", "    invoke-static {p0}, Lcom/almas/official/ModMenuService;->start(Landroid/content/Context;)V\n\n    invoke-super", 1)
                    with open(path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"[+] Инекция жасалды: {path}")

if __name__ == "__main__":
    patch_all()
