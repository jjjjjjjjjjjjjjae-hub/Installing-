import os
def patch():
    os.system("sed -i '/SYSTEM_ALERT_WINDOW/d' apk_extracted/AndroidManifest.xml")
    os.system("sed -i '/<manifest/a \    <uses-permission android:name=\"android.permission.SYSTEM_ALERT_WINDOW\"/>' apk_extracted/AndroidManifest.xml")
    for r, d, f in os.walk("apk_extracted/smali"):
        for file in f:
            if "MainActivity.smali" in file or "UnityPlayerActivity.smali" in file:
                path = os.path.join(r, file)
                with open(path, "r", encoding="utf-8") as f:
                    c = f.read()
                if "ModMenuService" not in c:
                    c = c.replace("    invoke-super", "    invoke-static {p0}, Lcom/almas/official/ModMenuService;->start(Landroid/content/Context;)V\n\n    invoke-super", 1)
                    with open(path, "w", encoding="utf-8") as f:
                        f.write(c)
if __name__ == "__main__": patch()
