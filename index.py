from app import app
from layouts import dashboard
import callbacks # Include callbacks (Needs to be assigned after setting layout up)

# Include layout
app.layout = dashboard

if __name__ == '__main__':
    app.run_server(debug=False)