import dagshub
dagshub.init(repo_owner='oelbourki', repo_name='Kidney-Disease-Classification-MLOPS', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)
