import json
import os
import argparse
import commands as cd 

FILENAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME,"r") as file:
            return json.load(file)
    else:
        return []

def save_tasks(tasks):
    with open(FILENAME,"w") as f:
        json.dump(tasks , f)


def main():
    parser = argparse.ArgumentParser(description="A simple to-do list CLI")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("description")

    list_parser = subparsers.add_parser("list")

    complete_parser = subparsers.add_parser("complete")
    complete_parser.add_argument("task_id", type=int)

    remove_parser = subparsers.add_parser("remove")
    remove_parser.add_argument("task_id", type=int)

    args = parser.parse_args()
    tasks = load_tasks()

    if args.command == "add":
        cd.add_task(tasks,args.description)
        save_tasks(tasks)
    elif args.command == "list":
        cd.list_tasks(tasks)
    elif args.command == "complete":
        cd.complete_task(tasks,args.task_id)
        save_tasks(tasks)
    elif args.command == "remove":
        cd.remove_task(tasks,args.task_id)
        save_tasks(tasks)

if __name__ == "__main__":
    main()
    