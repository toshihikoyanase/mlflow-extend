import mlflow


import mlflow_extend.logging as lg

# Add new functions to mlflow.
for mod in [lg]:
    for func_name in [attr for attr in dir(lg) if not attr.startswith("_")]:
        setattr(mlflow, func_name, getattr(mod, func_name))