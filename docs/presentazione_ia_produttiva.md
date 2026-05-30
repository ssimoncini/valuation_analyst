# L'IA che Lavora: Architettura, Dominio, Strategia — Come Trasformare un Chatbot in un Collega

**Durata**: 25 minuti
**Formato**: 18 slide + 2 backup
**Caso reale**: Valuation Analyst — sistema multi-agente per valutazione aziendale e credit risk

---

## Slide 1 — Titolo

### L'IA che Lavora
#### Architettura, Dominio, Strategia — Come Trasformare un Chatbot in un Collega

[Nome relatore]
[Data, evento]

**Note speaker:**
Presentarsi in 15 secondi. Non partire dalla tecnologia, partire dal problema.
"Oggi non parliamo di cosa l'IA puo' fare in teoria. Parliamo di cosa serve
perche' faccia davvero qualcosa di utile in pratica."

---

## Slide 2 — Il Problema

### Il 90% delle aziende usa l'IA come un motore di ricerca glorificato

**Visual:** Piramide a 4 livelli con percentuali di adozione:

```
                    /\
                   /  \        5% — Sistema produttivo
                  /----\
                 /      \     10% — Automazione task
                /--------\
               /          \   25% — Assistente ad hoc
              /------------\
             /              \  60% — Chatbot / Q&A
            /________________\
```

**Bullet points:**
- La maggior parte delle implementazioni si ferma a "chiedere cose all'IA"
- Il risultato: output non riproducibili, non verificabili, non integrabili
- Il vero gap non e' tecnologico — e' architetturale e culturale
- **Domanda chiave:** cos'e' che separa il 5% in cima dal resto?

**Frase chiave:**
*"Il problema non e' che l'IA non funziona. E' che la usiamo come se fosse
Google con le buone maniere."*

**Note speaker:**
Qui il pubblico deve riconoscersi. La maggior parte delle aziende ha comprato
licenze, fatto workshop, e poi l'utilizzo si e' stabilizzato su "chiedo cose
alla chat". Non e' colpa loro — manca il framework per fare di piu'.
Anticipare: "Oggi vi mostro i tre ingredienti che servono per salire
in cima a quella piramide. Con un caso reale."

---

## Slide 3 — L'IA e' un Collaboratore Creativo

### Non e' un programma che fa i conti. E' un collega che ragiona.

**Visual:** Tabella a due colonne, contrasto netto:

