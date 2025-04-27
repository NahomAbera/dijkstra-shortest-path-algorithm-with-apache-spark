# How to Run
## Upload these two files to your Azure VM:
dijkstra_pyspark.py and weighted_graph.txt

## SSH into your VM.

## Go to the directory where the files are saved:

## Install required packages
### Install Required Software on Azure VM
#### Install Java:

sudo apt update
sudo apt install openjdk-11-jdk -y

#### Install Spark:
wget https://dlcdn.apache.org/spark/spark-3.4.1/spark-3.4.1-bin-hadoop3.tgz
tar -xvzf spark-3.4.1-bin-hadoop3.tgz
sudo mv spark-3.4.1-bin-hadoop3 /opt/spark

#### Add Spark to PATH:
echo 'export SPARK_HOME=/opt/spark' >> ~/.bashrc
echo 'export PATH=$SPARK_HOME/bin:$PATH' >> ~/.bashrc
source ~/.bashrc

#### Install Python and PySpark:
sudo apt install python3 python3-pip -y
pip3 install pyspark

## Run the Code
spark-submit dijkstra_pyspark.py

## After it finishes, the output will be saved to:
shortest_paths.txt

## Notes
Input file: weighted_graph.txt
Output file: shortest_paths.txt

## You can find a sample output I got after run dijkstra_pyspark.py on my azure vm in my_shortest_paths.txt