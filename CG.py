from time import sleep
import random
import pygame
from pygame import mixer
pygame.init()

mixer.set_num_channels(36)

length = 60 * 60 // 30

class clavier():
    def __init__(self, name, is_black, is_pressed):
        self.name = name
        # self.pitch_name = pitch_num
        self.is_black = is_black
        self.is_pressed = is_pressed
        self.must_play = False
        self.sound_length = length
        self.sound = mixer.Sound(f'.\\sounds\\piano\\{self.name}.wav')
    
    def note_play(self):
        self.sound.play()

    def note_stop(self):
        self.sound.stop()
        self.sound_length = length
        self.is_pressed = False


class chord_generator():
    def __init__(self):
        self.bass_index = -1
        self.third_index = -1
        self.fifth_index = -1
        self.seventh_index = -1
        #repeat mode values
        self.r_bass_index = -1
        self.r_third_index = -1
        self.r_fifth_index = -1
        self.r_seventh_index = -1

    def CG_output(self):
        claviers[self.bass_index].is_pressed = True
        claviers[self.bass_index].must_play = True
        claviers[self.bass_index].sound_length = length
        claviers[self.third_index].is_pressed = True
        claviers[self.third_index].must_play = True
        claviers[self.third_index].sound_length = length
        claviers[self.fifth_index].is_pressed = True
        claviers[self.fifth_index].must_play = True
        claviers[self.fifth_index].sound_length = length
        if self.seventh_index != -1:
            claviers[self.seventh_index].is_pressed = True
            claviers[self.seventh_index].must_play = True
            claviers[self.seventh_index].sound_length = length
     
        #saving for repeatition
        self.r_bass_index = self.bass_index
        self.r_third_index = self.third_index
        self.r_fifth_index = self.fifth_index
        self.r_seventh_index = self.seventh_index
        #reseting claviers
        # self.bass_index = -1
        # self.third_index = -1
        # self.fifth_index = -1
        self.seventh_index = -1
   
    def major_generator(self):
        self.bass_index = random.randrange(0, 18, 1)
        self.third_index = self.bass_index + 4
        self.fifth_index = self.bass_index + 7
        self.CG_output()
            
    def minor_generator(self):
        self.bass_index = random.randrange(0, 18, 1)
        self.third_index = self.bass_index + 3
        self.fifth_index = self.bass_index + 7
        self.CG_output()

    def diminished_generator(self):
        self.bass_index = random.randrange(0, 19, 1)
        self.third_index = self.bass_index + 3
        self.fifth_index = self.bass_index + 6
        self.CG_output()

    def augmented_generator(self):
        self.bass_index = random.randrange(0, 17, 1)
        self.third_index = self.bass_index + 4
        self.fifth_index = self.bass_index + 8
        self.CG_output()
            
    def dominant_seventh_generator(self):
        self.bass_index = random.randrange(0, 15, 1)
        self.third_index = self.bass_index + 4
        self.fifth_index = self.bass_index + 7
        self.seventh_index = self.bass_index + 10
        self.CG_output()

    def major_seventh_generator(self):
        self.bass_index = random.randrange(0, 14, 1)
        self.third_index = self.bass_index + 4
        self.fifth_index = self.bass_index + 7
        self.seventh_index = self.bass_index + 11
        self.CG_output()

    def repeat_chord(self):
        self.bass_index = self.r_bass_index
        self.third_index = self.r_third_index
        self.fifth_index = self.r_fifth_index
        self.seventh_index = self.r_seventh_index
        self.CG_output()

    def get_chord_notes(self):
        return(self.r_bass_index, self.r_third_index, self.r_fifth_index, self.r_seventh_index)

