"""Module for task-set implementation

"""
from collections.abc import Iterable



class TaskSet(Iterable):
    """Container for tasks"""
    
    def __init__(self, tasks=[]):
        """Initialize a task-set

        :param tasks [Task]: Initialize a task-set from a list of tasks.
        """
        self._tasks = []
        self._task_counter = 0
        for t in tasks:
            self.append(t)
        

    def __iter__(self):
        """Iterator for iterating over all tasks"""
        return self._tasks.__iter__()
    

    def __str__(self):
        return self._tasks.__str__()


    def __repr__(self):
        return str(self)
        

    def append(self, task):
        """Append task to this task-sets

        :param task taskgen.task.Task: Append task to this task-set
        
        """
        task.id = self._task_counter
        self._task_counter += 1
        self._tasks.append(task)


    def description(self):
        """Description of the task-set

        :return: Description of the task-set
        :rtype: dict
        """
        return {
            "taskset" :  self._tasks
        }


    def binaries(self):
        """List of used binaries
        
        :return: List of used binaries
        :rtype: (str, str,...)
        """
        return set(map(lambda x: x.binary(), self._tasks))

