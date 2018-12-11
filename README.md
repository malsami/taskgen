# TaskSet

A TaskSet is extending the Iterable type and can be initialized with a list of Task objects or an empty list.
An _append()_ function is provided, which acepts a Task.
It is represented as a List, but is not a List.
The _description()_ returns a dictionary representing the whole taskset, including tasks.
The _binaries()_ function returns a set of the necessary binaries for the TaskSet.


# Task

A Task is represented as a dictionary object with the following key-value pairs and an id() getter, an id(Int) setter and binary() function.

## init()

Its init function accepts dictionaries, containing the according elements or blocks functioncalls.

##  'id'
initial value: None

## 'priority'
initial value: 128
Priority is a value between 0 (high priority) and 127 (low priority).
A priority of 128 leads to the priority being ignored and instead of FP scheduling, EDF scheduling will be used

## 'deadline'
initial value: 1 (in ms)
If a priority of 128 is set (EDF scheduling), a deadline of 0 would trigger tons of tasks to be killed, even though there might not be one yet, so avoid that!!!


## 'quota'
initial vlaue: '0M' (in megabyte)
If the ram-quota is not set, the task will have no memory to use, so it will crash.

## 'caps'
initial value: 0
If the capabilities value is not set, the task won't be able to get any capabilities, thus it will crash. (little is known yet on how this works and how it correlates with the 'quota' value. A known working value is 235)

## 'pkg'
initial vlaue: ''
If the package is not defined it will be unknown which task it is, thus it will crash. Is represented by a string of the name of the task

## 'arg1'
initial value: 0
'arg1' is nested into the 'config':{} like this  
```Python
'config' : {
	'arg1' : 0 
}
```
The 'arg1' value should be adapted for each use case.

## 'cores'
initial value: 2
This value defines how many cores are expected to be available on the target machine. It should be adapted to the hardware in use.

## 'coreoffset'
initial value: 1
This value sets an offset from the core the parent is running on. Can be 0, but negative numbers are forbidden.

## 'criticaltime'
initial value: 0
A value of 0 leads to genode ignoring the parameter.
The parameter is used to ensure the start of the task at the next possible period.

## 'period'
initial value: 1
Values smaller than the combination of the times of the startup and destruction of the task make not much sense, but even a value of 1 or 0 will not break the system(might lead to unexpected behaviour though).

## 'numberofjobs'
initial value: 1
This value determines how often genode tries to start a periodic task.
It shall not be smaller than 1, as the distributor component is relying on each task being executed at least once.

## 'offset'
initial value: 0
This value is used to delay a task from the time genode wanted to start the task by the amount of the value in milliseconds.

## 'jobs'
initial value: {}
Here all job data is stored (added during runtime of this task).
The format to fill the dictionary looks like this:
'1' : [start_date, end_date, exit_value]



# Blocks

Blocks are small python snippets, which can be used to generate Tasks.

Example:
Here _pi_, _period_ and _priority_ are Blocks, _Value()_ is the function inside, which returns a corresponding dictionary element similar to the ones on the right for the _numberofjobs_ and _caps_ parameters.

```Python
from taskgen.blocks import *

task = Task(pi.Value(2000), period.Value(2), priority.Value(0), {"numberofjobs" : 1000}, {'caps':50})

```