| Calcolatrice | Collaboratore creativo |
| (quello che gia' avete) | (quello che cambia tutto) |
|---|---|
| Esegue una formula | Sceglie quale formula usare e perche' |
| Produce un numero | Chiede "questo numero ha senso?" |
| Fa quello che gli dici | Propone quello che non avevi considerato |
| Si ferma davanti a un errore | Spiega perche' e' un errore e suggerisce |
| Scala in velocita' | Scala in giudizio |
| Serve un programmatore per cambiarla | Si adatta al contesto in linguaggio naturale |

**Esempio concreto:**

> L'agente non calcola solo il Terminal Value di un'azienda.
> Verifica che sia coerente con 7 controlli indipendenti.
> Se il TV pesa piu' del 75% del valore totale, si ferma e ti avvisa.
> Se il tasso di crescita perpetua supera il PIL del paese, lo segnala.
> Poi chiede: "Procedo o vuoi rivedere le assunzioni?"
>
> Un programma non lo fa. Un collega si'.

**Frase chiave:**
*"Il valore dell'IA non e' fare i conti piu' in fretta. E' avere qualcuno
che ti chiede: sei sicuro che quei conti abbiano senso?"*

**Note speaker:**
Questa e' la slide piu' importante della presentazione. Se il pubblico esce
con un solo concetto, deve essere questo: l'IA non e' automazione, e'
collaborazione creativa. Il paragone col collega funziona perche' tutti ne
hanno avuto uno bravo — quello che ti fa la domanda giusta al momento giusto.
L'IA puo' fare esattamente quello, ma solo se glielo insegni.
Transizione: "Ma come si costruisce un collega cosi'? Servono tre cose."

---

## Slide 4 — I Tre Pilastri

### Tre ingredienti. Senza uno, il sistema non regge.

**Visual:** Triangolo equilatero con i tre vertici:

```
              ARCHITETTURA
                  /\
                 /  \
                / IA \
               / PRO- \
              / DUTTIVA \
             /___________\
    DOMINIO                STRATEGIA
```

- **Architettura** — Dal prompt singolo al sistema multi-agente
- **Dominio** — La conoscenza che rende l'IA competente, non solo veloce
- **Strategia** — Il percorso di adozione che rende il sistema utilizzabile

**Frase chiave:**
*"Un'IA senza architettura e' un giocattolo. Senza dominio e' un pericolo.
Senza strategia e' un progetto pilota che non finisce mai."*

**Note speaker:**
Slide di transizione. Dare 10 secondi al pubblico per leggere il triangolo,
poi anticipare: "Partiamo dal primo: l'architettura. Perche' e' qui che la
maggior parte dei progetti si arena."

---

## PILASTRO 1 — DAL TOOL ALL'ARCHITETTURA

---

## Slide 5 — Un Tool Non Scala

### Da prompt a sistema: la scala della maturita'

**Visual:** 4 gradini con freccia ascendente:

```
Livello 1: PROMPT SINGOLO
  "Quanto vale Apple?" → risposta generica, non verificabile

Livello 2: SCRIPT + IA
  Script Python che chiama l'IA → riproducibile ma rigido

Livello 3: AGENTE SPECIALIZZATO
  Un agente con skill, strumenti e memoria → flessibile ma isolato

Livello 4: SISTEMA MULTI-AGENTE
  Orchestratore + agenti specializzati + workflow → produttivo
```

**Bullet points:**
- Il livello 1 e' dove il 60% si ferma
- Il salto critico e' da 2 a 3: l'IA smette di essere chiamata e inizia a decidere
- Il livello 4 e' dove l'IA diventa un sistema produttivo

**Frase chiave:**
*"Un tool risolve un problema. Un'architettura risolve una classe di problemi."*

**Note speaker:**
Non soffermarsi troppo sui livelli bassi — il pubblico li conosce gia'.
Concentrarsi sul salto 2→3: "Un agente non e' uno script che chiama l'IA.
E' un'IA che sa usare gli script." E sul salto 3→4: "Il vero potere non e'
nell'agente singolo, ma in come collaborano tra loro."

---

## Slide 6 — Anatomia di un Sistema Multi-Agente

### 24 agenti, 76 skill, un orchestratore — caso reale

**Visual:** Diagramma hub-and-spoke:

```
                    [Orchestratore]
                    /    |    \     \
                   /     |     \     \
          [DCF]  [Risk] [Comparabili] [Credit Risk]
            |      |        |             |
        skill 1  skill 2  skill 3     skill 4-7
        skill 8  skill 9  skill 10    ...
```

Al centro: orchestratore che coordina.
Intorno: agenti specializzati, ciascuno con le proprie skill.

**I numeri del caso reale:**

| Componente | Quantita' |
|---|---|
| Agenti specializzati | 24 |
| Skill (workflow codificati) | 76 |
| Test automatizzati | 348 |
| Moduli Python | 40+ |
| Righe di codice | 26.000+ |
| Modalita' operative | 3 |

**Frase chiave:**
*"Non e' un chatbot grande. E' un team di specialisti che sa collaborare."*

**Note speaker:**
Mostrare il diagramma e spiegare: "Ogni agente e' uno specialista. Il DCF
analyst sa fare solo DCF, ma lo fa con la profondita' di un analista esperto.
L'orchestratore decide chi chiamare, in che ordine, e verifica che i risultati
siano coerenti tra loro." Pausa. "Esattamente come funziona un team vero."

---

## Slide 7 — Le Skill Come Contratti

### Una skill non e' un prompt. E' un workflow con garanzie.

**Visual:** Confronto prima/dopo:

```
PRIMA (prompt generico):              DOPO (skill strutturata):
                                      
"Calcola il DCF di questa azienda"   VINCOLI CRITICI
                                       - FCFF si sconta al WACC, mai al Ke
→ Output variabile                     - Terminal growth <= PIL nominale
→ Nessun controllo                     - TV non oltre 75% del valore
→ Non riproducibile                   
→ Nessun punto di verifica            WORKFLOW A CHECKPOINT
                                       Step 1: Validazione dati → GATE
40 righe                               Step 2: Calcolo FCFF → GATE
                                       Step 3: Proiezione multi-stage → GATE
                                       Step 4: Terminal Value + 7 check → GATE
                                       Step 5: Enterprise → Equity → GATE
                                      
                                      ERRORI COMUNI
                                       - Usare WACC per scontare FCFE
                                       - Terminal growth > PIL del paese
                                       - Ignorare il reinvestimento stabile
                                      
                                      250 righe — autosufficiente
```

**Frase chiave:**
*"La differenza tra un prompt e una skill e' la stessa che c'e' tra
chiedere un'opinione e avere una procedura operativa."*

**Note speaker:**
Questo e' il punto tecnico piu' importante per chi deve implementare.
"Una skill codifica non solo il COSA fare, ma il COME, il QUANDO FERMARSI,
e il COSA PUO' ANDARE STORTO. E' la differenza tra affidare un task a uno
stagista il primo giorno e affidarlo a un collega senior."
Far notare: da 40 righe a 250 righe. "La complessita' non e' nel calcolo —
e' nel sapere cosa controllare."

---

## Slide 8 — L'Autonomia Controllata

### "L'IA migliore e' quella che sa quando fermarsi a chiedere"

**Visual:** Timeline di un workflow reale con 5 gate:

```
[Dati] ──GATE──> [WACC] ──GATE──> [DCF] ──GATE──> [Risk] ──GATE──> [Report]
         |               |               |               |
    "Config OK.      "WACC = 8.2%.   "EV = 450M,     "Range 380-520M.
     Paese: IT.       Confermi?"      TV peso 68%.     IC 90%.
     Procedo?"                        Coerenza: OK.    Genero report?"
                                      Procedo?"
```

**Il principio:**
- L'IA procede autonomamente dove il rischio e' basso (calcoli, formattazione)
- Si ferma e chiede dove il rischio e' alto (assunzioni, parametri, giudizi)
- L'umano non deve controllare tutto — solo i punti che contano

**Matrice decisionale:**

|  | Reversibile | Irreversibile |
|---|---|---|
| **Rischio basso** | IA decide | IA propone, umano conferma |
| **Rischio alto** | IA propone, umano conferma | Umano decide, IA supporta |

**Frase chiave:**
*"Non vogliamo un'IA che fa tutto da sola. Vogliamo un'IA che sappia
distinguere cosa puo' fare da sola da cosa deve chiedere."*

**Note speaker:**
"Questo e' il motivo per cui i sistemi full-autonomous falliscono in contesti
professionali. Il valore non e' nell'autonomia totale — e' nella capacita'
di sapere quando il proprio output ha bisogno di validazione umana.
I decision gate non sono un freno. Sono il motivo per cui il sistema
e' adottabile in un contesto reale."

---

## Slide 9 — Sotto il Cofano: Stack e Fonti Dati

### Cosa rende il sistema un sistema — e da dove arrivano i dati reali

**Visual:** Tabella dello stack tecnologico e delle fonti dati:

| Livello | Tecnologia / Fonte | Ruolo |
|---|---|---|
| LLM | Claude (Anthropic) | Ragionamento, generazione, orchestrazione |
| Runtime | Claude Code · MCP | Esecuzione agenti, tool use, integrazioni |
| Calcolo | Python 3.11+ | Modelli finanziari · 348 test automatizzati |
| Skill layer | Markdown strutturato | Workflow, vincoli, checkpoint |
| Dati di mercato | Massive · FactSet · Capital IQ · Refinitiv | Prezzi, fondamentali, consensus |
| Parametri settore | Damodaran NYU Stern | Beta, ERP, multipli, WACC settoriali |
| Societa' italiane | Bureau van Dijk (AIDA) · CONSOB · Borsa Italiana | Bilanci, dati societari, depositi |
| Versionamento | Git + GitHub | Audit trail, collaborazione |

**Il punto:**
- La scelta piu' importante non e' il modello LLM — e' il layer di skill che codifica il dominio
- Le fonti dati sono provider professionali, non file sparsi: mercato e fondamentali da Massive/FactSet/Capital IQ/Refinitiv, parametri di settore da Damodaran, bilanci italiani da Bureau van Dijk/CONSOB/Borsa Italiana
- Se domani cambiasse il modello, skill e fonti restano: il dominio e' l'asset

**Frase chiave:**
*"Sotto il cofano non c'e' un trucco di prompt. C'e' uno stack di runtime, skill e fonti dati reali."*

**Note speaker:**
"Chiudo l'architettura con cosa c'e' sotto il cofano. Il runtime e' Claude Code,
con i suoi strumenti e i connettori MCP verso i data provider. I dati non sono
fogli di calcolo: sono le stesse fonti che usano gli analisti — Massive, FactSet,
Capital IQ e Refinitiv per mercato e fondamentali, Damodaran per i parametri di
settore, Bureau van Dijk, CONSOB e Borsa Italiana per le societa' italiane. Ma
la cosa che conta di piu' resta il layer di skill: e' li' che vive il dominio,
ed e' indipendente dal modello sottostante."

---

## PILASTRO 2 — CONOSCENZA DEL DOMINIO

---

## Slide 10 — Il Brillante Incompetente

### Senza dominio, l'IA sbaglia le cose che contano

**Visual:** Due output a confronto — stesso prompt, risultati opposti:

```
PROMPT: "Valuta il Terminal Value di questa azienda"

IA GENERICA:                          IA CON DOMINIO:
TV = FCF * (1+g) / (WACC-g)          TV = NOPAT * (1 - g/ROIC) / (wacc - g)
TV = 120 * 1.03 / (0.08-0.03)        
TV = 2.472M                          CHECK COERENZA:
                                      ✓ g (3%) < PIL nominale Italia (1.5%) — WARNING
"Il Terminal Value e' 2.472M."        ✓ ROIC nuovi inv. (12%) > WACC (8%) — OK
                                      ✗ Peso TV su EV: 82% — ANOMALO (soglia 75%)
                                      ✗ g > PIL paese — RIVEDERE
                                      
                                      "TV = 1.890M ma due check falliti.
                                       Raccomando: ridurre g a 1.5%.
                                       Procedo o rivediamo?"
```

**Il punto:**
- Il primo output e' matematicamente corretto ma professionalmente inutile
- Il secondo identifica due problemi che il primo ignora completamente
- In finanza, un numero sbagliato presentato con sicurezza e' peggio di nessun numero

**Frase chiave:**
*"L'IA generica sa fare i conti. L'IA con dominio sa quando i conti non tornano."*

**Note speaker:**
"Questo esempio e' reale. Il 10% dei report di analisti professionisti
contiene Terminal Value incoerenti — lo dice uno studio dell'Universita'
di Bergamo. Se gli analisti umani sbagliano il TV, figuriamoci un'IA
generica. La soluzione non e' un'IA piu' potente — e' un'IA che sa
cosa controllare."

---

## Slide 11 — Il Dominio Si Codifica

### Come si insegna un mestiere all'IA: paper → formule → vincoli → errori

**Visual:** Pipeline di codifica della conoscenza:

```
PAPER ACCADEMICI              CODICE PYTHON              SKILL OPERATIVA
                                                         
Scarano/Brughera 2008   →    bms/builder.py        →    bms-builder/SKILL.md
(Bilancio Medio Standard)    386 righe, 15 metodi        144 righe, 4 checkpoint
                                                         
Scarano/Di Napoli 2008  →    dcf/coherence.py      →    dcf-tv-coherence/SKILL.md
(Terminal Value coerente)    428 righe, 7 check          211 righe, 5 checkpoint
                                                         
Montesi/Papiro 2014     →    agentic_credit_risk/  →    agentic-credit-risk/SKILL.md
(Credit Risk Monte Carlo)   1.430 righe, 6 moduli       187 righe, 6 checkpoint
```

**I tre livelli della codifica:**

| Livello | Cosa | Esempio |
|---|---|---|
| **Formule** | Le equazioni del paper | TV = NOPAT*(1 - g/ROIC)/(wacc - g) |
| **Vincoli** | I limiti di validita' | g <= PIL nominale, h_T in [0,1] |
| **Errori comuni** | Cosa NON fare | Mai mescolare pre-tax e after-tax WACC |

**Frase chiave:**
*"Il dominio non si spera — si codifica. Ogni paper, ogni best practice,
ogni errore che avete visto fare diventa una regola che l'IA applica sempre."*

**Note speaker:**
"Abbiamo preso tre paper accademici — pubblicati, peer-reviewed, con formule
precise — e li abbiamo tradotti in codice e skill. Non e' stato un lavoro
di programmazione. E' stato un lavoro di ingegneria della conoscenza.
La parte difficile non e' implementare la formula — e' capire quando
la formula non si applica."

---

## Slide 12 — La Compliance Come Dominio

### Il porting dei financial tool al framework regolatorio europeo

**Visual:** Tabella degli 8 ambiti normativi codificati:

| Ambito | Normativa | Cosa fa l'IA |
|---|---|---|
| Antitrust | AGCM | Verifica soglie fatturato (532M/32M EUR) |
| Settori strategici | Golden Power | Flag settori D.L. 21/2012 |
| Mercati | CONSOB | Conformita' Regolamento Emittenti |
| Adeguatezza | MiFID II | Profiling, target market, ESG |
| Antiriciclaggio | D.Lgs. 231/2007 | 3 livelli adeguata verifica |
| Sostenibilita' | SFDR | Classificazione art. 6/8/9 |
| Resilienza | DORA | Check Reg. UE 2022/2554 |
| Fiscalita' | IRES+IRAP, PEX, ROL | Parametri automatici per Italia |

**Il punto:**
- I financial tool nascono in un contesto regolatorio diverso: il valore e' stato portarli sul quadro normativo europeo e italiano
- Un output non compliant e' inutilizzabile; la compliance codificata non rallenta — accelera (niente rework)
- L'IA che conosce le regole produce output direttamente utilizzabili dal business

**Frase chiave:**
*"L'IA che non conosce le regole vi fa lavorare due volte.
Una per generare l'output, una per renderlo compliant."*

**Note speaker:**
"La compliance e' dominio a tutti gli effetti, ed e' la seconda tappa della storia
del progetto: abbiamo preso i financial tool e li abbiamo portati sul framework
regolatorio europeo e italiano — MiFID II, Golden Power, 231/2007, SFDR, DORA.
Se l'IA non conosce queste regole, ogni suo output deve essere rivisto da un
compliance officer. Se le conosce, l'output esce gia' utilizzabile. La compliance
non e' il freno dell'innovazione — e' il prerequisito per l'adozione."

---

## Slide 13 — Arricchire il Dominio

### Dallo strumento specifico alla suite integrata: tre strati che si arricchiscono

**Visual:** Piramide dell'arricchimento del dominio (dal basso verso l'alto):

