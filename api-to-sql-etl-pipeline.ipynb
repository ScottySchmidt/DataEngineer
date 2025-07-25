{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "6a0d9ea3",
   "metadata": {
    "papermill": {
     "duration": 0.002833,
     "end_time": "2025-07-25T19:43:53.950103",
     "exception": false,
     "start_time": "2025-07-25T19:43:53.947270",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "## Data Engineering Pipeline: API to Normalized SQL\n",
    "https://pokeapi.co/api/v2/pokemon?limit=10000"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "2ec962e8",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-07-25T19:43:53.956674Z",
     "iopub.status.busy": "2025-07-25T19:43:53.956230Z",
     "iopub.status.idle": "2025-07-25T19:43:55.943370Z",
     "shell.execute_reply": "2025-07-25T19:43:55.942141Z"
    },
    "papermill": {
     "duration": 1.992438,
     "end_time": "2025-07-25T19:43:55.945252",
     "exception": false,
     "start_time": "2025-07-25T19:43:53.952814",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Imports\n",
    "import urllib.request\n",
    "import requests\n",
    "import pandas as pd\n",
    "import json"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "6976aef1",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-07-25T19:43:55.952190Z",
     "iopub.status.busy": "2025-07-25T19:43:55.951665Z",
     "iopub.status.idle": "2025-07-25T19:43:56.008974Z",
     "shell.execute_reply": "2025-07-25T19:43:56.008099Z"
    },
    "papermill": {
     "duration": 0.062598,
     "end_time": "2025-07-25T19:43:56.010506",
     "exception": false,
     "start_time": "2025-07-25T19:43:55.947908",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[{'name': 'bulbasaur', 'url': 'https://pokeapi.co/api/v2/pokemon/1/'}, {'name': 'ivysaur', 'url': 'https://pokeapi.co/api/v2/pokemon/2/'}]\n",
      "<class 'list'>\n"
     ]
    }
   ],
   "source": [
    "url = 'https://pokeapi.co/api/v2/pokemon?limit=2'\n",
    "r = requests.get(url)\n",
    "example = r.json()\n",
    "example = example['results']\n",
    "print(example)\n",
    "print(type(example))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "a3706290",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-07-25T19:43:56.016867Z",
     "iopub.status.busy": "2025-07-25T19:43:56.016587Z",
     "iopub.status.idle": "2025-07-25T19:43:56.060063Z",
     "shell.execute_reply": "2025-07-25T19:43:56.058966Z"
    },
    "papermill": {
     "duration": 0.048541,
     "end_time": "2025-07-25T19:43:56.061628",
     "exception": false,
     "start_time": "2025-07-25T19:43:56.013087",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[{'name': 'bulbasaur', 'url': 'https://pokeapi.co/api/v2/pokemon/1/'}, {'name': 'ivysaur', 'url': 'https://pokeapi.co/api/v2/pokemon/2/'}, {'name': 'venusaur', 'url': 'https://pokeapi.co/api/v2/pokemon/3/'}, {'name': 'charmander', 'url': 'https://pokeapi.co/api/v2/pokemon/4/'}, {'name': 'charmeleon', 'url': 'https://pokeapi.co/api/v2/pokemon/5/'}]\n"
     ]
    }
   ],
   "source": [
    "def get_data(num):\n",
    "    url = 'https://pokeapi.co/api/v2/pokemon?limit='+str(num)\n",
    "    r = requests.get(url)\n",
    "    if r.status_code == 200:\n",
    "        data = r.json()\n",
    "        #print(\"Data within get_data function:\")\n",
    "        #print(data)\n",
    "        return data\n",
    "    else:\n",
    "        print(\"Failed to retrieve data: \", response)\n",
    "data = get_data(5)\n",
    "data = data['results']\n",
    "print(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "bf815f65",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-07-25T19:43:56.068110Z",
     "iopub.status.busy": "2025-07-25T19:43:56.067796Z",
     "iopub.status.idle": "2025-07-25T19:43:56.073877Z",
     "shell.execute_reply": "2025-07-25T19:43:56.072699Z"
    },
    "papermill": {
     "duration": 0.01095,
     "end_time": "2025-07-25T19:43:56.075285",
     "exception": false,
     "start_time": "2025-07-25T19:43:56.064335",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['bulbasaur', 'ivysaur', 'venusaur', 'charmander', 'charmeleon']\n",
      "['https://pokeapi.co/api/v2/pokemon/1/', 'https://pokeapi.co/api/v2/pokemon/2/', 'https://pokeapi.co/api/v2/pokemon/3/', 'https://pokeapi.co/api/v2/pokemon/4/', 'https://pokeapi.co/api/v2/pokemon/5/']\n"
     ]
    }
   ],
   "source": [
    "names = []\n",
    "urls = []\n",
    "\n",
    "for d in data:\n",
    "    n=d['name']\n",
    "    names.append(n)\n",
    "    u=d['url']\n",
    "    urls.append(u)\n",
    "print(names)\n",
    "print(urls)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "d3fa4ab2",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-07-25T19:43:56.081557Z",
     "iopub.status.busy": "2025-07-25T19:43:56.081244Z",
     "iopub.status.idle": "2025-07-25T19:43:56.272436Z",
     "shell.execute_reply": "2025-07-25T19:43:56.271466Z"
    },
    "papermill": {
     "duration": 0.195986,
     "end_time": "2025-07-25T19:43:56.273876",
     "exception": false,
     "start_time": "2025-07-25T19:43:56.077890",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[{'ability': {'name': 'overgrow', 'url': 'https://pokeapi.co/api/v2/ability/65/'}, 'is_hidden': False, 'slot': 1}, {'ability': {'name': 'chlorophyll', 'url': 'https://pokeapi.co/api/v2/ability/34/'}, 'is_hidden': True, 'slot': 3}]\n",
      "{'ability': {'name': 'overgrow', 'url': 'https://pokeapi.co/api/v2/ability/65/'}, 'is_hidden': False, 'slot': 1}\n",
      "{'ability': {'name': 'chlorophyll', 'url': 'https://pokeapi.co/api/v2/ability/34/'}, 'is_hidden': True, 'slot': 3}\n",
      "[{'ability': {'name': 'overgrow', 'url': 'https://pokeapi.co/api/v2/ability/65/'}, 'is_hidden': False, 'slot': 1}, {'ability': {'name': 'chlorophyll', 'url': 'https://pokeapi.co/api/v2/ability/34/'}, 'is_hidden': True, 'slot': 3}]\n",
      "{'ability': {'name': 'overgrow', 'url': 'https://pokeapi.co/api/v2/ability/65/'}, 'is_hidden': False, 'slot': 1}\n",
      "{'ability': {'name': 'chlorophyll', 'url': 'https://pokeapi.co/api/v2/ability/34/'}, 'is_hidden': True, 'slot': 3}\n",
      "[{'ability': {'name': 'overgrow', 'url': 'https://pokeapi.co/api/v2/ability/65/'}, 'is_hidden': False, 'slot': 1}, {'ability': {'name': 'chlorophyll', 'url': 'https://pokeapi.co/api/v2/ability/34/'}, 'is_hidden': True, 'slot': 3}]\n",
      "{'ability': {'name': 'overgrow', 'url': 'https://pokeapi.co/api/v2/ability/65/'}, 'is_hidden': False, 'slot': 1}\n",
      "{'ability': {'name': 'chlorophyll', 'url': 'https://pokeapi.co/api/v2/ability/34/'}, 'is_hidden': True, 'slot': 3}\n",
      "[{'ability': {'name': 'blaze', 'url': 'https://pokeapi.co/api/v2/ability/66/'}, 'is_hidden': False, 'slot': 1}, {'ability': {'name': 'solar-power', 'url': 'https://pokeapi.co/api/v2/ability/94/'}, 'is_hidden': True, 'slot': 3}]\n",
      "{'ability': {'name': 'blaze', 'url': 'https://pokeapi.co/api/v2/ability/66/'}, 'is_hidden': False, 'slot': 1}\n",
      "{'ability': {'name': 'solar-power', 'url': 'https://pokeapi.co/api/v2/ability/94/'}, 'is_hidden': True, 'slot': 3}\n",
      "[{'ability': {'name': 'blaze', 'url': 'https://pokeapi.co/api/v2/ability/66/'}, 'is_hidden': False, 'slot': 1}, {'ability': {'name': 'solar-power', 'url': 'https://pokeapi.co/api/v2/ability/94/'}, 'is_hidden': True, 'slot': 3}]\n",
      "{'ability': {'name': 'blaze', 'url': 'https://pokeapi.co/api/v2/ability/66/'}, 'is_hidden': False, 'slot': 1}\n",
      "{'ability': {'name': 'solar-power', 'url': 'https://pokeapi.co/api/v2/ability/94/'}, 'is_hidden': True, 'slot': 3}\n",
      "[[{'ability': {'name': 'overgrow', 'url': 'https://pokeapi.co/api/v2/ability/65/'}, 'is_hidden': False, 'slot': 1}, {'ability': {'name': 'chlorophyll', 'url': 'https://pokeapi.co/api/v2/ability/34/'}, 'is_hidden': True, 'slot': 3}], [{'ability': {'name': 'overgrow', 'url': 'https://pokeapi.co/api/v2/ability/65/'}, 'is_hidden': False, 'slot': 1}, {'ability': {'name': 'chlorophyll', 'url': 'https://pokeapi.co/api/v2/ability/34/'}, 'is_hidden': True, 'slot': 3}], [{'ability': {'name': 'overgrow', 'url': 'https://pokeapi.co/api/v2/ability/65/'}, 'is_hidden': False, 'slot': 1}, {'ability': {'name': 'chlorophyll', 'url': 'https://pokeapi.co/api/v2/ability/34/'}, 'is_hidden': True, 'slot': 3}], [{'ability': {'name': 'blaze', 'url': 'https://pokeapi.co/api/v2/ability/66/'}, 'is_hidden': False, 'slot': 1}, {'ability': {'name': 'solar-power', 'url': 'https://pokeapi.co/api/v2/ability/94/'}, 'is_hidden': True, 'slot': 3}], [{'ability': {'name': 'blaze', 'url': 'https://pokeapi.co/api/v2/ability/66/'}, 'is_hidden': False, 'slot': 1}, {'ability': {'name': 'solar-power', 'url': 'https://pokeapi.co/api/v2/ability/94/'}, 'is_hidden': True, 'slot': 3}]]\n"
     ]
    }
   ],
   "source": [
    "ability_lists = []\n",
    "for u in urls:\n",
    "    r = requests.get(u)\n",
    "    json = r.json()\n",
    "    abilities = json['abilities']\n",
    "    print(abilities)\n",
    "    a_list = []\n",
    "    for a in abilities:\n",
    "        print(a)\n",
    "        a_list.append(a)\n",
    "    ability_lists.append(a_list)\n",
    "    \n",
    "print(ability_lists)\n",
    "#print(abilities)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "61382483",
   "metadata": {
    "papermill": {
     "duration": 0.002349,
     "end_time": "2025-07-25T19:43:56.279263",
     "exception": false,
     "start_time": "2025-07-25T19:43:56.276914",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "aec0de1c",
   "metadata": {
    "papermill": {
     "duration": 0.002243,
     "end_time": "2025-07-25T19:43:56.284215",
     "exception": false,
     "start_time": "2025-07-25T19:43:56.281972",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "db9c47c3",
   "metadata": {
    "papermill": {
     "duration": 0.002339,
     "end_time": "2025-07-25T19:43:56.289061",
     "exception": false,
     "start_time": "2025-07-25T19:43:56.286722",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "## Turn into Pandas DataFrame"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "63116809",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-07-25T19:43:56.295389Z",
     "iopub.status.busy": "2025-07-25T19:43:56.294789Z",
     "iopub.status.idle": "2025-07-25T19:43:56.325564Z",
     "shell.execute_reply": "2025-07-25T19:43:56.324796Z"
    },
    "papermill": {
     "duration": 0.035532,
     "end_time": "2025-07-25T19:43:56.326984",
     "exception": false,
     "start_time": "2025-07-25T19:43:56.291452",
     "status": "completed"
    },
    "tags": []
   },
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
       "      <th>abilities</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>bulbasaur</td>\n",
       "      <td>[{'ability': {'name': 'overgrow', 'url': 'http...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>ivysaur</td>\n",
       "      <td>[{'ability': {'name': 'overgrow', 'url': 'http...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>venusaur</td>\n",
       "      <td>[{'ability': {'name': 'overgrow', 'url': 'http...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>charmander</td>\n",
       "      <td>[{'ability': {'name': 'blaze', 'url': 'https:/...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>charmeleon</td>\n",
       "      <td>[{'ability': {'name': 'blaze', 'url': 'https:/...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         name                                          abilities\n",
       "0   bulbasaur  [{'ability': {'name': 'overgrow', 'url': 'http...\n",
       "1     ivysaur  [{'ability': {'name': 'overgrow', 'url': 'http...\n",
       "2    venusaur  [{'ability': {'name': 'overgrow', 'url': 'http...\n",
       "3  charmander  [{'ability': {'name': 'blaze', 'url': 'https:/...\n",
       "4  charmeleon  [{'ability': {'name': 'blaze', 'url': 'https:/..."
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dict = {'name': names, 'abilities': ability_lists}\n",
    "df = pd.DataFrame(dict)\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8ce5c6e9",
   "metadata": {
    "papermill": {
     "duration": 0.002611,
     "end_time": "2025-07-25T19:43:56.332727",
     "exception": false,
     "start_time": "2025-07-25T19:43:56.330116",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "## Archived Code\n",
    "Requests much easier than urlib "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "08877754",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-07-25T19:43:56.339493Z",
     "iopub.status.busy": "2025-07-25T19:43:56.338903Z",
     "iopub.status.idle": "2025-07-25T19:43:56.396840Z",
     "shell.execute_reply": "2025-07-25T19:43:56.395835Z"
    },
    "papermill": {
     "duration": 0.062786,
     "end_time": "2025-07-25T19:43:56.398280",
     "exception": false,
     "start_time": "2025-07-25T19:43:56.335494",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'str'>\n",
      "{\"count\":1302,\"next\":\"https://pokeapi.co/api/v2/pokemon?offset=1&limit=1\",\"previous\":null,\"results\":[{\"name\":\"bulbasaur\",\"url\":\"https://pokeapi.co/api/v2/pokemon/1/\"}]}\n"
     ]
    }
   ],
   "source": [
    "def get_content(num):\n",
    "    url = \"https://pokeapi.co/api/v2/pokemon?limit=\"+str(num)\n",
    "    response = urllib.request.urlopen(url)\n",
    "    content = response.read().decode('utf-8')\n",
    "    #content = content[0]\n",
    "    print(type(content))\n",
    "    print(content)\n",
    "get_content(1) #show what data looks like"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d519b9a5",
   "metadata": {
    "papermill": {
     "duration": 0.002821,
     "end_time": "2025-07-25T19:43:56.404205",
     "exception": false,
     "start_time": "2025-07-25T19:43:56.401384",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kaggle": {
   "accelerator": "none",
   "dataSources": [],
   "dockerImageVersionId": 31089,
   "isGpuEnabled": false,
   "isInternetEnabled": true,
   "language": "python",
   "sourceType": "notebook"
  },
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.11.13"
  },
  "papermill": {
   "default_parameters": {},
   "duration": 7.549324,
   "end_time": "2025-07-25T19:43:56.925827",
   "environment_variables": {},
   "exception": null,
   "input_path": "__notebook__.ipynb",
   "output_path": "__notebook__.ipynb",
   "parameters": {},
   "start_time": "2025-07-25T19:43:49.376503",
   "version": "2.6.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
