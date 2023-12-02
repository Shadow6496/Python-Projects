class tasks:
    def __init__(self):
        self.tasks = []

    def list_tasks(self):
      if not self.tasks:
        print("No tasks to complete.")
        return

      for index, task in enumerate(self.tasks):
        status = "Complete" if task["completed"] else "Incomplete"
        print(f'{index}: {task["name"]} (Status: {status}, Due: {task["due_date"]})')


    def add_task(self):
        task_text = input('Please add a task: ')
        due_date = input('Please enter due date (MM-DD-YYYY): ')
        new_task = {f'name': task_text, 'completed': False, 'due_date': due_date}
        self.tasks.append(new_task)
        print('New task has been added. ')

    def remove_task(self):
       self.list_tasks()
       task_index = self.get_index('Enter task to be removed: ')

       if task_index is not None:
          del self.tasks[task_index]
          print('Task has been removed.')
 
    def mark_task_complete(self):
        self.list_tasks()
        task_index = self.get_index('Enter the corresponding index to mark task as complete: ')

        if task_index is not None:
            if self.tasks[task_index]['completed']:
              print("Task is already marked as complete.")
              return
            else:
                self.tasks[task_index]['completed'] = True
                print("Task marked as complete")

    def tip_calculator(self):
       print("Tip calculator")
       bill = float(input("What is the total bill? $"))
       tip = int(input("What percent would you like to tip? 10, 12, 15, or 20: "))
       people = int(input('How many people will you be splitting the bill with? '))

       tip_in_percent = tip / 100
       total_tip = bill * tip_in_percent
       total_bill = bill + total_tip
       person_split = total_bill / people
       final = "{:.2f}".format(person_split)
       print (f"Your total bill per person is ${final}")

    def get_index(self, message):
       while True:
          try:
            task_index = int(input(message))
            if 0 <= task_index < len(self.tasks):
               return task_index
            else:
               print("Index option not found please try another option.")
          except ValueError:
             print('Inputs only accepted in numerical values please try again.')     
    
    def run(self):
        menu_text = """
        ====================
        1. List the tasks
        2. Add a task
        3. Remove a task
        4. Mark task complete
        5. Tip calculator
        6. Quit

        What would you like to do? """

        program_is_running = True

        while program_is_running:
         decision = input(menu_text)

         if decision == '1':
            self.list_tasks()
         elif decision == '2':
            self.add_task()
         elif decision == '3':
            self.remove_task()
         elif decision == '4':
            self.mark_task_complete()
         elif decision == '5':
            self.tip_calculator()
         elif decision == '6':
            print("Exiting. ")
            break

if __name__ == "__main__":
   class_tasks = tasks()
   class_tasks.run()

