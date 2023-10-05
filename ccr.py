import pandas as pd
import logging
from datetime import datetime
import os
import traceback

def read_files(file_paths_dict):
    dataframes = []
  
    for data_type, paths in file_paths_dict.items():
  
        for path in paths:
    
            df = pd.read_csv(path)  
            dataframes.append((data_type, df))

    return dataframes 

def aggregate_data(dataframes):

    logging.info("Standardizing columns...")
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S") 
    for data_type, df in dataframes:
        if 'Student Identifier' in df.columns:
            
            df = df.rename(columns={'Student Identifier': 'StudentNumber'})
            
            # Save CSV 
            output_file = f"standardized_{data_type}_{timestamp}.csv" 
            df.to_csv(output_file)
    
    logging.info("Adding suffixes...")
    suffixed_dfs = []
    for data_type, df in dataframes:
        logging.info(f"{data_type}_shape is_{df.shape}")
        df = df.rename(columns=lambda x: f"{x}_{data_type}")
        output_file = f"suffixed_{data_type}_{timestamp}.csv" 
        df.to_csv(output_file)
        suffixed_dfs.append((data_type, df))
        logging.info(f"Suffix added: {data_type}")
 
    logging.info("Merging dataframes...")
 
    # Initialize merged 
    merged_df = suffixed_dfs[0]
 
    # Merge 
    for data_type, df in suffixed_dfs[1:]:
        logging.info(f"Merging df: {df.shape}")
               
        """I need to adjust the merge operatoin
        Its trying to merged df which is a dataframe as intended
        but merged_df is a tuple of data_type and the df, this needs extracted
        out before trying to merged it with df"""
        
        merged_df = pd.merge(merged_df, df, on='StudentNumber_std', how='outer')
        output_file = f"merged_{data_type}_{timestamp}.csv" 
        merged_df.to_csv(output_file)
        logging.info(f"Post-merge shape: {merged_df.shape}")
        
   
    return merged_df

def calculate_weight(score, ranges, weights):
    """
    This may need refactored after changes to read and aggregate functions
    """
    for i, range_ in enumerate(ranges):
        if score in range_:
            return weights[i]
    return 0

def compute_weights(df):
    """
    This may need refactored after changes to read and aggregate functions
    """
    act_ranges = [range(0, 18), range(18, 22), range(22, 26), range(26, 36)]
    act_weights = [0.25, 0.75, 1, 1.25]
    
    asvab_ranges = [range(0, 30), range(30, 63), range(63, 88), range(88, 101)]
    asvab_weights = [0.25, 0.75, 1, 1.25]
    
    workkeys_ranges = [range(0, 4), range(4, 5), range(5, 6), range(6, 8)]
    workkeys_weights = [0.25, 0.75, 1, 1.25]
    
    grade_ranges = [range(90, 101), range(80, 90), range(70, 80), range(0, 70)]  # Assuming grades are out of 100
    grade_weights = [1, 1, 1, 0]
    
    ap_exam_ranges = [range(3, 6)]
    ap_exam_weights = [1.25]
    
    irc_exam_ranges = [range(1, 2)]  # Assuming a pass is represented as 1
    irc_exam_weights = [1]
    
    pltw_exam_ranges = [range(6, 11)]
    pltw_exam_weights = [1]

    # Apply the ranges and weights to calculate the weight for each assessment
    df['ACT Weight'] = df['ACT'].apply(calculate_weight, args=(act_ranges, act_weights))
    df['ASVAB Weight'] = df['ASVAB'].apply(calculate_weight, args=(asvab_ranges, asvab_weights))
    df['WorkKeys Weight'] = df['WorkKeys'].apply(calculate_weight, args=(workkeys_ranges, workkeys_weights))
    df['S1 AP Weight'] = df['S1 AP Grade'].apply(calculate_weight, args=(grade_ranges, grade_weights))
    df['S2 AP Weight'] = df['S2 AP Grade'].apply(calculate_weight, args=(grade_ranges, grade_weights))
    df['S1 DC Weight'] = df['S1 DC Grade'].apply(calculate_weight, args=(grade_ranges, grade_weights))
    df['S2 DC Weight'] = df['S2 DC Grade'].apply(calculate_weight, args=(grade_ranges, grade_weights))
    df['AP Exam Weight'] = df['AP Exam'].apply(calculate_weight, args=(ap_exam_ranges, ap_exam_weights))
    df['IRC Exam Weight'] = df['IRC Exam'].apply(calculate_weight, args=(irc_exam_ranges, irc_exam_weights))
    df['PLTW Exam Weight'] = df['PLTW Exam'].apply(calculate_weight, args=(pltw_exam_ranges, pltw_exam_weights))

    return df

