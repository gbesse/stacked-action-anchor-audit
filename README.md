# stacked-action-anchor-audit

## Français

Détecter un ancrage temporel périmé malgré un aller-retour correct.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m stacked_action_anchor_audit examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Détecter un ancrage temporel périmé malgré un aller-retour correct : calcul déterministe sur entrées structurées, témoins et cas limites explicites.

### Limites

Modèle borné, données fictives, aucun service ou matériel de production validé. Méthodes classiques ; aucune supériorité SOTA générale ni adoption humaine démontrée.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Detect stale temporal anchors despite correct round trips.

Synthetic data; no network access or secret required.

```sh
python -m stacked_action_anchor_audit examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Detect stale temporal anchors despite correct round trips: deterministic computation over structured inputs, explicit witnesses and boundary cases.

### Limits

Bounded model and synthetic data; no production service or hardware validated. Classical methods; no general SOTA superiority or human adoption demonstrated.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Detectar anclas temporales obsoletas pese a ida y vuelta correcta.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m stacked_action_anchor_audit examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Detectar anclas temporales obsoletas pese a ida y vuelta correcta: cálculo determinista con entradas estructuradas, testigos y casos límite explícitos.

### Límites

Modelo acotado y datos ficticios; ningún servicio ni hardware de producción validado. Métodos clásicos; sin superioridad SOTA general ni adopción humana demostrada.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://github.com/huggingface/lerobot/issues/5315
- https://github.com/huggingface/lerobot/issues/5289
- https://github.com/huggingface/lerobot/issues/5284
- https://github.com/huggingface/lerobot/issues/5313
- https://github.com/huggingface/lerobot/issues/5187

## Projets voisins / Neighboring projects / Proyectos vecinos

FR : [episode-video-index-audit](https://github.com/gbesse/episode-video-index-audit) est un autre diagnostic du portefeuille. Ici : Détecter un ancrage temporel périmé malgré un aller-retour correct. Comparaison de périmètres seulement, sans affiliation ni benchmark de supériorité.

EN: [episode-video-index-audit](https://github.com/gbesse/episode-video-index-audit) is a different portfolio diagnostic. Here: Detect stale temporal anchors despite correct round trips. Scope comparison only, no affiliation or superiority benchmark.

ES: [episode-video-index-audit](https://github.com/gbesse/episode-video-index-audit) es otro diagnóstico del portafolio. Aquí: Detectar anclas temporales obsoletas pese a ida y vuelta correcta. Comparación de alcance, sin afiliación ni benchmark de superioridad.
