# Alla funzione vengono passati:
# - la radice, che corrisponde al nodo che esegue la funzione
# - il grafo della rete, definito da 
#   - l'insieme di stringhe "nodi"
#   - il dizionario "archi", che associa coppie di nodi collegati da un link alla metrica.
#   Questi due dati sono stati precedentemente derivati dai link state ricevuti dai vicini 
#   tramite il flooding.
# L'algoritmo svuota progressivamente l'insieme dei "nodi" aggiungendo
# quelli che rimuove al dizionario "raggiunti" e calcolandone la
# distanza.
# Il dizionario "raggiunti" e' la tabella di routing,
# e associa a ciascuna destinazione una t-upla (ultimo hop, distanza, primo hop),
# e viene aggiornato con il risultato dell'algoritmo.
# Il primo elemento della tupla, l'ultimo hop, e' funzionale  all'algoritmo, ma non e'
# rilevante ai fini del routing.
#
# In conclusione, un elemento nel dizionario "raggiunti" si legge come:
# destinazione = (primo hop, metrica, ultimo hop)
# I primi tre dati sono quelli che vanno a far parte della tabella di routing,
# mentre il terzo è funzionale solo all'esecuzione dell'algoritmo

def dijkstra(radice, nodi,archi):
  raggiunti = {radice: ("",0,"")} # è un dizionario, il valore è una t-upla di 3 elementi
  print ("Nodi:",nodi,"\nArchi:",archi,"\nRadice:",radice,"\nRaggiunti:",raggiunti)
  while nodi:      # Si arresta quando l'insieme "nodi" e' vuoto 
# PREPARAZIONE
# Trovo nodo con distanza minima tra quelli raggiunti
      print("=========== Inizio iterazione ============")
      nodo_min = None
      for nodo in nodi:
        if nodo in raggiunti:
          if nodo_min is None: nodo_min = nodo
          elif raggiunti[nodo][1] < raggiunti[nodo_min][1]: nodo_min = nodo
      if nodo_min is None: break
      print("Nodi=",nodi,". Elimino "+nodo_min)
      nodi.remove(nodo_min)
      distanza_min = raggiunti[nodo_min][1]
# Calcolo mappa archi uscenti da min -> distanza da min
      distanze_da_min={}
      for arco in archi.keys():
        if arco[0] == nodo_min: distanze_da_min[arco[1]]=archi[arco]
        if arco[1] == nodo_min: distanze_da_min[arco[0]]=archi[arco]
      print("Distanze da " + nodo_min + ":", distanze_da_min)
#      print(raggiunti)
#ALGORITMO di Dijkstra
      for destinazione in distanze_da_min.keys():
# Calcolo la distanza della destinazione passando da nodo_min
        nuova_distanza = distanza_min + distanze_da_min[destinazione]
# Se migliore della precedente sostituisco distanza e prossimo
        if destinazione not in raggiunti or nuova_distanza < raggiunti[destinazione][1]:
          if raggiunti[nodo_min][2] == "":
            raggiunti[destinazione] = (nodo_min, nuova_distanza, destinazione)
          else:
            raggiunti[destinazione] = (nodo_min, nuova_distanza, raggiunti[nodo_min][2])
      print("Raggiunti = ",raggiunti)
  return raggiunti

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
l = dijkstra(
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
print(l)
