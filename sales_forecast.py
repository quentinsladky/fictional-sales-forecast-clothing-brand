#Sales-Forecast-Clothing-Brand.py
import numpy as np
import matplotlib.pyplot as plt

#sonnées de ventes 
MOIS = np.arange(1,13)
VENTES = np.array([20,25,23,32,44,39,43,50,53,54,61,55])#ventes victives par mois

#stat de base 
Moyenne_ventes = np.mean(VENTES)
Minimum_ventes = np.min(VENTES)
Maximum_ventes = np.max(VENTES)
Croissance_ventes = ((VENTES[-1]-VENTES[1])/VENTES[1])*100
print(f"Moyenne des ventes = {Moyenne_ventes:.0f}")
print(f"Minimum_ventes = {Minimum_ventes}")
print(f"Maximum_ventes = {Maximum_ventes}")
print(f"Croissance_ventes = {Croissance_ventes:.1f}")

#previsions sur plusieurs mois (3 prochains)
COEFFS = np.polyfit(MOIS, VENTES, 1)
TENDANCE = np.poly1d(COEFFS)
MOIS_PREVISIONS = np.array([VENTES[-1],TENDANCE(13),TENDANCE(14),TENDANCE(15)])
print(f"tendance 13ème mois = {MOIS_PREVISIONS[0]:.1f}")
print(f"tendance 14ème mois = {MOIS_PREVISIONS[1]:.1f}")
print(f"tendance 15ème mois = {MOIS_PREVISIONS[2]:.1f}")
MOIS_FUTURS = np.array([12,13,14,15]) 

#tracé du graphqiue de l'évolution 
plt.figure() #crée le graphique 
plt.plot(MOIS, VENTES,label="Ventes réelles") #courbe des ventes réelles 
plt.plot(MOIS_FUTURS, MOIS_PREVISIONS, "r--", label="Ventes futures") #courbe des prédictions futurs 
plt.title("Évolution des ventes marque")
plt.xlabel("Mois") #nom de l'ordonné 
plt.ylabel("Ventes par unité") #nom de l'abcisse 
plt.grid(True, alpha=0.5) #cadrillage 
plt.savefig("/Users/quentin/Desktop/sales_forecast.png", dpi=150)
plt.legend() #noms des courbes 
plt.show()