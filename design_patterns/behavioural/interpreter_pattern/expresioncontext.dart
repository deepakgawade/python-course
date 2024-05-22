class ExpressionContext{
  final List<String> _solution=[];

  int catCow=0;

  List<String> get solutionSteps=>_solution;

  void addSolutionStep(String operator,int left,int right,int result){
    final solution='${solutionSteps.length+1} ${left} ${operator} ${right}=${result}';
  _solution.add(solution);
  }
}

