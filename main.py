import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import csv
import pandas as pd
import numpy as np
from tools import *
from collections import OrderedDict
from ctypes import windll

windll.shcore.SetProcessDpiAwareness(1)

headings = list()


def add_sheet(file):
    with open(f'{file}', 'r') as f:
        records = list(csv.reader(f))

    for i in records[0]:
        headings.append(i)

    table.config(columns=records[0])
    for col in records[0]:
        table.column(col, width=70)
        table.column(col, anchor='n')

    for heading in records[0]:
        table.heading(heading, text=heading)

    for record in records[1:]:
        table.insert('', tk.END, values=record)


def open_file():
    def calculate():

        def download():
            result_df.to_csv('measures.csv')
            download_csv_button.pack_forget()
            ttk.Label(result_window, text='Downloaded!').pack(pady=(20,20))

        selected_cols_list = []
        for i in range(len(check_variables)):
            if check_variables[i].get() == 1:
                selected_cols_list.append(headings[i])

        selected_measures_list = []
        selected_measures = []
        for i in range(len(measure_variables)):
            if measure_variables[i].get() == 1:
                selected_measures_list.append(measures[i])
                selected_measures.append(measures[i][0])

        df = pd.read_csv(file)
        df = df[selected_cols_list]

        result_dict = {}
        for i in selected_measures_list:
            result_dict.update({
                i[0]: i[1](df)
            })

        result_df = pd.DataFrame(result_dict)
        result_df = result_df.transpose()
        result_df.reset_index(inplace=True)
        result_df.columns = ['Measures'] + selected_cols_list



        result_window = tk.Toplevel(root)

        result_table_scroll = ttk.Scrollbar(result_window)
        result_table_scroll.pack(side='right', fill='y')

        result_table = ttk.Treeview(result_window, show="headings", yscrollcommand=result_table_scroll.set,
                                    columns=list(result_df.columns), height=8)
        result_table.pack(pady=(20,20), padx=(20,20))
        result_table_scroll.config(command=result_table.yview)

        download_csv_button = ttk.Button(result_window, text='Download CSV', command=download)
        download_csv_button.pack(side='top', pady=(20,20))


        for col in result_df.columns:
            result_table.column(col, width=180)
            result_table.column(col, anchor='n')

        for heading in result_df.columns:
            result_table.heading(heading, text=heading)

        for record in result_df.itertuples():
            result_table.insert('', tk.END, values=record[1:])
        result_window.mainloop()

    file = askopenfilename(filetypes=[('CSV File', '*.csv')])
    add_sheet(file)

    open_file_button.pack_forget()
    columns_label.pack(side='top', pady=(0, 15))

    check_variables = [tk.IntVar(value=1) for i in range(len(headings))]
    for index, value in enumerate(headings):
        ttk.Checkbutton(ux_frame, text=value, variable=check_variables[index], onvalue=1, offvalue=0).pack(side='top',
                                                                                                           pady=(0, 10),
                                                                                                           anchor='w')

    select_measures = ttk.Label(ux_frame, text='Select Measures')
    select_measures.pack(side='top', pady=(15, 20))

    measures = (('Standard Deviation', std), ('Mean', mean), ('Mean Absolute Deviation', mean_ad),
                ('Median Absolute Deviation', median_ad), ('Inter Quartile Range', iqr), ('Variance', var))

    measure_variables = [tk.IntVar(value=1) for i in range(len(measures))]
    for index, tup in enumerate(measures):
        ttk.Checkbutton(ux_frame, text=tup[0], variable=measure_variables[index], onvalue=1, offvalue=0).pack(
            side='top',
            pady=(0, 10), anchor='w')

    calculate_button = ttk.Button(ux_frame, text='Calculate', command=calculate)
    calculate_button.pack(side='top', pady=(30, 0), padx=(30, 30))


root = tk.Tk()
root.resizable(True, False)

root.tk.call('source', 'forest-dark.tcl')
ttk.Style().theme_use('forest-dark')

ux_frame = ttk.Frame(root)
ux_frame.pack(side='left', padx=(30, 0), pady=(30, 30), fill='both', expand=True)

open_file_button = ttk.Button(ux_frame, text='Open File', command=open_file)
open_file_button.pack(side='top', pady=(180, 0), padx=(60, 60))

columns_label = ttk.Label(ux_frame, text='Select Columns')

tableFrame = ttk.Frame(root)
tableFrame.pack(side='left', pady=(10, 10), padx=(30, 10))

tableScroll = ttk.Scrollbar(tableFrame)
tableScroll.pack(side='right', fill='y')

cols = ('1', '2', '3')
table = ttk.Treeview(tableFrame, show="headings", yscrollcommand=tableScroll.set, columns=cols, height=20)
table.pack()
tableScroll.config(command=table.yview)

root.mainloop()
