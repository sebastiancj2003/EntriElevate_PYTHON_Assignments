{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "fda57330-0739-4873-9cd9-8c0c946c4fbd",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "6f25e973-c724-4957-9438-8147ef52d532",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10])"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s1=np.arange(1,11,1)\n",
    "s1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "a7804331-e893-43d5-a774-ea1b8c5b1df4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 1,  2,  3,  4,  5],\n",
       "       [ 6,  7,  8,  9, 10]])"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s1.reshape(2,5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "89190166-6715-41b3-86cb-16c753db5454",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17,\n",
       "       18, 19, 20])"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s2=np.arange(1,21,1)\n",
    "s2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "34a7c184-18b2-4859-a741-cc45ad43f52d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 6,  7,  8,  9, 10, 11, 12, 13, 14, 15])"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s2[5:15]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "22c53aab-54a5-44e7-98da-0f5cb68a4bd5",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "f22aff3d-dedc-4b0f-ae34-ef2ebd4bcbcc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "apples     3\n",
      "bananas    2\n",
      "oranges    1\n",
      "pears      4\n",
      "dtype: int64\n"
     ]
    }
   ],
   "source": [
    "data={'apples':3,'bananas':2,'oranges':1}\n",
    "series=pd.Series(data)\n",
    "series['pears']=4\n",
    "print(series)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "00a5b7c2-b9b4-4bd1-968a-a0ad3df59263",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>name</th>\n",
       "      <th>age</th>\n",
       "      <th>gender</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Alice</td>\n",
       "      <td>25</td>\n",
       "      <td>F</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Bob</td>\n",
       "      <td>30</td>\n",
       "      <td>M</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Charlie</td>\n",
       "      <td>35</td>\n",
       "      <td>M</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>David</td>\n",
       "      <td>40</td>\n",
       "      <td>M</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Eva</td>\n",
       "      <td>28</td>\n",
       "      <td>F</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Frank</td>\n",
       "      <td>32</td>\n",
       "      <td>M</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Grace</td>\n",
       "      <td>26</td>\n",
       "      <td>F</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Hannah</td>\n",
       "      <td>29</td>\n",
       "      <td>F</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Ian</td>\n",
       "      <td>31</td>\n",
       "      <td>M</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>Jack</td>\n",
       "      <td>27</td>\n",
       "      <td>M</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      name  age gender\n",
       "0    Alice   25      F\n",
       "1      Bob   30      M\n",
       "2  Charlie   35      M\n",
       "3    David   40      M\n",
       "4      Eva   28      F\n",
       "5    Frank   32      M\n",
       "6    Grace   26      F\n",
       "7   Hannah   29      F\n",
       "8      Ian   31      M\n",
       "9     Jack   27      M"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.DataFrame({\n",
    "    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hannah', 'Ian', 'Jack'],\n",
    "    'age': [25, 30, 35, 40, 28, 32, 26, 29, 31, 27],\n",
    "    'gender': ['F', 'M', 'M', 'M', 'F', 'M', 'F', 'F', 'M', 'M']\n",
    "},columns=['name','age','gender'])\n",
    "df\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "731ad2ec-2573-4488-a823-8f6e7f3146ca",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "      name  age gender  occupation\n",
      "0    Alice   25      F  Programmer\n",
      "1      Bob   30      M     Manager\n",
      "2  Charlie   35      M     Analyst\n",
      "3    David   40      M  Programmer\n",
      "4      Eva   28      F     Manager\n",
      "5    Frank   32      M     Analyst\n",
      "6    Grace   26      F  Programmer\n",
      "7   Hannah   29      F     Manager\n",
      "8      Ian   31      M     Analyst\n",
      "9     Jack   27      M  Programmer\n"
     ]
    }
   ],
   "source": [
    "df['occupation'] = ['Programmer', 'Manager', 'Analyst', 'Programmer', 'Manager',\n",
    "                    'Analyst', 'Programmer', 'Manager', 'Analyst', 'Programmer']\n",
    "print(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "2ef30add-d17f-41e3-a2a7-49a6a681e7df",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "      name  age gender  occupation\n",
      "1      Bob   30      M     Manager\n",
      "2  Charlie   35      M     Analyst\n",
      "3    David   40      M  Programmer\n",
      "5    Frank   32      M     Analyst\n",
      "8      Ian   31      M     Analyst\n"
     ]
    }
   ],
   "source": [
    "filtered_df=df[df['age']>=30]\n",
    "print(filtered_df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "1c118b2d-28b2-4b31-bc73-563e80e02923",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "      name  age gender  occupation\n",
      "0    Alice   25      F  Programmer\n",
      "1      Bob   30      M     Manager\n",
      "2  Charlie   35      M     Analyst\n",
      "3    David   40      M  Programmer\n",
      "4      Eva   28      F     Manager\n",
      "5    Frank   32      M     Analyst\n",
      "6    Grace   26      F  Programmer\n",
      "7   Hannah   29      F     Manager\n",
      "8      Ian   31      M     Analyst\n",
      "9     Jack   27      M  Programmer\n"
     ]
    }
   ],
   "source": [
    "# Save DataFrame to a CSV file\n",
    "data = pd.read_csv('data.csv')\n",
    "data\n",
    "# Read the CSV file\n",
    "df_new = pd.read_csv('data.csv')\n",
    "\n",
    "# Display contents\n",
    "print(df_new)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5b5fa6f2-5821-4435-a668-d315d475aa07",
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