```
                    /\
                   /  \       INTEGRAZIONE
                  /    \      "I tre progetti fusi in una suite ampliata e
                 /______\      omogenea: modelli e regole si compongono"
                /        \
               /FRAMEWORK \   FRAMEWORK UE
              /    UE      \  "Porting dei financial tool al quadro normativo
             /______________\  europeo: MiFID II, Golden Power, SFDR, DORA"
            /                \
           /    STRUMENTI     \  STRUMENTI
          /__________________  \ "Valuation Analyst (Damodaran) e Rating &
                                  Valuation: modelli per le PMI italiane"
```

**I tre strati (la storia del progetto):**
- **Strumenti** — due plugin Claude specifici: Valuation Analyst con metodo Damodaran e Rating & Valuation con modelli su misura per la realta' italiana
- **Framework UE** — il porting dei financial tool al quadro regolatorio europeo: la compliance diventa dominio
- **Integrazione** — i tre progetti fusi in un'unica suite ampliata e omogenea, dove modelli e regole parlano la stessa lingua

**Frase chiave:**
*"Il dominio non si aggiunge tutto insieme: si arricchisce per strati.
Ogni strato eredita e potenzia quello sotto."*

**Note speaker:**
"Questa e' la storia del progetto in una piramide. Siamo partiti da due strumenti
specifici — Valuation Analyst sul metodo Damodaran e Rating & Valuation per le PMI
italiane. Poi abbiamo portato i financial tool sul framework regolatorio europeo,
quello della slide precedente. Infine abbiamo integrato i tre progetti in una
suite unica e omogenea. Non e' stato un big bang: ogni strato ha ereditato e
arricchito quello sotto. E' cosi' che un dominio cresce — per strati, non per
sostituzione."

