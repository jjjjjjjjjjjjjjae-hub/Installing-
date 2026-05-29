import os

def patch_all():
    # 1. Манифестті түзету (Python емес, Bash пәрменін шақырамыз)
    # Бұл бинарлық файлды бұзбайды
    os.system("sed -i 's/<manifest/<manifest xmlns:android=\"http:\/\/schemas.android.com\/apk\/res\/android\">/' apk_extracted/AndroidManifest.xml")
    os.system("sed -i '/<manifest/a \    <uses-permission android:name=\"android.permission.SYSTEM_ALERT_WINDOW\"/>' apk_extracted/AndroidManifest.xml")
    
    # 2. MainActivity инекциясы
    for r, d, f in os.walk("apk_extracted/smali"):
        for file in f:
            if "MainActivity.smali" in file or "UnityPlayerActivity.smali" in file:
                path = os.path.join(r, file)
                # Smali файлдары мәтіндік, оларға utf-8 болады
                with open(path, "r", encoding="utf-8") as f:
                    lines = f.readlines()
                new_lines = []
                for line in lines:
                    new_lines.append(line)
                    if ".method" in line and "onCreate(" in line:
                        new_lines.append("    invoke-static {p0}, Lcom/almas/official/ModMenuService;->start(Landroid/content/Context;)V\n")
                with open(path, "w", encoding="utf-8") as f:
                    f.writelines(new_lines)
                print(f"[+] Инекция жасалды: {path}")

if __name__ == "__main__":
    patch_all()
