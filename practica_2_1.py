# -*- coding: utf-8 -*-
"""Practica 2.1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iwAjy-1_IaUQVmWiu4-WSRa1O7uejkY3
"""

import numpy as np

class Simulacion:

  t_atencion = 30

  def __init__(self):
    self.num_en_sistema = 0
    self.relog = 0.0

    self.t_llegada = self.interarribo()
    self.t_salida = float('inf')

    self.num_llegadas = 0
    self.num_salidas = 0
    self.t_sistema = 0.0

  def tiempo_anticipacion(self):
    t_evento = min(self.t_llegada, self.t_salida)
    self.t_sistema += self.num_en_sistema*(t_evento -  self.relog)
    self.relog = t_evento

    if self.t_llegada <= self.t_salida:
      self.evento_llegada()
    else:
      self.evento_salida()

  def evento_llegada(self):
    self.num_en_sistema += 1
    self.num_llegadas += 1
    if self.num_en_sistema <=1:
      self.t_salida = self.relog + self.t_atencion

    self.t_llegada = self.relog + self.interarribo()

  def evento_salida(self):
    self.num_en_sistema -= 1
    self.num_salidas += 1
    if self.num_en_sistema > 0:
      self.t_salida = self.relog + self.t_atencion
    else:
      self.t_salida = float('inf')

  def interarribo(self):
    return np.random.uniform(0.5,50)

s = Simulacion()

for i in range(50000):
  s.tiempo_anticipacion()

print(s.t_sistema)