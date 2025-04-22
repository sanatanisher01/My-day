#!/bin/bash
# Shell script to run the MyDay application on Linux/Mac

echo "MyDay Server Launcher"
echo "====================="

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

# Check if virtual environment exists, create if not
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install requirements if needed
if [ ! -f "venv/bin/gunicorn" ]; then
    echo "Installing requirements..."
    pip install -r requirements.txt
fi

# Default values
MODE="prod"
PORT=8000
WORKERS=3

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --mode)
            MODE="$2"
            shift 2
            ;;
        --port)
            PORT="$2"
            shift 2
            ;;
        --workers)
            WORKERS="$2"
            shift 2
            ;;
        *)
            shift
            ;;
    esac
done

# Run the server
echo "Running server in $MODE mode on port $PORT..."
python run_server.py --mode=$MODE --port=$PORT --workers=$WORKERS
