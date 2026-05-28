import os

def patch_all():
    # 1. AndroidManifest-ке рұқсат қосу
    manifest_path = "apk_extracted/AndroidManifest.xml"
    if os.path.exists(manifest_path):
        with open(manifest_path, "r", encoding="utf-8") as f:
            content = f.read()
        permission = '<uses-permission android:name="android.permission.SYSTEM_ALERT_WINDOW" />'
        if permission not in content:
            content = content.replace("<manifest", f"<manifest \n    {permission}")
            with open(manifest_path, "w", encoding="utf-8") as f:
                f.write(content)
            print("[+] Manifest-ке рұқсат қосылды.")

    # 2. MainActivity-ге сервис шақыруын қосу
    # Мұнда MainActivity-дің орнын өзгертіп ал
    activity_path = "apk_extracted/smali/com/dts/freefireth/MainActivity.smali" 
    if os.path.exists(activity_path):
        with open(activity_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        
        for i, line in enumerate(lines):
            if ".method" in line and "onCreate" in line:
                lines.insert(i + 2, "    invoke-static {p0}, Lcom/almas/official/ModMenuService;->start(Landroid/content/Context;)V\n")
                break
        with open(activity_path, "w", encoding="utf-8") as f:
            f.writelines(lines)
        print("[+] MainActivity-ге сервис инекциясы жасалды.")

if __name__ == "__main__":
    patch_all()

