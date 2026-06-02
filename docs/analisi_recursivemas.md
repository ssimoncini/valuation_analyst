# Analisi: RecursiveMAS — utilizzabilità diretta e dipendenza dai modelli

**Oggetto**: RecursiveMAS — *Recursive Multi-Agent Systems* (arXiv:2604.25917, apr. 2026)
**Repo**: https://github.com/RecursiveMAS/RecursiveMAS · **Sito**: https://recursivemas.github.io · **Checkpoint**: https://huggingface.co/RecursiveMAS
**Data analisi**: 2026-06-02
**Domande**: (1) il framework è direttamente utilizzabile? (2) è model-agnostic o richiede classi di modelli specifiche per il deployment effettivo?

> Nota di metodo: analisi basata su README, abstract del paper, project page e materiali derivati. Non ho eseguito il codice né ispezionato i sorgenti riga per riga; i punti tecnici di fondo (scambio di stati latenti, training dei moduli) sono però affermati esplicitamente e in modo convergente nelle fonti.

---

## Verdetto in due righe

RecursiveMAS **non è model-agnostic** e **non è plug-and-play**. È un framework di ricerca che sostituisce la comunicazione *testuale* tra agenti con il **trasferimento diretto di stati latenti (hidden states)**: questo richiede modelli **open-weight** serviti localmente con **accesso white-box** alle attivazioni, e richiede di **addestrare** i moduli di collegamento (RecursiveLink) prima dell'uso. Esclude per costruzione tutti i modelli **closed/API** (Claude, GPT, Gemini).

---

## Cos'è (in breve)

L'idea è portare il paradigma dei *looped / recursive language models* (raffinare iterativamente la stessa computazione su stati latenti per "ragionare più a fondo") dal singolo modello al **sistema multi-agente**. L'intero MAS viene trattato come **un'unica computazione ricorsiva nello spazio latente**:

- Agenti eterogenei sono connessi in un *loop* di collaborazione tramite il modulo **RecursiveLink**, che genera "latent thoughts" in-distribution per l'agente successivo e trasferisce gli stati latenti **cross-agent senza serializzare in testo**.
- L'ottimizzazione avviene con un algoritmo **inner-outer loop**: un *inner loop* allinea in parallelo ogni agente alla generazione di latent thoughts; un *outer loop* srotola la ricorsione completa e ottimizza congiuntamente tutti i RecursiveLink con *gradient-based credit assignment* condiviso tra i round.
- 4 pattern di collaborazione (Sequential, Mixture, Distillation, Deliberation), 9 benchmark (matematica, scienze, medicina, search, codice).
- Risultati dichiarati: **+8,3%** accuratezza media, **1,2×–2,4×** speedup end-to-end, **−34,6%…−75,6%** token. Lo speedup e il risparmio di token derivano proprio dall'evitare il "round-trip" testuale tra agenti.

---

## Domanda 1 — È direttamente utilizzabile?

**Solo in senso limitato: sì per riprodurre gli esperimenti del paper, no come framework drop-in per un caso d'uso arbitrario.**

A favore (cosa abbassa la barriera):
- Implementazione ufficiale pubblica con API di alto livello (`system_loader.py`, `run.py` parametrizzato per stile/batch/temperature/dataset).
- **Checkpoint pre-addestrati** su Hugging Face per le configurazioni del paper → si possono lanciare i pattern già pronti senza ri-addestrare, almeno sui setup forniti.
- Footprint hardware contenuto: modelli da **1,5B–9B**, memoria di training riportata ~**15,3 GB** → fattibile su una singola GPU di fascia consumer/prosumer.
- Stack di inferenza standard (vLLM).

Contro (cosa impedisce il "plug-and-play"):
- **Richiede addestramento dei RecursiveLink** per ogni nuova configurazione (combinazione di modelli, ruoli, dominio/dataset). I checkpoint pronti coprono *gli scenari del paper*, non il tuo. Cambi task, dominio o modelli → devi rieseguire l'inner-outer loop.
- **Serve infrastruttura GPU** e un percorso di inferenza che esponga gli stati latenti (non basta un endpoint testuale).
- Per il pattern **Deliberation** serve una **API key Tavily** (tool di ricerca esterna).
- È codice di ricerca recente (apr. 2026): aspettarsi maturità/robustezza/documentazione da prototipo, non da libreria di produzione.

**In pratica**: utilizzabile *subito* per valutare/riprodurre i benchmark sui modelli e domini supportati. Per applicarlo a un dominio proprio (es. credit risk/valuation) servono dati, una pipeline di training dei link e GPU — quindi è un **progetto di R&D**, non un'integrazione.

---

## Domanda 2 — È model-agnostic o servono classi di modelli specifiche?

