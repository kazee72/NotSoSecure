import hash_manager, charset_generator
from time import perf_counter
import multiprocessing

class BruteForceEngine:
    def __init__(self, target, hash_algorithm, min_length, max_length):
        self.hash_algorithm = hash_algorithm
        self.target = target
        self.charset_generator = charset_generator.CharsetGenerator(True,
                                                                    False,
                                                                    False,
                                                                    False,
                                                                    min_length,
                                                                    max_length)

    def start_worker(self):
        result_queue = multiprocessing.Queue()
        charset = self.charset_generator.build_charset()
        processes = []
        stop_event = multiprocessing.Event()

        start_time = perf_counter()

        # create as many processes as there are characters in the charset
        for i in range(len(charset)):
            p = multiprocessing.Process(target=self.worker_function, args=(charset[i], result_queue, stop_event))
            p.start()
            processes.append(p)

        # wait for one process to put something in queue
        result = result_queue.get()

        stop_time = perf_counter()
        elapsed_time = stop_time - start_time

        print(f"Password found: '{result[0]}' taking {elapsed_time:.4f} s")

        # stop all processes
        for p in processes:
            p.join()

    def worker_function(self, prefix, result_queue, stop_event):
        local_guesses = 0
        local_hash_manager = hash_manager.HashManager(self.hash_algorithm)
        target_hash = local_hash_manager.hash(self.target)
        for guess in self.charset_generator.generate_with_prefix(prefix):
            # check if other process was successful
            if stop_event.is_set():
                return

            local_guesses += 1
            if local_hash_manager.is_match(guess, target_hash):
                result_queue.put((guess, local_guesses))
                stop_event.set() # tell other processes this one was successful
                return


if __name__ == "__main__":
    engine = BruteForceEngine("hebqm", "sha256", 2, 5)

    engine.start_worker()