class draw_chord_buttons():
    def draw_maj_btn(self, color):
        maj_btn = pygame.draw.rect(screen, color, [WIDTH - 1250, HEIGHT - 300, 180, 90], 0, 5)
        maj_text = label_font.render('Major', True, white)
        screen.blit(maj_text, (WIDTH - 1200, HEIGHT - 280))
        return maj_btn
    
    def draw_min_btn(self, color):
        min_btn = pygame.draw.rect(screen, color, [WIDTH - 1000, HEIGHT - 300, 180, 90], 0, 5)
        min_text = label_font.render('Minor', True, white)
        screen.blit(min_text, (WIDTH - 950, HEIGHT - 280))
        return min_btn
    
    def draw_v7_btn(self, color):
        v7_btn = pygame.draw.rect(screen, color, [WIDTH - 750, HEIGHT - 300, 180, 90], 0, 5)
        v7_text = label_font.render('V7', True, white)
        screen.blit(v7_text, (WIDTH - 680, HEIGHT - 280))
        return v7_btn
    
    def draw_maj7_btn(self, color):
        maj7_btn = pygame.draw.rect(screen, color, [WIDTH - 500, HEIGHT - 300, 180, 90], 0, 5)
        maj7_text = label_font.render('Maj7th', True, white)
        screen.blit(maj7_text, (WIDTH - 460, HEIGHT - 280))
        return maj7_btn
    
    def draw_dim_btn(self, color):
        dim_btn = pygame.draw.rect(screen, color, [WIDTH - 1250, HEIGHT - 150, 180, 90], 0, 5)
        dim_text = label_font.render('Diminished', True, white)
        screen.blit(dim_text, (WIDTH - 1235, HEIGHT - 125))
        return dim_btn
    
    def draw_aug_btn(self, color):
        aug_btn = pygame.draw.rect(screen, color, [WIDTH - 1000, HEIGHT - 150, 180, 90], 0, 5)
        aug_text = label_font.render('Augmented', True, white)
        screen.blit(aug_text, (WIDTH - 985, HEIGHT - 125))
        return aug_btn
    
#defining the keyboard
claviers = []
#first octave
claviers.append(clavier('C1', False, False))
claviers.append(clavier('C1#', True, False))
claviers.append(clavier('D1', False, False))
claviers.append(clavier('D1#', True, False))
claviers.append(clavier('E1', False, False))
claviers.append(clavier('F1', False, False))
claviers.append(clavier('F1#', True, False))
claviers.append(clavier('G1', False, False))
claviers.append(clavier('G1#', True, False))
claviers.append(clavier('A1', False, False))
claviers.append(clavier('A1#', True, False))
claviers.append(clavier('B1', False, False))
#second octave
claviers.append(clavier('C2', False, False))
claviers.append(clavier('C2#', True, False))
claviers.append(clavier('D2', False, False))
claviers.append(clavier('D2#', True, False))
claviers.append(clavier('E2', False, False))
claviers.append(clavier('F2', False, False))
claviers.append(clavier('F2#', True, False))
claviers.append(clavier('G2',  False, False))
claviers.append(clavier('G2#', True, False))
claviers.append(clavier('A2', False, False))
claviers.append(clavier('A2#', True, False))
claviers.append(clavier('B2', False, False))
#third octave
claviers.append(clavier('C3', False, False))

CG = chord_generator()
DB = draw_chord_buttons()


WIDTH = 1400
HEIGHT = 800

#colors
black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128)
light_gray = (170, 170, 170)
dark_gray = (50, 50, 50)
cyan = (34, 179, 174)
light_green = (84,243,0)
purple = (203,61,242)
orange = (246, 114, 5)
red = (246, 5, 49)
red2 = (217, 16, 127)
answer_color = (57, 171, 8)

run = True
hidden_mode = False
quiz_pressed = False
mode_text = "Visible"
time = pygame.time.Clock()
fps = 60
screen = pygame.display.set_mode([WIDTH, HEIGHT])
label_font = pygame.font.Font('.\\timesi.ttf', 32)
medium_font = pygame.font.Font('.\\timesi.ttf', 24)
quiz_list = ['major_generator', 'minor_generator', 'diminished_generator', 'augmented_generator', 
             'dominant_seventh_generator', 'major_seventh_generator']
btn_func = {'major_generator': 'draw_maj_btn',
            'minor_generator': 'draw_min_btn',
            'dominant_seventh_generator': 'draw_v7_btn',
            'major_seventh_generator': 'draw_maj7_btn',
            'diminished_generator': 'draw_dim_btn',
            'augmented_generator': 'draw_aug_btn'}

pygame.display.set_caption('Chord Generator')

