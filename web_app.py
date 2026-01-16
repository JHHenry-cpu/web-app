from flask import Flask, render_template, request, redirect



sample = Flask(__name__)

tasks = []



@sample.route("/", methods=["GET"])

def main():

    return render_template("index.html", tasks=tasks)



@sample.route("/add", methods=["POST"])

def add_task():

    task = request.form.get("task")

    if task:

        tasks.append(task)

    return redirect("/")



@sample.route("/delete/<int:task_id>")

def delete_task(task_id):

    if task_id < len(tasks):

        tasks.pop(task_id)

    return redirect("/")



if __name__ == "__main__":

    sample.run(host="0.0.0.0", port=5050)


