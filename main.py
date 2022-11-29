import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import cm
from joypy import joyplot


def ridgeline():
    data = pd.read_csv("Barcelona_rent_price.csv")
    data.dropna()

    # Solo nos interesa el precio mensual
    data_rent = data[data["Average _rent"] == "average rent (euro/month)"]

    """
    clusters = data_rent.groupby(['Year'])
    data_rent['year_avg'] = clusters['Price'].transform('mean')

    data_rent.head()
    """

    plt.figure()

    joyplot(
        data=data_rent[['Price', 'Year']],
        by='Year',
        figsize=(12, 8)
    )
    plt.xlabel('Average monthly rent (euros)', fontsize=12)
    plt.title("Barcelona's average rent price (2014-2022)", fontsize=20)
    plt.xlim(0, 2000)
    plt.savefig('ridgeline_barcelona.png')


if __name__ == '__main__':
    ridgeline()