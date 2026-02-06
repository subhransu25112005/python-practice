class TaskIterator:
    def __init__(self, tasks):
        self.tasks = tasks
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.tasks):
            raise StopIteration
        task = self.tasks[self.index]
        self.index += 1
        return task

tasks = [
    "Revise DSA",
    "Practice Python",
    "Gym workout",
    "Read one chapter",
    "Sleep on time"
]

task_iterator = TaskIterator(tasks)

print("\n🎯 Welcome to Daily Task Player \n")

for task in task_iterator:
    print(f"👉 Current Task: {task}")
    choice = input("Mark as done? (y/n): ").lower()

    if choice == 'y':
        print("✅ Task completed!\n")
    else:
        print("⏭ Task skipped!\n")

print("🎉 All tasks processed. Day completed!")
