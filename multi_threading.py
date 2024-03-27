import threading

def print_thread_name():
    """Function to print the name of the current thread."""
    thread_name = threading.current_thread().name
    print("Thread name:", thread_name)

def main():
    """Main function to create and start multiple threads."""
    num_threads = 5
    threads = []

    # Create threads
    for i in range(num_threads):
        thread = threading.Thread(target=print_thread_name)
        threads.append(thread)

    # Start threads
    for thread in threads:
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
