# 021 - Faça um programa em python que abra e reproduza o áudio de um arquivo MP3
import pygame
pygame.init()
pygame.mixer.music.load('arquivo.mp3')
pygame.mixer.music.play()
pygame.event.wait()