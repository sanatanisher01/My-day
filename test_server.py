#!/usr/bin/env python
"""
Script to test if the MyDay server is running correctly.
"""
import argparse
import sys
import time
import urllib.request
import urllib.error

def test_server(url, max_attempts=5, wait_seconds=2):
    """Test if the server is running by making HTTP requests."""
    print(f"Testing server at {url}...")
    
    for attempt in range(1, max_attempts + 1):
        try:
            print(f"Attempt {attempt}/{max_attempts}...")
            response = urllib.request.urlopen(url)
            
            if response.status == 200:
                print(f"✅ Success! Server is running at {url}")
                print(f"Response code: {response.status}")
                return True
            else:
                print(f"❌ Server responded with status code: {response.status}")
                
        except urllib.error.URLError as e:
            print(f"❌ Error connecting to server: {e.reason}")
            
        if attempt < max_attempts:
            print(f"Waiting {wait_seconds} seconds before next attempt...")
            time.sleep(wait_seconds)
    
    print("❌ Server test failed after multiple attempts.")
    return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test if the MyDay server is running")
    parser.add_argument("--url", default="http://localhost:8000", help="URL to test (default: http://localhost:8000)")
    parser.add_argument("--attempts", type=int, default=5, help="Maximum number of connection attempts (default: 5)")
    parser.add_argument("--wait", type=int, default=2, help="Seconds to wait between attempts (default: 2)")
    
    args = parser.parse_args()
    
    success = test_server(args.url, args.attempts, args.wait)
    sys.exit(0 if success else 1)
