# StatMetrics

A desktop application built with Python and Tkinter that allows users to upload CSV files, select specific columns, and calculate various statistical metrics like standard deviation, mean, variance, and more. The results can be visualized in a table and downloaded as a CSV file for further analysis.

## Features

- **CSV File Upload**: Load CSV datasets for analysis.
- **Column Selection**: Choose specific columns from the dataset for focused analysis.
- **Statistical Calculations**:
  - Standard Deviation
  - Mean
  - Mean Absolute Deviation
  - Median Absolute Deviation
  - Interquartile Range (IQR)
  - Variance
- **Download Results**: Export the calculated metrics as a CSV file.

## Technologies Used

- **Python**: Core programming language used for building the application.
- **Tkinter**: For building the desktop GUI.
- **Pandas**: For handling CSV data and performing calculations.
- **NumPy**: Supporting efficient numerical computations.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/data-insights-tool.git
    ```
   
2. **Install required libraries**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the application**:
    ```bash
    python app.py
    ```

## How to Use

1. Launch the application and click on "Open File" to select a CSV file.
2. Once the file is uploaded, the columns of the dataset will appear. Select the columns you wish to include in your analysis.
3. Choose the statistical measures you want to calculate (e.g., mean, standard deviation).
4. Click "Calculate" to generate the results, which will be displayed in a table.
5. Optionally, download the results as a CSV by clicking "Download CSV".

## Demo
![demo](https://github.com/Himank-Khatri/PyStaticsGUI/assets/86199877/ada1778c-dc31-4777-922d-1315776b687b)

## Future Enhancements

- Add support for more statistical metrics.
- Improve performance with larger datasets.
- Include visual data representations (graphs/charts).

## License

This project is licensed under the MIT License.

