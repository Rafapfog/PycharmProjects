# faça um programa em Python que abra e reproduza o audio de um arquivo MP3.
import winsound
import pygame
pygame.init()
pygame.mixer_music.load('ex021.mp3')
pygame.mixer_music.play()
input()
pygame.event.wait()
