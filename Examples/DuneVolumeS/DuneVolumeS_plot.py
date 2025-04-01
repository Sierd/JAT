# loop throught files in C:\Users\svries\Documents\GitHub\JAT\Examples\DuneVolumeS\C_dimensions_dataframes_per_transect folder
import os
import pickle
import matplotlib.pyplot as plt

folder = r'C:\Users\svries\Documents\GitHub\JAT\Examples\DuneVolumeS\C_dimensions_dataframes_per_transect'

for file in os.listdir(folder):
    if file.endswith('.pickle'):
        with open(os.path.join(folder, file), 'rb') as f:
            data = pickle.load(f)
            fig, ax = plt.subplots()
            data['DuneVol_fix'].plot(ax=ax,marker='o', linestyle='None')
            ax.set_title('DuneToe fix' + ' Transect ' + file.split('_')[1].split('.')[0])
            ax.set_ylabel('m$^3$/m')
            plt.savefig(r'C:\Users\svries\Documents\GitHub\JAT\Examples\DuneVolumeS\DV_plots\DuneToe_fix_' + file.split('_')[1].split('.')[0] + '.png')
            # close plot
            plt.close()
            
