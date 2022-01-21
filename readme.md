# Comma Separated Value Table to LaTex Table Converter

This is a short python script which converts csv files into LaTex formatted tables. The output is a text file which contains the desired LaTex formatted table. There are two styles of table available, the first (style 1) is a simple LaTex `tabular` which creates a simple table without captions. The LaTex case for this style looks something like this,

```tex
\begin{center}
    \begin{tabular}{c c}
        cell A1 & cell B1 \\
        cell A2 & cell B2
    \end{tabular}
\end{center}
```

The second style (style 2) adds the LaTex `table` type with a float specifier of here, `[h!]`. An example of style 2:

```tex
\begin{table}[h!]
\begin{center}
    \begin{tabular}{c c}
        cell A1 & cell B1 \\
        cell A2 & cell B2
    \end{tabular}
\end{center}
\end{table}
```
