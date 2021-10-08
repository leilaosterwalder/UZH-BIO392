"""
sarcoma group: J. Chalabi, A. K. Jochum, D. Walther
bio392: survival project
plots were made in R. There are specific reasons for the only partial success of doing the task in python.
"""


#%% Importing Python Packages

# packages for file handling
import csv

# packages for numerical computation (arrays, matrices, data frames - more practical data types for changing & plotting)
#import numpy as np
import pandas as pd  # basically numpy with additional names for rows/columns, instead of only indeces.

# packages for plotting
import matplotlib.pyplot as plt
from lifelines import KaplanMeierFitter


#%% Data Handling

# Functions to get gene data (cheatsheet)


def transform_to_df(data):
    """
    transform ... data format to pandas data frame format.
    :param data: input dataset of type
    :return: same dataset but as a pandas data frame (pd.DataFrame)
    """
    data = pd.DataFrame(data)
    data.columns = data.iloc[0]  # passes the header row with column names to the pandas data frame '.columns'
    data = data[1:]  # passes the actual data to the pandas data frame
    return data


def get_gene_data(cancer_type, gene_name):
    """
    reads in specific .csv data files (provided by course),
    transforms them into lists,
    clears all empty rows (ignoring 'uninteresting' variables (= columns)),
    transforms these cleared lists into pd.DataFrame format (via 'transform_to_df()' function)
    :param cancer_type: e.g. sarcoma - only cancer_type file is the survival file
    :param gene_name: e.g. tp53 - cancer_type + gene_name in filename is gene CNV data corresponding to cancer data
    :return: pd.dataframe variables of the survival file, gene CNV data, list of the gene CNV data
    """

    # survival data set
    with open(cancer_type + '.csv', 'r') as read_obj:
        csv_reader = csv.reader(read_obj)
        cancer = list(csv_reader)
        header = cancer[0]  # the header row of the data set

        # filtering out empty rows of variables (columns) of interest
        #   1. copy over interesting rows in new

    # extract some ids
    ids = []
    for id in cancer:
        ids.append(id[14])  # extract the ids of the patients from which an observation stems

    # gene CNV data set
    with open(cancer_type + '_' + gene_name + '.csv', 'r') as read_obj:
        csv_reader = csv.reader(read_obj)
        gene_all = list(csv_reader)
        header2 = gene_all[0]

    gene_data = []
    for line in gene_all:
        if line[16] in ids: # previously line[14]
            gene_data.append(line)

    # transform list version of data to pd.dataframe version of data
    cancerdf = transform_to_df(cancer)
    genedf = transform_to_df(gene_data)

    print(len(ids), len(gene_data))

    return cancerdf, genedf, cancer  # added return variable 'cancer', a list version of the cancer gene CNV data set

# df.column_name != whole string from the cell
# now, all the rows with the column: Name and Value: "dog" will be deleted

# calling the functions for saving data sets to usable variables here.
sarcoma, tp53, tp53_list = get_gene_data('sarcoma', 'tp53del')
    # survival set (pd.dataframe), cancer gene CNV set (pd.dataframe), cancer gene CNV set (list)
sarcoma, cdkn2a, cdkn2a_list = get_gene_data('sarcoma', 'cdkn2adel')
sarcoma, erbb2, erbb2_list = get_gene_data('sarcoma', 'erbb2dup')
sarcoma, myc, myc_list = get_gene_data('sarcoma', 'mycdup')

    #for el in tp53_list:
        #print(el[51])

sarcomanum = sarcoma.apply(pd.to_numeric, errors='coerce').fillna(sarcoma)
    # changes format from pd.dataframe to some numeric format (which one? what changed, simply no column names?)


#%% Kaplan-Meier plot (survival plot)

NCIT_surv = sarcomanum['histologicalDiagnosis.label'].unique()
## KM-plot works with: i=0, i=1, i=2, i=4, i=7 where i is index in NCIT_surv[i]


def plot_survival(i):
    group = sarcomanum.groupby("histologicalDiagnosis.label").get_group(NCIT_surv[i])
    kmf = KaplanMeierFitter()
    durations = group['info.followupMonths']  # cnvcoverage ("test for me") -> change to followup
    event_observed = group['info.death']

    kmf.fit(durations, event_observed, label=NCIT_surv[i])
    kmf.plot(ci_show=False)


# could make a loop out of this, but let's stop here.
plot_survival(i=0)
plot_survival(i=1)
plot_survival(i=2)
plot_survival(i=4)
plot_survival(i=7)
plt.xlabel('duration (Months)')
plt.ylabel('survival (proportion)')
plt.title('sarcoma survival, comparison of subtypes')

plt.show()


#%% Boxplot (CNV fraction) (cheatsheet)

NCIT_box = sarcomanum['histologicalDiagnosis.label'].unique()  # moved to previous chunk
i = 0

mean = sarcomanum.groupby("histologicalDiagnosis.label").get_group(NCIT_box[i])
ax = plt.subplot(1, 1, 1)
mean.boxplot()

ax.set_xticklabels(['cnvcoverage', 'delcoverage', 'dupcoverage', 'death']) # rotation=90 changed to 180
ax.set_title(NCIT_box[i])

plt.show()



#%% Communication - spoken
