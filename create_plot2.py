#
#   Packages and modules
#
import sys

# pandas is a (somewhat slow) library to do complicated
# things with CSV files. We will use it here to identify
# data by column
import pandas as pd

# seaborn and matplotlib are for plotting.  The matplotlib
# library is the actual graphics library, and seaborn provides
# a nice interface to produce plots more easily.
import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib import ticker as ticktools

def main(argv):

    if len(argv) != 3:
        print("Usage:",
                "create_plot2.py <data file> <graphics file>")
        sys.exit(-1)

    csv_filename = argv[1]
    graphics_filename = argv[2]

    try:
        csv_df = pd.read_csv(csv_filename)

    except IOError as err:
        print("Unable to open source file", csv_filename,
                ": {}".format(err), file=sys.stderr)
        sys.exit(-1)

    fig = plt.figure()

    ax = sns.lineplot(x = "Date", y = "Number of Cases", hue="Type of Data", data=csv_df)

    ax.xaxis.set_major_locator(ticktools.MaxNLocator(8))

    plt.xticks(rotation = 45, ha = 'right')
  
    fig.savefig(graphics_filename, bbox_inches="tight")


main(sys.argv)
