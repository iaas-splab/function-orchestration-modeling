{
  "StartAt": "ListFilesActivity_0ilzrs0",
  "States": {
    "ListFilesActivity_0ilzrs0": {
      "Type": "Task",
      "Resource": "ListFiles_ARN",
      "TimeoutSeconds": 300000, 
      "Retry": [
        {
          "ErrorEquals": [ "States.ALL" ],
          "MaxAttempts": 0
        }
      ],
      "Next": "TransformDataFanoutActivity_05pkx7y"
    },
    "TransformDataFanoutActivity_05pkx7y": {
      "Type": "Map",
      "ItemsPath": "$.value",
      "ResultPath": "$.value",
      "Iterator": {
        "StartAt": "TransformDataActivity_05pkx7y",
        "States": {
          "TransformDataActivity_05pkx7y": {
            "Type": "Task",
            "Resource": "TransformData_ARN",
            "TimeoutSeconds": 300000, 
            "Retry": [
              {
                "ErrorEquals": [ "States.ALL" ],
                "MaxAttempts": 0
              }
            ],
            "End": true
          }
        }
      },
      "Next": "AggregateDataActivity_0upzanx"
    },
    "AggregateDataActivity_0upzanx": {
      "Type": "Task",
      "Resource": "AggregateData_ARN",
      "TimeoutSeconds": 300000, 
      "Retry": [
        {
          "ErrorEquals": [ "States.ALL" ],
          "MaxAttempts": 0
        }
      ],
      "Next": "CleanUpActivity_1e1zojm"
    },
    "CleanUpActivity_1e1zojm": {
      "Type": "Task",
      "Resource": "CleanUp_ARN",
      "TimeoutSeconds": 300000, 
      "Retry": [
        {
          "ErrorEquals": [ "States.ALL" ],
          "MaxAttempts": 0
        }
      ],
      "End": true
    }
  }
}