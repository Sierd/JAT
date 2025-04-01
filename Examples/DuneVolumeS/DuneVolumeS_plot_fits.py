# loop throught files in C:\Users\svries\Documents\GitHub\JAT\Examples\DuneVolumeS\C_dimensions_dataframes_per_transect folder
import os
import pickle
import pwlf
#import numpy as np
import matplotlib.pyplot as plt

# Function to process and plot data from a pickle file
def process_and_plot(file_path, output_folder):
    with open(file_path, 'rb') as f:
        data = pickle.load(f)
        data = data.dropna(subset=['DuneVol_fix'])

        # Check if data is empty and skip if so
        if data.shape[0] < 35:
            return
        

        # Extract x and y values
        x = data.index
        y = data['DuneVol_fix']

        # Initatie the basic plot
        cm = 1 / 2.54
        fig, ax = plt.subplots(figsize=(20 * cm, 15 * cm))
        ax.plot(x, y, 'o', label='Data')

        # Initialize piecewise linear fit with the data
        my_pwlf = pwlf.PiecewiseLinFit(x, y)

        # Fit the data with 1 line segment (linear fit)
        res1 = my_pwlf.fit(1)
        y_hat1 = my_pwlf.predict(x)

        # plot the linear fit with 1 line segment
        ax.plot(x, y_hat1, '-', label='Linear Fit R$^2$ = ' + str(my_pwlf.r_squared())[0:5] +
        '\nSlope = ' + str(my_pwlf.slopes[0])[0:3] + ' m$^3$/m/year')

        # Fit the data with 2 line segments (piecewise linear fit)
        res2 = my_pwlf.fit(2)
        y_hat2 = my_pwlf.predict(x)

        # plot the linear fit with 1 line segment
        ax.plot(x, y_hat2, '-', label='Piecewise Linear Fit R$^2$ = ' + str(my_pwlf.r_squared())[0:5] +
                '\nSlope1 = ' + str(my_pwlf.slopes[0])[0:3] + ' m$^3$/m/year' +
                '\nSlope2 = ' + str(my_pwlf.slopes[1])[0:3] + ' m$^3$/m/year')

        # Add vertical line for the optimal breakpoint
        ax.axvline(x=res2[1], color='r', linestyle='--', zorder=0, label='Optimal breakpoint ' + str(res2[1].round())[0:4])

        # Set plot title and labels
        #ax.set_title('DuneToe fix' + ' Transect ' + file_path.split('_')[1].split('.')[0])
        ax.set_ylabel('Dune Volume [m$^3$/m]')
        ax.set_xlabel('Year')

        # Add legend and save plot
        ax.legend()
        # save figure in pdf format keeping the figure size
        plt.savefig(os.path.join(output_folder, 'DuneToe_fix_' + file_path.split('_')[5].split('.')[0] + '.pdf'))
        # plt.savefig(os.path.join(output_folder, 'DuneToe_fix_' + file_path.split('_')[5].split('.')[0] + '.png'))
        plt.close()

# Main function to loop through files and process them
def main():
    folder = r'C:\Users\svries\Documents\GitHub\JAT\Examples\DuneVolumeS\C_dimensions_dataframes_per_transect2'
    output_folder = r'C:\Users\svries\Documents\GitHub\JAT\Examples\DuneVolumeS\DV_plots3'

    for file in os.listdir(folder):
        if file.endswith('.pickle'):
            file_path = os.path.join(folder, file)
            process_and_plot(file_path, output_folder)

if __name__ == "__main__":
    main()

