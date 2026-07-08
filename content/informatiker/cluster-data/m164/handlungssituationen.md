---
cms: true
aliases:
  - /cluster-data/m164/handlungssituationen/
  - /v2/cluster-data/m164/handlungssituationen/
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

Mia setzt für eine Tierarztpraxis eine neue Datenbank auf. Aus einem bestehenden Datenmodell soll eine lauffähige Datenbank für die Kunden- und Patientenverwaltung entstehen, die mit Daten befüllt und auf Korrektheit geprüft wird.

## Handlungsziel 1 - Logisches, relationales Datenmodell interpretieren

Mia erhält vom Datenarchitekten ein logisches, relationales Datenmodell mit rund zehn Tabellen für Tierhalter, Tiere, Behandlungen und Rechnungen. Sie liest die Darstellung korrekt: Sie erkennt Primär- und Fremdschlüssel, versteht die einfachen, komplexen und rekursiven Beziehungstypen und weiss, welche Tabelle welche Information hält.

## Handlungsziel 2 - Datenmodell im DBMS implementieren

Mia setzt das Modell in einem relationalen Datenbankmanagementsystem um. Sie erstellt mit DDL die Tabellen, definiert Spalten samt passenden Datentypen und legt die Primär- und Fremdschlüssel gemäss Modell an.

## Handlungsziel 3 - Referenzielle Integrität sicherstellen

Damit keine Behandlung ohne zugehöriges Tier und kein Tier ohne Halter existieren kann, richtet Mia Integritätsbedingungen (Constraints) ein. Über Fremdschlüsselbeziehungen sowie NOT-NULL- und UNIQUE-Bedingungen stellt sie die referenzielle Integrität im Datenbankschema sicher.

## Handlungsziel 4 - Daten mittels DML einfügen

Mia erfasst erste Datensätze über die Datenbearbeitungssprache. Mit INSERT-Anweisungen fügt sie Tierhalter, deren Tiere und einige Behandlungen ein und achtet darauf, dass die Fremdschlüssel korrekt auf bestehende Datensätze verweisen.

## Handlungsziel 5 - Daten importieren

Die Praxis besitzt bereits eine Kundenliste in einer CSV-Datei. Mia importiert diese Daten in die passende Tabelle der neuen Datenbank und kontrolliert, dass die Zuordnung der Spalten und die Datentypen beim Import stimmen.

## Handlungsziel 6 - Eingefügte Daten prüfen

Mit einfachen Abfragen prüft Mia die Vollständigkeit und Korrektheit der eingefügten und importierten Daten. Sie zählt Datensätze, sucht nach fehlenden Pflichtangaben und kontrolliert, ob jede Behandlung einem existierenden Tier zugeordnet ist.

## Handlungsziel 7 - Fehlerhafte Daten korrigieren

Beim Prüfen findet Mia unvollständige Adressen und ein falsch zugeordnetes Tier. Sie korrigiert die fehlerhaften und unvollständigen Daten mit gezielten UPDATE-Anweisungen und stellt so einen sauberen, konsistenten Datenbestand her.
