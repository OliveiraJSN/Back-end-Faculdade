
class Config:

    #O mecanismo de sessão do Flask exige que a SECRET_KEY esteja configurada. Essa chave é usada para assinar criptograficamente os cookies da sessão, garantindo que les não possam ser modificados pelo usuário no navegador.

    #Quando um usuário faz login, o Flask cria um "cookie de sessão" no navegador do usuário. Para evitar que esse cookie seja adulterado, o Flask "assina" criptograficamente usando o SECRET_KEY.
    SECRET_KEY = "Joao123"
    DB_CONFIG = {
        'host': 'localhost',
        'user': 'root',
        'password': 'Neto0302*',
        'database': 'login_usuarios'
    }