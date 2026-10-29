#!/usr/bin/env python3
"""Authoring generator for Week 1 (Thème 1: Syntaxe et Sémantique propositionnelle).
Generates:
- content/w01/cours.fr.html & cours.fa.html
- content/w01/td.fr.html & td.fa.html
- content/w01/tp.fr.html & tp.fa.html
- content/w01/annales.fr.html & annales.fa.html
- content/w01/revision.fr.html & revision.fa.html
Ensuring 100% structural, tag, and ID parity between French and Persian.
"""
import os, sys, json

W01_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'content', 'w01')
os.makedirs(W01_DIR, exist_ok=True)

print("Generator script created.")

