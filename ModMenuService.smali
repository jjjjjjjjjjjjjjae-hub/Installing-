.class public Lcom/almas/official/ModMenuService;
.super Landroid/app/Service;
.method public onCreate()V
    .registers 2
    invoke-super {p0}, Landroid/app/Service;->onCreate()V
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
