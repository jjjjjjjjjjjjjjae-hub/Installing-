.class public Lcom/almas/official/ModMenuService;
.super Landroid/app/Service;

.method public onCreate()V
    .registers 4
    invoke-super {p0}, Landroid/app/Service;->onCreate()V
    
    # Рұқсатты тексеру: бар болса аттап өту
    invoke-static {p0}, Landroid/provider/Settings;->canDrawOverlays(Landroid/content/Context;)Z
    move-result v0
    if-eqz v0, :cond_permission_ok

    # Рұқсат жоқ болса ғана сұрау
    new-instance v0, Landroid/content/Intent;
    const-string v1, "android.settings.action.MANAGE_OVERLAY_PERMISSION"
    invoke-direct {v0, v1}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V
    const/high16 v1, 0x10000000
    invoke-virtual {v0, v1}, Landroid/content/Intent;->addFlags(I)Landroid/content/Intent;
    invoke-virtual {p0, v0}, Lcom/almas/official/ModMenuService;->startActivity(Landroid/content/Intent;)V

    :cond_permission_ok
    return-void
.end method

.method public static start(Landroid/content/Context;)V
    .registers 3
    new-instance v0, Landroid/content/Intent;
    const-class v1, Lcom/almas/official/ModMenuService;
    invoke-direct {v0, p0, v1}, Landroid/content/Intent;-><init>(Landroid/content/Context;Ljava/lang/Class;)V
    invoke-virtual {p0, v0}, Landroid/content/Context;->startService(Landroid/content/Intent;)Landroid/content/ComponentName;
    return-void
.end method

.method public onBind(Landroid/content/Intent;)Landroid/os/IBinder;
    .registers 2
    const/4 v0, 0
    return-object v0
.end method
