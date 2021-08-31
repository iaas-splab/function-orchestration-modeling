import azure.functions as func
import azure.durable_functions as df

def orchestrator_function(context: df.DurableOrchestrationContext):
    result = context.get_input()
    result = yield context.call_activity("ListFiles", result)
    tasks = []
    for item in result['value']:
        tasks.append(context.call_activity("TransformData", item))
    result = yield context.task_all(tasks)
    result = yield context.call_activity("AggregateData", result)
    result = yield context.call_activity("CleanUp", result)
    return result

main = df.Orchestrator.create(orchestrator_function)