---

## PILASTRO 3 — STRATEGIA DI ADOZIONE

---

## Slide 14 — Non Serve un Big Bang

### Tre modalita' coesistenti — adozione progressiva, non sostitutiva

**Visual:** Tre binari paralleli che convergono:

```
MODALITA' 1: Damodaran (Python)          Per chi gia' usa Python
  Config JSON → Script → Report PDF       Output: report automatico
  Target: societa' quotate                Curva: bassa — lancia e ottieni
                                          
MODALITA' 2: FSI Excel (interattivo)     Per chi vive in Excel
  Claude guida → Review a ogni step       Output: workbook con formule vive
  Target: societa' italiane quotate       Curva: media — step-by-step
                                          
MODALITA' 3: Rating & Valuation (PMI)    Per analisti credit risk
  BMS → DCF → Monte Carlo → Rating       Output: PD, rating, report
  Target: PMI non quotate                 Curva: alta — pipeline completa
```

**Il principio:**
- Non stai sostituendo nulla — stai aggiungendo un canale
- Ogni modalita' si rivolge a un utente diverso con un livello di confidenza diverso
- L'adozione e' un percorso: parti da dove hai meno resistenza

**Percorso tipico:**

```
Mese 1-2: Modalita' 1        Mese 3-4: Modalita' 2        Mese 5+: Modalita' 3
"L'IA genera report"     →   "L'IA costruisce modelli"  →  "L'IA stima il rischio"
Basso rischio, alta         Medio rischio, feedback        Alto valore, massima
visibilita' dei risultati   continuo dell'utente           integrazione nel processo
```

