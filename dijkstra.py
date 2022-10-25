# Alla funzione vengono passati:
# - la radice, che corrisponde al nodo che esegue la funzione
# - il grafo della rete, definito da 
#   - l'insieme di stringhe "nodi"
#   - il dizionario "archi", che associa coppie di nodi collegati da un link alla metrica.
#   Questi due dati sono stati precedentemente derivati dai link state ricevuti dai vicini 
#   tramite il flooding.
# L'algoritmo svuota progressivamente l'insieme dei "nodi" aggiungendo
# quelli che rimuove al dizionario "routingTable" e calcolandone la
# distanza.
# Il dizionario "routingTable" e' la tabella di routing,
# e associa a ciascuna destinazione una 2-upla (primo hop, distanza),
# e viene via via aggiornato dall'algoritmo.

def dijkstra(radice, nodi,archi):
  # Inizializzo la oruting table con la radice e le metriche dei nodi adiacenti
  routingTable = {radice: ("",0)} 
  routingTable.update({n2: (n2,m) for (n1,n2),m in archi.items() if n1 == radice})
  routingTable.update({n1: (n1, m) for (n1,n2),m in archi.items() if n2 == radice}) 
  print ("Nodi:",nodi,"\nArchi:",archi,"\nRadice:",radice,"\nroutingTable:",routingTable)
  while nodi:      # Si arresta quando l'insieme "nodi" e' vuoto 
      print("=========== Inizio iterazione ============")
      print("Nodi=",nodi)
# PREPARAZIONE
# Trovo nodo con distanza minima tra quelli nella tabella di routing
      nonRaggiunti = {k: v for k, v in routingTable.items() if k in nodi}
      print("Distanze non raggiunti: ", nonRaggiunti)
      nodo_min = min(nonRaggiunti.keys(), key=lambda d: nonRaggiunti[d][1])
      print("Elimino "+nodo_min)
      nodi.remove(nodo_min)
      distanza_min = routingTable[nodo_min][1]
# Calcolo mappa archi uscenti da min -> distanza da min
#      distanze_da_min={}
      distanze_da_min = {dest: m for (src,dest),m in archi.items() if src == nodo_min}
      distanze_da_min.update({src: m for (src,dest),m in archi.items() if dest == nodo_min}) 
#      for ((src,dest),metrica) in archi.items():
#        if src == nodo_min: distanze_da_min[dest]=metrica
#        if dest == nodo_min: distanze_da_min[src]=metrica
      print("Link uscenti da " + nodo_min + ":", distanze_da_min)
#      print(routingTable)
#ALGORITMO di Dijkstra
      for destinazione in distanze_da_min.keys():
# Calcolo la distanza della destinazione passando da nodo_min
        nuova_distanza = distanza_min + distanze_da_min[destinazione]
# Se migliore della precedente sostituisco distanza e prossimo
        if destinazione not in routingTable or nuova_distanza < routingTable[destinazione][1]:
          routingTable[destinazione] = (routingTable[nodo_min][0], nuova_distanza)
      print("Tabella di routing: ",routingTable)
  print("=========== Algoritmo terminato ===========")
  return routingTable

# 4 nodi: provare a disegnare la rete
#l = dijkstra(
#'a',
#set(['a','b','c','d']),	# l'insieme dei nodi
#{('a','b'):1,		# l'insieme degli archi (coppie di nodi)
# ('b','c'):2,
# ('a','d'):3,
#})
#print(l)

# Questo grafo e' tratto dalla pagina di wikipedia, arricchito con
# un ulteriore nodo '7' raggiungibile solo da nodi non adiacenti alla 
# radice
rt = dijkstra(
'1',
set(['1','2','3','4', '5', '6', '7']),
{('1','2'):7,
 ('1','3'):9,
 ('1','6'):14,
 ('2','3'):10,
 ('2','4'):15,
 ('3','4'):11,
 ('3','6'):2,
 ('6','5'):9,
 ('4','5'):6,
 ('4','7'):6,
 ('5','7'):2
})
print("\nTabella di routing:",rt)
