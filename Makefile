PYTHON = python3
PIP = pip3

SRC = $(wildcard py_file/*.py)        # tous les fichiers Python du dossier py_file
VENV = venv                           # nom du dossier de l'environnement virtuel
TESTS = tests                         # dossier contenant tes tests

all: run

# venv -> dossier isolé où Python installe ses propres librairies
venv:
	$(PYTHON) -m venv $(VENV)

# Installer les dépendances
install: venv
	$(VENV)/bin/$(PIP) install -r requirements.txt

# Lancer le programme principal
run:
	$(PYTHON) py_file/main.py

# Lancer les tests (si tu as un dossier tests avec pytest)
test:
	$(VENV)/bin/pytest $(TESTS)

# =========================
# Nettoyage
# =========================

# Nettoie les fichiers compilés Python (.pyc, __pycache__)
clean:
	find py_file -name "*.pyc" -delete
	find py_file -name "__pycache__" -type d -exec rm -rf {} + 
# pour chaque dossier trouvé ({} = le dossier trouvé) : supprime-le.
# Le + signifie qu’on peut passer plusieurs dossiers à la fois à rm -rf.

# Nettoyage complet : fichiers compilés + environnement virtuel
fclean: clean
	rm -rf $(VENV)

# Recompile tout : clean puis all
re: fclean all

# Indique que ces règles ne sont pas des fichiers réels
.PHONY: all venv install run test clean fclean re
