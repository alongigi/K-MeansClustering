import pandas as pd

"""
    Filling the missing values (NA) with mean.

    df - Data Frame
"""


def fillMissingValuesWithMean(df):
    df_without_missing_values = df.fillna(df.mean())
    return df_without_missing_values



"""
Returns the mean of specific feature

df - Data Frame
feature_name - The mean of the feature
"""


def getFeatureMean(df, feature_name):
    return df[feature_name].mean()


"""
Returns the STD of specific feature

df - Data Frame
feature_name - The STD of the feature
"""


def getFeatureSTD(df, feature_name):
    return df[feature_name].std()


"""
Normilizes the data frame by mean and value -> (value - mean) / STD

df - Data Frame.
"""


def normalize(df):
    "Makes a copy of the data frame."
    result = df.copy()

    "For each feature in we normalize the data, except for those feature who are not numeric."
    for feature_name in df.columns:
        if feature_name == "country":
            continue

        try:
            mean = getFeatureMean(df, feature_name)
            std = getFeatureSTD(df, feature_name)

            "Inserting to the feature the normalized value."
            result[feature_name] = (df[feature_name] - mean) / std
        except:
            "Exception is thrown when the feature is not a value, for example country."
            continue

    return result


def kibuzData(df):
    "Makes a copy of the data frame."
    result = df.copy()

    """ Dictionary which the key is the country and the value is array -
    the first part of table is the number of values and the second is the sum of year
    for example Israel -> [2, 4000] --- there are two values of the country israel with both year 2000
    """
    dict = {}

    index = getNumberOfRows(result, "country") - 1

    while index >= 0:
        country_name = df["country"][index]

        if not country_name in dict:
            dict[country_name] = [0] * 2

        dict[country_name][0] += 1
        dict[country_name][1] += df["year"][index]

        index -= 1

    index = getNumberOfRows(result, "country") - 1

    newValues = []

    while (index >= 0):
        country_name = result["country"][index]

        newValues.append(dict[country_name][1] / dict[country_name][0])

        index -= 1

    df["country"] = newValues

    return df


def getNumberOfRows(df, feature):
    return df[feature].count()


