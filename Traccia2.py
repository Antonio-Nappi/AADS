import enum

from priority_queue.heap_priority_queue import HeapPriorityQueue
import time
import random


class Scheduler(HeapPriorityQueue):

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
        :param v: is the tuple that contains the job's name and how many time slices requires.
        :raise PriorityNotAllowedExceptio: is the priority for the task is not a valid number.'''
        if -20 <= k <= 19:
            self.add(k, v)
        else:
            raise Exception("This Job has a priority not allowed.")

    def _change_priority(self):
        '''
        This method increments by one all the priority of the jobs in the queue.
        '''
        self._increment_priority()

    def job_execution(self):
        '''
        This method prints information about the current job in execution. After the value of time slices defined by the user
        it increments the priority. If the queue is empty an error message is printed.
        '''
        try:
            job = self.remove_min()
            for i in range(job[1][0]):
                print(job[1][1])
                self._number_time_slice += 1
                if self._number_time_slice % self._slice_to_increment == 0:
                    self._change_priority()
        except:
            print("The scheduler has no tasks.")


time_slice = "" #per inserire i time slice all'utente
while not time_slice.isdigit(): #verifica che time_slice sia un intero
    time_slice = input("Insert the desired time slice for the scheduler (integer value required): ")
time_slice = int(time_slice)
scheduler = Scheduler(time_slice)
while 1:
    scheduler.job_execution()
    time.sleep(4)



