from flask import Flask, request, render_template, jsonify
from utils.data_loader import load_data
from utils.email_handler import send_email
from utils.scheduler import schedule_emails

app = Flask(__name__)

# Load data route
@app.route('/load-data', methods=['POST'])
def load_data_route():
    source_type = request.form.get('source_type')
    file_path = request.form.get('file_path')
    sheet_url = request.form.get('sheet_url')
    
    try:
        data = load_data(source_type, file_path=file_path, sheet_url=sheet_url)
        return jsonify({"message": "Data loaded successfully", "data": data.head().to_dict()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Email sending route
@app.route('/send-email', methods=['POST'])
def send_email_route():
    subject = request.form.get('subject')
    body = request.form.get('body')
    to_email = request.form.get('to_email')
    sender_email = request.form.get('sender_email')
    app_password = request.form.get('app_password')
    
    try:
        send_email(subject, body, to_email, sender_email, app_password)
        return jsonify({"message": "Email sent successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Schedule emails
@app.route('/schedule-emails', methods=['POST'])
def schedule_emails_route():
    schedule_emails()  # This function would handle scheduling logic
    return jsonify({"message": "Emails scheduled successfully"})

if __name__ == '__main__':
    app.run(debug=True)
