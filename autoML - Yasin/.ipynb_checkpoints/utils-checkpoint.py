import pandas as pd



# --------------------------------------------------------------------------
def get_preproccessed_df(s3_link):
    df_raw = pd.read_csv(s3_link, dtype={'DAY_OF_MONTH': str, 'CRS_ARR_TIME': str, 'CRS_DEP_TIME': str, 'WHEELS_OFF': str})
    columns_to_drop = ['YEAR', 'MONTH', 'FL_DATE', 'ORIGIN_STATE_NM', 'DEST_CITY_NAME', 'DEST_STATE_NM', 'DEP_TIME', 
                       'DEP_TIME_BLK', 'ARR_TIME', 'ARR_TIME_BLK', 'CARRIER_DELAY', 'WEATHER_DELAY', 'NAS_DELAY', 
                       'SECURITY_DELAY', 'LATE_AIRCRAFT_DELAY', 'FLIGHTS', 'Unnamed: 54', 
                       'OP_CARRIER_AIRLINE_ID',	'OP_CARRIER_FL_NUM', 'ORIGIN_AIRPORT_ID', 'ORIGIN_AIRPORT_SEQ_ID',	
                       'ORIGIN_CITY_MARKET_ID',	'ORIGIN_STATE_FIPS', 'DEST_AIRPORT_ID',	'DEST_AIRPORT_SEQ_ID',	
                       'DEST_CITY_MARKET_ID', 'DEST_STATE_FIPS', 'DEP_DELAY', 'DEP_DELAY_NEW', 'DEP_DEL15', 'DEP_DELAY_GROUP', 
                       'WHEELS_ON', 'ARR_DELAY', 'ARR_DEL15', 'ARR_DELAY_GROUP', 'CRS_ELAPSED_TIME', 'ACTUAL_ELAPSED_TIME', 
                       'AIR_TIME', 'OP_CARRIER',
                       'TAIL_NUM', 'ORIGIN_CITY_NAME']
    
    # drop flights which are either canceled or diverted
    # as this is a conceptually different thing than being delayed
    df_raw = df_raw.drop(df_raw.index[(df_raw['CANCELLED'] == 1) | 
                         (df_raw['DIVERTED'] == 1)]).reset_index(drop=True)
    
    df_raw = df_raw.drop(columns_to_drop, axis=1)
    df_raw = df_raw.drop(['CANCELLED', 'DIVERTED'], axis=1)
    
    # to get label column up front
    df_raw = df_raw[sorted(df_raw.columns)]
    
    return df_raw