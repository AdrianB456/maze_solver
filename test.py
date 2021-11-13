content = '''
ALGORITME 
Q LEARNING

Alumne: Adrian Vasile Belei
Curs: 2nd BAT Tecnològic
Institut: Celestí Bellera
Tutor: Òscar Esteve
Curs: 2021 - 2022

Índex

Introducció

Història

Us

Exemples

Limitacions

Conclusió

Introducció



Avui en dia podem veure millons d’exemples d'intel·ligència artificial, per exemple, potser utilitzes algun tipus de xarxes socials i segurament la raó per la qual utilitzes molt aquella aplicació és perquè hi ha una intel·ligència artificial que monitoritza el que fas en la aplicació per després atreure’t cada vegada més. O potser t’agrada utilitzar aquells filtres que us fan a tu i als teus amics una cara divertida. Això realment és degut a un tipus d’intel·ligència artificial que és diu “image recognition” o reconeixement d’imatge, que és responsable de identificar les diferents parts de la teva cara.      

He escollit aquest tema perquè sempre m’ha fascinat el fet de que d’una cosa tan bàsica hagi sorgit un sistema que pot prendre decisions per si mateix i de manera automatizada. Crec que és un pas molt important en la nostra evolució humana, ja que pot complir tasques en diferents dominis (com informàtica,  màrqueting, matemàtiques, ciència, etc.) que abans no es podien complir.

Potser t'estaras preguntant què és la intel·ligència artificial, o quina és la relació entre aquesta i el Q learning. Primer de tot hem d’entendre que el Q learning és un tipus d'intel·ligència artificial i n’hi ha diferents categories entre aquestes dues.


A continuació explicaré cadascuna d’elles.

Intel·ligència artificial: És l'habilitat d’un programa de poder prendre decisions semblants a la d’un humà.

Machine Learning: Un sistema que té un objectiu i “apren” a complir aquell objectiu de la millor manera possible i generalment ho fa basant-se en el concepte de prova i error. L’aprenentatge s’acaba quan es considera que no es pot millorar més.


Reinforcement learning: És l’intent de confrontar un agent en una situació que és similar a un videojoc, però representa una situació que es pot aplicar en la vida real. Aquest agent interacciona amb l’entorn per aprendre què ha de fer i què no ha de fer fins arribar a l’objectiu. Si agafem l’exemple anterior, el ratolí seria l’agent i el laberint seria la situació.

Q learning: El concepte principal d’aquest algoritme és que depenent d’un estat i una acció, l’agent pot rebre una penalització o una recompensa depenent de que tan favorable ha estat aquella acció. Per exemple la posició d’un cotxe, la seva velocitat i l’angle en el que esta direccionat és un estat, l’acció pot ser girar a l'esquerra, girar a la dreta, etc. i la penalització es pot aplicar si s’ha xocat amb una paret o no.                                                            

Mentre estava plantejant el tema d’aquest projecte he trobat molta informació sobre aquest algoritme, llavors m’he posat la pregunta: És el Q learning una eina útil per el nostre dia a dia? I si ho és, quina diferencia n’hi ha entre aquesta i un altre algoritme?


El procediment es basa en trobar els límits d’aquest algoritme creant diferents proves en les que el Q learning tindrà un rol molt important.

Primer he fet la recerca de tota la informació necessària per veure en que consta, com s’ha creat aquest algoritme i com podria fer la meva pròpia versió d’aquest algoritme.

Una vegada he entès com funciona aquest algoritme i he creat un exemple de com es pot aplicar aquest tipus d'intel·ligència artificial en un problema comú del nostre món, tractaré de veure quines limitacions té i com resoldre aquelles limitacions.

Història


Abans d’entendre la història del Q learning hem d’entendre la història del reinforcement learning, quin té un rol molt important en aquest tema.

Al principi de tot, el reinforcement learning ha estat dividit en dues parts independents.

La primera s’enfoca en el concepte matemàtic “optimal control” que es basa en l’intent d’optimitzar un sistema dinàmic per complir els requisits desitjats. Una forma és utilitzant l’equació Bellman, que intenta trobar el millor control (una variable que l’agent o el controlador pot canviar) depenent d’una funció de pèrdua, que es responsable per decidir què tan favorable ha estat una acció. O una altra versió de l’equació Bellman és el Markov Decision Process (MDP), però aquesta ajuda a organitzar les diferents decisions que pot tenir un agent en casos en el que les decisions són parcialment aleatòries i parcialment sota el control de l’agent (o majoritàriament, quan parlem de MDP, un “controlador”). 

Els dos mètodes que he explicat anteriorment tenen la característica d’agafar un problema i amb una funció, calcular cada part del problema (cada situació), de tal manera que un problema gran es divideix en problemes més petits, que si els resols et donen el resultat del problema principal (procediment que es diu “programació dinàmica”).


L'altra part del reinforcement learning és el concepte de prova i error (també conegut com a "Law of Effect") que abans era sols un concepte que s'utilitzava en la psicologia i consta que si un individu ha fet alguna cosa que l'ha satisfet, llavors és molt més probable que la torni a fer, però en canvi si ha fet una cosa que no li ha agradat gens, llavors és poc probable que ho faci un altra vegada. Quan parlem de prova i error ens referim a dos aspectes molt importants:




Selecció: L'agent ha d'escollir entre vàries accions depenent de com és la situació actual


Associatiu: Si l'agent es troba en una situació similar a la que ha estat abans, llavors farà uns moviments similars a aquella situació.


El model prova i error va ser implementat en l'enginyeria informàtica el 1954 per Minsky, Farley i Clark. La primera màquina que va funcionar amb aquest concepte es va dir SNARC (Stochastic Neural-Analog Reinforcement Calculators), però poc temps després s'ha fet un altra versió, a la qual li van posar el nom de "reinforcement learning", però en aquell moment hi va haver un problema, no se sabia com dir-li a la màquina que tan bé ha fet una acció, ja que hi havia massa.

Després d'aquest període Farley i Clark perden interès pel reinforcement learning i passen a estudiar el supervised learning i reconeixement de patrons. Com la gent es pensava que ells seguien treballant amb el reinforcement learning, això va crear una gran confusió entre aquesta i el supervised learning, cosa que encara es pot veure en alguns documents.

Tot i això la gent aconsegueix crear tota mena de grans invents amb aquest mètode d'aprenentatge com màquines que poden jugar tres en ratlla (com va ser la màquina MENACE de Donald Michie) o una màquina que pot posar en equilibri un pal (com el controler BOXS de Michi i Chambers), però hem de recordar que no era realment reinforcement learning, ja que aquest tipus d'intel·ligència artificial es basava més a seguir un model ja determinat que no pas mirar per si mateix quines són les errades que ha fet, el que significa que ells, realment el que aplicaven era el supervised learning. És sols quan Widrow, Gupta i Maitra creen un algoritme que funciona amb senyals que representen si la màquina ha fet un error o no, que es comença a implementar la forma moderna del concepte "prova i error" i es para d'utilitzar un model que l'agent ha de seguir.



El 1980 es considera l'any en el qual els conceptes de "prova i error" i "optimal control" s'uneixen. N'hi ha un període en el qual la gent comença a oblidar-se del reinforcement learning, però després torna amb els estudis de Klapof i els seus algoritmes que representen molt bé la idea moderna del reinforcement learning. Amb aquest nou període es forma una tercera i menys famosa branca de reinforcement learning, aquesta es diu temporal-difference learning i es basa a fer aprendre a fer prediccions depenent de futurs valors. Aquest algoritme encara que no sigui el més conegut de tots, és molt important per la situació actual de reinforcement learning. Temporal-difference learning sorgeix de la psicologia d'aprenentatge dels animals.

En 1989 Chris Watkins va introduir Q learning com una branca del reinforcement learning. En la seva tesi de doctorat l'anomena "learning from delayed rewards". Un enfocament similar va ser estudiat 8 anys abans amb la màquina de Bozinovski "Crossbar Adaptive Array" (CAA), que en aquell període el problema tenia el nom de "Delayed reinforcement learning". La matriu de la memòria que utilitza aquell problema (W = ||(s, a)||) és molt similar a la taula Q que s'utilitza en Q learning.


Com funciona Q learning


Hem d'entendre que Q learning és un algoritme de la categoria "model-free", és a dir que no fa servir la funció de recompensa que utilitza el sistema de control MDP, ni tampoc fa servir una eina que es diu "distribució de la probabilitat de transició" (el que també s'anomena com "Markov chain") quin el seu propòsit és calcular la probabilitat de futures accions depenent de les que ja s'han fet. És a dir que si l'agent ha fet moltes vegades una acció en concret, l'agent serà més probable fer la mateixa acció.

El Q learning no és sols un mètode, sinó que es pot separar en diferents categories que funcionen diferent, però es basen en conceptes bastants similars. Entre aquests es pot determinar Vanilla Q learning, Deep Q learning i Double Q learning.

Nota: La Q de "Q learning" ve de qualitat, és a dir que l'agent fa una acció depenent de la seva qualitat.



Vanilla Q learning

El vanilla Q learning és la categoria menys complex de totes. Per entendre Vanilla Q learning hem d'entendre els següents conceptes:

Situació (s): Quina és la situació actual de l'agent. Generalment això sols implica la posició de l'agent, però depenent del problema al qual aquesta s'enfronta, es poden incloure més variables com angle, pes i moltes altres.

Acció (a): Les diferents accions que pot fer l'agent per interaccionar amb l'entorn que se li ha posa. Majoritàriament es tracta de fer un desplaçament de l'agent d'una situació cap a un altre, però n'hi ha casos en els quals no es tracta sols de fer un desplaçament, sinó interaccionar d'un altra manera (com agafar una cosa del terra, o llençar una cosa a terra, etc.)


Episodis: Un episodi es refereix a un intent de l'agent de passar el problema. Per exemple, si fas que el teu agent aprengui a fer un salt, llavors cada salt és un intent, per tant un episodi.

La Taula Q: Aquesta taula és com un registre de quina és la millor opció de cada situació. Ho fa assignant a cada acció de cada situació un nombre aleatori (o en pocs casos un número en concret), quan l'agent passa per aquella situació escull l'acció amb el valor més gran. Després d'haver fet l'acció, la taula Q s'actualitza amb la situació que es troba l'agent posteriorment, per exemple si l'agent després d'haver fet l'acció es xoca amb la paret, llavors el valor de la situació anterior tindrà un valor més petit per evitar que es repeteixi aquella acció. Aquest procés l'explicaré amb més detall més endavant.

Recompensa (r): un número que rep l’agent després de cada acció per entendre que tan favorable ha estat aquella acció, per exemple si l’agent ha anat al .

La Taula de recompensa (opcional): Aquesta és una taula en la qual es guarda totes les recompenses de cada situació on l'agent es pot trobar, per exemple si la situació actual és que hem guanyat, llavors ens dona una recompensa gran, però si l'agent s'ha xocat amb una paret, llavors ens dona una penalització bastant gran.

Factor de descompte (γ): És un número entre 0 i 1 que indica que tant ens interessa les recompenses futures a diferència de les actuals, ja que no sols ajuda a l'agent explorar l'entorn i trobar el camí més curt, però també és per evitar situacions en les quals es repeteixen les mateixes accions.

Epsilon (ε): És un número entre 0 i 1 que indica la probabilitat de l'agent de fer un moviment aleatori. D'aquesta manera l'agent es posa en una situació que potser no ha estat abans, llavors explora l'entorn per veure si hi ha un camí més curt que no l'ha vist abans, en comptes d'anar al mateix camí tot el temps.

Velocitat d'aprenentatge (α): És un número entre 0 i 1 que indica que tan ràpid volem que el nostre agent aprengui. La forma en la qual aquest component afecta l'aprenentatge de l'agent estarà explicat quan començo a explicar l'equació Q. 

Entorn

El primer pas a fer un agent que pugui utilitzar el Q learning és fer un entorn que aquesta pugui practicar. Un entorn pot dependre molt de quin és l'objectiu que tu vols complir amb aquesta intel·ligència artificial.

El procés de trobar la forma amb la qual dissenyar un entorn és molt simple, però el problema és fer l'entorn massa complicat. Coses que s'han de tenir en compte a l'hora de fer l'entorn són les següents:

No es pot canviar l'entorn a mesura que l'agent va entrenant. És molt important que si vols crear un entorn per la teva intel·ligència artificial, que ho facis amb un entorn estable, perquè el procés d'entrenament de Vanilla Q learning fa de tal manera que si l'agent ha fet un error una vegada pensarà que en fer la mateixa acció tindrà el mateix resultat. Explicat d'una altra manera, pensa com una persona que té els ulls tapats té l'objectiu de trobar la sortida d'una habitació diverses vegades, però en la dècima vegada que ha de fer, tu treus una taula que abans estava entre ell i la sortida. Encara que la taula no estigués allà, la persona amb els ulls tapats dedueix que la taula segueix sent allà. El mateix passa amb Vanilla Q learning, l'agent, una vegada que s'ha donat d'un cos, ell pensarà que el cos seguirà sent allà.


Ara que ja entenem això hem de concentrar-nos en determinar quines seran les dades que crearan la nostra taula Q. Primer hem de determinar les categories per cadascuna de les parts de la nostra taula. Primer sempre es tenen en compte les categories de les situacions i per últim la categoria de les accions. Per posar aquestes dades en forma de taula, cada categoria estarà composta d'una llista que tindrà la següent categoria i així successivament, per explicar-lo millor he fet l'esquema següent:


Imagineu que el nostre entorn té 4 possibles posicions en l'eix x, 4 possibles posicions en l'eix y i 4 possibles anglès (0º/360º, 90º, 180º o 270º), llavors en cada possible "x" poso una llista amb totes les possibles "y" i el mateix amb les y i els angles. Ara fixat que realment tenim una forma d'indexar molt fàcilment cada situació s, per exemple si vull indexar la situació que té com a x 4, com a y 1 i l'angle és 90º (el segon possible angle), llavors me'n vaig a la 4ª llista de les y, on trobaré totes les possibles y que hi ha, però a mi m'interessa la 1ª posició y, una vegada l'he localitzat tinc 4 possibles angles dels quals m'interessa l'angle 2 (90º). Amb aquest procediment es pot trobar molt fàcilment cada s que hi ha en tot l'entorn.

L'única cosa que li falta a la nostra taula Q és que cada a situació s hi ha una llista de zeros com la següent [0, 0, 0, ...], quin seria el número per defecte de cada acció (no tot el temps vols que el número sigui 0) i el número de 0 que hi ha en cada situació és el nombre de possibles accions que té l'agent, d'aquesta manera té un valor 0 per cada acció, que després anirà canviant el valor.

Una part que també és molt important és fer que l'entorn sigui visual, ja que volem veure com el nostre agent entrena. En aquest cas hi han moltes maneres de visualitzar l'entorn, però jo sempre utilitzo un mòdul (un set d'eines que estan creades per programadors per no crear tot des de 0, que també es pot referir com a llibreria) que és molt fàcil d'utilitzar i es diu Pygame. Explicaré com l'he fet servir en la part de programació.

Agent

Una vegada tenim l'entorn fet hem de crear l'agent. El que aniria sent la part visual, l'agent serà sols una imatge que interacciona amb l'entorn (i també podria girar si dones l'opció de fer-ho). El que determina la seva situació és generalment una llista com la següent [posició x, posició y, angle]. Aquesta llista està feta d'aquesta manera per facilitar el procés d'indexar la situació en la taula Q.

El moviment d'aquest agent està determinat per un canvi d'un estat a un altre, per exemple si està en la situació [1, 3, 4] (que recordem que aquesta llista significa [x, y, angle]) i vol anar cap a la dreta, és a dir una posició mes en l'eix x, pasem d'una situació [1, 3, 4] a una [2, 3, 4].

Procés d’entrenament.

Com vaig explicar abans, a cada situació s hi ha una llista amb un 0 per cada possible acció, significant que si tenim 4 possibles accions tenim a cada situació una llista com aquesta: [0, 0, 0, 0].

El significat d'aquests valors és la qualitat que té cada acció en cada situació, aquest valor està a 0 perquè l'agent realment no sap res del seu entorn. Per canviar aquest valor s'ha de fer un procés d'entrenament.

En el procés d'entrenament l'agent ha de passar per diversos intents de resoldre el problema. Mentre que l'agent passa per diferents situacions, els valors de cada acció que ell fa es canvia. Quan el procés d'entrenament acaba, el problema és considerat "resolt" i per demostrar-ho l'agent sols ha d'escollir les accions amb valor més gran i es podrà veure la solució d'aquell problema, o a vegades es guarda els moviments que condueix fins a la solució en un fitxer per després poder comprovar si realment s'ha resolt o no el problema, però si l'agent encara no ha pogut resoldre durant tot el temps d'entrenament, s'ha de verificar quin és el factor que impedeix que l'agent pugui arribar a la solució, aquest és un procés del qual parlarem més endavant.

En cada episodi (és a dir intent) l'agent interacciona amb el seu entorn, però com ho fa?

A cada situació l'agent escull l'acció amb major valor, és a dir que si les accions es presenten en una llista com aquesta [-0.99, 2.34, 0, -10], el valor més gran és el segon, el que significa que la segona opció serà la que escollirà l'agent. Per calcular la qualitat d'aquesta acció s'utilitza la següent equació:

On q(s, a) és el valor de l'acció que ha fet (en aquest cas 2.34), Rt+1 és la recompensa que l'agent rep i maxq(s', a') és el valor més gran de la següent situació. Hi ha més variacions d'aquesta funció, però aquesta és la que a mi m'ha sigut més útil.

Les parts d'aquesta equació funcionen de la següent manera:

El ritme d’aprenentatge (α) en aquesta equació ens indica que tant valorem la informació nova sobre la vella, per això en la part (1 - α) * q(s, a) de l’equació, el ritme d’aprenentatge té el rol de disminuir el valor vell (old value) i en la part α(Rt+1 + γ * maxq(s’, a’)) on té l’objectiu d’augmentar el valor nou (learned value).

El maxq(s', a') és la part més important de l'aprenentatge, perquè és la part que crea la combinació que condueix a la solució del problema. La forma en la qual aquesta ajuda a fer això és molt simple: si en una situació hi ha els següents valors [-100, -0.99, 100, -100] el maxq(s', a') serà 100 (aquest valor és tan gran perquè el més probable condueix a la solució del problema, és a dir que volem que l'agent passi per aquella situació per tal d'arribar a la solució), llavors si l'agent està en una situació posterior d'aquesta, llavors amb el maxq(s', a') fa que l'agent trobí quin és el millor camí a poc a poc, amb cada intent. 

El Rt+1 és la variable que indica la penalització/recompensa que l’agent rep a cada acció. Generalment hi ha tres tipus de recompensa/penalització:

Penalització per cada acció: com no volem que l'agent vagi pel mateix camí tot el temps, se li posa una petita penalització cada vegada que fa una acció que no condueix cap a cap part. Aquesta penalització generalment és -1, ja que és prou petita per no afectar massa.
Penalització per fer un error: cada vegada que l'agent ha fet un error, volem que aquella acció sigui nul·la, és a dir que tingui un valor tan petit que no hauria de recrear mai la mateixa acció. A vegades veuràs que un agent segueix fent errors evidents, això és causat per l'epsilon (que està explicat en els conceptes previs per entendre Vanilla Q learning). El valor d'aquesta penalització generalment és -100, però has de tenir en compte que la penalització per cada acció és acumulativa, llavors és possible que si el problema és massa complicat la penalització de fer un error, pot arribar a ser un valor més gran que la penalització per cada acció, per tant l'agent preferiria fer aquell error evident a fer una acció que no condueix a res.
Recompensa per arribar a la solució o fer una part: L'agent no sols pot rebre una recompensa per trobar una solució, però pot rebre varies depenent de quin és el seu objectiu, quin és un procés molt més complicat de fer. El valor d'aquesta recompensa pot ser qualsevol valor mentre sigui més gran que la de la penalització per cada acció, però s'ha de tenir en compte que la quantitat d'aquesta recompensa afecta la velocitat amb la qual la solució es resol. Per exemple si el valor és massa petit, haurà de passar per diversos intents en ordre de trobar la solució de tot el problema, però la solució serà més eficaç, o si el valor és massa gran, tindrà un major impacte en tot l'entorn, significant que troba una solució molt ràpid, però no tan eficaç.

Com es pot observar l'equació se separa en dues parts: un valor nou (learned value) quina és la part que realment aprèn, i un valor vell (old value) per poder acumular el valor per poder diferenciar quin és el millor camí. Amb aquestes dues parts l'agent pot canviar els valors de cada acció per entendre quina és la millor acció a cada situació. Aquest procediment es diu programació dinàmica on un problema es divideix en petits problemes i que la solució de tots els petits problemes dona la solució al problema gran, molt similar a com l'agent resol cada situació en particular per trobar la solució de tot el problema.

Una vegada l'agent ha entrenat suficient, els valors han canviat tant que partint de la posició inicial un agent podria trobar la solució sols seguint les accions amb major valor.


I si no s’ha resolt el problema?

No qualsevol combinació de variables condueix automàticament a la solució, per tant hi ha una manera de comprovar quina és la variable que afecta no complir l'objectiu.

Primer s'ha de fer tres llistes per guardar el progrés de l'agent durant la fase d'entrenament. La primera serveix per determinar quin va ser el valor mitjà de les accions que l'agent ha fet en un intent, el segon serveix per saber quin va ser el valor mínim d'un intent, i el tercer per registrar el valor màxim d'un intent.

Una vegada ja s'han fet les llistes amb les dades que s'han extret de cada episodio, l'únic que falta és expressar-la en un gràfic, d'aquest gràfic tu pots canviar les dades que l'agent rep per determinar quina és la variable que dona problemes a l'agent.

Moltes vegades aquest procés s'utilitza també per veure quina combinació és més eficient que altre, perquè un agent pot arribar a una solució, però no a la millor solució, o ha arribat a la millor solució que hi ha, però ha trigat massa a fer-ho.



Exemple de Vanilla Q learning (maze solver)

Tot el codi es podra veure i instalar des de:
https://github.com/AdrianB456/maze_solver

Traduït de l'anglès, un "maze solver" significa un solucionador de laberint. Com bé el seu nom indica, el maze solver és un tipus de problema que consta en arribar d'un punt A a un punt B sense xocar amb cap obstacle. Per crear l'entorn d'aquest programa, vaig crear un altre fitxer que es diu "create_maps.py", que bàsicament és una forma interactiva de crear un mapa per l'agent. Aquests mapes estaran després guardats en un fitxer que s'anomenarà "map[número del mapa].pkl" per poder utilitzar-les quan es necessita.

La raó per la qual vaig escollir aquest problema ha sigut perquè és un problema que qualsevol programa de navegació s'ha d'enfrontar tot el temps, llavors s'ha de saber com fer la ruta més curta entre dos punts sense tardar massa temps.

Per fer aquesta intel·ligència artificial vaig fer servir els següents requisits:

Python: és un llenguatge de programació que serveix per a molts àmbits i és molt fàcil d'aprendre, però les dificultats que aquesta té és que és bastant lenta i que el codi és obert, és a dir que un programa fet en un altre llenguatge serà compilat en un fitxer que ningú no entendria res, en canvi en python es pot veure tot el codi, cosa que a vegades pot causar problemes.

Numpy: és una llibreria que ajuda a fer llistes molt fàcilment i a més té altres eines per crear, esborrar, indexar i manipular llistes que ajuda molt en el procés de qualsevol programa que requereix llistes, sense aquesta hi haurà un procés molt més lent i complex de desenvolupament d'un programa.

Pygame: és una llibreria que generalment s'utilitza per videojocs, però en aquest cas ens ve molt de gust tenir una llibreria que ens permet visualitzar molt fàcilment qualsevol mena d'imatge, forma, animació, etc. L'únic inconvenient és que si hi ha massa cosa a processar, el "frame rate" (es a dir la velocitat del programa per donar una imatge) serà molt baixa, per tant no es veuria molt bé que estaria passant.

Pickle: és una llibreria que et permet guardar informació en forma de bites, ja que un programa no pot sols utilitzar text per guardar dades, sinó que hi ha molts altres tipus de variables que s'han de tenir en compte que no es poden posar en un sol fitxer.

Random, sys, os: llibreries bàsiques que simplement ajuden en el procés de creació d'un programa.

El primer pas és crear un fitxer que es diu main.py, quin és generalment el nom de la part principal de qualsevol programa fet amb aquest llenguatge de programació. Després afegir totes les eines que utilitza el nostre programa:



El import serveix per afegir aquestes eines al nostre projecte, el import ... as ... fa el mateix, però canviant el nom de l'eina per facilitar el procés i el pygame.init() simplement inicialitza totes les eines de pygame.

Ara que totes les eines estan preparades s'ha de posar les dades de la pantalla i tot seguit s'ha d'inicialitzar la pantalla junt amb una eina que ens ajuda a controlar el "frame rate".










Aquest tros de codi es pot separar en 3 parts:

La primera part consta de les dues primeres línies de codi i com vaig explicar, pickle s'utilitza per guardar tota mena d'informació, llavors aquesta part simplement explica això: amb (with) aquest fitxer obert (map2.pkl) jo vull llegir la informació que hi ha en forma de bites (rb+ → "read bytes") y guardar-la en una variable que es diu contingut (content)

La segona part és des de la fila 8 fins a la 20. Aquesta sols defineix les dades importants que s'utilitzaran en tot el programa, com els colors, la posició de cada cosa (les parets, la posició inicial de l'agent i el fi del mapa) i els paràmetres del mapa (l'altitud i la longitud). Per definir el paràmetre uso la següent fórmula: np * Lc (nombre de posicions en un eix multiplicat per la longitud del quadrat (rect_size) en pixels). Està feta d'aquesta manera per poder saber el nombre de píxels que requereix un eix.

L'última part consta de les últimes dues línies d'aquest tros de codi. Són les encarregades d'inicialitzar la pantalla (screen) amb el nombre de píxels que hem definit amb la fórmula d'abans (x_screen, y_screen) i inicialitzar també la variable que controla el frame rate del programa (clock).

El problema que hem de resoldre ara és que tenim un paràmetre que funciona amb nombre de coordenada i una pantalla que funciona amb píxels, llavors sabem quina posició té l'agent o els murs, però no sabem la posició en píxels que té cadascú. La manera de solucionar això és tenir una funció que passa la posició en píxels. La manera en la qual ho farà serà trobar la posició del centre de qualsevol objecte amb la mateixa fórmula que hem utilitzat per saber el nombre de píxels en cada eix sols sabent la posició, però en aquest cas se suma la meitat de la longitud del quadrat, ja que volem trobar el centre d'una posició, llavors el centre serà la meitat de la mida d'un quadrat. La funció és la següent:



En aquesta funció (get_pos) la coordenada actual (state) es converteix en la posició x i y d’un objecte en píxels (x_pos i y_pos). Amb el return estem extraient la informació que és útil per nosaltres.

En la següent imatge representa la part que defineix les rectes de tots els objectes (agent, punt final, parets):



Els quadrats es defineixen amb la funció pygame.Rect. Aquests quadrats ens serviran per detectar col·lisió entre els objectes i visualitzar cada objecte. El que requereix aquesta funció són quatre dades: distància de la part esquerra i superior de la pantalla fins al quadrat (dels quals els dos tenen el valor de 0, ja que al principi no ens importa en quina posició se situa el quadrat, sols que el quadrat estigui creat), la longitud i l'altura del rectangle (que tenen el mateix valor, ja que és un quadrat, però si fos un rectangle tindria un valor diferent a cada part).



Una vegada ja tenim els quadrats fets, hem de col·locar-los en la posició correcta, ja que de moment tots els quadrats estan col·locats a una distància de 0 píxels de la part superior i esquerra de la pantalla. Cada quadrat té unes variables que defineixen la seva altura, longitud, distància de cada cantó fins a un extrem de la pantalla, però el que nosaltres hem de fer és modificar el centre del quadrat, cosa que ja modifica totes les variables necessàries. La variable que defineix el centre es pot modificar de la següent manera: quadrat.center = coordenada que indica el centre, per exemple finish_rect.center = get_pos(finish) on finish_rect és el quadrat que indica el fi del laberint, get_pos és la funció que hem creat anteriorment per saber la posició del centre d'un objecte en píxels i finish és la coordenada de l'objecte que després serà canviada en distància en píxels.

Com que cada part de la paret està representada com un objecte, en la fila 35 hi ha una eina que ens ajudarà de fer un quadrat a totes les parts de la paret. Aquesta eina s'anomena for loop i funciona de la següent manera: for (per cada) wall (paret) in walls (en parets) → fes un quadrat que representi aquella paret amb la funció pygame.Rect, després col·loca-la amb la funció get_pos i per últim afegeix-lo en una llista que es diu walls_rect que ha sigut creada en la fila 34. Aquesta cadena no para fins que no s'han creat totes les parts de la paret.

Nota: El “for loop” és una eïna que és pot traduir com el “per cada bucle”, és a dir que per a cada variable d’una llista o per cada valor entre dos nombres (ex.: els valors entre 0 i 3 són 0, 1, 2 i 3).



Aquest tros de codi és on tu pots canviar les dades que afecten en l'aprenentatge de l'agent. Dues coses que és important assenyalar són la variable episodes quina està feta de tal manera que el nombre d'episodis és proporcional a la mida de la taula q, ja que volem que el nombre d'episodis s'ajusti a la dificultat de mapa, i la variable espilon_decade que és una divisió entre la variable epsilon i la variable episodes, aquesta variable serà l'encarregada de baixar el valor de l'epsilon a cada episodi de manera que al final de tot el període d'entrenament hi hagi molt poca probabilitat de fer un moviment aleatori.

La resta de variables ja van ser explicades anteriorment menys el moves_limit. Aquesta variable indica el límit d'accions que té l'agent en cada episodi, ja que volem que l'agent entreni primer una petita part per fer aquest procés d'entrenament més ràpid.



Aquí és quan comença la fase d'entrenament i cosa molt importat de tenir en compte és que tot el codi que sortirà a continuació serà dintre d'aquest “for loop” i una vegada hem acabat tots els episodis s’ha acabat també la fase d’entrenament.

Al principi de cada episodi volem baixar una mica el valor del epsilon (línea 49), posar l'agent en la posició inicial del mapa (línea 50), definir/posar la variable done (que indica si l'intent s'ha acabat o no) en fals (False) i definir/canviar-li el valor a 0 a la variable moves (la variable que indica el nombre d'accions que ha fet l'agent), ja que no volem acumular aquesta variable a cada episodi.

El variable show l'utilitzo per determinar quan vull veure que està fent l'agent, ja que la part visual fa tot el procés d'entrenament molt lent i jo només vull veure a vegades si hi ha alguna cosa que no hauria de passar o si l'agent ho ha fet molt de pressa per disminuir el nombre d'episodis. El moment en el qual jo vull veure que està fent l'agent és quan el nombre d'episodis és divisible a 1000 (es a dir a cada 1000 episodis), això és possible per l'operació episode % 1000 == 0 que verifica si la resta de la divisió entre els episodis i 1000 és 0.

Dues coses que també passen cada 1000 episodis és: dir quin és l'episodi per saber quan falta perquè s'acabi la fase d'entrenament (print(episode)) i augmentar el valor de la variable move_limit ja que 1000 episodis són suficients per explorar una petita part, per tant ja pot passar a explorar una part més gran.

El while not done es un bucle que no para fins que no es considera acabar l’episodi i dintre de l’episodi posem  for ev in pygame.event.get() què és un bucle que detecta totes les accions que l’usuari utilitza (com tancar la pantalla, prémer un botó, etc.), en aquest cas sols volem si l’acció de l’usuari (ev) vol tancar la pantalla (pygame.QUIT) per tancar la pantalla (pygame.quit()) i l’aplicació (sys.exit()).



El new_state és la situació en la qual l'agent es trobarà a continuació, però de moment té els valors [0, 0] perquè encara no hem fet l'acció. Des de la fila 68 fins a la 71 és la part que determina quina serà la següent acció. Majoritàriament serà escollint el valor més gran (per escollir la variable més gran d'una llista es pot utilitzar np.argmax), però en les línies 68 i 69 són les encarregades de fer un moviment aleatori a vegades.

Des de la fila 73 fins a la 84 és la part que s'encarrega de canviar la nova posició (new_state) dependent de l'acció (action), per exemple si escull l'acció 1, aquesta serà l'equivalent d'anar a la dreta, és a dir la y és la mateixa i la x és 1 valor més gran.



Aquí sols estem definint la penalització/recompensa de l'agent (reward). Per defecte tenim -1 com a recompensa per defecte, aquesta serà la recompensa que tindrà l'agent per no arribar en un lloc que no té res especial, però també hi han dues maneres de canviar la recompensa:

Si l'agent ha arribat al final (fila 88-91), llavors li donem una gran recompensa (reward = q_table.size) i s'acaba l'episodi (done = True). La recompensa d'acabar el mapa pot ser qualsevol, però jo he decidit que sigui mida del q table, ja que vull que tingui un major o menor impacte en els valors depenent de la dificultat del mapa. També amb el print em diu quan i en quin episodi ha arribat al final.

Si l'agent fa algun error molt evident com xocar-se amb una paret (fila 92 - 95) o sortir-se del mapa (fila 97 - 104), ell rep una penalització molt gran (reward = -q_table.size) què és el mateix valor que s'utilitza per a la recompensa, però negativa. Aquí és molt important que posem un valor bastant gran, ja que la penalització que rep l'agent per cada acció que no condueix a cap part pot acumular-se fins al punt que l'agent preferiria xocar-se mil vegades contra la paret que fer les altres possibles accions. Tot seguit s'acaba l'episodi.




Aquesta part és la més important, ja que és la que calcula la qualitat de cada acció. Si l'episodi no està acabat (fila 106 - 111) el que volem fer és utilitzar la fórmula Q per canviar el valor vell amb un nou valor, però si l'episodi s'ha acabat (fila 112) volem igualar el valor Q amb la recompensa per assegurar el màxim impacte possible sobre el valor Q, perquè d'aquesta manera el procés serà molt més ràpid.



Aquesta imatge representa molt bé com he utilitzat la funció Q en el codi en la fila 110. Per recapitular molt breument que és el que fa cada part de la funció:

learning_rate és la variable que representa quan valorem la informació nova (new value) per la informació vella (old value)

reward és la recompensa de l’agent per fer una acció.

max_next_q és el el valor màxim de les accions de la situació posterior

 discount és el valor que ens indica que tant ens importa el futurs valors (max_next_q), ja que si posem el valor original dóna massa impacte en tot el procés, aixì que és millor que almenys estigués una mica disminuït el valor.

Nota: Si vols fer el teu propi agent, fixat molt bé en la funció Q perquè és molt fàcil equivocar-se en aquesta part.



Tot aquest procés ha sigut per canviar el valor Q de l’acció que ha decidit fer, però en realitat no ha canviat de posició, ja que el new_state era sols per veure que passa quan l’agent es posés en la nova posició. Aquí sols actualitzem la situació (state) amb la nova situació (new_state) i amb aquesta situació actualitzem també la seva posició central (fila 119 - 120).



Com vaig dir anteriorment, el variable show ens permet veure que està fent l’agent. El pygame.draw ens permet dibuixar els rectangles que representa cada cosa i el pygame.time.wait(50) fa que l’aplicació esperi una mica a cada acció per donar temps de visualitzar tot.

Aquí és quan s’acaba la fase d’entrenament i l’únic que ens falta ara és veure la solució.

Per demostrar la solució utilitzarem una forma més simplificada del codi anterior:



Aquí el done i el state té la mateixa funció i hi ha una variable nova: move. Aquesta variable és la que fa que l'agent es mogui. En les files 144 - 146 canviem el valor de la variable move a verdader (True) quan premem la tecla enter (return). Està feta d'aquesta manera perquè volem veure la solució del mapa quan nosaltres estem presents, és a dir que l'agent no ens ensenya la solució fins que no rep el senyal que ho pot fer.



El que fa l’agent quan es pot moure és bàsicament escollir l’acció que té el major valor, una vegada escull l’acció la situació es canvia.

Aquí és el mateix que en la fase d’entrenament, on es detecta si l’agent s’ha xocat amb una paret o s’ha anat fora del mapa, o ha arribat a la solució.

Potser que la solució del mapa no ha sigut realment la solució que nosaltres volem, però un error que no hem tingut en compte que impedeix l’agent resoldre completament el problema, per aquest motiu encara estem verificant si l’agent s’ha donat d’una paret o no.


I per últim fem visual tot el procés i tanquem el pygame una vegada la demostració de la solució s’ha acabat (pygame.quit()).


Com he comentat abans, és molt possible que després de la fase d’entrenament l’agent encara no sap la solució del problema, per tant la forma més útil de veure quin ha sigut el problema és utilitzar una llibreria que es diu matplotlib en especial una eina que es diu matplotlib.plot que ajuda a fer gràfics. Aquestes gràfiques ens ajudaran a veure quin és el problema o com es pot millorar les variables.



Per fer una gràfica s’han de tenir en compte dues variables. Com a variable X quasi sempre serà l’episodi mentre que la variable Y majoritàriament és el número total de recompensa que rep l’agent durant tot un episode.

Primer he afegit abans de la fase d’entrenament una variable que tindrà totes les recompenses totals de cada episodi ep_rewards i un diccionari dict_rewards que s'actualitzarà cada 1000 episodis i que tindrà el número d’episodi, el valor mitjà de tots els valors, el màxim i el mínim valor de cada 1000 intents.



Una vegada tenim aquestes variables definides podem actualitzar-les a cada 1000 episodis de la següent manera:


Abans de cada episodi volem tenir una variable que ens indica el valor total de les recompenses de cada episodi (episode_reward) i que tingui el valor inicial de 0.



La funció append inclueix una nova variable en una llista. Primer afegim el número de l'episodi a la llista dels episodis (‘ep’), després afegim el valor mitjà de tota la llista (que és bàsicament la suma de tots els valors dividit pel nombre de valors) a la llista dels valors mitjans (‘avg’ de average que significa mitjà) i afegim el valor min i max de cada 1000 episodis a la llista corresponent (‘min’ i ‘max’). Per últim també igualem la variable ep_rewards a una llista buida per no acumular tots els valors. 

Nota: Aquesta part ha sigut posada dintre de la fase d’entrenament, es pot fer fora, però és menys complicat d’aquesta manera.

Per canviar el valor de episode_reward, a cada acció que l’agent fa afegirem el valor de la recompensa d’aquella acció al valor total de recompensa d’aquell  episodi.



Abans de que s’acabi cada episode volem afegir el valor total de les recompenses de cada episodi a la llista ep_rewards.



Per últim he afegit el tros de codi següent per crear la gràfica:



Per posar-ho tot en la gràfica he afegit tres variables que serviran com la y (‘avg’ ‘min’ i ‘max’) i com a x és sols la variable ‘ep’ utilitzant la funció plot(). La funció legend() és el lloc on vols posar la llegenda (en aquest cas loc=4 és la part d’abaix cap a la dreta) i la funció show() mostra la gràfica.

Ara si executem el programa podrem veure al final de la fase d’entrenament una gràfica com la següent:



Amb aquesta gràfica m’he pogut donar compte que l’epsilon tenia un valor massa gran, que el que feia era fer massa cops moviments aleatoris, per tant l’he canviat de 0.05 a 0.005 i m’ha donat aquesta gràfica.



Aquesta és una gran millora comparat de com era anteriorment, però ara el problema és que l’agent ja ha resolt el problema molt abans de que s'acabés la fase d’entrenament, per tant he canviat el número d’episodis de ser int(q_table.size * 4) a int(q_table.size * 1.5) i m’ha donat el següent resultat:



Amb quasi 4 vegades menys episodis aconsegueix arribar a la mateixa solució. D’aquest punt l'única petita millora que he trobat era canviar el learning_rate de 0.1 a 0.15. Crec que ara ja es suficientment optimitzat com per fer qualsevol mapa.

Si vols utilitzar aquest procés per trobar el motiu pel qual el teu agent no troba la solució, t'explicaré tres situacions comunes que poden passar en aquest cas.

L’agent rep recompenses molt poca penalització encara que no avanci en el problema. El problema en aquest cas pot ser dues coses:
la penalització per no fer res no és tan gran (generalment deuria de ser -1 o -2)
la funció Q està mal feta.



La corba és normal però l’agent encara no sap la solució. Això és degut generalment perquè no l’hi has donat massa temps per solucionar el problema, per tant podries intentar posar més episodis, o també pot ser perquè l’epsilon tingui un valor massa gran.



L’agent encara que rep molta penalització no para de fer el mateix error. Pot ser que sigui la mateixa situació que la d’abans, però també pot ser degut a no posar massa penalització per fer una cosa malament (com xocar-se amb la paret), ja que la penalització de fer un moviment que no condueix a res és acumulativa i en cert punt arriba a ser més favorable xocar-se contra la paret que fer qualsevol altre moviment. Una situació no molt comuna en aquest cas és que la variable discount tingui un valor massa petit, o que la variable  learning_rate tingui un valor massa gran.

Nota: hi han més variables que es poden tenir com a referencia en la variable y, però les que més ens interessa són les que més afecten en l’aprenentatge del nostre agent

Una vegada hem tingut la forma més òptima de trobar la solució del nostre problema, podem considerar la nostre inteligencia artificial un èxit.
Limitacions del Q learning

El Q learning pot ser molt eficient si li dones les condicions adequades, per aquest motiu també volia parlar de les limitacions que té aquest tipus d'intel·ligència artificial.

The curse of dimensionality (la maledicció de la dimensionalitat) és el problema més important de tenir en compte quan vols fer una intel·ligència artificial d'aquest tipus. Aquest concepte es basa en el fet que la demanda computacional creix molt amb el creixement dels valors i creix molt més si vols afegir més valors que l'agent haurà de tenir en compte.

Per explicar-lo millor prendre com a referència el meu propi projecte. En aquest projecte l'agent té en compte la seva posició x i y, per tant el valor del paràmetre serà afectat per aquestes dues dades, tot seguit afectarà la complexitat d'un mapa, per exemple un mapa podria tenir 30 columnes (posible x) i 30 files (posible y) per tant el mapa tundra 900 (30*30) possibles posicions i tenint en compte que a cada situació hi ha 4 possibles accions la taula Q tindrà 3600 valors Q que haurà de manipular. Si canviéssim per 60 columnes i 60 files, de sobte hi ha 14400 valors Q (60*60*4).

Una cosa que també ens explica aquest concepte és que el nombre de valors que un agent ha de tenir en compte afecta molt més el nombre total de valors Q. Per exemple si a part de tenir en compte el valor x i y de cada mapa, també posarem la possibilitat de canviar entre 4 possibles angles i ara en comptes de l'agent anar davant, enrere, cap a la dreta o cap a la dreta podrà anar endavant, enrere, girar cap a la dreta o girar cap a l'esquerra, d'aquesta manera seguirà tenint 4 possibles accions. Ara el nombre total de valors Q passarà de ser 3600 (si hi ha sols 30 columnes, 30 files i 30 accions) a ser 14400 (si tenim en compte que també té 4 possibles angles).

Una de les limitacions d’aquesta AI també és el fet que no saps quan ha trobat la solució, sols has d'esperar fins que els episodis s’acaben per veure si l’agent ha arribat a la solució o no.

L'última limitació que se m'acut és que es pot aplicar en situacions molt específiques. Les situacions on es pot posar aquest tipus d'intel·ligència artificial és un entorn molt simplificat.

Una possible solució a aquests problemes pot ser la versió més complicada de Vanilla Q learning: Deep Q learning. Volia fer una intel·ligència artificial amb aquest tipus de Q learning, però és massa complicat per a fer-ho en uns mesos.

La forma resumida de com funciona aquesta AI, en comptes de calcular una valor Q amb una situació i una acció, el Deep Q learning utilitza una newral network (xarxa neuronal) com la següent per calcular l'acció més òptima donat més situacions.




La manera amb la qual aquesta funciona és molt complicada, però explicada molt resumidament: donat diferents situacions l'agent s'adona que està passant en el seu entorn i com està passant, després fa uns càlculs per veure quina és l'acció més bona, una vegada feta l'acció observa una altra vegada el seu entorn per veure com afecta aquella acció, si l'acció ha sigut exitosa, utilitza un procés molt semblant a l'anterior si es troba en una situació semblant, però si l'acció no ha estat exitosa, intenta canviar el procés per veure com podria millorar aquest procés.
Aplicacions de Q learning en la vida real

Q learning és molt útil per trobar el millor model que podria seguir un programa quan no es sap molt bé com seria la solució.

Nota: En aquesta part explicaré les aplicacions de tots els tipus de Q learning, no sols de Vanilla Q learning.

Les aplicacions més comunes d’aquest tipus d’intel·ligència artificial són:

Robots: Moltes vegades es necessita un robot que fa una tasca en específic que també implica adaptar-se al seu entorn, per exemple un robot que agafi coses del terra. Les coses que tindrà en compte el robot a l'hora d'aprendre serà saber com col·locar-se, saber com agafar les coses i com transportar-les sense que faci mal a ningú en el procés.

Gestió de recursos limitats en ordinadors: És molt difícil saber com gestionar les tasques dels ordinadors, ja que si un ordinador no organitza tota la informació i totes les tasques és molt més propens a donar un error, però si es posa a organitzar massa passa més temps organitzant que fent les coses. Per aquest motiu es pot utilitzar el Q learning per poder organitzar les tasques de la manera més bona.

Anuncis: És el lloc on més s’utilitza la intel·ligència artificial, per tant no és gran sorpresa que el Q learning sigui uns dels algoritmes que ajudin a seleccionar els anuncis.

Recomanacions personalitzables: És molt semblant a l’anterior, però en aquest cas és molt més difícil perquè hi ha molt més contingut que s’ha de tenir en compte, com el número de clics en una publicació, el temps dedicat a cada publicació, etc.

Conclusió 


El món i la nostra societat estan en un estat constant de canvi des de molts punts de vista, com econòmic, demogràfic, i el més important, tecnològic. La tecnologia té un rol molt rellevant a la nostra vida, ja que cada vegada més ens facilita les tasques que hem de fer i ens ajuda a connectar-nos no només amb informació, sinó que també amb altres persones. Un element molt rellevant de la tecnologia moderna i a base de la qual funcionen molts dels aparells que utilitzem cada dia és la intel·ligència artificial.

Tenint en compte l'evolució que ha tingut la intel·ligència artificial a la nostra societat durant els darrers anys, no només podem concloure que és un factor molt rellevant en com vivim ara la nostra vida en un món que cada vegada més digital, sinó que també, al ser una tecnologia tan estudiada, hi ha molts tipus d'intel·ligència artificial. L'objectiu del meu projecte va ser argumentar perquè el Q learning, un tipus d'intel·ligència artificial, podria ser molt útil en el nostre dia a dia, i com es compara amb altres tipus d'intel·ligència artificial.

El Q learning en concret és un tipus d'intel·ligència artificial que tracta de solucionar certs problemes donades unes dades i un entorn virtual. Treballant amb aquest, he pogut demostrar la seva eficacia prenent com a criteri el temps en el qual tarda a resoldre aquests problemes i que tant òptima ha sigut aquesta resolució.

Mentre estava fent aquest projecte van sorgir certes dificultats, com la potència de l'ordinador amb el qual vaig treballar, ja que en plantejar un problema més complicat es necessita més potencia computacional. Tenint en compte això, els resultats, tot i ser més lents, van representar una solució molt eficaç obtinguda per l'agent, encara que es podien millorar alguns petits moviments.

Agraeixo la finalització d'aquest treball a la meva família per ajudar-me amb el treball, el meu tutor, en Oscar, per fer un bon seguiment del projecte i a la gran comunitat que hi ha dedicada a aquest àmbit i la seva ampliació en certs llibres.

Bibliografia

Incomplete ideas
Reinforcement learning: An introduction
http://incompleteideas.net/book/first/ebook/

Youtube - Sendex
Q learning
https://www.youtube.com/watch?v=yMk_XtIEzH8
https://www.youtube.com/watch?v=Gq1Azv_B4-4
https://www.youtube.com/watch?v=CBTbifYx6a8


Reinforcement Q-Learning from Scratch in Python with OpenAI Gym
https://www.learndatasci.com/tutorials/reinforcement-q-learning-scratch-python-openai-gym/

Revoledu
Q learning Numerical example
https://people.revoledu.com/kardi/tutorial/ReinforcementLearning/Q-Learning-Example.htm

Towards data science 
Applications of Reinforcement Learning in Real World
https://towardsdatascience.com/applications-of-reinforcement-learning-in-real-world-1a94955bcd12

Youtube - Deeplizard
Deep Q-Learning - Combining Neural Networks and Reinforcement Learning
https://www.youtube.com/watch?v=wrBUkpiRvCA


Nota: Hi ha molts més llocs dels quals he extret informació, però els he posat és molt poca informació que he extret
'''

content_split = content.split()
print(len(content_split))