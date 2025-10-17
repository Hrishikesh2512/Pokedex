import pandas as pd
import numpy as np

def stat_analysis(df):
    stats = df[['HP', 'Attack', 'Defense', 'Speed']].to_numpy()
    avg = np.mean(stats, axis=0)
    print("\nStat Summary:")
    print(f"HP: {avg[0]:.1f}, Attack: {avg[1]:.1f}, Defense: {avg[2]:.1f}, Speed: {avg[3]:.1f}")
