def analyser_log(fichier_log, fichier_rapport):
    erreurs = {"INFO": 0, "WARNING": 0, "ERROR": 0}

    # Codes couleurs ANSI
    couleurs = {
        "INFO": "\033[94m",
        "WARNING": "\033[93m",
        "ERROR": "\033[91m",
        "ENDC": "\033[0m"
    }

    with open(fichier_log, "r") as f:
        for ligne in f:
            if "INFO" in ligne:
                erreurs["INFO"] += 1
                print(f"{couleurs['INFO']}INFO: {ligne.strip()}{couleurs['ENDC']}")
            elif "WARNING" in ligne:
                erreurs["WARNING"] += 1
                print(f"{couleurs['WARNING']}WARNING: {ligne.strip()}{couleurs['ENDC']}")
            elif "ERROR" in ligne:
                erreurs["ERROR"] += 1
                print(f"{couleurs['ERROR']}ERROR: {ligne.strip()}{couleurs['ENDC']}")

    with open(fichier_rapport, "w") as f:
        for type_log, count in erreurs.items():
            f.write(f"{type_log}: {count}\n")

if __name__ == "__main__":
    analyser_log("log.txt", "rapport.txt")
    print("Analyse terminée. Rapport généré dans rapport.txt.")