def draw_clavier(mode):
    drawn_claviers = []
    count = 0
    # one = True
    for i in range(len(claviers)):
        if claviers[i].is_black == False:
            if mode:
                color = white
            else:
                if claviers[i].is_pressed:
                    color = dark_gray
                else:
                    color = white
            white_clavier = pygame.draw.rect(screen, color, [150 + count * 75, 50, 75, 400], 0, 5)
            count += 1
            drawn_claviers.append(white_clavier)
        x_pos = count * 75 + 150
        pygame.draw.line(screen, black, (x_pos, 50), (x_pos, 450), 3)
    count = 0
    for i in range(len(claviers)):
        if claviers[i].is_black == True:
            if mode:
                color = black
            else:
                if claviers[i].is_pressed:
                    color = light_gray

                else:
                    color = black
            black_clavier = pygame.draw.rect(screen, color, [(count + 1) * 75  + 50, 50, 50, 225], 0, 5)
            drawn_claviers.insert(i, black_clavier)
        else:
            count += 1

    return drawn_claviers

def play_claviers(harmonic):
    # stop_playing()
    for i in range(len(claviers)):
        if claviers[i].is_pressed and claviers[i].must_play:
            claviers[i].note_play()
            claviers[i].must_play = False
            if not harmonic:
                draw_clavier(False)
                pygame.display.flip()
                sleep(1)
   
        elif claviers[i].is_pressed and claviers[i].sound_length > 0:
            claviers[i].sound_length -= 1
        elif not claviers[i].is_pressed or claviers[i].sound_length <= 0:
            claviers[i].note_stop()    

def stop_playing():
    for i in range(len(claviers)):
        claviers[i].note_stop()


