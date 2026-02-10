{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "b2c61817-99c0-4daf-8524-9d26d86d2c8f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   Student_Id  Math_Score  Science_Score  Attendance  Math_Score_Log  \\\n",
      "0           1        75.0           75.0        85.0        4.330733   \n",
      "1           2        80.0           82.0        90.0        4.394449   \n",
      "2           3        97.0            NaN        95.0        4.584967   \n",
      "3           4         NaN           88.0        88.0             NaN   \n",
      "4           5        67.0           60.0         NaN        4.219508   \n",
      "5           6       120.0           95.0       110.0        4.795791   \n",
      "6           7        88.0           85.0        92.0        4.488636   \n",
      "7           8        95.0           90.0        94.0        4.564348   \n",
      "8           9        80.0           58.0        80.0        4.394449   \n",
      "9          10         NaN            NaN        82.0             NaN   \n",
      "\n",
      "   Science_Score_Standardized  \n",
      "0                   -0.321024  \n",
      "1                    0.223744  \n",
      "2                         NaN  \n",
      "3                    0.690689  \n",
      "4                   -1.488386  \n",
      "5                    1.235458  \n",
      "6                    0.457217  \n",
      "7                    0.846337  \n",
      "8                   -1.644034  \n",
      "9                         NaN  \n"
     ]
    }
   ],
   "source": [
    "# Experiment - 2\n",
    "\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "from sklearn.preprocessing import StandardScaler\n",
    "\n",
    "data = {\n",
    "    \"Student_Id\": range(1, 11),\n",
    "    \"Math_Score\": [75, 80, 97, np.nan, 67, 120, 88, 95, 80, np.nan],\n",
    "    \"Science_Score\": [75, 82, np.nan, 88, 60, 95, 85, 90, 58, np.nan],\n",
    "    \"Attendance\": [85, 90, 95, 88, np.nan, 110, 92, 94, 80, 82],\n",
    "}\n",
    "\n",
    "df = pd.DataFrame(data)\n",
    "#print(df)\n",
    "\n",
    "#print(df.isnull().sum())\n",
    "\n",
    "#df[\"Math_Score\"].fillna(df[\"Math_Score\"].mean(), inplace=True)\n",
    "# df[\"Science_Score\"].fillna(df[\"Science_Score\"].mean(), inplace=True)\n",
    "\n",
    "# df[\"Math_Score\"] = df[\"Math_Score\"].clip(0, 100)\n",
    "# df[\"Science_Score\"] = df[\"Science_Score\"].clip(0, 100)\n",
    "\n",
    "#def remove_outliers(column):\n",
    "#    Q1 = column.quantile(0.25)\n",
    "#    Q3 = column.quantile(0.75)\n",
    "#    IQR = Q3 - Q1\n",
    "#    lower = Q1 - 1.5 * IQR\n",
    "#    upper = Q3 + 1.5 * IQR\n",
    "#    return column.clip(lower, upper)\n",
    "\n",
    "#df[\"Math_Score\"] = remove_outliers(df[\"Math_Score\"])\n",
    "#df[\"Science_Score\"] = remove_outliers(df[\"Science_Score\"])\n",
    "#df[\"Attendance\"] = remove_outliers(df[\"Attendance\"])\n",
    "\n",
    "#print(df)\n",
    "\n",
    "df[\"Math_Score_Log\"] = np.log1p(df[\"Math_Score\"]) # Data Transformation\n",
    "\n",
    "from sklearn.preprocessing import StandardScaler\n",
    "\n",
    "scaler = StandardScaler()\n",
    "df[\"Science_Score_Standardized\"] = scaler.fit_transform(\n",
    "    df[[\"Science_Score\"]]\n",
    ")\n",
    "\n",
    "print(df)\n",
    "\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
