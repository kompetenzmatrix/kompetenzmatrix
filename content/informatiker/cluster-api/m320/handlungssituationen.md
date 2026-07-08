---
cms: true
aliases:
  - /cluster-api/m320/handlungssituationen/
  - /v2/cluster-api/m320/handlungssituationen/
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

Tim entwickelt in einem kleinen Softwareteam eine Anwendung zur Verwaltung einer Vereinsbibliothek. Bücher, Mitglieder und Ausleihen sollen objektorientiert abgebildet werden. Tim setzt den Auftrag von der Analyse bis zur geprüften Implementierung um.

## Handlungsziel 1 - Anwendungsproblem analysieren

Aus der Aufgabenstellung «Ausleihe von Büchern an Vereinsmitglieder» arbeitet Tim die relevanten Begriffe heraus. Er identifiziert die fachlichen Klassen Buch, Mitglied und Ausleihe, bestimmt deren Verantwortlichkeiten und überlegt, welche Daten und welches Verhalten zu welcher Klasse gehören. So legt er die Grundlage für ein objektorientiertes Programm mit drei bis fünf fachlichen Klassen.

## Handlungsziel 2 - Objektorientiertes Design modellieren und dokumentieren

Tim modelliert die gefundenen Klassen in einem UML-Klassendiagramm. Er zeichnet Attribute, Methoden und die Beziehungen zwischen Buch, Mitglied und Ausleihe ein (z.B. ein Mitglied kann mehrere Ausleihen haben) und entscheidet, wo Vererbung oder Aggregation sinnvoll ist. Das Diagramm dokumentiert das Design nachvollziehbar für das Team.

## Handlungsziel 3 - Objektorientiertes Design implementieren

Auf Basis des Modells setzt Tim die Klassen im Code um. Er implementiert Kapselung über private Attribute mit Zugriffsmethoden, bildet die Beziehungen als Referenzen ab und nutzt Vererbung, um gemeinsame Eigenschaften in einer Basisklasse zusammenzufassen. Fehlerfälle wie eine bereits ausgeliehene Buchkopie fängt er mit Exceptions ab.

## Handlungsziel 4 - Implementierung auf Korrektheit und Qualität überprüfen

Tim schreibt Unit-Tests für die zentralen Klassen und prüft, ob Ausleihe und Rückgabe wie erwartet funktionieren. Er kontrolliert seinen Code auf Lesbarkeit, sinnvolle Benennung und Einhaltung der objektorientierten Prinzipien und verbessert Stellen, an denen Verantwortlichkeiten unsauber verteilt sind. So stellt er Korrektheit und Qualität der Anwendung sicher.
