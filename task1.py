import queue
import random
import time

# Create a queue of applications
queue = queue.Queue()

# Function to generate a new request and add it to the queue
def generate_request():
    new_request = {"id": random.randint(1, 1000)}  # Generating a unique ID for the request
    queue.put(new_request)
    print(f"New request added to the queue: {new_request}")

# Function to process a request from the queue
def process_request():
    if not queue.empty():
        request = queue.get()
        print(f"Processing request: {request}")
        # Simulating processing time
        time.sleep(random.uniform(0.5, 2))
        print(f"Request {request} processed.")
    else:
        print("Queue is empty.")

# Main loop of the program
if __name__ == "__main__":
    while True:
        choice = input("Press 'g' to generate a request, 'p' to process a request, or 'q' to quit: ")
        if choice == 'g':
            generate_request()
        elif choice == 'p':
            process_request()
        elif choice == 'q':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
