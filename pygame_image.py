import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img_rev = pg.transform.flip(bg_img,True,False)
    img3 = pg.image.load("fig/3.png")
    img3 = pg.transform.flip(img3,True,False) #画像の左右反転(True=1,False=0)
    img3_rct = img3.get_rect()
    img3_rct.center = 300,200
    tmr = 0
    while True:
        x = tmr % 3200
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst = pg.key.get_pressed() # その瞬間に各キーが押されているかを表したリスト
        if key_lst[pg.K_UP]:
            img3_rct.move_ip((0,-1)) # move_ip(横座標の移動量,縦座標の移動量)
        elif key_lst[pg.K_DOWN]:
            img3_rct.move_ip((0,1))
        elif key_lst[pg.K_RIGHT]:
            img3_rct.move_ip((1,0))
        elif key_lst[pg.K_LEFT]:
            img3_rct.move_ip((-1,0))
        # 大きな画像1枚目
        screen.blit(bg_img, [-x, 0]) # (0,0)に貼り付け
        screen.blit(bg_img_rev, [-x+1600, 0]) 
        # 大きな画像2枚目
        screen.blit(bg_img, [-x+3200, 0]) 
        screen.blit(bg_img_rev, [-x+4800, 0]) 
        screen.blit(img3,img3_rct) # こうかとん
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()