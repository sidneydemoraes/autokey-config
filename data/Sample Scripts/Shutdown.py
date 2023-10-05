# Enter script code

exit_code, resposta = dialog.list_menu(
    [
        "Desligar",
        "Reiniciar",
        "Cancelar"
    ],
    "Escolha a ação",
    "O que deseja fazer?",
    "Cancelar"
)


if ("Desligar" == resposta):
    system.exec_command("shutdown -P now")
    exit(0)
elif ("Reiniciar" == resposta):
    system.exec_command("shutdown -r now")
    exit(0)
    
exit(1)