**Non è model-agnostic.** È, nelle parole degli autori, "structure-agnostic" — cosa diversa e più ristretta: indipendente dalla *famiglia/architettura* di transformer open-weight, ma **non** indipendente dal *tipo* di accesso al modello.

Le classi di modelli **necessarie** per il deployment effettivo:

| Requisito | Conseguenza | Cosa è ammesso / escluso |
|---|---|---|
| **Accesso white-box agli hidden states** | il RecursiveLink legge/scrive attivazioni interne | ✅ Open-weight transformer locali · ❌ qualunque modello solo-API |
| **Pesi modificabili / backprop** | inner-outer loop addestra i link attraverso i modelli | ✅ checkpoint open con gradienti · ❌ modelli congelati dietro API |
| **Esecuzione locale (vLLM + forward custom)** | servono attivazioni a runtime, non solo testo | ✅ self-hosting su GPU · ❌ inferenza gestita black-box |
| **Transformer decoder "latent-recursion friendly"** | trasferimento di stati latenti in-distribution | ✅ Qwen/Qwen3, Llama 3.2, Gemma3, DeepSeek-R1-Distill, BioMistral (1B–9B) · ❌ non-transformer / pipeline opache |

Note sull'eterogeneità: il framework **supporta agenti di famiglie e dimensioni diverse** (es. mix Qwen + Llama + Gemma) perché il RecursiveLink fa da **ponte appreso** tra spazi latenti con dimensioni nascoste/tokenizer differenti. Quindi è flessibile *tra* modelli open — ma resta vincolato alla **classe** "modelli open-weight self-hosted con attivazioni accessibili".

**Conclusione netta**: la dipendenza non è da uno *specifico* modello, ma da un'**intera classe** di modelli (open-weight, white-box, addestrabili, serviti localmente). Tutti i modelli **closed/API sono esclusi a livello di principio**, non di implementazione: il metodo *è* l'accesso al latente.

---

## Requisiti minimi per un deployment reale

1. **Modelli open-weight** scaricabili (1,5B–9B) con accesso agli hidden states.
2. **GPU** (anche singola, ~16 GB sufficienti per i modelli piccoli; di più per gli scaled/9B e i batch grandi).
3. **Stack**: vLLM + dipendenze Python del repo; Tavily API key per Deliberation.
4. **Fase di training** dei RecursiveLink (inner-outer loop) sul proprio mix di modelli/ruoli/dominio — a meno di limitarsi alle config con checkpoint già forniti.
5. **Dataset** del dominio target per allineare i "latent thoughts" e fare credit assignment.

---

## Implicazioni per il progetto Valuation Analyst

Rilevante perché tocca direttamente le nostre scelte di architettura:

- **Non integrabile nella nostra suite così com'è.** Il nostro MAS gira su **Claude via API (closed)**: nessun accesso agli hidden states ⇒ RecursiveMAS è **inapplicabile** al nostro stack attuale senza ripiattaformare su modelli open self-hosted.
- **È l'opposto del nostro paradigma di comunicazione.** I nostri agenti collaborano via **testo/artefatti** (skill, report, gate espliciti, audit trail leggibile). RecursiveMAS scambia **vettori latenti**: più efficiente in token/latenza, ma **opaco e non ispezionabile** — in tensione con i nostri requisiti di tracciabilità/compliance (decision gate, audit). Per finanza regolata l'interpretabilità del passaggio inter-agente non è un dettaglio.
- **Collega bene alla slide "prototipo → produzione".** È un caso da manuale in cui il salto **non è di scaffolding ma di modello/architettura**: per ottenerne i benefici devi *possedere i pesi* e addestrare. Conferma la tesi al contrario — qui l'ingegneria scende fino al livello del modello, non resta nell'harness.
- **Dove potrebbe interessarci, in prospettiva R&D**: se un domani volessimo un *sotto-sistema* locale, a basso costo per token e ad alta frequenza (es. screening massivo di PMI su modelli 1–4B self-hosted), il pattern latent-recursion potrebbe ridurre costi/latenza. Ma sarebbe un binario separato, open-weight e on-prem, distinto dalla pipeline Claude.

**Sintesi operativa**: interessante come direzione di ricerca sull'efficienza della collaborazione multi-agente; **non adottabile** nella nostra architettura Claude-based; valutabile solo in un eventuale ramo open-weight/on-prem, con costo di training e perdita di ispezionabilità da mettere in conto.

---

## Fonti

- Paper (abstract): https://arxiv.org/abs/2604.25917 · HTML: https://arxiv.org/html/2604.25917v1
- Project page: https://recursivemas.github.io
- Repo ufficiale: https://github.com/RecursiveMAS/RecursiveMAS
- Checkpoint: https://huggingface.co/RecursiveMAS
- Hugging Face papers: https://huggingface.co/papers/2604.25917
