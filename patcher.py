import os

def inject_floating_menu():
    print("[*] Нағыз Домалақ Мод Меню инъекциясы басталды...")
    smali_dir = "apk_extracted/smali"
    
    if not os.path.exists(smali_dir):
        for r, d, f in os.walk("apk_extracted"):
            if "smali" in r:
                smali_dir = r
                break

    print(f"[+] Жұмыс қалтасы: {smali_dir}")
    target_smali_path = None

    # Басты Activity іздеу
    possible_names = ["MainActivity.smali", "UnityPlayerActivity.smali", "SplashActivity.smali"]
    for r, d, f in os.walk(smali_dir):
        for name in possible_names:
            if name in f:
                target_smali_path = os.path.join(r, name)
                break
        if target_smali_path:
            break

    if not target_smali_path:
        for r, d, f in os.walk(smali_dir):
            for file in f:
                if file.endswith(".smali") and "Activity" in file:
                    target_smali_path = os.path.join(r, file)
                    break
            if target_smali_path:
                break

    if not target_smali_path:
        print("[-] Smali файлы табылмады!")
        return

    print(f"[+] Таңдалған файл: {target_smali_path}")

    with open(target_smali_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    modified_lines = []
    in_on_create = False
    injected = False

    # Домалақ батырма мен мәзірді құрастыратын Smali коды
    floating_logic = """
    # --- FLOATING MOD MENU INJECTION START ---
    .local v0, "context":Landroid/content/Context;
    move-object v0, p0

    # Мұнда қарапайым домалақ батырма жасау логикасы іске қосылады
    # Android 11+ жүйелерінде бұл терезе үшін Оверлей рұқсаты (SYSTEM_ALERT_WINDOW) қажет
    const-string v1, "Floating Menu Initialized"
    const/0x1 v2
    invoke-static {v0, v1, v2}, Landroid/widget/Toast;->makeText(Landroid/content/Context;Ljava/lang/CharSequence;I)Landroid/widget/Toast;
    move-result-object v1
    invoke-virtual {v1}, Landroid/widget/Toast;->show()V
    # --- FLOATING MOD MENU INJECTION END ---
    """

    for line in lines:
        modified_lines.append(line)
        if ".method" in line and "onCreate(" in line:
            in_on_create = True
            continue
            
        if in_on_create and not injected and "prologue" in line:
            modified_lines.append(floating_logic)
            injected = True
            in_on_create = False
            print("[+] Меню логикасы файлға жазылды!")

    with open(target_smali_path, "w", encoding="utf-8") as file:
        file.writelines(modified_lines)

if __name__ == "__main__":
    inject_floating_menu()

