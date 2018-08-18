import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats


def find_column(db):
    return db.columns


def find_info(db):
    return db.info()


def describe(db):
    return db.describe()


def violin_plot(x, y, data):
    violin = sns.boxplot(x=x, y=y, data=data)
    violin.set_title('Violin plot of {}'.format(y))
    violin.set_xlabel('diabete or not')
    violin.set_ylabel('amount')
    plt.show()


def plot_correlations(db):
    corr = db.corr()
    # print(corr)
    f, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr, mask=np.zeros_like(corr, dtype=np.bool), cmap=sns.diverging_palette(220, 10, as_cmap=True),
                square=True, ax=ax)
    plt.show()


def replace_zeros(db):
    db = db.replace(0, np.NaN)
    db.dropna(inplace=True)


def replace_with_mean(db):
    db = db.replace(0, np.NaN)
    db.fillna(db.mean(), inplace=True)


def max_min_norm(db):
    return (df - df.mean()) / (df.max() - df.min())


def z_norm(db):
    return (df - df.mean()) / (df.std())


def cut_age(db):
    return pd.cut(db['Age'], [11, 21, 31, 41, 51, 61, 71, 81])


def add_data_age(db):
    db_new = db
    # bins = [11, 21, 31, 41, 51, 61, 71, 81]
    for i in bins:
        db_new['Age_{}_{}'.format(
            i, i + 9)] = db['Age'].between(i, i + 9).astype(int)
    return db_new


if __name__ == '__main__':
    df = pd.read_csv('diabetes.csv')
    plot_correlations(df)
    # for c in find_column(df):
    #     violin_plot('Outcome', c, df)
    # replace_zeros(df)
    # result = add_data_age(df)
    # result = cut_age(df)
    # age = df['Age']
    # bins = [-np.inf, 11, 21, 31, 41, 51, 61, 71, 81, 91, np.inf]
    # age_new = pd.cut(age, bins, labels=range(len(bins) - 1))
    # print(age_new)
