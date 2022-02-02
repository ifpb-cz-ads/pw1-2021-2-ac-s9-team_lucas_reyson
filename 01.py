class Televisao:
     def __init__(self):
           self.ligada = False
           self.canal = 2
           self.tamanho = 40
           self.marca = 'samsung'
     def muda_canal_para_baixo(self):
           self.canal -= 1
     def muda_canal_para_cima(self):
           self.canal += 1

tv = Televisao()
tv.muda_canal_para_cima()
tv.muda_canal_para_cima()
print(tv.canal)
tv.muda_canal_para_baixo()
print(tv.canal)

tv_sala = Televisao()
tv_sala.tamanho = 32
tv_sala.marca = 'philips'

print(f'O tamanho da tv é {tv.tamanho} e a marca é {tv.marca}')
print(f'O tamanho da tv da sala é {tv_sala.tamanho} e a marca é {tv_sala.marca}')