#Un Decorador 

def soy_tu_cto(func):
    def envoltura(*args,**kwargs):
        func(*args,**kwargs)
        print('Gustavo Adolfo es el CTO de Petal!')
    return envoltura

@soy_tu_cto
def dudaCTO():
    print('¿Quien es el CTO de Petal?')
        
dudaCTO()
print('att: La junta directiva') 