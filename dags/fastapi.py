import pandas as pd
import os
import requests
import json
from sklearn.metrics import confusion_matrix
from datetime import datetime, timedelta
from textwrap import dedent
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import (
    ExternalPythonOperator,
    PythonOperator,
    PythonVirtualenvOperator,
    BranchPythonOperator,
)

with DAG(
        'fish_predict',
    default_args={
        'depends_on_past': False,
        'retries': 1,
        'retry_delay': timedelta(seconds=3)
    },
    description='fish pred Dag',
    schedule=None,
    catchup=True,
    tags=['fish','predict','data'],
) as dag:

    def loadcsv():
        file_path = "/home/hahahellooo/data/fish_test_data.csv"
        save_path = '/home/hahahellooo/data/fish_parquet/'
        val_data=pd.read_csv(file_path)
        #val_data['Label'][val_data['Label']=='Bream']=0
        #val_data['Label'][val_data['Label']=='Smelt']=1
        if os.path.exists(save_path):
            val_data.to_parquet(f"{save_path}/fish_test_data.parquet")
        else:
            os.makedirs(os.path.dirname(save_path), exist_ok = False)
            val_data.to_parquet(f"{save_path}/fish_test_data.parquet")

    def prediction():
        load_path = "/home/hahahellooo/data/fish_parquet/"
        save_path = "/home/hahahellooo/data/fish_pred_parquet/"

        val_data=pd.read_parquet(load_path)
        val_data_cut = val_data[:100000]
        headers = {
            'accept': 'application/json',
        }
        neighbor=[1,5,15,25,49]
        for j in neighbor:  
            pred_result=[]
            for i in range(len(val_data_cut)):
                params = {
                'n_neighbors' : j,
                'length': val_data_cut['Length'][i],
                'weight': val_data_cut['Weight'][i],
                }
                response = requests.get('http://127.0.0.1:8765/fish_ml_predictor', params=params, headers=headers)
                data=json.loads(response.text)
                col_name = f"k{j}"
                if data['prediction'] == '도미':
                    pred_result.append('Bream')
                else :
                    pred_result.append('Smelt')

            val_data_cut[f'{col_name}']=pred_result

            if os.path.exists(save_path):
                val_data_cut.to_parquet(f"{save_path}/fish_pred{j}.parquet")
            else:
                os.makedirs(os.path.dirname(save_path), exist_ok = False)
                val_data_cut.to_parquet(f"{save_path}/fish_pred{j}.parquet")
  

    def aggregate():
        load_path = "/home/hahahellooo/data/fish_pred_parquet/fish_pred49.parquet"
        save_path = "/home/hahahellooo/data/fish_agg_parquet/"

        val_data=pd.read_parquet(load_path)
        val_data.replace({'Bream': 0, 'Smelt': 1}, inplace=True)
        val_data.to_parquet(f"{save_path}/fish_transform.parquet")
        
        for i in range(4,8):
            cm=confusion_matrix(val_data.iloc[:,3],val_data.iloc[:,i])
            Real=['Real_Bream','Real_Smelt']
            pred=['pred_Bream','pred_Smelt']
            cm_df = pd.DataFrame(cm, index=Real, columns=pred)
            print(cm_df)
            if os.path.exists(save_path):
                cm_df.to_parquet(f"{save_path}/fish_agg{i}.parquet")
            else:
                os.makedirs(os.path.dirname(save_path), exist_ok = False)
                cm_df.to_parquet(f"{save_path}/fish_agg{i}.parquet")


    start=EmptyOperator(
        task_id="start"
    )
    end = EmptyOperator(
        task_id="end"
    )

    load_csv = PythonOperator(
        task_id="load.csv",
        python_callable = loadcsv ,
    )

    predict = PythonOperator(
        task_id="predict",
        python_callable = prediction ,
    )

    agg = PythonOperator(
        task_id="agg",
        python_callable = aggregate ,
    )



    start >> load_csv >> predict >> agg >> end
