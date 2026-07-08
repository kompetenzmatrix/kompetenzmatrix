---
cms: true
aliases:
  - /cluster-data/m162/handlungssituationen/
  - /v2/cluster-data/m162/handlungssituationen/
title: Handlungssituationen
weight: 20
draft: false
---

# Handlungsziele und typische Handlungssituationen

Zu jedem Handlungsziel aus der Modulidentifikation (hier
gekürzt wiedergegeben) werden keine, eine oder mehrere
realistische, beispielhafte und konkrete Handlungssituationen
beschrieben, die zeigen, wie die Kompetenzen in der Praxis
angewandt werden.

Jonas unterstützt einen Sportverein, der seine Mitglieder-, Kurs- und Beitragsdaten bisher in mehreren Excel-Listen und Papierformularen führt. Er soll die Daten sichten und ein sauberes Datenmodell für eine künftige Vereinsdatenbank erstellen.

## Handlungsziel 1 - Daten sichten und einordnen

Jonas sammelt die vorhandenen Informationsbestände: strukturierte Excel-Listen der Mitglieder, unstrukturierte Notizen der Kursleitenden und ausgedruckte Anmeldeformulare. Er verschafft sich einen Überblick, ordnet die Datenquellen nach Inhalt ein und erkennt, welche Informationen mehrfach und an verschiedenen Orten geführt werden.

## Handlungsziel 2 - Informationsbestand charakterisieren und bereinigen

Jonas prüft die Mitgliederliste hinsichtlich Qualität: Er findet fehlende Geburtsdaten (Vollständigkeit), doppelt erfasste Personen (Redundanz) und widersprüchliche Adressangaben. Er charakterisiert den Bestand und bereinigt die Daten, wo es nötig ist, damit sie für die weitere Verarbeitung brauchbar sind.

## Handlungsziel 3 - Auswertbare Informationen auswählen

Für die geplante Beitragsauswertung wählt Jonas jene Informationen aus, die sich dafür eignen, etwa Mitgliedskategorie, Eintrittsdatum und bezahlte Beiträge. Dabei berücksichtigt er Schutzbedürfnisse: Personendaten wie Gesundheitsangaben aus alten Formularen lässt er weg oder behandelt sie vertraulich.

## Handlungsziel 4 - Konzeptionelles Datenmodell erstellen

Aus den bereinigten Daten entwirft Jonas ein konzeptionelles Datenmodell. Er bestimmt die Entitätstypen Mitglied, Kurs und Anmeldung, legt deren Attribute fest und modelliert die Beziehungen, etwa dass ein Mitglied sich für mehrere Kurse anmelden kann.

## Handlungsziel 5 - In ein logisches, relationales Datenmodell überführen

Jonas überführt das konzeptionelle Modell in ein logisches, relationales Datenmodell. Er ergänzt Identifikations- und Fremdschlüssel, wählt passende Datentypen und fügt für die Viele-zu-viele-Beziehung zwischen Mitglied und Kurs eine Zwischentabelle ein.

## Handlungsziel 6 - Datenmodell normalisieren

Jonas prüft das relationale Modell auf Redundanzen und Anomalien und normalisiert es. Er zerlegt Tabellen so, dass jede Information nur an einer Stelle geführt wird, und stellt damit die Konsistenz des Modells sicher.

## Handlungsziel 7 - Datenmodell darstellen

Zum Abschluss bildet Jonas das konzeptionelle und das logische, relationale Datenmodell in einer geeigneten Darstellung ab (z.B. als Entity-Relationship-Diagramm). So kann er das Modell dem Vereinsvorstand und späteren Entwicklern nachvollziehbar präsentieren.
