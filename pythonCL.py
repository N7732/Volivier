# class animal:
#     def __init__(self,name,colour,sound):
#         self.name=name
#         self.colour=colour
#         self.sound=sound
#     def makesound(self):
#         print(self.sound)
# a=animal("Dog","Black","MBA")
# a.makesound()
# B=animal("Cat","White","NYAW")
# B.makesound()

# # print(a.name)
class Task_manager:
    def __init__(self):
        self.tasks=[]
    def add_task(self,task):
        self.tasks.append(task)
    def list_tasks(self):
        print(self.tasks)
    def complete_task(self,task_id):
        del self.tasks[task_id]
w=Task_manager()
w.add_task("learning")
print(w.list_tasks())

    
        