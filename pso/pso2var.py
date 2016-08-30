import numpy as np
import matplotlib.pyplot as plt

def findBestGlobalIndex(performanceFn):
  return np.argmin(performanceFn)

nParticles = 10
iterations = 10000
c1 = 0.01
c2 = 0.01

x1 = np.random.rand(nParticles)
x2 = np.random.rand(nParticles)

bestLocalParticles = x1 # Mejores locales iniciales x1pl
bestLocalParticlesPerformance = 10000000 * np.ones(nParticles) #Desempeno local inicial fpl

bestGlobal = 0 #x1pg
bestGlobalPerformance = 1000000 #fpg

speed = np.zeros(nParticles) # Velocidades iniciales vx1

for k in range(iterations):
  performanceFn = x1 ** 2 # Calcular los desempenos del enjambre
  # Encontrar al mejor global
  index = findBestGlobalIndex(performanceFn)
  if (performanceFn[index] < bestGlobalPerformance):
    bestGlobal = x1[index]
    bestGlobalPerformance = performanceFn[index]

  for i in range(nParticles):
    if (performanceFn[i] < bestLocalParticlesPerformance[i]):
      bestLocalParticles[i] = x1[i]
      bestLocalParticlesPerformance[i] = performanceFn[i]

  speed = speed + c1 * np.random.rand(nParticles) * (bestGlobal - x1) \
                 + c2 * np.random.rand(nParticles) * (bestLocalParticles - x1)

  x1 = x1 + speed

performanceFn = x1 ** 2
x2 = np.arange(-10, 10, 0.01)
y = x2 ** 2

plt.plot(bestGlobal, bestGlobalPerformance, 'ro', x, performanceFn, 'b.', x2, y, 'b')
plt.show()
