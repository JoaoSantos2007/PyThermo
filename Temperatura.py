import pygame  # importa a biblioteca Pygame

pygame.init()

# Temas
dark = (103, 100, 107)
light = (240,240,240)
cor_fundo = dark
tocar = dark

# Cores textos
cor_texto = (0, 255, 0)
cor_temp = (255, 0, 0)

# Dimensões
height = 300
width = 600
dimensoes = (width, height)

source = "/home/joao/Arquivos/Temperatura/"

imagem_dark = pygame.image.load(source + "moon.png")
imagem_light = pygame.image.load(source + "sun.png")
icon = pygame.image.load(source + "temperatura.png")


clock = pygame.time.Clock()

fonte = pygame.font.SysFont("hack", 50)
tela = pygame.display.set_mode((dimensoes))

pygame.display.set_caption("Temperatura")
pygame.display.set_icon(icon)

def comandos(mouse, width, height, cor_fundo):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raise Exception
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 570 <= mouse[0] <= 600 and mouse[1] <= 30:
                if cor_fundo == dark:
                    cor_fundo = light
                elif cor_fundo == light:
                    cor_fundo = dark
    return cor_fundo

def fundo(mouse,dark,light,imagem_dark,imagem_light,tela,cor_fundo,tocar):
    if cor_fundo == dark:
        if 570 <= mouse[0] <= 600 and mouse[1] <= 30:
            tocar = light
        else:
            tocar = dark
        pygame.draw.rect(tela, tocar, [570, 0, 30, 30])
        tela.blit(imagem_light,(570, 0)) 
    elif cor_fundo == light:
        if 570 <= mouse[0] <= 600 and mouse[1] <= 30:
            tocar = dark
        else:
            tocar = light
        pygame.draw.rect(tela, tocar, [570, 0, 30, 30])
        tela.blit(imagem_dark, (570, 0))



while True:
    # Temperatura
    tfile = open('/sys/class/thermal/thermal_zone0/temp')
    temp = str((float(tfile.read()))/1000)

    # Imprimir temperatura
    tela.fill(cor_fundo)
    texto = fonte.render("Temperatura: ", True, cor_texto)
    tela.blit(texto, [100, 50])
    temperatura = fonte.render(temp, True, cor_temp)
    tela.blit(temperatura, [330, 50])

    mouse = pygame.mouse.get_pos()
    cor_fundo = comandos(mouse, width, height, cor_fundo)
    fundo(mouse,dark,light,imagem_dark,imagem_light,tela,cor_fundo,tocar)
    pygame.display.update()
    clock.tick(10)
    
