from pyspark import SparkContext

def run_dijkstra(file_path, start_node, output_file):
    sc = SparkContext(appName="Dijkstra_Spark")
    lines = sc.textFile(file_path)

    first_line = lines.first()
    edges = lines.filter(lambda line: line != first_line).map(lambda line: tuple(map(int, line.strip().split())))

    graph = edges.map(lambda x: (x[0], (x[1], x[2]))).groupByKey().mapValues(list).cache()

    nodes = edges.flatMap(lambda x: [x[0], x[1]]).distinct()
    distances = nodes.map(lambda node: (node, (0 if node == start_node else float('inf'), [])))

    for _ in range(20): 
        known_nodes = distances.filter(lambda x: x[1][0] != float('inf'))
        known_nodes_dict = dict(known_nodes.collect())
        known_broadcast = sc.broadcast(known_nodes_dict)

        updates = graph.flatMap(lambda x: [(dst, (known_broadcast.value.get(x[0], (float('inf'), []))[0] + weight, known_broadcast.value.get(x[0], (float('inf'), []))[1] + [x[0]])) for (dst, weight) in x[1] if x[0] in known_broadcast.value])

        all_distances = distances.union(updates).reduceByKey(lambda a, b: a if a[0] < b[0] else b)
        if all_distances.collect() == distances.collect():
            break
        distances = all_distances

    result = distances.collect()

    with open(output_file, "w") as f:
        for node, (dist, path) in sorted(result):
            path_str = "->".join(map(str, path + [node]))
            f.write(f"Node {node}: Distance {dist}, Path {path_str}\n")

    sc.stop()

if __name__ == "__main__":
    run_dijkstra("weighted_graph.txt", 0, "shortest_paths.txt")
