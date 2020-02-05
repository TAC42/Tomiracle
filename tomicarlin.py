from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    name = request.args.get("name")
    return render_template("index.html", name=name)


def main():
    return 1


 
if __name__ == "__main__":
    main()


