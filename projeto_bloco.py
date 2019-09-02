import pygame, random
branco  = (255,255,255)
preto = (0,0,0)
verde = (0,255,0)
azul = (0,0,156)
red = (255,0,0)
darkBlue = (2 , 24 , 89)
cores = [azul,red,darkBlue,preto]

pygame.mixer.init()

pygame.font.init()

largura_tela = 800
altura_tela = 600

tela = pygame.display.set_mode((largura_tela,altura_tela))

terminou = False

class Aba():
    def __init__(self,aba_type,cor):
        self.largura = 200
        self.altura = 60
        self.x = 200 * aba_type
        self.y = 0
        self.area = pygame.Rect(self.x,self.y,self.largura,self.altura)
        self.cor = cores[aba_type]
    def desenha(self, tela):
        pygame.draw.rect(tela,self.cor,self.area)

def mostra_titulo(texto,x,y):
    font = pygame.font.Font(None,24)
    text = font.render(texto,1,preto)
    textpos = text.get_rect(center=(x,y) )
    tela.blit(text,textpos)
    
def mostrar_dados(texto,y):
    font = pygame.font.Font(None,20)
    text = font.render(texto, 1 ,preto)
    textpos = text.get_rect(center =(tela.get_width()/4 ,y))
    tela.blit(text,textpos)

def montar_tabela(texto,y):
    font = pygame.font.Font(None,20)
    text = font.render(texto, 1 ,preto)
    textpos = text.get_rect(center =(tela.get_width()/2 ,y))
    tela.blit(text,textpos)

def mostra_titulo_aba(texto,x):
    font = pygame.font.Font(None,20)
    text = font.render(texto,1,branco)
    textpos = text.get_rect(center =(x,30))
    tela.blit(text, textpos)
def cria_abas():
    lista_de_abas = []
    for i in range(0,4):
        aba = Aba(i,cores)
        aba.desenha(tela)
        lista_de_abas.append(aba)
        mostra_titulo_aba(f"ABA {i}", (largura_tela/4 *i)+100)
    return lista_de_abas


tela.fill(branco)
aba0,aba1,aba2,aba3 =  cria_abas()
while not terminou:

    dicionario = {'alexandre': 456123789, 'anderson': 1245698456,
              'antonio': 123456456, 'carlos': 91257581,
              'cesar':987458, 'rosemary': 789456125 }

    valores_Bytes = dicionario.values()

    soma = sum(dicionario.values())
    soma = soma/1024/1024
    soma_media = soma/len(dicionario)
    soma_indices = 1

    for i in dicionario.keys():
        valor = dicionario[i]
        converter_mb = valor /1024/1024
        dicionario[i] = round(converter_mb,2)

    print("ACME Inc.           Uso do espaço em disco pelos usuários",)
    print("------------------------------------------------------------------------")
    print("Nr.    Usuário        Espaço utilizado     % do uso")
    print("")
        
    for i in dicionario.keys():
        dicionario[i] = round(dicionario[i],2)
        porcentagem = round((dicionario[i]/soma)*100,2)
        print('{:^1}     {:<10}        {:>9,.2f}      {:>11,.2f}'.format(soma_indices, i, dicionario[i], porcentagem))
        soma_indices = soma_indices + 1

    print(" ")
    print("Total de memoria usada:", round(soma,2), "Mb")
    print("Media de memoria usada:", round(soma_media,2), "Mb")
    

    
   
    #montar_tabela("ACME Inc.           Uso do espaço em disco pelos usuários",50)
    #mostrar_dados("", 30+soma_indices*10)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:
            pos = pygame.mouse.get_pos()
            if aba0.area.collidepoint(pos):
                tela.fill(branco)
                aba0, aba1, aba2, aba3 = cria_abas()
                mostra_titulo("ACME Inc.           Uso do espaço em disco pelos usuários",400,150)
                montar_tabela("------------------------------------------------------------------------",175)
                mostrar_dados("1  alexandre, 456123789",150+soma_indices*10)
                mostrar_dados("2  anderson 1245698456",170+soma_indices*10)
            if aba1.area.collidepoint(pos):
                tela.fill(branco)
                aba0, aba1, aba2, aba3 = cria_abas()
            if aba2.area.collidepoint(pos):
                tela.fill(branco)
                aba0, aba1, aba2, aba3 = cria_abas()
            if aba3.area.collidepoint(pos):
                tela.fill(branco)
                aba0, aba1, aba2, aba3 = cria_abas()
                
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True

    pygame.display.update()
    
pygame.display.quit()
     


