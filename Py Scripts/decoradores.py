#decoradores @

def nombre_decorador(name):
    def funcion_decorador(function):
        def envolvedor(*args, **kwargs):
            print('Name:',name)
            return function(*args,**kwargs)
        return envolvedor
    return funcion_decorador
@nombre_decorador('Nombre Decorador')
def sum(a,b):
    return a+b
print(sum)
#no entiendo una mierda, ¿qué retorna esto?