while run:
    time.tick(fps) 
    screen.fill(black)
    drawn_claviers = draw_clavier(hidden_mode)

    #chord buttons
    maj_btn = DB.draw_maj_btn(gray)
    min_btn = DB.draw_min_btn(gray)
    v7_btn = DB.draw_v7_btn(gray)
    maj7_btn = DB.draw_maj7_btn(gray)
    dim_btn = DB.draw_dim_btn(gray)
    aug_btn = DB.draw_aug_btn(gray)

    #control buttons
    mod_btn = pygame.draw.rect(screen, light_green, [WIDTH - 750, HEIGHT - 150, 180, 90], 0, 5)
    mod_label_text = label_font.render('Mode', True, white)
    screen.blit(mod_label_text, (WIDTH - 700, HEIGHT - 125))
    mod_value_text = medium_font.render(mode_text, True, black)
    screen.blit(mod_value_text, (WIDTH - 695, HEIGHT - 95))

    stop_btn = pygame.draw.rect(screen, cyan, [WIDTH - 500, HEIGHT - 150, 180, 90], 0, 5)
    stop_text = label_font.render('Stop', True, white)
    screen.blit(stop_text, (WIDTH - 440, HEIGHT - 125))    

    repeat_btn = pygame.draw.rect(screen, purple, [WIDTH - 280, HEIGHT - 300, 150, 240], 0, 5)
    repeat_text = label_font.render('Repeat', True, white)
    screen.blit(repeat_text, (WIDTH - 250, HEIGHT - 200))

    #quiz buttons
    quiz_btn = pygame.draw.rect(screen, orange, [WIDTH - 1380, HEIGHT - 750, 115, 90], 0, 5)
    quiz_text = label_font.render('Quiz', True, white)
    screen.blit(quiz_text, (WIDTH - 1355, HEIGHT - 730))

    ans_melodic_btn = pygame.draw.rect(screen, red, [WIDTH - 1380, HEIGHT - 650, 115, 90], 0, 5)
    ans_text = label_font.render('Answer', True, white)
    screen.blit(ans_text, (WIDTH - 1373, HEIGHT - 635))
    ans_caption = medium_font.render('Melodic', True, black)
    screen.blit(ans_caption, (WIDTH - 1365, HEIGHT - 600))

    ans_harmonic_btn = pygame.draw.rect(screen, red2, [WIDTH - 1380, HEIGHT - 550, 115, 90], 0, 5)
    ans_text = label_font.render('Answer', True, white)
    screen.blit(ans_text, (WIDTH - 1373, HEIGHT - 535))
    ans_caption = medium_font.render('Harmonic', True, black)
    screen.blit(ans_caption, (WIDTH - 1373, HEIGHT - 500))

    #playing claviers
    play_claviers(True)

    for event in pygame.event.get(): # It seems it's necessary to use event.get() to have a normal flow of your program
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:

            if mod_btn.collidepoint(event.pos):
                if hidden_mode:
                    hidden_mode = False
                    mode_text = "Visible"
                else:
                    hidden_mode = True
                    mode_text = "Hidden"
            elif repeat_btn.collidepoint(event.pos):
                CG.repeat_chord()
            else:
                stop_playing()
                if maj_btn.collidepoint(event.pos):
                    CG.major_generator()
                elif min_btn.collidepoint(event.pos):
                    CG.minor_generator()
                elif v7_btn.collidepoint(event.pos):
                    CG.dominant_seventh_generator()
                elif maj7_btn.collidepoint(event.pos):
                    CG.major_seventh_generator()
                elif dim_btn.collidepoint(event.pos):
                    CG.diminished_generator()
                elif aug_btn.collidepoint(event.pos):
                    CG.augmented_generator()
                elif stop_btn.collidepoint(event.pos):
                    stop_playing()
                
                elif quiz_btn.collidepoint(event.pos):
                    quiz_pressed = True
                    hidden_mode = True
                    mode_text = "Hidden"
                    quiz_number = random.randrange(0, len(quiz_list), 1)
                    quiz_question = getattr(CG, quiz_list[quiz_number])
                    quiz_question()
                elif ans_melodic_btn.collidepoint(event.pos):
                    if quiz_pressed:
                        hidden_mode = False
                        mode_text = "Visible"

                        mod_btn = pygame.draw.rect(screen, light_green, mod_btn, 0, 5)
                        mod_label_text = label_font.render('Mode', True, white)
                        screen.blit(mod_label_text, (WIDTH - 700, HEIGHT - 125))
                        mod_value_text = medium_font.render(mode_text, True, black)
                        screen.blit(mod_value_text, (WIDTH - 695, HEIGHT - 95))
                        button = getattr(DB, btn_func[quiz_list[quiz_number]])
                        button(answer_color)

                        chord_notes = CG.get_chord_notes()
                        for i in range(len(chord_notes)):
                            if chord_notes[i] != -1:
                                claviers[chord_notes[i]].is_pressed = True
                                claviers[chord_notes[i]].must_play = True
                                claviers[chord_notes[i]].sound_length = length
                                play_claviers(False)
                        
                        pygame.event.clear()
                elif ans_harmonic_btn.collidepoint(event.pos):
                    if quiz_pressed:
                        hidden_mode = False
                        mode_text = "Visible"
                        button = getattr(DB, btn_func[quiz_list[quiz_number]])
                        button(answer_color)
                        pygame.display.flip()
                        chord_notes = CG.get_chord_notes()
                        for i in range(len(chord_notes)):
                            if chord_notes[i] != -1:
                                claviers[chord_notes[i]].is_pressed = True
                                claviers[chord_notes[i]].must_play = True
                                claviers[chord_notes[i]].sound_length = length
                                play_claviers(True)

                   
                        sleep(2)
                        pygame.event.clear() 
                else:
                    for i in range(len(drawn_claviers)):
                        if drawn_claviers[i].collidepoint(event.pos):
                            if claviers[i].is_black: # There is a problem with two rectangles intersecting which forced me write this snipet of code to prevent clicking both black and white claviers at the same time
                                claviers[i - 1].is_pressed = False
                                claviers[i].is_pressed = True
                                claviers[i].must_play = True
                            else:
                                if claviers[i - 1].is_pressed == False:
                                    claviers[i].is_pressed = True
                                    claviers[i].must_play = True
                        

        if event.type == pygame.MOUSEBUTTONUP:
            for i in range(len(drawn_claviers)):
                if drawn_claviers[i].collidepoint(event.pos):
                    claviers[i].is_pressed = False
    pygame.display.flip()

pygame.quit()