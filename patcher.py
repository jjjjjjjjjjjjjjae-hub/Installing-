import os

def patch_all():
    # 1. Manifest-ке рұқсат қосу
    manifest = "apk_extracted/AndroidManifest.xml"
    if os.path.exists(manifest):
        with open(manifest, "r", encoding="latin-1") as f:
            c = f.read()
        perm = '<uses-permission android:name="android.permission.SYSTEM_ALERT_WINDOW"/>'
        if perm not in c:
            c = c.replace("<manifest", f"<manifest \n    {perm}")
            with open(manifest, "w", encoding="latin-1") as f:
                f.write(c)

    # 2. Activity-ге инекция жасау
    for r, d, f in os.walk("apk_extracted/smali"):
        for file in f:
            if "MainActivity.smali" in file or "UnityPlayerActivity.smali" in file:
                path = os.path.join(r, file)
                with open(path, "r", encoding="utf-8") as f:
                    lines = f.readlines()
                for i, line in enumerate(lines):
                    if ".method" in line and "onCreate(" in line:
                        lines.insert(i + 2, "    invoke-static {p0}, Lcom/almas/official/ModMenuService;->start(Landroid/content/Context;)V\n")
                        break
                with open(path, "w", encoding="utf-8") as f:
                    f.writelines(lines)
                print(f"[+] Инекция жасалды: {path}")

if __name__ == "__main__":
    patch_all()
