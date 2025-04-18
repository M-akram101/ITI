from flask import Flask, render_template, request, jsonify, session
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
from dotenv import load_dotenv
import os
import torch

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")

# Initialize the model with better settings
model_name = "facebook/opt-125m"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Create pipeline with specific parameters
generator = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    device=-1,  # CPU usage, use 0 for GPU if available
    framework="pt",
)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message")
    session_id = data.get("session_id", "default")

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    try:
        # Generate response with better parameters
        response = generator(
            user_message,
            max_length=150,
            min_length=30,
            do_sample=True,
            temperature=0.7,
            top_p=0.9,
            repetition_penalty=1.2,
            num_return_sequences=1,
        )

        # Clean up the response
        ai_response = response[0]["generated_text"].strip()

        # Store in session if needed
        if f"history_{session_id}" not in session:
            session[f"history_{session_id}"] = []

        session[f"history_{session_id}"].append(
            {"user": user_message, "ai": ai_response}
        )

        return jsonify({"response": ai_response, "session_id": session_id})

    except Exception as e:
        print(f"Error generating response: {str(e)}")  # For debugging
        return jsonify({"error": f"Error generating response: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(debug=True)