**Frase chiave:**
*"L'errore piu' comune e' voler fare tutto subito. Il percorso giusto
e' partire da dove il valore e' visibile e il rischio e' basso."*

**Note speaker:**
"Non chiedete alle persone di cambiare il modo in cui lavorano dal giorno 1.
Date loro un canale nuovo accanto a quello vecchio. Quando vedono che
il nuovo funziona, saranno loro a chiedere di piu'.
Nel nostro caso: il report automatico e' stato il cavallo di Troia.
Nessuno si sentiva minacciato da un PDF generato. Ma dopo averlo visto,
tutti volevano il modello Excel interattivo. E dopo l'Excel, il credit risk."

---

## Slide 15 — L'Uomo nel Loop

### Dove mettere l'umano — e dove toglierlo

**Visual:** Matrice 2x2:

```
                   REVERSIBILE              IRREVERSIBILE
                
RISCHIO        ┌─────────────────────┬──────────────────────┐
BASSO          │                     │                      │
               │  IA DECIDE          │  IA PROPONE          │
               │                     │  UMANO CONFERMA      │
               │  Calcoli, format,   │                      │
               │  data retrieval,    │  Scelta comparabili, │
               │  report draft       │  pubblicazione       │
               │                     │  report              │
               ├─────────────────────┼──────────────────────┤
RISCHIO        │                     │                      │
ALTO           │  IA PROPONE         │  UMANO DECIDE        │
               │  UMANO CONFERMA     │  IA SUPPORTA         │
               │                     │                      │
               │  Assunzioni DCF,    │  Raccomandazione      │
               │  parametri WACC,    │  BUY/SELL,           │
               │  scelta modello     │  rating creditizio   │
               │                     │                      │
               └─────────────────────┴──────────────────────┘
```

