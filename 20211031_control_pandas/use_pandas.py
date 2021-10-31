import pandas

df = pandas.DataFrame()
df.to_csv(path_or_buf=path_or_buf,
                      index=True,
                      index_label='index')

pandas.read_csv(filepath_or_buffer=filepath_or_buffer,
                header=0,
                index_col='index',
                dtype={'market_output_dir': str,
                       'project_output_dir': str,

                       'want_np1_day': str},
                na_values='NaN',
                thousands=',')
