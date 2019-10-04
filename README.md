# ML-Stuff  
Export data to csv from dataframe:  
```
    dataframe.to_csv(r'.\export_dataframe.csv', index=None, header=True)  
```
(if the file name is changed then need to edit that when reading in the csv in line 11)  
Run test.py (in Pycharm ideally, otherwise with suitable virtual env set up) and open the browser at  whatever address it gives you, probably http://127.0.0.1:5000/  
  
When lines 14-16 are commented and 17-19 are uncommented the table will only highlight values >= 0.5,  
If 14-16 are uncommented and 17-19 are commented the table will highlight those below 0.47 with shades of blue (deeper for farther away from centre), and above 0.53 with shades of red (same again)
