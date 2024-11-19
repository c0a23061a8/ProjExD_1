import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    img3 = pg.image.load("fig/3.png")
    img3 = pg.transform.flip(img3,True,False) #画像の左右反転(True=1,False=0)
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        tmr = tmr % 800
        screen.blit(bg_img, [-tmr, 0]) # (0,0)に貼り付け
        screen.blit(img3, [300, 200])
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()