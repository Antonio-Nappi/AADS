from priority_queue.adaptable_heap_priority_queue import AdaptableHeapPriorityQueue
import time
import random

def random_add(scheduler):
    '''This function random adds a new task to the scheduler.
    The task could be one for the CPU, memory or I/0.'''
    task = ["CPU", "MEMORY", "I/O"]
    scheduler.add_job(random.randint(0, 39) - 20, (random.randint(0, 100)+1, task[random.randint(0, 2)]+" "+str(random.randint(0, 100) + 1)))

class Scheduler(AdaptableHeapPriorityQueue):

    def __init__(self, slice_to_increment):
        '''
        This is the init method of the Scheduler class.
        :param slice_to_increment: is the value that indicates after how many iterations the priority of the scheduled tasks
        must be incremented.
        '''
        super().__init__()
        self._slice_to_increment = slice_to_increment
        self._number_time_slice = 0

    def add_job(self, k, v):
        '''
        This method insert a new job in the Scheduler queue.
        :param k: is the priority of the job.
        :param v: is the tuple that contains the job's name, how many time slices requires.
        :raise Exception: is the priority for the task is not a valid number.'''
        if -20 <= k <= 19:
            v2 = (v[0], v[1], self._number_time_slice)
            self.add(k, v2)
        else:
            raise Exception("This Job has a priority not allowed.")

    def job_execution(self):
        '''
        This method prints information about the current job in execution. After the value of time slices defined by the user
        it increments the priority. If the queue is empty an error message is printed.
        '''
        if not self.is_empty():
            job = self.remove_min()
            for i in range(job[1][0]):
                print("The job {0} requires {1} time slices.".format(job[1][1], job[1][0]))
                self._number_time_slice += 1
                for e in self._data:
                    if (self._number_time_slice + e._value[2]) % self._slice_to_increment == 0:
                        self.update(e, e._key-1, e._value)
        else:
            print("The scheduler has no tasks.")


time_slice = ""
while not time_slice.isdigit():
    time_slice = input("Insert the desired time slice for the scheduler (integer value required): ")
time_slice = int(time_slice)
scheduler = Scheduler(time_slice)
for i in range(5):
    random_add(scheduler)

while 1:
    if random.random() > 0.3:
        random_add(scheduler)
    scheduler.job_execution()
