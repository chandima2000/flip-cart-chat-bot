from flask import Flask, render_template, request
from src.retrieval_generation import generation
from src.data_ingestion import data_ingestion

# Get the vector store
vector_store = data_ingestion("done")


chain = generation(vector_store)


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("chat.html")


@app.route("/get", methods = ["POST", "GET"])
def chat():
   
   if request.method == "POST":
      msg = request.form["msg"]
      input = msg

      result = chain.invoke(
         {"input": input},
    config={
        "configurable": {"session_id": "abc1"}
    },
)["answer"]

      return str(result)

if __name__ == '__main__':
    
    app.run(host="0.0.0.0", port=5000, debug= True)