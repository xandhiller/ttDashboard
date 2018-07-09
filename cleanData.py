import pandas as pd


# Get the confirmed and provisional numbers into df(s)
# TODO: Generalise the function and put it in a module
def cleanData(io):

    # Aimed sales target for certain locations
    # TODO: Fix the target value for South Lunaga and Liuwa, they currently share a value but it is being spread between them
    target_bednights = {
        'Lower Zambezi':4050,
        'Nosy Ankao':1600,
        'South Luanga':5500,
        'Liuwa':5500,
        }

    # Used to make sure program uses the correct rows of the spreadsheet
    lower_zambezi_rows   =   {'Confirmed': 0,   'Provisional': 1}
    nosy_ankao_rows      =   {'Confirmed': 6,   'Provisional': 7}
    south_luanga_rows    =   {'Confirmed': 12,  'Provisional': 13}
    liuwa_rows           =   {'Confirmed': 14,  'Provisional': 15}

    # Path to data

    # Transpose the excel spreadsheet, and re-save it, it's quicker
    # Read original
    df = pd.read_excel(io, skiprows=0)

    # Transpose it
    df = df.T

    # Make a new path (hence won't overwrite)
    io = io.split(sep='.')
    io_transp = io[0]+'_TRANSPOSED.'+ io[1]

    # Save it
    df.to_excel(io_transp)

    # Re-read and skip columns necessary for certain areas
    df_lz = pd.read_excel(
        io_transp,
        usecols=[
            lower_zambezi_rows['Confirmed'],
            lower_zambezi_rows['Provisional'],
        ])
    df_lz = df_lz.drop('Lower Zambezi')
    df_lz.columns = ['Confirmed', 'Provisional']
    df_lz = df_lz.dropna()
    try:
        df_lz = df_lz.drop(['2019.1'], axis=0)
        df_lz = df_lz.drop([2019], axis=0)
    except:
        None

    df_na = pd.read_excel(
        io_transp,
        usecols=[
            nosy_ankao_rows['Confirmed'],
            nosy_ankao_rows['Provisional'],
        ])
    df_na = df_na.drop('Lower Zambezi')
    df_na.columns = ['Confirmed', 'Provisional']
    df_na = df_na.dropna()
    try:
        df_na = df_na.drop(['2019.1'], axis=0)
        df_na = df_na.drop([2019], axis=0)
    except:
        None


    df_sl = pd.read_excel(
        io_transp,
        usecols=[
            south_luanga_rows['Confirmed'],
            south_luanga_rows['Provisional'],
        ])
    df_sl = df_sl.drop('Lower Zambezi')
    df_sl.columns = ['Confirmed', 'Provisional']
    df_sl = df_sl.dropna()
    try:
        df_sl = df_sl.drop(['2019.1'], axis=0)
        df_sl = df_sl.drop([2019], axis=0)
    except:
        None

    df_liu = pd.read_excel(
        io_transp,
        usecols=[
            liuwa_rows['Confirmed'],
            liuwa_rows['Provisional'],
        ])
    df_liu = df_liu.drop('Lower Zambezi')
    df_liu.columns = ['Confirmed', 'Provisional']
    df_liu = df_liu.dropna()
    try:
        df_liu = df_liu.drop(['2019.1'], axis=0)
        df_liu = df_liu.drop([2019], axis=0)
    except:
        None
    #
    # logging.info(
    #     'Data frames beofre being returned from function:\n'
    #     + '\nLower Zambia dataframe has SHAPE:\n'         + str(df_lz.shape)
    #     + '\n\nLower Zambia dataframe has CONTENTS:\n'    + str(df_lz)
    #     + '\n\nNosy Ankao dataframe has SHAPE:\n'         + str(df_na.shape)
    #     + '\n\nNosy Ankao dataframe has CONTENTS:\n'      + str(df_na)
    #     + '\n\nSouth Luanga dataframe has SHAPE:\n'       + str(df_sl.shape)
    #     + '\n\nSouth Luanga dataframe has CONTENTS:\n'    + str(df_sl)
    #     + '\n\nLiuwa dataframe has SHAPE:\n'              + str(df_liu.shape)
    #     + '\n\nLiuwa dataframe has CONTENTS:\n\n'         + str(df_liu)
    #     )
    return df_lz, df_na, df_liu, df_sl