def compute_ccr_totals(df):
    """
    This may need refactored after changes to read and aggregate functions
    """
    df['CCR 1-3 Total'] = df[['ACT Weight', 'ASVAB Weight', 'WorkKeys Weight']].max(axis=1)
    df['CCR 4 Total'] = df[['S1 AP Weight', 'S1 DC Weight', 'S2 AP Weight', 'S2 DC Weight', 
                            'AP Exam Weight', 'IRC Exam Weight', 'PLTW Exam Weight']].max(axis=1)
    return df

def select_grades(df, grade_data):
    """Need to gather AP/DC export files before writing this"""
    pass

def generate_output_file(df, file_name):
    """
    Generates the output file containing the data.
    
    Parameters:
    df (DataFrame): The DataFrame containing the data.
    file_name (str): The name of the output file.
    """
    with pd.ExcelWriter(file_name) as writer:
        df.to_excel(writer, sheet_name='Data', index=False)

def create_pivot_table(df, file_name):
    """
    Creates a pivot table and appends it to the output file.
    
    Parameters:
    df (DataFrame): The DataFrame containing the data.
    file_name (str): The name of the output file.
    """
    
    pivot_table = pd.pivot_table(df, ... )  # Fill in the pivot table parameters
    with pd.ExcelWriter(file_name, mode='a') as writer:
        pivot_table.to_excel(writer, sheet_name='Pivot Table')

def main():
    logging.basicConfig(filename='script.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')


    try:
        # Step 1: File Reading and Data Aggregation
        file_paths = {
            'ACT_CY': [
                "dataSources/ACT_CY.csv"
            ],
            'ACT_PY1': [
                "dataSources/ACT_PY1.csv"
            ],
            'ACT_PY2' : [
                "dataSources/ACT_PY2.csv"
            ],
            'ACT_PY3' : [
                "dataSources/ACT_PY3.csv"
            ],
            'ACT_PY4' : [
                "dataSources/ACT_PY4.csv"
            ],
            'AP_School1_PY1' : [
                "dataSources/AP_School1_PY1.csv"
            ],
            'AP_School1_PY2' : [
                "dataSources/AP_School1_PY2.csv"
            ],
            'AP_School1_PY3' : [
                "dataSources/AP_School1_PY3.csv"
            ],
            'AP_School2_PY1': [
                "dataSources/AP_School2_PY1.csv"
            ],
            'AP_School2_PY2': [
                "dataSources/AP_School2_PY2.csv"
            ],
            'AP_School2_PY3': [
                "dataSources/AP_School2_PY3.csv"
            ],                          
            'AP_School3_PY1': [
                "dataSources/AP_School3_PY1.csv"
            ],
            'AP_School3_PY2': [
                "dataSources/AP_School3_PY2.csv"
            ],
            'AP_School3_PY3': [
                "dataSources/AP_School3_PY3.csv"            
            ],
            'ASVAB_PY1': [
                "dataSources/ASVAB_PY1.csv"
            ],
            'ASVAB_PY2': [
                "dataSources/ASVAB_PY2.csv"
            ],
            'ASVAB_PY3': [
                "dataSources/ASVAB_PY3.csv"
            ],
            'ASVAB_PY4': [
                "dataSources/ASVAB_PY4.csv"
            ],
            'WorkKeys_PY1': [
                "dataSources/workkeys_PY1.csv"
            ],
            'WorkKeys_PY2': [
                "dataSources/workkeys_PY2.csv"
            ],
            'WorkKeys_PY3': [
                "dataSources/workkeys_PY3.csv"
            ],
            'WorkKeys_PY4': [
                "dataSources/workkeys_PY4.csv"
            ],
            'IRC': [
                "dataSources/IRC.csv",
            ],
            # 'AP/DC': [...]  # to be filled in once the file names are known
        }


        dataframes = read_files(file_paths)
        logging.info('Files successfully read')
        #logging.info(f"Dataframes: {dataframes}")
        aggregated_data = aggregate_data(dataframes)
        logging.info('data frames successfully aggregated')

        # Step 2: Weight Calculation
        weighted_data = compute_weights(aggregated_data)
        logging.info('weighted calculations successfully completed')

        # Step 3: CCR Total Calculation
        ccr_data = compute_ccr_totals(weighted_data)
        logging.info('ccr totals calculated successfully')

        # Step 4: Grade Level Selection for S1 and S2 (To be completed)
        # Grade selection logic to be added
        logging.info('grade section successfully completed')

        # Step 5: Output File Generation
        date_str = datetime.now().strftime("%Y%m%d")
        output_file_name = f"Starship_{date_str}.xlsx"
        generate_output_file(ccr_data, output_file_name)
        logging.info('Output file generated successfully! Yay')

        # Step 6: Pivot Table Creation
        create_pivot_table(ccr_data, output_file_name)
                
        logging.info(f'Script completed successfully. Output written to {output_file_name}')

    except Exception as e:
        error_message = f"An error occurred: {e}\n"
        error_message += traceback.format_exc()
        logging.error(error_message)

    # Open the log file
    logging.shutdown()  # Shut down the logging module
    os.system(f"start script.log")

if __name__ == "__main__":
    main()
