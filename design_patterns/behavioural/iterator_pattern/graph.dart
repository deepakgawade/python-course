class Graph{
  final Map<int,Set<int>> adjacencyList={};
  void addTarget(int source, int target)=>adjacencyList.containsKey(source)?adjacencyList[source]!.add(target):adjacencyList[source]={target};
}