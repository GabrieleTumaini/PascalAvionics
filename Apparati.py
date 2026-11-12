Apparato = {}

STATI_AMMESSI = ("OK", "ATTENZIONE", "OFFLINE")

APPARATI = {
    "NAV-01": {"nome": "Ricevitore navigazione", "bus": "BUS-A", "stato": "OK"},
    "COM-02": {"nome": "Radio comunicazioni", "bus": "BUS-B", "stato": "ATTENZIONE"},
    "SEN-03": {"nome": "Sensore assetto", "bus": "BUS-A", "stato": "OFFLINE"},
}

def aggiungi_apparato(codice: str, nome: str, bus: str, stato: str) -> bool:
    stato_normalizzato = stato.upper()
    
    if codice in APPARATI or stato_normalizzato not in STATI_AMMESSI:
        return False
    
    APPARATI[codice] = {"nome": nome, "bus": bus, "stato": stato_normalizzato}
    return True


def aggiorna_stato(codice: str, stato: str) -> bool:
    stato_normalizzato = stato.upper()
    
    if codice not in APPARATI or stato_normalizzato not in STATI_AMMESSI:
        return False
    
    APPARATI[codice]["stato"] = stato_normalizzato
    return True

if __name__ == "__main__":
    print("--- TEST FIX URGENTE ---")
    
    esito_minuscolo = aggiorna_stato("NAV-01", "offline")
    print(f"Aggiornamento 'offline' (minuscolo): {'SUCCESSO' if esito_minuscolo else 'FALLITO'}")
    print(f"Stato attuale NAV-01: {APPARATI['NAV-01']['stato']}\n")
    
    esito_sconosciuto = aggiorna_stato("NAV-01", "rotto")
    print(f"Aggiornamento 'rotto' (sconosciuto): {'SUCCESSO' if esito_sconosciuto else 'FALLITO'}")
    print(f"Stato attuale NAV-01: {APPARATI['NAV-01']['stato']}")