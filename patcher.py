import os

def inject_test_menu():
    print("[*] Жаңа әмбебап Мод Меню инъекциясы басталды...")
    smali_dir = "apk_extracted/smali"
    
    if not os.path.exists(smali_dir):
        # Мульти-dex болса басқа smali қалтасын тексереміз
        smali_dir = "apk_extracted/smali_classes2"
        if not os.path.exists(smali_dir):
            # Ол да болмаса бірінші кездескен smali қалтасын аламыз
            found_dir = False
            for r, d, f in os.walk("apk_extracted"):
                if "smali" in r:
                    smali_dir = r
                    found_dir = True
                    break
            if not found_dir:
                print("[-] Қате: Smali қалтасы табылмады!")
                return

    print(f"[+] Нысана Smali қалтасы: {smali_dir}")
    target_smali_path = None

    # Ойынның басты терезесі болуы мүмкін ең негізгі файлдарды іздеу
    possible_names = ["MainActivity.smali", "UnityPlayerActivity.smali", "SplashActivity.smali"]
    
    for r, d, f in os.walk(smali_dir):
        for name in possible_names:
            if name in f:
                target_smali_path = os.path.join(r, name)
                break
        if target_smali_path:
            break

    # Егер стандартты аттар табылмаса, бірінші кездескен үлкенірек Activity-ді аламыз
    if not target_smali_path:
        for r, d, f in os.walk(smali_dir):
            for file in f:
                if file.endswith(".smali") and "Activity" in file:
                    target_smali_path = os.path.join(r, file)
                    break
            if target_smali_path:
                break

    if not target_smali_path:
        print("[-] Инъекция үшін сәйкес келетін Smali файлы табылмады!")
        return

    print(f"[+] Таңдалған файлға инъекция жасалады: {target_smali_path}")

    with open(target_smali_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    modified_lines = []
    in_on_create = False
    injected = False

    for line in lines:
        modified_lines.append(line)
        if ".method" in line and "onCreate(" in line:
            in_on_create = True
            continue
            
        if in_on_create and not injected and "prologue" in line:
            toast_smali = """
    # --- TEST MOD MENU INJECTION START ---
    const-string v0, "TEST MOD MENU: Бұлттық зауыт сәтті жұмыс істеп тұр!"
    const/0x1 v1
    invoke-static {p0, v0, v1}, Landroid/widget/Toast;->makeText(Landroid/content/Context;Ljava/lang/CharSequence;I)Landroid/widget/Toast;
    move-result-object v0
    invoke-virtual {v0}, Landroid/widget/Toast;->show()V
    # --- TEST MOD MENU INJECTION END ---
            """
            modified_lines.append(toast_smali)
            injected = True
            in_on_create = False
            print("[+] Тест меню коды сәтті енгізілді!")

    with open(target_smali_path, "w", encoding="utf-8") as file:
        file.writelines(modified_lines)

if __name__ == "__main__":
    inject_test_menu()

