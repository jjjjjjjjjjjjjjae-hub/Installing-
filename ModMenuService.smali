.class public Lcom/almas/official/ModMenuService;
.super Landroid/app/Service;

.method public onCreate()V
    .registers 4
    invoke-super {p0}, Landroid/app/Service;->onCreate()V
    
    # Рұқсатты тексеру (SYSTEM_ALERT_WINDOW)
    invoke-static {}, Landroid/os/Build$VERSION;->SDK_INT:I
    const/16 v0, 0x17
    if-lt v1, v0, :cond_permission_ok
    
    # Егер рұқсат жоқ болса, баптауларға жіберу
    new-instance v0, Landroid/content/Intent;
    const-string v1, "android.settings.action.MANAGE_OVERLAY_PERMISSION"
    invoke-direct {v0, v1}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V
    const/high16 v1, 0x10000000
    invoke-virtual {v0, v1}, Landroid/content/Intent;->addFlags(I)Landroid/content/Intent;
    invoke-virtual {p0, v0}, Lcom/almas/official/ModMenuService;->startActivity(Landroid/content/Intent;)V

    :cond_permission_ok
    return-void
.end method

.method public onBind(Landroid/content/Intent;)Landroid/os/IBinder;
    .registers 2
    const/4 v0, 0
    return-object v0
.end method
