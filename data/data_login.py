CASOS_LOGIN = [
    ("standard_user", "secret_sauce", True),     # usuario válido, login exitoso
    ("locked_out_user", "secret_sauce", False),  # usuario bloqueado, login falla
    ("usuario_malo", "password_malo", False),    # credenciales inválidas, login falla
]
