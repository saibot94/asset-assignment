# Run the server in test mode
from app import app
app.run(host='0.0.0.0', port=8000, debug=True)