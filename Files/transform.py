# Final Project - Big Data Access Management - NYPD Shooting Incident Data
#   Author: Rakesh Jothishankar
#   Date: 11/21/2021

# import libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


def main():
    # data load into dataFrame (and then drop columns which are not needed for further processing)
    inc_df = pd.read_csv("ny_shooting_inc.csv")
    inc_df = inc_df.drop(columns=["JURISDICTION_CODE", "LOCATION_DESC", "X_COORD_CD", "Y_COORD_CD", 
                                  "Latitude", "Longitude", "Lon_Lat"], axis=1)

    # "Data Transformation / Clean-up"
 
    # converting NaN values over to UNKNOWN
    # *_SEX already has a value of U for known, and hence converting NaN to U for SEX field
    inc_df = inc_df.replace(np.nan, "UNKNOWN")
    inc_df["PERP_SEX"] = inc_df["PERP_SEX"].replace("UNKNOWN", "U")
    inc_df["VIC_SEX"] = inc_df["VIC_SEX"].replace("UNKNOWN", "U")

    # bad values for PERP_AGE_GROUP present for 1 record each in 2010, 2013 and 2015
    inc_df["PERP_AGE_GROUP"] = inc_df["PERP_AGE_GROUP"].replace("1020", "UNKNOWN")
    inc_df["PERP_AGE_GROUP"] = inc_df["PERP_AGE_GROUP"].replace("940", "UNKNOWN")
    inc_df["PERP_AGE_GROUP"] = inc_df["PERP_AGE_GROUP"].replace("224", "UNKNOWN")

    # extract year value from occurrance date
    inc_df["OCCUR_YEAR"] = inc_df["OCCUR_DATE"].str[-4:].astype(int)

    # "Visualizations"
   
    # output to pdf
    out_pdf = PdfPages('output_visuals.pdf')

    # visualization to show the victim race counts
    sns.countplot(x='VIC_RACE', data=inc_df)
    plt.title('Victim Race - Counts')
    plt.xlabel("Race", fontsize=10)
    plt.ylabel("Count", fontsize=10)
    plt.xticks(rotation=90)
    plt.savefig(out_pdf, format='pdf', bbox_inches='tight')

    # visualization to show the victim age group counts
    sns.countplot(x='VIC_AGE_GROUP', data=inc_df)
    plt.title('Victim Age Group - Counts')
    plt.xlabel("Age Group", fontsize=10)
    plt.ylabel("Count", fontsize=10)
    plt.xticks(rotation=0)
    plt.savefig(out_pdf, format='pdf', bbox_inches='tight')

    # visualization to show the victim sex counts
    sns.countplot(x='VIC_SEX', data=inc_df)
    plt.title('Victim Sex - Counts')
    plt.xlabel("Sex", fontsize=10)
    plt.ylabel("Count", fontsize=10)
    plt.xticks(rotation=0)
    plt.savefig(out_pdf, format='pdf', bbox_inches='tight')

    # visualization to show the perpetrator race counts
    sns.countplot(x='PERP_RACE', data=inc_df)
    plt.title('Perpetrator Race - Counts')
    plt.xlabel("Race", fontsize=10)
    plt.ylabel("Count", fontsize=10)
    plt.xticks(rotation=90)
    plt.savefig(out_pdf, format='pdf', bbox_inches='tight')

    # visualization to show the perpetrator age group counts
    sns.countplot(x='PERP_AGE_GROUP', data=inc_df)
    plt.title('Perpetrator Age Group - Counts')
    plt.xlabel("Age Group", fontsize=10)
    plt.ylabel("Count", fontsize=10)
    plt.xticks(rotation=0)
    plt.savefig(out_pdf, format='pdf', bbox_inches='tight')

    # visualization to show the perpetrator sex counts
    sns.countplot(x='PERP_SEX', data=inc_df)
    plt.title('Perpetrator Sex - Counts')
    plt.xlabel("Sex", fontsize=10)
    plt.ylabel("Count", fontsize=10)
    plt.xticks(rotation=0)
    plt.savefig(out_pdf, format='pdf', bbox_inches='tight')

    # visualization to show incident occurrences per year
    sns.catplot(y="OCCUR_YEAR", kind="count", data=inc_df)
    plt.title('Count of Incidents by Year')
    plt.ylabel("Year", fontsize=10)
    plt.xlabel("Count", fontsize=10)
    plt.yticks(rotation=0)
    plt.savefig(out_pdf, format='pdf', bbox_inches='tight')

    # visualization to show incident occurrences per year split by murdered and not murdered
    sns.catplot(y="OCCUR_YEAR", hue="STATISTICAL_MURDER_FLAG", kind="count", data=inc_df)
    plt.title('NY Shooting Victims by Year - Survived (Flag - False) & Murdered (Flag - True)')
    plt.xticks(rotation=0)
    plt.ylabel("Year", fontsize=10)
    plt.xlabel("Count", fontsize=10)
    plt.savefig("output_visuals.png", format='png', bbox_inches='tight')

    # visualization to show incident occurrences per borough
    sns.catplot(x="BORO", kind="count", data=inc_df, palette="pastel")
    plt.title('Count of Incidents by Boroughs')
    plt.xticks(rotation=90)
    plt.ylabel("Count", fontsize=10)
    plt.xlabel("Borough", fontsize=10)
    plt.savefig(out_pdf, format='pdf', bbox_inches='tight')

    # visualization to show incident occurrences per borough split by murdered and not murdered
    sns.catplot(x="BORO", hue="STATISTICAL_MURDER_FLAG", kind="count", palette="pastel", data=inc_df)
    plt.title('NY Shooting Victims by Boroughs - Survived (Flag - False) & Murdered (Flag - True)')
    plt.xticks(rotation=90)
    plt.ylabel("Count", fontsize=10)
    plt.xlabel("Borough", fontsize=10)
    plt.savefig(out_pdf, format='pdf', bbox_inches='tight')

    out_pdf.close()


main()