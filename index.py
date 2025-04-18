from app import app
from layouts import dashboard
import callbacks  # Import callbacks after layout setup

# Include layout
app.layout = dashboard

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')