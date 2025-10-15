class Config:

    #Quando um usuário faz login, o Flask cria um "cookie de sessão" no navegador do usuário. Para evitar que esse cookie seja adulterado, o Flask o "assina" 
    # criptograficamente usando a SECRET_KEY. Se um usuário tentar modificar o cookie, a assinatura não corresponderá mais, e a sessão será invalidada.

    SECRET_KEY = 'Professor123'
    DB_CONFIG = {
        'host': 'localhost',
        'user': 'root',
        'password': 'Neto0302*',
        'database': 'login_usuarios'
    }