**Il principio:**
- Non tutto richiede supervisione umana — e' inefficiente
- Non tutto puo' essere delegato — e' irresponsabile
- La chiave e' sapere dove tracciare il confine

**Nel sistema reale:**
- **IA decide:** fetch dati, calcoli, formattazione, generazione tabelle
- **IA propone + gate:** WACC calcolato, valore DCF, composizione campione
- **Umano decide:** tasso di crescita terminale, peso dei metodi, raccomandazione finale

**Frase chiave:**
*"Non 'IA o umano'. Ma 'IA dove aggiunge velocita', umano dove aggiunge giudizio'."*

**Note speaker:**
"Questa matrice e' lo strumento piu' pratico che vi lascio oggi.
Prendetela e applicatela al vostro contesto: per ogni task che fate,
chiedetevi — e' reversibile? E' ad alto rischio? La risposta vi dice
se l'IA puo' procedere da sola o deve fermarsi a chiedere.
Nel nostro sistema, i decision gate sono posizionati esattamente
secondo questa logica."

---

## Slide 16 — Misurare il Valore

### Non "quanti prompt al giorno" — metriche che contano

**Visual:** Due colonne — metriche sbagliate vs metriche giuste:

| Metriche vanity (inutili) | Metriche di valore (utili) |
|---|---|
| Numero di prompt al giorno | Tempo da richiesta a output utilizzabile |
| Token consumati | Tasso di rework (output accettati al primo giro) |
| Utenti attivi | Copertura dei controlli (check eseguiti vs saltati) |
| "Soddisfazione" generica | Riproducibilita' (stesso input = stesso output) |
| Costo per query | Audit trail (tracciabilita' delle decisioni) |

**I numeri del caso reale:**

| Metrica | Valore |
|---|---|
| Righe di codice verificato | 26.284 |
| Test automatizzati | 348 (tutti verdi) |
| Checkpoint per workflow | 4-6 per skill |
| Modalita' operative | 3 (pubblici diversi) |
| Errori comuni codificati | 50+ (non ripetibili) |
| Da idea a sistema produttivo | 3 sessioni di lavoro |

**Frase chiave:**
*"Se la vostra metrica principale e' 'quanti prompt facciamo', state misurando
l'attivita', non il valore. Misurate gli output utilizzabili."*

**Note speaker:**
"Le metriche di adozione tradizionali — utenti attivi, prompt al giorno —
misurano se le persone usano l'IA. Non misurano se l'IA produce valore.
Il vero indicatore e': quanti output dell'IA finiscono nel processo
produttivo senza rework? Se la risposta e' 'pochi', il problema non
e' l'IA — e' l'architettura, il dominio o la strategia. Cioe' i tre
pilastri di oggi."

---

## CHIUSURA

---

## Slide 17 — I Tre Cardini — Recap

### Senza uno dei tre, il sistema non regge

**Visual:** Triangolo con conseguenze della mancanza:

```
              ARCHITETTURA
                  /\
                 /  \
                / IA \
               / PRO- \
              / DUTTIVA \
             /___________\
    DOMINIO                STRATEGIA
```

| Se manca... | Risultato |
|---|---|
| Architettura | IA brillante ma caotica — output non riproducibili, non integrabili |
| Dominio | IA veloce ma pericolosa — numeri sbagliati presentati con sicurezza |
| Strategia | IA potente ma inutilizzata — progetto pilota che non finisce mai |

**I tre punti da portare a casa:**

1. **Architettura**: non un prompt, un sistema. Agenti specializzati,
   skill con garanzie, autonomia controllata con decision gate.

2. **Dominio**: non dati, giudizio. Paper, formule, vincoli, errori comuni
   codificati — l'IA sa cosa controllare, non solo cosa calcolare.

3. **Strategia**: non big bang, percorso. Partire da dove il rischio e' basso
   e il valore e' visibile, espandere quando la fiducia cresce.

**Frase chiave:**
*"L'IA che lavora non e' quella piu' potente. E' quella meglio orchestrata,
piu' competente nel dominio, e adottata con il percorso giusto."*

**Note speaker:**
"Questi tre pilastri non sono teoria. Sono il risultato di un progetto reale
che oggi ha 24 agenti, 76 skill, 348 test e tre modalita' operative.
Non e' un prototipo — e' un sistema che produce output utilizzabili.
E la cosa piu' importante: non e' partito cosi'. E' partito da un prompt.
Il percorso da prompt a sistema produttivo e' esattamente quello che
vi ho raccontato oggi."

---

## Slide 18 — Call to Action

### Smettete di chiedere all'IA di fare cose. Iniziate a costruire sistemi che sanno farle.

**Tre azioni concrete per lunedi' mattina:**

1. **Prendete un workflow ripetitivo** del vostro team e scrivetelo come skill:
   vincoli, step, checkpoint, errori comuni. Non serve codice — basta un documento.

2. **Identificate i vostri decision gate**: dove l'IA puo' procedere da sola
   e dove deve fermarsi. Usate la matrice rischio/reversibilita'.

3. **Partite piccoli**: un agente, una skill, un workflow. Poi misurate
   gli output utilizzabili, non i prompt. Se funziona, espandete.

**Contatti:**
[Nome] — [Email] — [LinkedIn]

**Frase di chiusura:**
*"Il futuro non e' l'IA che sostituisce le persone. E' l'IA che rende
le persone piu' brave nel loro mestiere."*

**Note speaker:**
"Le tre azioni sono volutamente semplici. Non servono budget, non servono
approvazioni, non serve un team di data scientist. Servono 30 minuti
per scrivere un workflow come skill, 15 minuti per mappare i decision gate,
e la volonta' di misurare l'output, non l'attivita'. Grazie."

---

## SLIDE BACKUP (se ci sono domande)

---

## Backup 1 — Esempio Live: Pipeline Credit Risk

### Dal bilancio al rating in 5 step

```
STEP 1: Dataset            STEP 2: BMS settoriale
CSV con 48 aziende    →    Media standardizzata di 35 peer
Invarianti verificati       EBITDA margin 14%, leva D/TA 42%
                            GATE: "BMS costruito. Procedo?"

STEP 3: Differenziale      STEP 4: DCF coerente
Target vs settore      →    2 stadi, TV con reinvestimento
Margine +3pp, leva -5pp    7 check coerenza: tutti PASS
GATE: "6/8 favorevoli"     GATE: "EV = 38M. TV peso 64%"

STEP 5: Monte Carlo         RISULTATO
20.000 simulazioni     →    PD 3 anni: 2.8%
Weibull + copula            Rating implicito: BB+
Debito endogeno             EL = 1.2M, UL 95% = 3.8M
                            GATE: "Genero report?"
```

**Note speaker:**
"Questa pipeline non esisteva come prodotto. E' stata costruita traducendo
tre paper accademici in codice e skill. Il tempo totale: tre sessioni
di lavoro collaborativo con l'IA. Non tre mesi — tre sessioni."

---

## Backup 2 — ROI dell'Approccio

### Investimento vs ritorno

| Investimento | Tempo | Una tantum? |
|---|---|---|
| Codifica dominio (paper → skill) | 2-3 giorni per verticale | Si' |
| Architettura agenti | 1-2 giorni setup | Si' |
| Test e validazione | 1 giorno | Si' |
| **Totale setup** | **~1 settimana** | **Si'** |

| Ritorno | Per singola analisi | Cumulativo |
|---|---|---|
| Tempo analisi: da 2-3 giorni a 2-3 ore | -80% | Cresce con volume |
| Controlli: da manuali a automatici | 7+ check sempre eseguiti | Zero dimenticanze |
| Riproducibilita': da variabile a garantita | Stesso input = stesso output | Audit-friendly |
| Onboarding junior: da mesi a giorni | Skill = formazione codificata | Scala con il team |

**Note speaker:**
"Il setup e' un investimento una tantum. Il ritorno e' per ogni analisi
successiva. E il ritorno nascosto piu' grande e' l'onboarding: quando
un junior nuovo arriva, non deve imparare dal senior in 6 mesi.
Le skill SONO la formazione."
