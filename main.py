import pandas as pd
import numpy as np
from utils.analysis import stat_analysis

# Load extended data
pokedex = pd.read_csv("data/pokedex.csv")

def main_menu():
    print("\n===== POKÉDEX =====")
    print("1. View all Pokémon")
    print("2. Search by Name")
    print("3. Filter by Type")
    print("4. Show Legendary Pokémon")
    print("5. Evolution Chain")
    print("6. Stats Summary (NumPy)")
    print("7. Exit")
    return input("Choose an option: ")

def view_all():
    print(pokedex[['No', 'Name', 'Type1', 'Type2']])

def search_by_name():
    name = input("Enter Pokémon name: ").capitalize()
    result = pokedex[pokedex["Name"] == name]
    if result.empty:
        print("Not found.")
    else:
        print(result.to_string(index=False))

def filter_by_type():
    t = input("Type: ").capitalize()
    res = pokedex[(pokedex["Type1"] == t) | (pokedex["Type2"] == t)]
    print(res[['No','Name','Type1','Type2']])

def show_legendary():
    lg = pokedex[pokedex["Legendary"] == True]
    print(lg[['No', 'Name', 'Type1', 'Type2', 'HP', 'Attack', 'Defense', 'Speed']])

def evolution_chain():
    name = input("Enter Pokémon name: ").capitalize()
    # find it
    df = pokedex.set_index("Name")
    if name not in df.index:
        print("Not found.")
        return
    chain = [name]
    # forward chain
    current = name
    while True:
        next_evos = df.loc[current, "NextEvolutions"]
        if pd.isna(next_evos) or next_evos == "":
            break
        # may be multiple
        parts = [p.strip() for p in next_evos.split(",")]
        # pick the first for simplicity or list all
        current = parts[0]
        chain.append(current)
    print(" → ".join(chain))

def stats_summary():
    stats = pokedex[['HP','Attack','Defense','Speed']].to_numpy()
    print("Avg HP:", np.mean(stats[:,0]))
    print("Avg Attack:", np.mean(stats[:,1]))
    print("Avg Defense:", np.mean(stats[:,2]))
    print("Avg Speed:", np.mean(stats[:,3]))

def main():
    while True:
        choice = main_menu()
        if choice == '1':
            view_all()
        elif choice == '2':
            search_by_name()
        elif choice == '3':
            filter_by_type()
        elif choice == '4':
            show_legendary()
        elif choice == '5':
            evolution_chain()
        elif choice == '6':
            stats_summary()
        elif choice == '7':
            print("Exiting.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
