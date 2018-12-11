"""This module implements the task"""
from collections.abc import Iterable



class Task(dict):
    """A Task

    A task is defined by attributes like priority, period, usw. These attributes
    are represented by key-value pairs and stored in a dict.
    
    :param *blocks dict: A number of dicts as parameters, which are merged to
    this task. This concept is called Task-Blocks. Task-Blocks are located in
    the directory `taskgen.blocks`.

    """
    def __init__(self, *blocks):
        super().__init__({
            # default values
            'id' : None,
            'priority' : 128, # 0:high - 127:low - 128 ignore -> use deadline
            'deadline' : 1, # 0:stupid value

            # blob values
            'quota' : '0M', #init value will fail, has to be set
            'caps' : 0, # has to be set - known working value is 235
            'pkg' : '', # has to be not empty
            'config' : {
                'arg1' : 0 # will work, but does not make sense
            },

            # sets how many cores are available on the target machine
            'cores' : 2, # default is set to two, but depends on hardware

            # sets an offset from the core the parent is running on
            'coreoffset' : 1, # can't be negative, default is different core than parent

            # critical time - to ensure startup at next period
            'criticaltime' : 0, # 0 is ignore
            # periodic task
            'period' : 1, # 0 does not make sense but will not break genode
            
            'numberofjobs' : 1, # cant be smaller than 1
            'offset' : 0, 
            # stores all job data (added during runtime of this task)
            'jobs' : {
                # '1' : [start_date, end_date, exit_value] as an example for format
            }
        })

        # add inital blocks
        for block in blocks:
            if callable(block):
                block = block()
            # if not isinstance(attr, dict):
            #     raise ValueError("An attribute for a task must be dict.")
            super().update(block)


    @property
    def id(self):
        """Getter of the task id attribute
        
        This method is used by monitor implementations for finding the related
        task for an event.

        """
        return self['id']

 
    @id.setter
    def id(self, _id):
        """Setter for the task id

        This method is used by `taskgen.taskset.TaskSet`. If a task is added to a
        task-set, an unique id is assigned to the task.

        """
        self['id'] = _id


    def binary(self):
        """Binary of the task
        
        Every task has a binary. This method returns it.

        :return: binary of the task
        :rtype: str

        """
        return self['pkg']
